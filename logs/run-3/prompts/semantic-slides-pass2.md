You are an independent fact-checker. A teaching slide deck (Traditional Chinese) was written using ONLY a markdown wiki as its knowledge source. For every slide, check whether each claim is supported by the wiki pages that slide cites.

Files (project root = the current repo):
- Deck: `index.html`. Each `<section>` is one slide (number them 1..16 in document order; slide 1 is the title slide, skip it). `data-wiki="path#anchor,..."` lists the wiki pages (relative to `wiki/`) it was written from. INCLUDE `<aside class="notes">` (speaker notes), diagrams, and hidden quiz answers. Ignore only `<footer>`.
- Wiki: `wiki/concepts/*.md`, `wiki/sources/*.md`. Text marked （AI 補充） in the wiki is the AI's own explanation; on slides it must be inside a `<div class="ai-note">` box.

Rules:
- Read ONLY index.html and the cited wiki files (other wiki pages only to confirm something is NOT there). Do NOT read raw/, work/, logs/, slides/, submission.md, README.md or git history. No outside knowledge.
- SUPPORTED = cited pages state it (paraphrase OK). UNSUPPORTED = not stated in the cited pages (say which page would support it), or stronger/different (dropped hedge or caveat, missing comparator, changed number, superlative, unmarked AI explanation). MISLEADING = supported but likely to give a beginner a wrong impression, including diagrams.
- Speaker notes: teaching instructions ("ask the class…") are fine; factual claims about JEPA must be supported.

Write `logs/run-3/semantic-slides-pass2.md` in Traditional Chinese:
# 語意檢查：簡報 → Wiki（run-3 第 2 次）
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
(one row per content slide)
## 統計
SUPPORTED n / UNSUPPORTED n / MISLEADING n

Be strict and specific; a false "all good" is worse than a nitpick. Reply with the counts and every non-SUPPORTED slide with its problem.
