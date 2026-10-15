"""Shared helpers: configuration, paper data files, title matching and auto-classification."""
import datetime
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers"
FIELDS = ["title", "authors", "venue", "year", "category", "tags", "url", "pdf", "arxiv", "code",
          "status", "auto", "note", "source"]


def load_config():
    return yaml.safe_load((ROOT / "config.yaml").read_text())


def current_year():
    return datetime.datetime.now(datetime.timezone.utc).year


def load_papers():
    papers = []
    for f in sorted(DATA.glob("*.yaml")):
        papers += yaml.safe_load(f.read_text()) or []
    return papers


class _Dumper(yaml.SafeDumper):
    pass


def _represent_list(dumper, items):
    flow = all(isinstance(x, str) for x in items)
    return dumper.represent_sequence("tag:yaml.org,2002:seq", items, flow_style=flow)


_Dumper.add_representer(list, _represent_list)


def save_papers(papers):
    """Write one file per publication year, sorted by venue then title."""
    by_year = {}
    for p in papers:
        by_year.setdefault(p["year"], []).append(
            {k: p[k] for k in FIELDS if p.get(k) not in (None, [], "")})
    DATA.mkdir(parents=True, exist_ok=True)
    venues = list(load_config()["venues"])
    for year, ps in by_year.items():
        ps.sort(key=lambda p: (venues.index(p["venue"]), p["title"].lower()))
        text = yaml.dump(ps, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1000)
        (DATA / f"{year}.yaml").write_text(text.replace("\n- title:", "\n\n- title:"))


def norm_title(title):
    """Normalize a title for matching: drop E&A suffixes, punctuation and case."""
    title = re.sub(r"[:\s]*\[?Experiments? (&|and) Analysis\]?\.?$", "", title, flags=re.I)
    return re.sub(r"[^a-z0-9]", "", title.lower())


def _any(patterns, text):
    return any(re.search(p, text, re.I) for p in patterns)


def relevance(title, cfg):
    """'strong', 'weak' or None, from the title keywords in config.yaml."""
    if _any(cfg["keywords"]["strong"], title):
        return "strong"
    if _any(cfg["keywords"]["weak"], title):
        return "weak"
    return None


def classify(title, venue, cfg):
    """Best-guess category from title keywords; a human should confirm it."""
    for key in cfg["classify_order"]:
        cat = cfg["categories"][key]
        if cat.get("venues") and venue not in cat["venues"]:
            continue
        if _any(cat.get("rules", []), title):
            return key
    return cfg["default_category"]


def excluded_titles():
    path = ROOT / "data" / "excluded.txt"
    return {norm_title(line) for line in path.read_text().splitlines()
            if line.strip() and not line.startswith("#")}
