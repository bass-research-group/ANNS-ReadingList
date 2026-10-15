#!/usr/bin/env python3
"""Render README.md and papers/by-venue/*.md from data/papers.yaml.

Usage: python3 scripts/build.py
"""
import collections
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
VENUES = ["SOSP", "OSDI", "ASPLOS", "SIGMOD", "VLDB", "MLSys",
          "ISCA", "MICRO", "HPCA", "SC", "PPoPP"]
SUBTOPICS = {
    "algorithms": ("Algorithms",
                   "Index structures (graph, IVF, trees), quantization, filtered/hybrid search, "
                   "early termination, theory, and algorithmic benchmarks."),
    "systems": ("Systems",
                "Vector databases, disk/SSD-resident and distributed search, updates, "
                "DBMS integration, privacy, and retrieval for RAG / KV cache."),
    "accelerators": ("Accelerators",
                     "GPU, FPGA, ASIC, processing-in/near-memory, in-storage, and CXL-based "
                     "vector search."),
}
START = "<!-- BEGIN GENERATED -->"
END = "<!-- END GENERATED -->"


def load():
    papers = yaml.safe_load((ROOT / "data/papers.yaml").read_text())
    for p in papers:
        assert p["venue"] in VENUES, p
        assert p["subtopic"] in SUBTOPICS, p
    return papers


def sort_key(p):
    return (-p["year"], VENUES.index(p["venue"]), p["title"].lower())


def authors(p):
    a = p.get("authors") or []
    return ", ".join(a[:6]) + (", et al." if len(a) > 6 else "")


def entry(p, show_venue=True):
    links = []
    if p.get("url"):
        links.append(f"[[paper]]({p['url']})")
    if p.get("pdf") and p["pdf"] != p.get("url"):
        links.append(f"[[pdf]]({p['pdf']})")
    if p.get("arxiv"):
        links.append(f"[[arXiv]]({p['arxiv']})")
    if p.get("code"):
        links.append(f"[[code]]({p['code']})")
    line = f"- **{p['title']}**"
    if show_venue:
        line += f" [{p['venue']} {p['year']}]"
    if p.get("status") == "accepted":
        line += " *(accepted, to appear)*"
    line += f"<br>{authors(p)}"
    if links:
        line += " " + " ".join(links)
    if p.get("tags"):
        line += " " + " ".join(f"`{t}`" for t in p["tags"])
    if p.get("note"):
        line += f"<br><sub>{p['note']}</sub>"
    return line


def overview(papers):
    years = sorted({p["year"] for p in papers})
    count = collections.Counter((p["venue"], p["year"]) for p in papers)
    rows = ["| Venue | " + " | ".join(map(str, years)) + " | Total |",
            "|---" * (len(years) + 2) + "|"]
    for v in VENUES:
        cells = [str(count[(v, y)]) if count[(v, y)] else "—" for y in years]
        total = sum(count[(v, y)] for y in years)
        rows.append(f"| [{v}](papers/by-venue/{v}.md) | " + " | ".join(cells) + f" | {total} |")
    sub = collections.Counter((p["subtopic"], p["year"]) for p in papers)
    rows += ["", "| Sub-topic | " + " | ".join(map(str, years)) + " | Total |",
             "|---" * (len(years) + 2) + "|"]
    for s, (name, _) in SUBTOPICS.items():
        cells = [str(sub[(s, y)]) for y in years]
        rows.append(f"| [{name}](#{name.lower()}) | " + " | ".join(cells)
                    + f" | {sum(sub[(s, y)] for y in years)} |")
    return "\n".join(rows)


def by_subtopic(papers):
    out = []
    for s, (name, desc) in SUBTOPICS.items():
        group = sorted((p for p in papers if p["subtopic"] == s), key=sort_key)
        out += [f"### {name}", "", f"_{desc}_", ""]
        for (y, v), ps in _groups(group):
            out += [f"#### {v} {y}", ""] + [entry(p, show_venue=False) for p in ps] + [""]
    return "\n".join(out).rstrip()


def _groups(ps):
    groups = collections.OrderedDict()
    for p in ps:
        groups.setdefault((p["year"], p["venue"]), []).append(p)
    return groups.items()


def venue_pages(papers):
    d = ROOT / "papers/by-venue"
    d.mkdir(parents=True, exist_ok=True)
    for v in VENUES:
        ps = sorted((p for p in papers if p["venue"] == v), key=sort_key)
        out = [f"# {v}", "", f"ANNS / vector search papers at {v}, from 2025 on. "
               "Generated from [`data/papers.yaml`](../../data/papers.yaml); edit that file, "
               "not this one.", ""]
        if not ps:
            out.append("_No papers found yet._")
        for y in sorted({p["year"] for p in ps}, reverse=True):
            out += [f"## {v} {y}", ""]
            for s, (name, _) in SUBTOPICS.items():
                group = [p for p in ps if p["year"] == y and p["subtopic"] == s]
                if group:
                    out += [f"### {name}", ""] + [entry(p, show_venue=False) for p in group] + [""]
        (d / f"{v}.md").write_text("\n".join(out).rstrip() + "\n")


def main():
    papers = load()
    venue_pages(papers)
    readme = ROOT / "README.md"
    text = readme.read_text()
    body = "\n\n".join([
        f"There are **{len(papers)}** papers so far.",
        overview(papers),
        "## Papers by sub-topic",
        by_subtopic(papers),
    ])
    head, _, rest = text.partition(START)
    _, _, tail = rest.partition(END)
    readme.write_text(f"{head}{START}\n{body}\n{END}{tail}")


if __name__ == "__main__":
    main()
