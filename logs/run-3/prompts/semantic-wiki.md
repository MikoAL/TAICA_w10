You are an independent fact-checker. A markdown wiki about JEPA claims every statement is backed by a verbatim quote from a source. A script already confirmed each quote exists in the source. Your job is what the script cannot do: judge whether the quote actually SUPPORTS the claim it is attached to.

Files (project root = the current repo): `wiki/concepts/*.md` (9 pages), `wiki/sources/*.md` (6 pages); source texts in `raw/<id>/*.txt` (PDF text is two-column, so sentences may be interleaved). Text marked （AI 補充） is the AI's own explanation and needs no quote, but report it if it contradicts the sources. Numbers marked （表 N） must match the right row/column of that table in raw.

Rules: read ONLY wiki/ (not wiki/log.md) and raw/. Do NOT read index.html, logs/, slides/, work/, submission.md, README.md or git history. Judge against raw text, not outside knowledge.
For each cited paragraph / bullet / table row: SUPPORTED; PARTIAL (the source supports it but the attached quote does not, or a hedge/comparator/condition is missing); WRONG (the source says something else).

Write `logs/run-3/semantic-wiki.md` in Traditional Chinese:
# 語意檢查：Wiki → 原文（run-3）
## 有問題的項目
| 頁 | 行 | 判定 | Wiki 寫的 | 原文（附檔案:行） | 建議 |
|---|---|---|---|---|---|
## 每頁統計
| 頁 | 檢查項數 | SUPPORTED | PARTIAL | WRONG |
|---|---|---|---|---|

Be strict and specific, but do not list pure wording taste. Reply with the totals and every WRONG and PARTIAL item.
