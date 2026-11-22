"""Verify every > "quote" in work/takeaways/<id>.md appears in raw/<id>."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from quotes import find_quote, load_source  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
QUOTE_RE = re.compile(r'^\s*>\s*"(.+)"\s*$')


def main() -> int:
    errors = total = 0
    for note in sorted((ROOT / "work/takeaways").glob("*.md")):
        sid = note.stem
        text = load_source(ROOT / "raw", sid)
        for n, line in enumerate(note.read_text(encoding="utf-8").splitlines(), 1):
            m = QUOTE_RE.match(line)
            if not m:
                continue
            total += 1
            if not find_quote(m.group(1), text):
                errors += 1
                print(f"QUOTE_NOT_FOUND work/takeaways/{note.name}:{n} {m.group(1)[:80]}")
    print(f"SUMMARY quotes={total} errors={errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
