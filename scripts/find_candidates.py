#!/usr/bin/env python3
"""List likely-relevant papers that are not yet in data/papers.yaml.

Pulls the DBLP-derived per-venue lists maintained at
https://github.com/RealZST/csconf-papers (SOSP, OSDI, ASPLOS, SIGMOD, VLDB, MLSys),
keyword-filters the titles, and prints the ones in neither data/papers.yaml nor
data/excluded.txt.
Each hit still needs a human read before it goes into the list.

ISCA, MICRO, HPCA, SC and PPoPP are not covered by that dataset; check DBLP
(https://dblp.org/db/conf/isca/ etc.) and the conference programs by hand.

Usage: python3 scripts/find_candidates.py [YEAR ...]   (default: 2025 onwards)
"""
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://raw.githubusercontent.com/RealZST/csconf-papers/main/data"
VENUES = ["SOSP", "OSDI", "ASPLOS", "SIGMOD", "VLDB", "MLSys"]
KEYWORDS = re.compile(
    r"nearest neighbo|\bA?k?-?NNS?\b|vector (search|database|data|index|retriev|similar|quer)|"
    r"similarity (search|join)|quantiz|HNSW|DiskANN|proximity graph|maximum inner product|"
    r"\bMIPS\b|multi-vector|embedding (search|retriev)|retrieval-augmented|\bRAG\b|range.filter",
    re.I)


def norm(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def main():
    with urllib.request.urlopen(f"{BASE}/index.json") as r:
        index = json.load(r)
    years = [int(y) for y in sys.argv[1:]] or sorted(
        {f["year"] for f in index["files"] if f["year"] >= 2025})
    known = {norm(p["title"]) for p in yaml.safe_load((ROOT / "data/papers.yaml").read_text())}
    known |= {norm(line) for line in (ROOT / "data/excluded.txt").read_text().splitlines()
              if line.strip() and not line.startswith("#")}
    for y in years:
        for v in VENUES:
            try:
                with urllib.request.urlopen(f"{BASE}/{y}/{v}.json") as r:
                    papers = json.load(r)["papers"]
            except urllib.error.HTTPError:
                continue
            for p in papers:
                if KEYWORDS.search(p["title"]) and norm(p["title"].rstrip(".")) not in known:
                    print(f"{v} {y}\t{p['title']}\t{p.get('url') or ''}")


if __name__ == "__main__":
    main()
