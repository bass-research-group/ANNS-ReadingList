"""Offline tests: no network. Run with `python -m pytest`."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build  # noqa: E402
import update  # noqa: E402
from readinglist import classify, load_config, load_papers, norm_title, relevance  # noqa: E402

FIX = ROOT / "tests" / "fixtures"
CFG = load_config()


def test_data_is_valid():
    papers = load_papers()
    build.check(papers, CFG)
    for p in papers:
        assert p["year"] >= CFG["start_year"]
        assert p.get("authors"), p["title"]


def test_parse_sparql_toc():
    papers = update.parse_sparql_toc((FIX / "sparql-journals-pvldb-pvldb19-trimmed.json").read_text(), "VLDB", 2026)
    assert len(papers) == 30
    red = next(p for p in papers if p["title"].startswith("RED-ANNS"))
    assert red["url"].startswith("https://www.vldb.org/pvldb/vol19/")
    assert all(not a[-4:].isdigit() for p in papers for a in p["authors"])  # homonym suffix dropped


def test_merge_matches_known_and_skips_excluded():
    papers = load_papers()
    before = len(papers)
    records = update.parse_sparql_toc((FIX / "sparql-journals-pvldb-pvldb19-trimmed.json").read_text(), "VLDB", 2026)
    added, _ = update.merge(papers, records, CFG, log=lambda m: None)
    titles = {norm_title(p["title"]) for p in added}
    assert norm_title("RT-RkNN: Reverse k Nearest Neighbor Queries as a Graphics Ray Casting Problem") not in titles
    assert norm_title("RED-ANNS: A RDMA-Enabled Distributed Framework for Graph-Based Approximate Nearest Neighbor Search") not in titles
    assert len(papers) == before + len(added)


def test_accepted_paper_is_promoted_when_published():
    papers = [{"title": "Some Vector Search Paper", "authors": ["A. Author", "et al."], "venue": "SIGMOD",
               "year": 2027, "category": "indexing-algorithm", "status": "accepted", "source": "preprint",
               "arxiv": "https://arxiv.org/abs/2601.00001"}]
    rec = {"title": "Some vector search paper.", "authors": ["A. Author", "B. Author"], "venue": "SIGMOD",
           "year": 2027, "url": "https://doi.org/10.1145/1", "source": "dblp"}
    added, _ = update.merge(papers, [rec], CFG, log=lambda m: None)
    assert not added
    assert "status" not in papers[0] and papers[0]["url"] == rec["url"]
    assert papers[0]["authors"] == ["A. Author", "B. Author"]


def test_arxiv_acceptance_and_code():
    entries = list(update.arxiv_entries((FIX / "arxiv-feed.xml").read_text()))
    assert entries and all(e["arxiv"].startswith("https://arxiv.org/abs/") for e in entries)
    assert update.accepted_venue_year("Accepted to SIGMOD 2027", ["SIGMOD"], 2027)
    assert update.accepted_venue_year("To appear in VLDB'27", ["VLDB"], 2027)
    assert not update.accepted_venue_year("Under submission to SIGMOD 2027", ["SIGMOD"], 2027)
    assert not update.accepted_venue_year("Accepted to ESC 2027", ["SC"], 2027)
    e = {"comment": "Code: https://github.com/foo/bar.", "summary": ""}
    assert update.find_code(e) == "https://github.com/foo/bar"


def test_expand_keys():
    assert update.expand("journals/pvldb/pvldb{year-2007}", 2026) == "journals/pvldb/pvldb19"
    assert update.expand("conf/asplos/asplos{year}-{vol}", 2027, 2) == "conf/asplos/asplos2027-2"


def test_classifier():
    assert relevance("Fast Graph-Based Approximate Nearest Neighbor Search", CFG) == "strong"
    assert relevance("A RAG Serving System", CFG) == "weak"
    assert relevance("Transaction Processing on CXL", CFG) is None
    cases = {
        ("VecBench: A Benchmark for Filtered Vector Search: [Experiments & Analysis]", "SIGMOD"): "benchmark",
        ("WiFlash: Approximate Nearest Neighbor Search Inside Flash Cell Array", "MICRO"): "fpga-in-storage",
        ("Fast Graph Vector Search on FPGAs", "VLDB"): "fpga-in-storage",
        ("MFNNS: A Multiplier-Free Near-Memory Accelerator for Graph-based ANNS", "MICRO"): "domain-specific-accelerator",
        ("Billion-Scale ANNS on Real-World PIM", "SC"): "domain-specific-accelerator",
        ("Characterizing Vector Search Workloads on CPUs", "ISCA"): "characterization",
        ("Vector Databases: A Survey", "VLDB"): "survey",
        ("Accelerating Graph Indexing for ANNS on Modern CPUs", "SIGMOD"): "indexing-algorithm",
        ("Billion-Scale Vector Search on a Single GPU", "SIGMOD"): "gpu-system",
        ("RDMA-Enabled Distributed ANNS", "VLDB"): "distributed-system",
        ("Vector Search on Modern SSDs", "VLDB"): "out-of-core-system",
        ("Range-Filtered Approximate Nearest Neighbor Search", "VLDB"): "filtered-algorithm",
        ("Multi-Vector Retrieval with Graphs", "SIGMOD"): "hybrid-algorithm",
    }
    for (title, venue), want in cases.items():
        assert classify(title, venue, CFG) == want, title


def test_listing_renders_every_category():
    text = build.listing(load_papers(), CFG)
    for cat in CFG["categories"].values():
        assert cat["description"] in text


def test_official_page_parser():
    html = """<html><body><h2>Round 1</h2><ul>
    <li><strong>Metric Algebra: Embedding-Independence in Vector Databases</strong><br>
    Alice Smith (University of Edinburgh), Bob Jones (University of Edinburgh)</li>
    <li><strong>Efficient Transaction Processing on CXL</strong><br>Carol White (MIT)</li>
    <li><b>Fast Graph-Based Approximate Nearest Neighbor Search on SSDs</b></li>
    </ul></body></html>"""
    recs = update.parse_official_page(html, "SIGMOD", 2027, CFG)
    assert [r["title"] for r in recs] == ["Metric Algebra: Embedding-Independence in Vector Databases",
                                         "Fast Graph-Based Approximate Nearest Neighbor Search on SSDs"]
    assert recs[0]["authors"] == ["Alice Smith", "Bob Jones"]
    assert recs[1]["authors"] == ["(see program)"]
    # a placeholder author list in the data gets replaced by the program's names
    papers = [{"title": recs[0]["title"], "authors": ["University of Edinburgh authors (to be filled in)"],
               "venue": "SIGMOD", "year": 2027, "category": "indexing-algorithm", "status": "accepted"}]
    update.merge(papers, recs, CFG, log=lambda m: None)
    assert papers[0]["authors"] == ["Alice Smith", "Bob Jones"]
    assert papers[0]["status"] == "accepted"


def test_official_page_real_excerpt():
    """Excerpt of https://2027.sigmod.org/sigmod_papers.shtml as text (bulleted, affiliations in parentheses)."""
    recs = update.parse_official_page((FIX / "sigmod2027-papers-excerpt.txt").read_text(), "SIGMOD", 2027, CFG)
    titles = [r["title"] for r in recs]
    assert len(titles) == 12
    assert "All-in-one Graph-based Indexing for Hybrid Search on GPUs" in titles
    assert not any("Jaro-Winkler" in t or "Community Search" in t for t in titles)
    jing = next(r for r in recs if r["title"].startswith("Reverse Neighbor"))
    assert jing["authors"][0] == "Liuchang JING" and len(jing["authors"]) == 5  # nested parentheses removed


def test_official_page_linklings_program():
    """Excerpt of https://sc26.conference-program.com/ (author names run together)."""
    recs = update.parse_official_page((FIX / "sc26-program-excerpt.txt").read_text(), "SC", 2026, CFG)
    assert [r["title"][:7] for r in recs] == ["RT-HiSS", "PIMCQG:"]
    assert recs[0]["authors"] == ["Revanth Reddy Munugala", "Michael Gowanlock"]
    assert recs[1]["authors"][-1] == "Amelie Chi Zhou" and len(recs[1]["authors"]) == 6
