"""Shared quote-matching helpers: normalize text and look up quotes in raw sources."""
import re
import unicodedata
from pathlib import Path

SOURCE_FILES = {
    "meta-lecun-blog": "meta-lecun-blog/page.txt",
    "meta-ijepa-blog": "meta-ijepa-blog/page.txt",
    "ijepa": "ijepa/paper.txt",
    "vjepa": "vjepa/paper.txt",
    "vicreg": "vicreg/paper.txt",
    "jepa-anything": "jepa-anything/paper_html.txt",
}
# Extra text versions of the same source that also count as a match.
ALT_FILES = {"jepa-anything": ["jepa-anything/paper.txt"]}

_QUOTES = {"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-"}


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for k, v in _QUOTES.items():
        s = s.replace(k, v)
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)  # re-join hyphenated line breaks
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def _squash(s: str) -> str:
    """Fallback: drop all whitespace (pdftotext sometimes splits words, e.g. 'VICR EG')."""
    return re.sub(r"\s+", "", s)


def find_quote(quote: str, text: str) -> bool:
    q, t = normalize(quote), normalize(text)
    if q in t:
        return True
    return _squash(q) in _squash(t)


def load_source(raw_dir: Path, source_id: str) -> str:
    paths = [SOURCE_FILES[source_id]] + ALT_FILES.get(source_id, [])
    return "\n".join(
        (raw_dir / p).read_text(encoding="utf-8", errors="ignore") for p in paths if (raw_dir / p).exists()
    )


def slug(heading: str) -> str:
    """GitHub-style heading anchor: lowercase, drop punctuation (keep CJK, letters, digits, '-', '_'), spaces -> '-'."""
    h = heading.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)  # \w keeps CJK in Python 3
    return h.replace(" ", "-")
