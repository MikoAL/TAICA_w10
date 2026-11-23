# 先前各次 subagent 的 prompt（run-3 時從 Claude Code 對話逐字稿匯出，本機路徑改成 `<repo>`）

## 2026-11-23 00:48:17　Takeaways: I-JEPA paper（model: sonnet）

````text
You are preparing a pre-discussion note for one source being ingested into an "LLM Wiki" (Karpathy-style markdown knowledge base) about JEPA (Joint-Embedding Predictive Architecture). The wiki will later feed a teaching slide deck (Traditional Chinese, English terms kept) for university students who know roughly what a neural network is but have never studied self-supervised learning.

Source: <repo>/raw/ijepa/paper.txt (pdftotext -layout of the I-JEPA paper, Assran et al., CVPR 2023, arXiv 2301.08243). Read the WHOLE file (use Read with offset/limit in chunks). Do not use any outside knowledge for facts; everything must come from this file.

Write the note to <repo>/work/takeaways/ijepa.md in English, with these sections:

1. `## One-line summary`
2. `## Key takeaways` — 5–8 bullets, the things a beginner must get from this source. Each bullet ends with one supporting quote in this exact form: `> "exact quote"` on the next line. 
3. `## Numbers` — every quantitative result worth teaching (dataset, metric, value, comparison), each with an exact quote.
4. `## Concepts a beginner needs` — terms this source defines or relies on, with a one-line plain explanation as this source frames it.
5. `## Proposed wiki pages` — which concept pages this source should create or update (slug-style names like `jepa`, `collapse`, `masking-strategy`), one line why.
6. `## Caveats / limitations / things that might conflict with other sources` — including claims that sound like hype, and what the paper itself admits.
7. `## Questions for the human` — 1–3 genuine questions about scope/emphasis that the human should decide.

QUOTE RULES (a script will verify every quote by searching the source file after normalizing whitespace and removing hyphenation at line ends): quotes must be copied character-for-character from the file, contiguous, 5–30 words, no ellipses, no paraphrase, no added punctuation. The file is two-column layout text, so a sentence may be split across columns — pick quotes that sit inside one contiguous run of text. Avoid quoting math symbols or table cells; for table numbers, quote the nearby prose sentence that states the number if one exists, otherwise write `(table N, not quotable)`.

Keep the note under 900 words. Reply with just the file path and a 2-line summary when done.
````

## 2026-11-23 00:48:24　Takeaways: V-JEPA paper（model: sonnet）

````text
You are preparing a pre-discussion note for one source being ingested into an "LLM Wiki" (Karpathy-style markdown knowledge base) about JEPA (Joint-Embedding Predictive Architecture). The wiki will later feed a teaching slide deck (Traditional Chinese, English terms kept) for university students who know roughly what a neural network is but have never studied self-supervised learning.

Source: <repo>/raw/vjepa/paper.txt (pdftotext -layout of the V-JEPA paper, Bardes et al., "Revisiting Feature Prediction for Learning Visual Representations from Video", arXiv 2404.08471). Read the WHOLE file (use Read with offset/limit in chunks). Do not use any outside knowledge for facts; everything must come from this file.

Write the note to <repo>/work/takeaways/vjepa.md in English, with these sections:

1. `## One-line summary`
2. `## Key takeaways` — 5–8 bullets, the things a beginner must get from this source. Each bullet ends with one supporting quote in this exact form: `> "exact quote"` on the next line.
3. `## Numbers` — every quantitative result worth teaching (dataset, metric, value, comparison), each with an exact quote.
4. `## Concepts a beginner needs` — terms this source defines or relies on, with a one-line plain explanation as this source frames it.
5. `## Proposed wiki pages` — which concept pages this source should create or update (slug-style names like `jepa`, `collapse`, `pixel-vs-feature-prediction`), one line why.
6. `## Caveats / limitations / things that might conflict with other sources` — including claims that sound like hype, and what the paper itself admits.
7. `## Questions for the human` — 1–3 genuine questions about scope/emphasis that the human should decide.

QUOTE RULES (a script will verify every quote by searching the source file after normalizing whitespace and removing hyphenation at line ends): quotes must be copied character-for-character from the file, contiguous, 5–30 words, no ellipses, no paraphrase, no added punctuation. The file is two-column layout text, so a sentence may be split across columns — pick quotes that sit inside one contiguous run of text. Avoid quoting math symbols or table cells; for table numbers, quote the nearby prose sentence that states the number if one exists, otherwise write `(table N, not quotable)`.

