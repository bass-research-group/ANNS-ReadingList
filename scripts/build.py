#!/usr/bin/env python3
"""Render README.md, papers/by-venue/*.md and archive/<year>.md from data/papers/*.yaml.

The README lists the most recent `readme_years` years (config.yaml). Older years are
moved to archive/<year>.md automatically, so the README stays short as the list grows.

Usage: python3 scripts/build.py [--year YYYY]   (--year overrides "now", for testing)
"""
import argparse
import collections

from readinglist import ROOT, current_year, load_config, load_papers

START = "<!-- BEGIN GENERATED -->"
END = "<!-- END GENERATED -->"


def check(papers, cfg):
    seen = set()
    for p in papers:
        assert p["venue"] in cfg["venues"], f"unknown venue in {p['title']}: {p['venue']}"
        assert p["category"] in cfg["categories"], f"unknown category in {p['title']}: {p['category']}"
        key = p["title"].lower()
        assert key not in seen, f"duplicate paper: {p['title']}"
        seen.add(key)


def authors(p):
    a = p.get("authors") or []
    return ", ".join(a[:6]) + (", et al." if len(a) > 6 else "")


def entry(p, show_venue):
    links = []
    for key, label in (("url", "paper"), ("pdf", "pdf"), ("arxiv", "arXiv"), ("code", "code")):
        if p.get(key) and not (key == "pdf" and p["pdf"] == p.get("url")):
            links.append(f"[[{label}]]({p[key]})")
    line = f"- **{p['title']}**"
    if show_venue:
        line += f" [{p['venue']} {p['year']}]"
    if p.get("status") == "accepted":
        line += " *(accepted, to appear)*"
    if p.get("auto"):
        line += " *(auto-added, not yet reviewed)*"
    line += f"<br>{authors(p)}"
    if links:
        line += " " + " ".join(links)
    if p.get("tags"):
        line += " " + " ".join(f"`{t}`" for t in p["tags"])
    if p.get("note"):
        line += f"<br><sub>{p['note']}</sub>"
    return line


def groups(cfg):
    out = collections.OrderedDict()
    for key, cat in cfg["categories"].items():
        out.setdefault(cat["group"], []).append(key)
    return out


def anchor(text):
    return "".join(c for c in text.lower().replace(" ", "-") if c.isalnum() or c in "-_")


def listing(papers, cfg, heading="##"):
    """Papers grouped by group > category > (year, venue)."""
    venues = list(cfg["venues"])
    out = []
    for group, keys in groups(cfg).items():
        out += [f"{heading} {group}", ""]
        for key in keys:
            cat = cfg["categories"][key]
            ps = sorted((p for p in papers if p["category"] == key),
                        key=lambda p: (-p["year"], venues.index(p["venue"]), p["title"].lower()))
            if len(keys) > 1:
                out += [f"{heading}# {cat['name']}", ""]
            out += [f"_{cat['description']}_", ""]
            if not ps:
                out += ["_None yet._", ""]
            last = None
            for p in ps:
                if (p["year"], p["venue"]) != last:
                    last = (p["year"], p["venue"])
                    out += ["", f"**{p['venue']} {p['year']}**", ""]
                out.append(entry(p, show_venue=False))
            out.append("")
    return "\n".join(out).rstrip()


def tables(papers, cfg, years, archived):
    count = collections.Counter((p["venue"], p["year"]) for p in papers)
    head = "| Venue | " + " | ".join(map(str, years)) + " | Total |"
    rows = [head, "|---" * (len(years) + 2) + "|"]
    for v in cfg["venues"]:
        cells = [str(count[(v, y)]) if count[(v, y)] else "—" for y in years]
        rows.append(f"| [{v}](papers/by-venue/{v}.md) | " + " | ".join(cells)
                    + f" | {sum(count[(v, y)] for y in years)} |")
    cat = collections.Counter((p["category"], p["year"]) for p in papers)
    rows += ["", head.replace("Venue", "Sub-topic"), rows[1]]
    for key, c in cfg["categories"].items():
        title = c["name"] if c["name"] == c["group"] else f"{c['group']}: {c['name']}"
        cells = [str(cat[(key, y)]) for y in years]
        rows.append(f"| [{title}](#{anchor(c['name'])}) | " + " | ".join(cells)
                    + f" | {sum(cat[(key, y)] for y in years)} |")
    if archived:
        rows += ["", "Archived years (not shown in this README): "
                 + ", ".join(f"[{y}](archive/{y}.md)" for y in archived)]
    return "\n".join(rows)


def venue_pages(papers, cfg):
    d = ROOT / "papers" / "by-venue"
    d.mkdir(parents=True, exist_ok=True)
    for v in cfg["venues"]:
        ps = [p for p in papers if p["venue"] == v]
        out = [f"# {v}", "", f"{cfg['topic']} papers at {v}, all years. Generated from "
               "[`data/papers/`](../../data/papers/); edit those files, not this one.", ""]
        if not ps:
            out.append("_No papers found yet._")
        for y in sorted({p["year"] for p in ps}, reverse=True):
            out += [f"## {v} {y}", ""]
            for key, c in cfg["categories"].items():
                group = sorted((p for p in ps if p["year"] == y and p["category"] == key),
                               key=lambda p: p["title"].lower())
                if group:
                    out += [f"### {c['name']}", ""] + [entry(p, False) for p in group] + [""]
        (d / f"{v}.md").write_text("\n".join(out).rstrip() + "\n")


def archive_pages(papers, cfg, archived):
    d = ROOT / "archive"
    for y in archived:
        d.mkdir(exist_ok=True)
        ps = [p for p in papers if p["year"] == y]
        out = [f"# {cfg['topic']} papers, {y} (archived)", "",
               f"{len(ps)} papers. Generated from [`data/papers/{y}.yaml`](../data/papers/{y}.yaml).",
               "", listing(ps, cfg)]
        (d / f"{y}.md").write_text("\n".join(out).rstrip() + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, default=current_year())
    args = ap.parse_args()
    cfg = load_config()
    papers = load_papers()
    check(papers, cfg)
    first_shown = args.year - cfg["readme_years"] + 1
    recent = [p for p in papers if p["year"] >= first_shown]
    years = sorted({p["year"] for p in recent})
    archived = sorted({p["year"] for p in papers if p["year"] < first_shown}, reverse=True)
    venue_pages(papers, cfg)
    archive_pages(papers, cfg, archived)
    readme = ROOT / "README.md"
    text = readme.read_text()
    body = "\n\n".join([
        f"**{len(recent)}** papers from {first_shown} on"
        + (f" ({len(papers)} including the archive)." if archived else "."),
        tables(recent, cfg, years, archived),
        listing(recent, cfg, heading="###"),
    ])
    head, _, rest = text.partition(START)
    _, _, tail = rest.partition(END)
    readme.write_text(f"{head}{START}\n{body}\n{END}{tail}")


if __name__ == "__main__":
    main()
