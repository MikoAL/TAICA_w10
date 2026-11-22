#!/usr/bin/env python3
"""Lint the JEPA wiki: frontmatter, footnotes, citations, numbers, links, orphan pages.

Usage: python3 scripts/check_wiki.py [--wiki DIR] [--raw DIR]
Exit code is 1 if any error is found, else 0.
"""
import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from quotes import SOURCE_FILES, find_quote, load_source, normalize

REPO = Path(__file__).resolve().parent.parent
SKIP_HEADINGS = {"引文", "相關頁面"}  # sections whose content is never checked
FOOTNOTE_DEF = re.compile(r'^\[\^([^\]]+)\]:\s*\[[^\]]*\]\([^)]*\)\s*—\s*"(.*)"\s*$')
FOOTREF = re.compile(r"\[\^([^\]]+)\]")
LINK = re.compile(r'\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
LIST_ITEM = re.compile(r"^(?:[-*]|\d+\.)\s")
TABLE_SEP = re.compile(r"^\s*\|[\s|:-]*---")
TABLE_MARK = re.compile(r"[（(]表\s*\d+[）)]")
NUMBER = re.compile(r"(?<![A-Za-z0-9.\-/])\d+(?:\.\d+)?(?![A-Za-z0-9])")
AI_NOTE = re.compile(r"^（AI 補充）")
YEAR = re.compile(r"(19|20)\d\d")


@dataclass
class Issue:
    code: str
    severity: str  # "error" | "warning"
    path: str
    line: int
    msg: str


def _fence_mask(lines):
    """True for every line inside a code fence or $$ math block, including the delimiter lines."""
    mask, inside = [], False
    for line in lines:
        st = line.strip()
        if st.startswith("```"):
            inside = not inside
            mask.append(True)
        elif not inside and st.startswith("$$"):  # display math: one-line $$...$$ or opening/closing $$
            mask.append(True)
            if not (len(st) > 2 and st.endswith("$$")):
                inside = not inside
        else:
            mask.append(inside)
    return mask


def _frontmatter_end(lines):
    """Index of the closing '---' line, or None if there is no closed frontmatter block."""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i
    return None


def _links(lines, mask):
    """Yield (lineno, path) for local markdown link targets outside code fences."""
    for i, line in enumerate(lines):
        if mask[i]:
            continue
        for m in LINK.finditer(line):
            target = m.group(1)
            if not target.startswith(("http", "#", "mailto:")):
                yield i + 1, target.split("#")[0]


def _footnote_defs(lines, mask, rel, raw_dir, sources, out):
    """Validate footnote definition lines. Returns {footnote_id: normalized quote, or None if malformed}."""
    defs = {}
    for i, line in enumerate(lines):
        if mask[i] or not line.startswith("[^"):
            continue
        no = i + 1
        idm = re.match(r"\[\^([^\]]+)\]", line)
        fm = FOOTNOTE_DEF.match(line)
        sid, _, num = idm.group(1).rpartition("-") if idm else ("", "", "")
        if not fm or not sid or not num.isdigit():
            out.append(Issue("BAD_FOOTNOTE", "error", rel, no, f"malformed footnote definition: {line[:60]}"))
            defs[idm.group(1) if idm else line] = None
            continue
        fid, quote = idm.group(1), fm.group(2)
        defs[fid] = normalize(quote)
        if sid not in SOURCE_FILES:
            out.append(Issue("UNKNOWN_SOURCE", "error", rel, no, f"unknown source id '{sid}'"))
            continue
        if sid not in sources:
            sources[sid] = load_source(raw_dir, sid)
        if not quote.strip() or not find_quote(quote, sources[sid]):
            out.append(Issue("QUOTE_NOT_FOUND", "error", rel, no, f"quote not found in raw/{SOURCE_FILES[sid]}"))
    return defs


def _blocks(lines, mask, start):
    """Split body lines into citable blocks, each a list of (lineno, text)."""
    blocks, cur, kind, in_table, skip = [], [], None, False, False

    def close():
        nonlocal cur, kind
        if cur:
            blocks.append(cur)
        cur, kind = [], None

    for i in range(start, len(lines)):
        line, no = lines[i], i + 1
        if mask[i]:
            close()
            continue
        if line.startswith("#"):
            close()
            in_table = False
            skip = line.lstrip("#").strip() in SKIP_HEADINGS
            continue
        if skip:
            continue
        s = line.strip()
        if not s or line.startswith("[^"):
            close()
            in_table = False
            continue
        if s.startswith("|"):
            close()
            if not in_table:  # first row of a table is the header: not checked
                in_table = True
            elif not TABLE_SEP.match(line):
                blocks.append([(no, line)])
            continue
        in_table = False
        if LIST_ITEM.match(line):
            close()
            kind = "list"
        elif kind == "list" and not line[0].isspace():
            close()
            kind = "para"
        elif not cur:
            kind = "para"
        cur.append((no, line))
    close()
    return blocks


def _check_block(block, defs, rel, out, sources=None):
    """Check one block for citation presence and for numbers that appear in its cited quotes."""
    text = "\n".join(t for _, t in block)
    if AI_NOTE.match(LIST_ITEM.sub("", block[0][1].strip(), count=1)):
        out.append(Issue("AI_NOTE", "warning", rel, block[0][0], "AI-added explanation (no source)"))
        return
    if "[^" not in text:
        out.append(Issue("UNCITED_PARAGRAPH", "error", rel, block[0][0], "block has no [^...] citation"))
    quotes = [defs[f] for f in FOOTREF.findall(text) if defs.get(f)]
    table = TABLE_MARK.search(text) is not None
    for no, line in block:
        body = re.sub(r"\]\([^)]*\)", "]", re.sub(r"\[\^[^\]]*\]", "", line))
        body = LIST_ITEM.sub("", body.lstrip(), count=1)
        body = TABLE_MARK.sub("", body)
        for m in NUMBER.finditer(body):
            n = m.group()
            if YEAR.fullmatch(n) or any(re.search(rf"(?<![\d.]){re.escape(n)}(?!\d)", q) for q in quotes):
                continue
            if table:
                cited = {f.rpartition("-")[0] for f in FOOTREF.findall(text)}
                if not any(re.search(rf"(?<![\d.]){re.escape(n)}(?!\d)", (sources or {}).get(sid, ""))
                           for sid in cited):
                    out.append(Issue("TABLE_NUMBER_NOT_IN_SOURCE", "error", rel, no,
                                     f"table number {n} appears nowhere in the cited source text"))
                    continue
                out.append(Issue("TABLE_NUMBER_UNVERIFIED", "warning", rel, no,
                                 f"number {n} not in cited quote (table reference, verify manually)"))
            else:
                out.append(Issue("NUMBER_NOT_IN_QUOTE", "error", rel, no, f"number {n} not in any cited quote"))


def _check_page(path, rel, raw_dir, sources, out):
    """Run every per-page rule on one wiki page."""
    lines = path.read_text(encoding="utf-8").splitlines()
    mask = _fence_mask(lines)
    close = _frontmatter_end(lines)
    if close is None:
        out.append(Issue("MISSING_FRONTMATTER", "error", rel, 1, "no closing --- frontmatter block"))
        start = 0
    else:
        keys = {ln.split(":", 1)[0].strip() for ln in lines[1:close]}
        missing = [k for k in ("title", "type", "sources") if k not in keys]
        if missing:
            out.append(Issue("MISSING_FRONTMATTER", "error", rel, 1, f"frontmatter lacks {', '.join(missing)}"))
        start = close + 1

    defs = _footnote_defs(lines, mask, rel, raw_dir, sources, out)

    seen = set()
    for i, line in enumerate(lines):
        if mask[i] or line.startswith("[^"):
            continue
        for fid in FOOTREF.findall(line):
            if fid not in defs and fid not in seen:
                seen.add(fid)
                out.append(Issue("MISSING_FOOTNOTE", "error", rel, i + 1, f"no definition for [^{fid}]"))

    for block in _blocks(lines, mask, start):
        _check_block(block, defs, rel, out, sources)

    for no, target in _links(lines, mask):
        if not (path.parent / target).exists():
            out.append(Issue("BROKEN_LINK", "error", rel, no, f"link target not found: {target}"))


def check(wiki_dir: Path, raw_dir: Path) -> list[Issue]:
    """Return all issues for the wiki, sorted by path and line."""
    wiki_dir, raw_dir = wiki_dir.resolve(), raw_dir.resolve()
    base = wiki_dir.parent
    out, sources = [], {}
    pages = sorted(p for d in ("concepts", "sources") if (wiki_dir / d).is_dir()
                   for p in (wiki_dir / d).rglob("*.md"))
    for page in pages:
        _check_page(page, str(page.relative_to(base)), raw_dir, sources, out)

    index = wiki_dir / "index.md"
    for name in ("index.md", "log.md"):  # these two only get the broken-link check
        f = wiki_dir / name
        if f.exists():
            lines = f.read_text(encoding="utf-8").splitlines()
            for no, target in _links(lines, _fence_mask(lines)):
                if not (f.parent / target).exists():
                    out.append(Issue("BROKEN_LINK", "error", str(f.relative_to(base)), no,
                                     f"link target not found: {target}"))

    linked = set()
    if index.exists():
        lines = index.read_text(encoding="utf-8").splitlines()
        linked = {(index.parent / t).resolve() for _, t in _links(lines, _fence_mask(lines))}
    for page in pages:
        if page.resolve() not in linked:
            out.append(Issue("ORPHAN_PAGE", "warning", str(page.relative_to(base)), 1,
                             "page is not linked from index.md"))

    out.sort(key=lambda i: (i.path, i.line))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check wiki pages against the citation rules.")
    ap.add_argument("--wiki", type=Path, default=REPO / "wiki", help="wiki directory")
    ap.add_argument("--raw", type=Path, default=REPO / "raw", help="raw source directory")
    args = ap.parse_args(argv)
    issues = check(args.wiki, args.raw)
    for i in issues:
        print(f"{i.code} {i.path}:{i.line} {i.msg}")
    errors = sum(i.severity == "error" for i in issues)
    warnings = sum(i.severity == "warning" for i in issues)
    print(f"SUMMARY errors={errors} warnings={warnings}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
