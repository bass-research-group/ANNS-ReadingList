#!/usr/bin/env python3
"""Find new papers and fill in missing metadata. Runs monthly from .github/workflows/update.yml.

Sources:
  1. csconf-papers (DBLP-derived lists for SOSP, OSDI, ASPLOS, SIGMOD, VLDB, MLSys).
  2. The DBLP SPARQL endpoint, for venues or years csconf-papers does not have
     (dblp.org's website and search API sit behind bot protection since 2026-09).
  3. The arXiv API, for preprints whose comments say they were accepted to a venue.
  4. Official accepted-paper pages (`official` in config.yaml), e.g. SIGMOD's per-round list.

What it changes, all additive:
  - known papers: fills in url/pdf/arXiv links; once a paper marked `status: accepted`
    shows up in DBLP it gets the official link and full author list and loses the mark;
  - new papers whose titles match the `strong` keywords are added with an auto-classified
    category and `auto: true`, so a human can check them later;
  - titles matching only the `weak` keywords go to data/candidates.md for review;
  - papers with an arXiv preprint but no code link get one if the arXiv abstract or
    comments point to GitHub/GitLab.
Papers are never removed.

Usage: python3 scripts/update.py [--dry-run] [--skip csconf,dblp,arxiv,code]
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from readinglist import (ROOT, classify, current_year, excluded_titles, load_config, load_papers,
                         norm_title, relevance, save_papers)

CSCONF = "https://raw.githubusercontent.com/RealZST/csconf-papers/main/data"
SPARQL = "https://sparql.dblp.org/sparql"
ARXIV = "https://export.arxiv.org/api/query"
USER_AGENT = "ANNS-ReadingList-updater (+https://github.com/bass-research-group/ANNS-ReadingList)"
ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

TOC_QUERY = """\
PREFIX dblp: <https://dblp.org/rdf/schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
SELECT ?paper ?title ?primary ?ord ?name WHERE {{
  ?paper dblp:listedOnTocPage <https://dblp.org/db/{key}> .
  ?paper rdf:type ?type . VALUES ?type {{ dblp:Inproceedings dblp:Article }}
  ?paper dblp:title ?title .
  OPTIONAL {{ ?paper dblp:primaryDocumentPage ?primary }}
  OPTIONAL {{ ?paper dblp:hasSignature ?sig .
             ?sig dblp:signatureDblpName ?name ; dblp:signatureOrdinal ?ord . }}
}} ORDER BY ?paper xsd:integer(?ord)"""
NON_PAPER = re.compile(r"^(front matter|corrigend|errat|(demo|poster|abstract)\s*:)|PACMMOD,?\s*V\d+,\s*N\d+", re.I)
ACCEPTED = re.compile(r"accepted|to appear|camera[- ]ready|published (in|at)|in proceedings", re.I)
CODE_URL = re.compile(r"https?://(?:www\.)?(?:github\.com|gitlab\.com)/[\w.-]+/[\w.-]+", re.I)


class Fetcher:
    def __init__(self, throttle=3.0, retries=4):
        self.throttle, self.retries, self.last = throttle, retries, 0.0

    def get(self, url, missing_ok=False):
        for attempt in range(self.retries):
            time.sleep(max(0.0, self.last + self.throttle - time.time()))
            self.last = time.time()
            try:
                req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=60) as r:
                    return r.read().decode("utf-8")
            except urllib.error.HTTPError as e:
                if e.code == 404 and missing_ok:
                    return None
                if e.code not in (429, 500, 502, 503, 504):
                    raise
            except (urllib.error.URLError, TimeoutError):
                pass
            time.sleep(5 * 2 ** attempt)
        raise RuntimeError(f"giving up on {url}")


def expand(key, year, vol=None):
    """Fill "{year}", "{vol}" and simple offsets such as "{year-2007}" into a DBLP key."""
    def sub(m):
        expr = m.group(1).replace(" ", "")
        name, _, off = re.match(r"(year|vol)([+-]\d+)?$", expr).group(1, 0, 2)
        base = year if name == "year" else vol
        return str(base + int(off or 0))
    return re.sub(r"\{([^}]+)\}", sub, key)


def clean_title(t):
    return re.sub(r"\s+", " ", t).strip().rstrip(".").strip()


# ---------- sources ----------

def parse_csconf(text, venue, year):
    out = []
    for p in json.loads(text)["papers"]:
        if NON_PAPER.search(p["title"]):
            continue
        rec = {"title": clean_title(p["title"]), "venue": venue, "year": year, "source": "dblp",
               "authors": [a.get("display_name") or a["name"] for a in p.get("authors", [])],
               "url": p.get("url")}
        if p.get("pdf_url") and p.get("pdf_source") != "publisher-doi":
            rec["pdf"] = p["pdf_url"]
        if p.get("arxiv_id"):
            rec["arxiv"] = f"https://arxiv.org/abs/{p['arxiv_id']}"
        out.append(rec)
    return out


def parse_sparql_toc(text, venue, year):
    papers = {}
    for row in json.loads(text)["results"]["bindings"]:
        val = {k: v["value"] for k, v in row.items()}
        p = papers.setdefault(val["paper"], {"title": clean_title(val["title"]), "venue": venue,
                                             "year": year, "source": "dblp", "authors": [],
                                             "url": val.get("primary"), "_ords": set()})
        if "name" in val and val.get("ord") not in p["_ords"]:
            p["_ords"].add(val.get("ord"))
            p["authors"].append(re.sub(r"\s+\d{4}$", "", val["name"]))  # drop DBLP homonym suffix
    out = []
    for p in papers.values():
        p.pop("_ords")
        if not NON_PAPER.search(p["title"]):
            out.append(p)
    return out


def arxiv_entries(text):
    root = ET.fromstring(text)
    for e in root.findall("a:entry", ATOM):
        abs_url = re.sub(r"v\d+$", "", e.findtext("a:id", "", ATOM).strip()).replace("http://", "https://")
        yield {"title": clean_title(e.findtext("a:title", "", ATOM)),
               "authors": [a.findtext("a:name", "", ATOM) for a in e.findall("a:author", ATOM)],
               "arxiv": abs_url,
               "comment": e.findtext("arxiv:comment", "", ATOM) or "",
               "summary": e.findtext("a:summary", "", ATOM) or ""}


def accepted_venue_year(comment, spellings, year):
    """True if an arXiv comment says the paper was accepted to <venue> <year>."""
    yy = str(year)[2:]
    for s in spellings:
        pat = rf"(?<![A-Za-z]){re.escape(s)}\s*(?:'|’)?\s*(?:{year}|{yy})\b"
        if re.search(pat, comment) and ACCEPTED.search(comment):
            return True
    return False


def parse_official_page(html, venue, year, cfg):
    """Accepted papers from a conference's own accepted-papers page.

    Pages differ in markup, so this works on visible text lines: a line matching the
    `strong` title keywords is taken as a title, and the next line as its author list
    when it looks like one (commas, no keywords). Affiliations in parentheses are dropped.
    """
    from readinglist import relevance
    html = re.sub(r"(?is)<(script|style).*?</\1>", " ", html)
    html = re.sub(r"(?i)<br\s*/?>|</(p|li|div|tr|td|h\d|strong|b|em|i|span)>", "\n", html)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&amp;", "&", re.sub(r"&nbsp;|&#160;", " ", text))
    lines = [re.sub(r"^[*\u2022\-]\s+", "", re.sub(r"\s+", " ", l).strip()) for l in text.splitlines()]
    lines = [l for l in lines if l]
    out = []
    for i, line in enumerate(lines):
        if not (15 <= len(line) <= 300) or relevance(line, cfg) != "strong":
            continue
        if line.endswith(".") or re.match(r"(Description|Abstract|Session)\b", line):  # prose, not a title
            continue
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        authors = []
        if re.match(r"Authors?(?=[A-Z])", nxt):
            # Linklings programs (SC, ...) print "AuthorsFirst LastFirst Last": split at
            # lower-to-upper case boundaries.
            nxt = re.sub(r"^Authors?", "", nxt)
            authors = [a.strip() for a in re.split(r"(?<=[a-z\u00df-\u00ff])(?=[A-Z\u00c0-\u00de])", nxt)
                       if a.strip()]
        elif re.search(r"[,;]", nxt) or re.search(r"\(.+\)\*?$", nxt):
            if relevance(nxt, cfg) is None:
                while re.search(r"\([^()]*\)", nxt):  # affiliations, possibly nested
                    nxt = re.sub(r"\([^()]*\)", "", nxt)
                # affiliations are gone, so commas and semicolons both separate names
                parts = re.split(r"[,;]|\band\b", nxt)
                authors = [a.strip(" *") for a in parts if a.strip(" *")]
        out.append({"title": clean_title(line), "authors": authors or ["(see program)"],
                    "venue": venue, "year": year, "status": "accepted", "source": "program",
                    "note": f"Listed on the official {venue} {year} accepted-papers page."})
    return out


def find_code(entry):
    for text in (entry["comment"], entry["summary"]):
        m = CODE_URL.search(text)
        if m:
            return m.group(0).rstrip(".,;)")
    return None


def collect(cfg, years, fetcher, skip, log):
    records = []
    for venue, src in cfg["venues"].items():
        for year in years:
            got = []
            if src.get("csconf") and "csconf" not in skip:
                try:
                    text = fetcher.get(f"{CSCONF}/{year}/{src['csconf']}.json", missing_ok=True)
                    got = parse_csconf(text, venue, year) if text else []
                except Exception as e:  # keep going: one bad venue must not stop the run
                    log(f"csconf {venue} {year}: {e}")
            if not got and src.get("dblp") and "dblp" not in skip:
                for key in src["dblp"]:
                    vols = range(1, 5) if "{vol}" in key else [None]
                    for vol in vols:
                        k = expand(key, year, vol)
                        try:
                            q = urllib.parse.urlencode({"query": TOC_QUERY.format(key=k), "format": "json"})
                            got += parse_sparql_toc(fetcher.get(f"{SPARQL}?{q}"), venue, year)
                        except Exception as e:
                            log(f"dblp {k}: {e}")
            log(f"{venue} {year}: {len(got)} papers indexed")
            records += got
    if "official" not in skip:
        for venue, src in cfg["venues"].items():
            for url_t in src.get("official", []):
                for year in years:
                    if year < current_year():
                        continue
                    url = expand(url_t.replace("{yy}", str(year)[2:]), year)
                    try:
                        html = fetcher.get(url, missing_ok=True)
                        got = parse_official_page(html, venue, year, cfg) if html else []
                        log(f"official {venue} {year}: {len(got)} matching titles")
                        records += got
                    except Exception as e:
                        log(f"official {url}: {e}")
    if "arxiv" not in skip:
        topic = '(abs:"nearest neighbor" OR abs:"vector search" OR abs:"vector database" OR abs:"similarity search")'
        for venue, src in cfg["venues"].items():
            for year in years:
                if year < current_year():
                    continue
                for s in src.get("arxiv", []):
                    q = f'co:"{s} {year}" AND {topic}'
                    url = f"{ARXIV}?" + urllib.parse.urlencode({"search_query": q, "max_results": 100})
                    try:
                        for e in arxiv_entries(fetcher.get(url)):
                            if accepted_venue_year(e["comment"], [s], year):
                                records.append({"title": e["title"], "authors": e["authors"],
                                                "venue": venue, "year": year, "arxiv": e["arxiv"],
                                                "code": find_code(e), "status": "accepted",
                                                "source": "preprint",
                                                "note": f"arXiv comment: {e['comment'][:120]}"})
                    except Exception as e:
                        log(f"arxiv {venue} {year}: {e}")
    return records


# ---------- merging ----------

def is_placeholder(authors):
    return not authors or any(a.strip().lower() in ("et al.", "et al") or "to be filled" in a
                              or "see program" in a for a in authors)


def merge(papers, records, cfg, log):
    by_title = {norm_title(p["title"]): p for p in papers}
    by_arxiv = {p["arxiv"]: p for p in papers if p.get("arxiv")}
    excluded = excluded_titles()
    added, candidates, seen = [], [], set()
    for r in records:
        key = norm_title(r["title"])
        if key in excluded or key in seen:
            continue
        seen.add(key)
        p = by_title.get(key) or (by_arxiv.get(r.get("arxiv")) if r.get("arxiv") else None)
        if p:
            enrich(p, r, log)
            continue
        rel = relevance(r["title"], cfg)
        if rel == "strong":
            new = {k: v for k, v in r.items() if v}
            new["category"] = classify(r["title"], r["venue"], cfg)
            new["auto"] = True
            papers.append(new)
            by_title[key] = new
            added.append(new)
            log(f"added [{new['category']}] {r['venue']} {r['year']}: {r['title']}")
        elif rel == "weak":
            candidates.append(r)
    return added, candidates


def enrich(p, r, log):
    if r["source"] == "dblp" and p.get("status") == "accepted":
        log(f"now published: {p['title']} ({r['venue']} {r['year']})")
        p.pop("status")
        p["source"] = "dblp"
        p["venue"], p["year"] = r["venue"], r["year"]
        if p.get("note", "").startswith(("Listed in", "arXiv comment", "Acceptance")):
            p.pop("note")
    if not is_placeholder(r.get("authors")) and (is_placeholder(p.get("authors")) or r["source"] == "dblp") \
            and len(r["authors"]) >= len([a for a in p.get("authors", []) if "et al" not in a]):
        p["authors"] = r["authors"]
    for k in ("url", "pdf", "arxiv", "code"):
        if r.get(k) and not p.get(k):
            p[k] = r[k]


def add_code_links(papers, fetcher, log):
    todo = [p for p in papers if p.get("arxiv") and not p.get("code")]
    for i in range(0, len(todo), 40):
        batch = {re.sub(r"^.*/abs/", "", p["arxiv"]): p for p in todo[i:i + 40]}
        url = f"{ARXIV}?" + urllib.parse.urlencode({"id_list": ",".join(batch), "max_results": 40})
        try:
            for e in arxiv_entries(fetcher.get(url)):
                p = batch.get(re.sub(r"^.*/abs/", "", e["arxiv"]))
                code = find_code(e)
                if p and code:
                    p["code"] = code
                    log(f"code link: {p['title']} -> {code}")
        except Exception as e:
            log(f"arxiv code lookup: {e}")


def write_candidates(candidates, years):
    lines = ["# Candidates for review", "",
             f"Papers from {min(years)}–{max(years)} whose titles match only the weak keywords in "
             "`config.yaml`. Generated by `scripts/update.py`; it is overwritten on every run.", "",
             "To keep a paper, add it to `data/papers/<year>.yaml`. To dismiss it, add its title "
             "to `data/excluded.txt`.", ""]
    if not candidates:
        lines.append("_None._")
    for r in sorted(candidates, key=lambda r: (-r["year"], r["venue"], r["title"])):
        link = r.get("url") or r.get("arxiv") or ""
        lines.append(f"- [{r['venue']} {r['year']}] {r['title']}" + (f" ({link})" if link else ""))
    (ROOT / "data" / "candidates.md").write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip", default="", help="comma-separated: csconf,dblp,official,arxiv,code")
    args = ap.parse_args()
    skip = set(filter(None, args.skip.split(",")))
    cfg = load_config()
    years = list(range(cfg["start_year"], current_year() + 2))
    log_lines = []

    def log(msg):
        print(msg)
        log_lines.append(msg)

    fetcher = Fetcher()
    papers = load_papers()
    before = len(papers)
    records = collect(cfg, years, fetcher, skip, log)
    added, candidates = merge(papers, records, cfg, log)
    if "code" not in skip:
        add_code_links(papers, fetcher, log)
    log(f"{before} -> {len(papers)} papers; {len(added)} added; {len(candidates)} weak candidates")
    if not args.dry_run:
        save_papers(papers)
        write_candidates(candidates, years)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write("## Reading list update\n\n```\n" + "\n".join(log_lines) + "\n```\n")
    if not records and not ({"csconf", "dblp", "official", "arxiv"} <= skip):
        sys.exit("no records fetched from any source")


if __name__ == "__main__":
    main()
