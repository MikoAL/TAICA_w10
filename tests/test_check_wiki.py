import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_wiki import check  # noqa: E402
from quotes import find_quote  # noqa: E402

RAW_TEXT = """Joint-Embedding Predictive Architectures learn to predict the embeddings of a signal y
from a compatible signal x. We train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in
under 72 hours to achieve strong down-
stream performance. It is “notoriously” hard."""

GOOD_QUOTE = "Joint-Embedding Predictive Architectures learn to predict the embeddings of a signal y"


def page(body: str, sources: str = "[ijepa]") -> str:
    return f"---\ntitle: T\ntype: concept\nsources: {sources}\n---\n" + textwrap.dedent(body)


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.raw = base / "raw"
        self.wiki = base / "wiki"
        (self.raw / "ijepa").mkdir(parents=True)
        (self.raw / "ijepa" / "paper.txt").write_text(RAW_TEXT, encoding="utf-8")
        (self.wiki / "concepts").mkdir(parents=True)
        (self.wiki / "sources").mkdir(parents=True)
        (self.wiki / "sources" / "ijepa.md").write_text(
            page(f"""
            # I-JEPA
            重點。[^ijepa-1]

            ## 引文
            [^ijepa-1]: [ijepa](ijepa.md) — "{GOOD_QUOTE}"
            """),
            encoding="utf-8",
        )
        (self.wiki / "index.md").write_text(
            "# Index\n- [I-JEPA](sources/ijepa.md)\n- [A](concepts/a.md)\n", encoding="utf-8"
        )

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, body: str, name: str = "a.md"):
        (self.wiki / "concepts" / name).write_text(page(body), encoding="utf-8")

    def codes(self):
        return [i.code for i in check(self.wiki, self.raw) if i.severity == "error"]


class TestCheckWiki(Fixture):
    def test_quote_found(self):
        self.write(f"""
        # A
        JEPA 在表示空間預測。[^ijepa-1]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "{GOOD_QUOTE}"
        """)
        self.assertEqual(self.codes(), [])

    def test_quote_normalization(self):
        # hyphenated line break ("down-\nstream") and curly quotes in raw text
        self.write("""
        # A
        句子。[^ijepa-1] 另一句。[^ijepa-2]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "to achieve strong downstream performance"
        [^ijepa-2]: [ijepa](../sources/ijepa.md) — "It is "notoriously" hard."
        """)
        self.assertEqual(self.codes(), [])
        self.assertTrue(find_quote("It is “notoriously” hard", 'it is "notoriously" hard'))

    def test_quote_not_found(self):
        self.write("""
        # A
        句子。[^ijepa-1]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "JEPA beats every other method on every benchmark"
        """)
        self.assertEqual(self.codes(), ["QUOTE_NOT_FOUND"])

    def test_unknown_source(self):
        self.write("""
        # A
        句子。[^wiki-1]

        ## 引文
        [^wiki-1]: [wiki](../sources/wiki.md) — "anything at all goes here ok"
        """)
        self.assertIn("UNKNOWN_SOURCE", self.codes())

    def test_uncited_paragraph(self):
        self.write(f"""
        # A
        有引用的段落。[^ijepa-1]

        這段沒有引用。

        - 這個條列也沒有引用

        ## 相關頁面
        - [I-JEPA](../sources/ijepa.md)

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "{GOOD_QUOTE}"
        """)
        self.assertEqual(self.codes(), ["UNCITED_PARAGRAPH", "UNCITED_PARAGRAPH"])

    def test_broken_link(self):
        self.write(f"""
        # A
        見 [不存在](nope.md)。[^ijepa-1]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "{GOOD_QUOTE}"
        """)
        self.assertEqual(self.codes(), ["BROKEN_LINK"])

    def test_number_not_in_quote(self):
        self.write(f"""
        # A
        用 16 張 A100 訓練不到 72 小時。[^ijepa-1]

        只用 12 張標註圖。[^ijepa-1]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "{GOOD_QUOTE}"
        """)
        self.assertEqual(self.codes(), ["NUMBER_NOT_IN_QUOTE"] * 3)

    def test_number_in_quote_ok_and_model_names_ignored(self):
        # 16 and 72 are in the quote; "ViT-H/14", "L2" and the year are not numbers to check
        self.write("""
        # A
        2023 年的 ViT-H/14 用 16 張 A100、不到 72 小時，loss 是 L2 距離。[^ijepa-1]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "ImageNet using 16 A100 GPUs in under 72 hours"
        """)
        self.assertEqual(self.codes(), [])

    def test_table_number_is_warning(self):
        self.write(f"""
        # A
        像素 40.7、表示 66.9（表 7）。[^ijepa-1]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "{GOOD_QUOTE}"
        """)
        issues = check(self.wiki, self.raw)
        self.assertEqual([i.code for i in issues if i.severity == "error"], [])
        self.assertIn("TABLE_NUMBER_UNVERIFIED", [i.code for i in issues if i.severity == "warning"])

    def test_missing_frontmatter_and_footnote(self):
        (self.wiki / "concepts" / "a.md").write_text("# A\n句子。[^ijepa-9]\n", encoding="utf-8")
        self.assertEqual(sorted(self.codes()), ["MISSING_FOOTNOTE", "MISSING_FRONTMATTER"])

    def test_orphan_page_warning(self):
        self.write(f"""
        # B
        句子。[^ijepa-1]

        ## 引文
        [^ijepa-1]: [ijepa](../sources/ijepa.md) — "{GOOD_QUOTE}"
        """, name="b.md")
        warnings = [i.code for i in check(self.wiki, self.raw) if i.severity == "warning"]
        self.assertIn("ORPHAN_PAGE", warnings)


if __name__ == "__main__":
    unittest.main()
