#!/usr/bin/env python3
"""Check each content slide in the deck: wiki refs, footer links, and numbers supported by the cited pages.

Usage: python3 scripts/check_slides.py [--html PATH] [--wiki DIR]
Exit code is 1 if any error is found, 2 if the HTML file is missing, else 0.
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from check_wiki import Issue, NUMBER, YEAR
from quotes import slug

REPO = Path(__file__).resolve().parent.parent
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SKIP_TAGS = {"footer", "script", "style"}
HEADING = re.compile(r"^#+(.*)$", re.M)


def _classes(attrs: dict) -> set:
    return set((attrs.get("class") or "").split())


class SlideParser(HTMLParser):
    """Collect every <section> inside div.slides with its attributes, visible text and footer.src links."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # open (tag, attrs) pairs, void elements excluded
        self.slides = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and any(t == "div" and "slides" in _classes(x) for t, x in self.stack):
            self.current = {"attrs": a, "text": [], "links": []}
            self.slides.append(self.current)
        if tag not in VOID:
            self.stack.append((tag, a))
        if tag == "a" and self.current is not None and any(
                t == "footer" and "src" in _classes(x) for t, x in self.stack):
            self.current["links"].append(a.get("href") or "")

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
        if tag == "section":
            self.current = None

    def handle_data(self, data):
        skipped = any(t in SKIP_TAGS or (t == "aside" and "notes" in _classes(x)) for t, x in self.stack)
        if self.current is not None and not skipped:
            self.current["text"].append(data)


def parse_slides(html_path: Path) -> list:
    """Return the parsed slides of a deck (dicts with attrs, text and links)."""
    parser = SlideParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    parser.close()
    return parser.slides


def _read(path: Path, cache: dict):
    """Return the text of a wiki page, or None if it does not exist (cached)."""
    if path not in cache:
        cache[path] = path.read_text(encoding="utf-8") if path.is_file() else None
    return cache[path]


def _check_slide(slide: dict, wiki_dir: Path, name: str, n: int, cache: dict) -> list:
    """Run rules 2-5 on one slide."""
    issues = []

    def err(code, msg):
        issues.append(Issue(code, "error", name, n, msg))

    refs = [r.strip() for r in (slide["attrs"].get("data-wiki") or "").split(",") if r.strip()]
    if not refs:
        err("NO_WIKI_REF", "slide has no data-wiki reference")
        return issues
    hrefs = [h.split("#")[0] for h in slide["links"]]
    cited = []
    for ref in refs:
        rel, _, anchor = ref.partition("#")
        page = _read(wiki_dir / rel, cache)
        if page is None:
            err("WIKI_PAGE_MISSING", f"{rel} not found in wiki")
        else:
            cited.append(page)
            if anchor and anchor not in {slug(h) for h in HEADING.findall(page)}:
                err("WIKI_ANCHOR_MISSING", f"no heading with anchor #{anchor} in {rel}")
        if not any(h == rel or h.endswith("/" + rel) for h in hrefs):
            err("FOOTER_MISSING_LINK", f"footer has no link to {rel}")
    text = "".join(slide["text"])
    for num in dict.fromkeys(NUMBER.findall(text)):
        if YEAR.fullmatch(num):
            continue
        pat = re.compile(rf"(?<![\d.]){re.escape(num)}(?!\d)")
        if not any(pat.search(p) for p in cited):
            err("SLIDE_NUMBER_UNSUPPORTED", f"number {num} not found in cited wiki pages")
    return issues


def check_slides(html_path: Path, wiki_dir: Path) -> list[Issue]:
    """Return issues for every non-title slide of the deck; Issue.line is the 1-based slide number."""
    cache, out = {}, []
    for n, slide in enumerate(parse_slides(html_path), 1):
        if slide["attrs"].get("data-kind") != "title":
            out += _check_slide(slide, wiki_dir, html_path.name, n, cache)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check deck slides against the wiki citation rules.")
    ap.add_argument("--html", type=Path, default=REPO / "index.html", help="deck HTML file")
    ap.add_argument("--wiki", type=Path, default=REPO / "wiki", help="wiki directory")
    args = ap.parse_args(argv)
    if not args.html.is_file():
        print(f"ERROR: deck not found: {args.html}", file=sys.stderr)
        return 2
    issues = check_slides(args.html, args.wiki)
    for i in issues:
        print(f"{i.code} {i.path}:slide{i.line} {i.msg}")
    errors = sum(i.severity == "error" for i in issues)
    warnings = sum(i.severity == "warning" for i in issues)
    print(f"SUMMARY slides={len(parse_slides(args.html))} errors={errors} warnings={warnings}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