Keep the note under 900 words. Reply with just the file path and a 2-line summary when done.
````

## 2026-11-23 00:48:31　Takeaways: VICReg paper（model: sonnet）

````text
You are preparing a pre-discussion note for one source being ingested into an "LLM Wiki" (Karpathy-style markdown knowledge base) about JEPA (Joint-Embedding Predictive Architecture). The wiki will later feed a teaching slide deck (Traditional Chinese, English terms kept) for university students who know roughly what a neural network is but have never studied self-supervised learning. This source's role in the wiki is mainly to explain representation collapse and how to prevent it.

Source: <repo>/raw/vicreg/paper.txt (pdftotext -layout of VICReg, Bardes, Ponce, LeCun, ICLR 2022, arXiv 2105.04906). Read the WHOLE file (use Read with offset/limit in chunks). Do not use any outside knowledge for facts; everything must come from this file.

Write the note to <repo>/work/takeaways/vicreg.md in English, with these sections:

1. `## One-line summary`
2. `## Key takeaways` — 5–8 bullets, the things a beginner must get from this source. Each bullet ends with one supporting quote in this exact form: `> "exact quote"` on the next line.
3. `## Numbers` — every quantitative result worth teaching (dataset, metric, value, comparison), each with an exact quote.
4. `## Concepts a beginner needs` — terms this source defines or relies on (e.g. Siamese/joint-embedding, collapse, variance/invariance/covariance terms), with a one-line plain explanation as this source frames it.
5. `## Proposed wiki pages` — which concept pages this source should create or update (slug-style names), one line why.
6. `## Caveats / limitations / things that might conflict with other sources`.
7. `## Questions for the human` — 1–3 genuine questions about scope/emphasis that the human should decide.

QUOTE RULES (a script will verify every quote by searching the source file after normalizing whitespace and removing hyphenation at line ends): quotes must be copied character-for-character from the file, contiguous, 5–30 words, no ellipses, no paraphrase, no added punctuation. Note pdftotext may have mangled small-caps (e.g. "VICR EG"); quote text as it literally appears in the file. Pick quotes inside one contiguous run of text. Avoid quoting math symbols or table cells; for table numbers, quote the nearby prose sentence that states the number if one exists, otherwise write `(table N, not quotable)`.

Keep the note under 900 words. Reply with just the file path and a 2-line summary when done.
````

## 2026-11-23 00:48:39　Takeaways: JEPA-Anything paper（model: sonnet）

````text
You are preparing a pre-discussion note for one source being ingested into an "LLM Wiki" (Karpathy-style markdown knowledge base) about JEPA (Joint-Embedding Predictive Architecture). The wiki will later feed a teaching slide deck (Traditional Chinese, English terms kept) for university students who know roughly what a neural network is but have never studied self-supervised learning. In the deck this paper will be the final "frontier / latest progress" part, so the note should focus on: what problem it tackles, the core idea in plain terms, the headline reported results, and limitations — not every experiment detail.

Source: <repo>/raw/jepa-anything/paper_html.txt (text extracted from the arXiv HTML of "JEPA-Anything: Learning Predictive Models across Different Worlds", arXiv 2609.20800v1, Sept 2026). A pdftotext version is at raw/jepa-anything/paper.txt in the same project if the HTML text is unclear somewhere. Read the WHOLE HTML-text file (use Read with offset/limit in chunks). This paper is newer than your training data: use NO outside knowledge; everything must come from the file.

Write the note to <repo>/work/takeaways/jepa-anything.md in English, with these sections:

1. `## One-line summary`
2. `## Key takeaways` — 5–8 bullets. Each bullet ends with one supporting quote in this exact form: `> "exact quote"` on the next line.
3. `## Numbers` — the headline quantitative results the paper reports, each with an exact quote.
4. `## Concepts a beginner needs` — terms this source defines or relies on, with a one-line plain explanation as this source frames it.
5. `## Proposed wiki pages` — which concept pages this source should create or update (slug-style names), one line why.
6. `## Caveats / limitations / things that might conflict with other sources` — what the paper itself admits (e.g. where standard JEPA wins), and the fact it is a v1 preprint.
7. `## Questions for the human` — 1–3 genuine questions about scope/emphasis.

