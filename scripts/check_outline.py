#!/usr/bin/env python3
"""Check slides/outline.md rows against the wiki: refs exist, numbers are sourced, caveats kept.

Usage: python3 scripts/check_outline.py [--outline PATH] [--wiki DIR]
Exit code is 1 if any error is found, 2 if the outline file is missing.
"""
import argparse
import re
import sys
from pathlib import Path

from check_wiki import NUMBER, YEAR, Issue
from quotes import slug

REPO = Path(__file__).resolve().parent.parent
REQUIRED = {"要點", "但書", "引用 Wiki"}
BACKTICK = re.compile(r"`([^`]+)`")
EMPTY_CAVEATS = {"", "—", "-", "–"}


def _cells(line):
    """Split a markdown table row on '|' and strip each cell."""
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _rows(outline_path):
    """Return (file_lineno, {header: cell}) for each data row of the first matching table."""
    lines = outline_path.read_text(encoding="utf-8").splitlines()
    start = next((i for i, ln in enumerate(lines) if ln.startswith("|") and REQUIRED <= set(_cells(ln))), None)
    if start is None:
        return []
    header = _cells(lines[start])
    rows = []
    for i in range(start + 1, len(lines)):
        ln = lines[i]
        if not ln.startswith("|"):
            break
        if set(ln.strip()) <= set("|-: "):  # the |---| separator
            continue
        cells = _cells(ln) + [""] * len(header)
        rows.append((i + 1, dict(zip(header, cells))))
    return rows


def _refs(cell):
    """Yield (file, anchor) per backtick token; a bare '#anchor' reuses the previous file in the cell."""
    last = None
    for tok in BACKTICK.findall(cell):
        if tok.startswith("#"):
            yield last, tok[1:]
        else:
            last, _, anchor = tok.partition("#")
            yield last, anchor or None


def _load(wiki_dir, rel, cache):
    """Return the text of wiki/rel (cached), or None if the file does not exist."""
    if rel not in cache:
        p = wiki_dir / rel
        cache[rel] = p.read_text(encoding="utf-8") if p.is_file() else None
    return cache[rel]


def _headings(text):
    """Heading texts with the leading #'s and whitespace stripped."""
    return [ln.lstrip("#").strip() for ln in text.splitlines() if ln.startswith("#")]


def check_outline(outline_path: Path, wiki_dir: Path) -> list[Issue]:
    """Return one Issue per broken ref, unsupported number, or missing caveat in the outline rows."""
    out, texts, name = [], {}, outline_path.name
    rows = _rows(outline_path)
    if not rows:
        return [Issue("OUTLINE_TABLE_MISSING", "error", name, 1, "no table with 要點 / 但書 / 引用 Wiki columns")]
    for lineno, row in rows:
        num = row.get("#", "")
        line = int(num) if num.isdigit() else lineno
        refs_cell = row.get("引用 Wiki", "")
        if "封面" in refs_cell:
            continue
        cited = set()
        for f, anchor in _refs(refs_cell):
            text = _load(wiki_dir, f, texts) if f else None
            if text is None:
                out.append(Issue("OUTLINE_REF_MISSING", "error", name, line, f"cited file not found: {f}"))
                continue
            cited.add(f)
            if anchor and anchor not in {slug(h) for h in _headings(text)}:
                out.append(Issue("OUTLINE_REF_MISSING", "error", name, line, f"anchor #{anchor} not in {f}"))
        cited_texts = [texts[f] for f in cited]
        for col in ("要點", "但書"):
            for n in NUMBER.findall(row.get(col, "")):
                if YEAR.fullmatch(n):
                    continue
                pat = re.compile(rf"(?<![\d.]){re.escape(n)}(?!\d)")
                if not any(pat.search(t) for t in cited_texts):
                    out.append(Issue("OUTLINE_NUMBER_UNSUPPORTED", "error", name, line,
                                     f"number {n} not in any cited page"))
        has_caveat = any(h.startswith("注意") for t in cited_texts for h in _headings(t))
        if has_caveat and row.get("但書", "") in EMPTY_CAVEATS:
            out.append(Issue("OUTLINE_CAVEAT_MISSING", "error", name, line,
                             "cited page has a 注意 caveat; fill 但書 or waive with 無：reason"))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check outline rows against wiki pages.")
    ap.add_argument("--outline", type=Path, default=REPO / "slides" / "outline.md", help="outline markdown file")
    ap.add_argument("--wiki", type=Path, default=REPO / "wiki", help="wiki directory")
    args = ap.parse_args(argv)
    if not args.outline.is_file():
        print(f"error: outline file not found: {args.outline}", file=sys.stderr)
        return 2
    issues = check_outline(args.outline, args.wiki)
    for i in issues:
        print(f"{i.code} {i.path}:row{i.line} {i.msg}")
    errors = sum(i.severity == "error" for i in issues)
    warnings = sum(i.severity == "warning" for i in issues)
    print(f"SUMMARY rows={len(_rows(args.outline))} errors={errors} warnings={warnings}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
