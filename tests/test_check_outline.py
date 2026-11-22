import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_outline import check_outline  # noqa: E402

PAGE_WITH_CAVEAT = """---
title: I-JEPA
type: source
sources: [ijepa]
---
# I-JEPA

## 結果
預測表示 66.9、像素 40.7（表 7）。[^ijepa-1]

## 注意
完整微調 87.1 vs 87.8。[^ijepa-2]
"""

PAGE_NO_CAVEAT = """---
title: JEPA
type: concept
sources: [ijepa]
---
# JEPA

## 三個零件
context encoder、target encoder、predictor。[^ijepa-1]
"""

HEADER = "| # | 標題 | 教學目的 | 要點 | 但書 | 引用 Wiki |\n|---|---|---|---|---|---|\n"


class TestCheckOutline(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.wiki = base / "wiki"
        (self.wiki / "sources").mkdir(parents=True)
        (self.wiki / "concepts").mkdir(parents=True)
        (self.wiki / "sources" / "ijepa.md").write_text(PAGE_WITH_CAVEAT, encoding="utf-8")
        (self.wiki / "concepts" / "jepa.md").write_text(PAGE_NO_CAVEAT, encoding="utf-8")
        self.outline = base / "outline.md"

    def tearDown(self):
        self.tmp.cleanup()

    def codes(self, rows: str):
        self.outline.write_text("# 大綱\n\n" + HEADER + rows, encoding="utf-8")
        return [i.code for i in check_outline(self.outline, self.wiki) if i.severity == "error"]

    def test_ok(self):
        rows = ("| 0 | 封面 | 封面 | — | — | （封面，不引用） |\n"
                "| 1 | 零件 | 概念 | 三個零件 | — | `concepts/jepa.md#三個零件` |\n"
                "| 2 | 證據 | 證據 | 66.9 vs 40.7 | 微調 87.1 vs 87.8 | `sources/ijepa.md#結果`、`#注意` |\n")
        self.assertEqual(self.codes(rows), [])

    def test_missing_anchor(self):
        rows = "| 1 | 零件 | 概念 | x | — | `concepts/jepa.md#沒有這節` |\n"
        self.assertEqual(self.codes(rows), ["OUTLINE_REF_MISSING"])

    def test_shorthand_anchor_uses_previous_file(self):
        rows = "| 1 | 零件 | 概念 | x | — | `concepts/jepa.md#三個零件`、`#不存在` |\n"
        self.assertEqual(self.codes(rows), ["OUTLINE_REF_MISSING"])

    def test_number_unsupported(self):
        rows = "| 1 | 零件 | 概念 | 準確度 99.9 | — | `concepts/jepa.md#三個零件` |\n"
        self.assertEqual(self.codes(rows), ["OUTLINE_NUMBER_UNSUPPORTED"])

    def test_caveat_required_when_cited_page_has_caveats(self):
        # run-1 finding: slides dropped the 注意 caveats of the pages they cited
        rows = "| 1 | 證據 | 證據 | 66.9 vs 40.7 | — | `sources/ijepa.md#結果` |\n"
        self.assertEqual(self.codes(rows), ["OUTLINE_CAVEAT_MISSING"])

    def test_caveat_can_be_explicitly_waived(self):
        rows = "| 1 | 證據 | 證據 | 66.9 vs 40.7 | 無：下一頁專講 | `sources/ijepa.md#結果` |\n"
        self.assertEqual(self.codes(rows), [])

    def test_missing_table_is_error(self):
        self.outline.write_text("# 大綱\n\n沒有表格。\n", encoding="utf-8")
        codes = [i.code for i in check_outline(self.outline, self.wiki) if i.severity == "error"]
        self.assertEqual(codes, ["OUTLINE_TABLE_MISSING"])


if __name__ == "__main__":
    unittest.main()