QUOTE RULES (a script will verify every quote by searching paper_html.txt after normalizing whitespace and removing hyphenation at line ends): quotes must be copied character-for-character from paper_html.txt, contiguous, 5–30 words, no ellipses, no paraphrase, no added punctuation. Math was stripped from the HTML text, so avoid quoting sentences with formulas. For table-only numbers write `(table N, not quotable)`.

Keep the note under 900 words. Reply with just the file path and a 2-line summary when done.
````

## 2026-11-23 00:48:48　Takeaways: two Meta blog posts（model: sonnet）

````text
You are preparing pre-discussion notes for two sources being ingested into an "LLM Wiki" (Karpathy-style markdown knowledge base) about JEPA (Joint-Embedding Predictive Architecture). The wiki will later feed a teaching slide deck (Traditional Chinese, English terms kept) for university students who know roughly what a neural network is but have never studied self-supervised learning. These two blog posts are the beginner-friendly entry points: the "why" (LeCun's world-model vision) and the plain-language intro to I-JEPA.

Sources (read each WHOLE file; use no outside knowledge for facts):
- A: <repo>/raw/meta-lecun-blog/page.txt — Meta AI blog, "Yann LeCun on a vision to make AI systems learn and reason like animals and humans", Feb 23 2022. (Ignore site navigation / "recommended reads" boilerplate.)
- B: <repo>/raw/meta-ijepa-blog/page.txt — Meta AI blog, "I-JEPA: The first AI model based on Yann LeCun's vision for more human-like AI", June 13 2023.

Write TWO notes, in English:
- <repo>/work/takeaways/meta-lecun-blog.md
- <repo>/work/takeaways/meta-ijepa-blog.md

Each note has these sections:
1. `## One-line summary`
2. `## Key takeaways` — 5–8 bullets. Each bullet ends with one supporting quote in this exact form: `> "exact quote"` on the next line.
3. `## Numbers` — any quantitative claims, each with an exact quote.
4. `## Concepts a beginner needs` — terms the post introduces (e.g. world model, the modules of LeCun's architecture, self-supervised learning, representation), one-line plain explanation as the post frames it.
5. `## Proposed wiki pages` — slug-style concept page names this source should create or update (e.g. `world-model`, `jepa`, `self-supervised-learning`), one line why.
6. `## Caveats / things that might conflict with other sources` — marketing/hype language, claims stated without evidence, numbers that the underlying paper should be checked against.
7. `## Questions for the human` — 1–2 genuine questions about scope/emphasis.

QUOTE RULES (a script will verify every quote by searching the source file after normalizing whitespace): quotes must be copied character-for-character from the file, contiguous, 5–30 words, no ellipses, no paraphrase, no added punctuation. Watch for curly apostrophes (’) and quotes in the source — copy them exactly as they appear.

Keep each note under 700 words. Reply with just the two file paths and a 2-line summary when done.
````

## 2026-11-23 01:06:43　Semantic check: slides vs wiki（model: sonnet）

````text
You are an independent fact-checker. A teaching slide deck (Traditional Chinese) was written using ONLY a markdown wiki as its knowledge source. Your job: for every slide, check whether each claim on the slide is supported by the wiki pages that slide cites.

Files (project root <repo>):
- The deck: `index.html`. Each `<section>` is one slide (number them 1..15 in document order; slide 1 is the title slide with data-kind="title", skip it). Each content slide has `data-wiki="path#anchor,..."` listing the wiki pages (relative to `wiki/`) it was written from. Ignore `<aside class="notes">` (speaker notes) and the `<footer>`.
- The wiki: `wiki/concepts/*.md` and `wiki/sources/*.md`. Each wiki claim has a footnote with an exact English quote from the original paper. Text marked （AI 補充） in the wiki is the AI's own explanation, not from a source; on slides the equivalent is a `<div class="ai-note">` box.

Rules:
- Read ONLY index.html and the wiki files the slides cite (you may open other wiki pages only to confirm something is NOT in the wiki). Do NOT read `raw/`, `work/`, `logs/`, or anything else. Use no outside knowledge about JEPA — judge only against the wiki text.
- A claim is SUPPORTED if the cited wiki pages state it (translation/paraphrase is fine). UNSUPPORTED if the cited pages don't state it (even if another wiki page does — then say which page should be added to data-wiki), or if the slide says something stronger/different than the wiki (e.g. drops a caveat, changes a number, says "same setting" when the wiki says otherwise, turns "論文報告" into fact). AI-note boxes are fine if the wiki marks the same content as （AI 補充）; an unmarked AI explanation on a slide is UNSUPPORTED.
- Also flag MISLEADING: technically supported but likely to give a beginner a wrong impression.

Write your report to `logs/run-1/semantic.md` in Traditional Chinese, with this format:

# 語意檢查（run-1）
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
(one row per content slide; 判定 = SUPPORTED / UNSUPPORTED / MISLEADING; 問題 = empty or a short description quoting the slide text and naming which wiki page/heading does or doesn't support it)

## 統計
SUPPORTED n / UNSUPPORTED n / MISLEADING n

Be strict and specific; this report is part of a graded check record, and false "all good" is worse than a nitpick. Reply with the summary counts and the list of non-SUPPORTED slides.
````

## 2026-11-23 01:08:49　Semantic re-check pass 2（model: sonnet）

````text
You are an independent fact-checker. A teaching slide deck (Traditional Chinese) was written using ONLY a markdown wiki as its knowledge source. Your job: for every slide, check whether each claim on the slide is supported by the wiki pages that slide cites.

Files (project root <repo>):
- The deck: `index.html`. Each `<section>` is one slide (number them 1..15 in document order; slide 1 is the title slide with data-kind="title", skip it). Each content slide has `data-wiki="path#anchor,..."` listing the wiki pages (relative to `wiki/`) it was written from. Ignore `<aside class="notes">` (speaker notes) and the `<footer>`.
- The wiki: `wiki/concepts/*.md` and `wiki/sources/*.md`. Each wiki claim has a footnote with an exact English quote from the original paper. Text marked （AI 補充） in the wiki is the AI's own explanation, not from a source; on slides the equivalent is a `<div class="ai-note">` box.

Rules:
- Read ONLY index.html and the wiki files the slides cite (you may open other wiki pages only to confirm something is NOT in the wiki). Do NOT read `raw/`, `work/`, `logs/`, or anything else. Use no outside knowledge about JEPA — judge only against the wiki text.
- A claim is SUPPORTED if the cited wiki pages state it (translation/paraphrase is fine). UNSUPPORTED if the cited pages don't state it (even if another wiki page does — then say which page should be added to data-wiki), or if the slide says something stronger/different than the wiki (e.g. drops a caveat, changes a number, turns "論文報告/論文認為" into fact). AI-note boxes are fine if the wiki marks the same content as （AI 補充）; an unmarked AI explanation on a slide is UNSUPPORTED.
- Also flag MISLEADING: technically supported but likely to give a beginner a wrong impression.

Write your report to `logs/run-1/semantic-pass2.md` in Traditional Chinese:

# 語意檢查（run-1 第 2 次）
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
(one row per content slide; 判定 = SUPPORTED / UNSUPPORTED / MISLEADING; 問題 = empty or short description quoting slide text and naming the wiki page/heading)

## 統計
SUPPORTED n / UNSUPPORTED n / MISLEADING n

Be strict and specific; a false "all good" is worse than a nitpick. Reply with the summary counts and the list of non-SUPPORTED slides.
````

## 2026-11-23 01:12:51　Semantic check run-2 (final)（model: sonnet）

````text
You are an independent fact-checker. A teaching slide deck (Traditional Chinese) was written using ONLY a markdown wiki as its knowledge source. Your job: for every slide, check whether each claim on the slide is supported by the wiki pages that slide cites.

Files (project root <repo>):
- The deck: `index.html`. Each `<section>` is one slide (number them 1..16 in document order; slide 1 is the title slide with data-kind="title", skip it). Each content slide has `data-wiki="path#anchor,..."` listing the wiki pages (relative to `wiki/`) it was written from. Ignore `<aside class="notes">` (speaker notes) and the `<footer>`.
- The wiki: `wiki/concepts/*.md` and `wiki/sources/*.md`. Each wiki claim has a footnote with an exact English quote from the original paper. Text marked （AI 補充） in the wiki is the AI's own explanation, not from a source; on slides the equivalent is a `<div class="ai-note">` box.

Rules:
- Read ONLY index.html and the wiki files the slides cite (you may open other wiki pages only to confirm something is NOT in the wiki). Do NOT read `raw/`, `work/`, `logs/`, `slides/`, or anything else. Use no outside knowledge about JEPA — judge only against the wiki text.
- A claim is SUPPORTED if the cited wiki pages state it (translation/paraphrase is fine). UNSUPPORTED if the cited pages don't state it (even if another wiki page does — then say which page should be added to data-wiki), or if the slide says something stronger/different than the wiki (drops a caveat, changes a number, adds a superlative, turns "論文報告/論文認為" into fact). AI-note boxes are fine if the wiki marks the same content as （AI 補充）; an unmarked AI explanation on a slide is UNSUPPORTED.
- Also flag MISLEADING: technically supported but likely to give a beginner a wrong impression (including diagrams).

Write your report to `logs/run-2/semantic.md` in Traditional Chinese:

# 語意檢查（run-2）
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
(one row per content slide; 判定 = SUPPORTED / UNSUPPORTED / MISLEADING; 問題 = empty or short description quoting slide text and naming the wiki page/heading)

## 統計
SUPPORTED n / UNSUPPORTED n / MISLEADING n

## 小建議（不影響判定）
(optional nitpicks)

Be strict and specific; a false "all good" is worse than a nitpick. Reply with the summary counts and the list of non-SUPPORTED slides.
````

## 2026-11-23 01:14:39　Targeted semantic recheck 4 slides（model: sonnet）

````text
You are an independent fact-checker. A teaching slide deck (Traditional Chinese) was written using ONLY a markdown wiki as its knowledge source. Check ONLY slides 2, 5, 12 and 16 (number the `<section>` elements of `index.html` 1..16 in document order).

Project root: <repo>
- Deck: `index.html`. Each content slide has `data-wiki="path#anchor,..."` (paths relative to `wiki/`) naming the wiki pages it was written from. Ignore `<aside class="notes">` and `<footer>`. Diagrams count as claims.
- Wiki: `wiki/concepts/*.md`, `wiki/sources/*.md`. Text marked （AI 補充） in the wiki is the AI's own explanation; on slides that must appear inside a `<div class="ai-note">` box.

Rules: read ONLY index.html and the cited wiki files (other wiki pages only to confirm something is NOT in the wiki). Do NOT read raw/, work/, logs/, slides/. No outside knowledge. SUPPORTED = the cited pages state it (paraphrase OK). UNSUPPORTED = not stated in cited pages, or stronger/different (dropped hedge like 認為/論文報告, superlative, changed number, unmarked AI explanation). MISLEADING = supported but likely to give a beginner a wrong impression (including diagram contradictions).

Previously found problems these slides were revised to fix (verify they are fixed, and look for any new problems):
- slide 2: "LeCun's answer is world model" lacked a cited source; "人類靠觀察累積大量背景知識" dropped the hedge.
- slide 5: diagram fed "y" into the target encoder while also saying masking is on the output — contradictory.
- slide 12: "尚未經過同儕審查" is （AI 補充） in the wiki but was shown as plain text.
- slide 16: answer about MAE computing loss in pixel space lacked the pixel-vs-feature page in data-wiki.

Write `logs/run-2/semantic-recheck.md` in Traditional Chinese:
# 語意複查（run-2，第 2、5、12、16 頁）
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
## 統計
SUPPORTED n / UNSUPPORTED n / MISLEADING n

Be strict. Reply with the counts and any non-SUPPORTED slide.
````

## 2026-11-23 01:15:42　Semantic recheck slide 12 only（model: sonnet）

````text
Independent fact-check of ONE slide. Project root <repo>. In `index.html`, number the `<section>` elements 1..16 in document order and look ONLY at slide 12 (the JEPA-Anything slide). Its `data-wiki` attribute lists the wiki pages (relative to `wiki/`) it was written from. Ignore `<aside class="notes">` and `<footer>`.

Read ONLY index.html and the wiki files slide 12 cites. Do NOT read raw/, work/, logs/, slides/. No outside knowledge. Text marked （AI 補充） in the wiki is the AI's own explanation and must appear in a `<div class="ai-note">` box if used on the slide.

Judge every claim on the slide (including the title and the bar diagram): SUPPORTED (cited pages state it, paraphrase OK) / UNSUPPORTED (not stated, or stronger/different: dropped hedge, superlative, changed number, unmarked AI explanation) / MISLEADING (supported but likely to give a beginner a wrong impression, e.g. dropping a caveat from a cited page's 注意 section).

Previously flagged and supposedly fixed: (1) slide showed only improvements and omitted that standard JEPA wins on Hopper; (2) title "最新進展" came only from an （AI 補充） line.

Append to `logs/run-2/semantic-recheck.md` (it exists; add at the end):

## 第 12 頁再複查
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|

Reply with the verdict and any problem.
````

## 2026-11-23 16:08:22　Whole-repo independent review（model: opus）

````text
You are an independent senior reviewer. Review the finished student assignment in <repo> (git repo, HEAD 3691f33, whole history is in scope; first commit 61c25b4). You have no earlier context; that is on purpose.

## Assignment requirements (TAICA w10, 用 LLM Wiki 做一份教學 HTML 簡報, due tonight)
- An LLM Wiki on a chosen topic, made by 「先討論、後生成」, with at least 5 ingested sources.
- A teaching HTML deck that uses the wiki as its knowledge source.
- A loop/graph explanation: what repeats, where checks or regeneration happen, and why.
- One real execution/check record.
- A reflection: which node fails most, where the check was moved earlier, whether and why the workflow changed.
- Title format: 學校 學號 系級 姓名 主題 (the 〈〉 placeholders in submission.md are left for the student on purpose; don't report them).
- Top grade band (9–10): clear wiki↔deck correspondence, sensible clear graph, REAL records, real reflection, clear teaching structure. Plagiarism penalised.

## Where things are
submission.md (what gets handed in), README.md (graph), index.html (reveal.js deck), CLAUDE.md (wiki rules), wiki/, raw/ (source texts, local only; includes the extracted text), work/takeaways/, slides/outline.md, scripts/, tests/, logs/run-0, run-1, run-2, run-2-live. Spec and plan: docs/superpowers/specs/2026-11-23-jepa-wiki-design.md, docs/superpowers/plans/2026-11-23-jepa-wiki.md (has a Review Focus section: check each line deliberately). Executor's decisions: the `Ruling:` lines in .superpowers/sdd/2026-11-23-jepa-wiki/progress.md; weigh them.

## What to check, in order of importance
1. **Truthfulness of the records.** For every quantitative or factual claim in submission.md, README.md, wiki/log.md, logs/run-1/SUMMARY.md and logs/run-2/SUMMARY.md about what happened, recompute or trace it to the raw logs, git history (timestamps too), takeaways and code. Report every claim that is wrong, unverifiable, or overstated (including causal claims). Give the correct value and the evidence. List claims you verified as correct in one compact line each.
2. **Wiki vs raw sources.** The wiki checker only confirms quotes exist. Read each wiki page's claims against its footnote quotes (and raw text where needed) and report claims the quote does not support, misattributions, or missing context. Cover all 15 pages.
3. **Deck vs wiki.** Every slide in index.html INCLUDING speaker notes and quiz answers: unsupported statements, missing caveats, correctness problems, wrong cited page. Also teaching clarity for classmates who have not studied self-supervised learning.
4. **Graph/reflection quality** against the requirements: do the graph and loop descriptions match what the code and process really do?
5. **Code**: do the checkers do what the docs claim? Real bugs or false negatives only (try small adversarial inputs in a temp dir), tests meaningful. Run `python3 -m unittest discover tests`, `python3 scripts/check_wiki.py`, `check_outline.py`, `check_slides.py`; report outputs. Re-run numbers rather than trusting logs.

## Rules
Read-only on this checkout: do not modify files, index, HEAD or branches; no commits, no network posts. Put scratch files under /tmp/claude-1000/-home-miko-Desktop-Projects-SchoolStuff-TAICA-TAICA-w10/cd7c8734-3582-4fae-bb28-d1de68b8735c/scratchpad/review. Do not spawn subagents. Where the spec is silent, judge by what a reasonable grader or reader would expect. Report uncertainty plainly; don't pad with nitpicks.

## Output (English, but keep quoted Chinese as is)
### Strengths (short)
### Issues: Critical / Important / Minor. Each: file:line, what's wrong, evidence, why it matters, concrete fix wording (in Traditional Chinese where the file is Chinese).
### Claims verified as correct (compact list)
### Declined to judge (one line each with reason)
### Assessment: ready to submit? Yes / With fixes / No, with 1–2 sentences.
````

