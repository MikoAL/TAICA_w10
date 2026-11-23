You are an independent fact-checker. `logs/run-3/wiki-changes.diff` lists the lines changed in a markdown wiki about JEPA (added lines start with `+`). A script already confirmed each footnote quote exists in the source text. Judge only the ADDED/CHANGED claims: does the attached quote (or the raw text it comes from) actually SUPPORT the claim, with its hedges, comparators and conditions?

Read ONLY that diff, wiki/concepts, wiki/sources, and raw/<id>/*.txt (PDF text is two-column, sentences may be interleaved; search tables and appendices before saying something is absent). Do NOT read index.html, other logs, slides/, work/, submission.md, README.md or git history. No outside knowledge. Text marked （AI 補充） needs no quote, but report it if it contradicts the sources.

Write `logs/run-3/semantic-wiki-recheck.md` in Traditional Chinese:
# 語意複查：run-3 改過的 Wiki 內容 → 原文
| 頁 | 行 | 判定（SUPPORTED / PARTIAL / WRONG） | Wiki 寫的 | 原文（檔案:行） | 建議 |
|---|---|---|---|---|---|
(list every PARTIAL / WRONG; SUPPORTED ones only as a count)
## 統計
SUPPORTED n / PARTIAL n / WRONG n

Skip wording taste. Reply with the totals and each PARTIAL/WRONG item.
