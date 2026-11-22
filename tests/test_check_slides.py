import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_slides import check_slides  # noqa: E402

WIKI_PAGE = """---
title: JEPA
type: concept
sources: [ijepa]
---
# JEPA（Joint-Embedding Predictive Architecture）

## 三個零件
用 16 張 A100、不到 72 小時。[^ijepa-1]

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "using 16 A100 GPUs in under 72 hours"
"""

GH = "https://github.com/MikoAL/TAICA_w10/blob/main/wiki/"


def deck(*sections: str) -> str:
    return ('<html><body><div class="reveal"><div class="slides">'
            + "".join(sections) + "</div></div></body></html>")


def slide(body: str, refs: str = "concepts/jepa.md#三個零件", footer: str | None = None) -> str:
    if footer is None:
        footer = "".join(f'<a href="{GH}{r}">{r}</a>' for r in refs.split(",")) if refs else ""
    attr = f' data-wiki="{refs}"' if refs else ""
    return f'<section{attr}>{body}<footer class="src">來源：{footer}</footer></section>'


class TestCheckSlides(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.wiki = base / "wiki"
        (self.wiki / "concepts").mkdir(parents=True)
        (self.wiki / "concepts" / "jepa.md").write_text(WIKI_PAGE, encoding="utf-8")
        self.html = base / "index.html"

    def tearDown(self):
        self.tmp.cleanup()

    def codes(self, html: str):
        self.html.write_text(html, encoding="utf-8")
        return [i.code for i in check_slides(self.html, self.wiki) if i.severity == "error"]

    def test_slide_ok(self):
        self.assertEqual(self.codes(deck(slide("<h2>JEPA</h2><p>16 張 A100、72 小時</p>"))), [])

    def test_title_slide_exempt(self):
        html = deck('<section data-kind="title"><h1>JEPA 2026</h1></section>', slide("<p>JEPA</p>"))
        self.assertEqual(self.codes(html), [])

    def test_slide_missing_ref(self):
        self.assertEqual(self.codes(deck(slide("<p>JEPA</p>", refs=""))), ["NO_WIKI_REF"])

    def test_slide_missing_page(self):
        self.assertIn("WIKI_PAGE_MISSING", self.codes(deck(slide("<p>x</p>", refs="concepts/nope.md"))))

    def test_slide_missing_anchor(self):
        self.assertEqual(self.codes(deck(slide("<p>x</p>", refs="concepts/jepa.md#不存在"))),
                         ["WIKI_ANCHOR_MISSING"])

    def test_slide_number_unsupported(self):
        # 87.8 is not anywhere in the cited wiki page; numbers in speaker notes and footer are ignored
        body = '<p>準確度 87.8</p><aside class="notes">講者備註 99</aside>'
        self.assertEqual(self.codes(deck(slide(body))), ["SLIDE_NUMBER_UNSUPPORTED"])

    def test_footer_must_link_every_ref(self):
        html = deck(slide("<p>x</p>", footer="（沒有連結）"))
        self.assertEqual(self.codes(html), ["FOOTER_MISSING_LINK"])


if __name__ == "__main__":
    unittest.main()
