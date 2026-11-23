# 獨立審查報告（原文，2026-11-23 16:21:11 收到；審查對象是 commit 3691f33）

> subagent 的原始輸出，未修改。裡面的判斷不一定都對，查證與處理見 `SUMMARY.md`。prompt 見 `prompts/earlier-prompts.md` 最後一則。

### Strengths
- Real tooling, all re-run by me: 28 unit tests OK; `check_wiki` errors=0 warnings=35; `check_outline`, `check_slides` and `check_takeaways` all 0 errors.
- Every wiki footnote quote is really in raw/.
- The live site returns 200 and is byte-identical to HEAD. origin/main equals HEAD. All 15 distinct footer wiki URLs return 200.
- The wiki ↔ deck link (`data-wiki` plus footer) is clear, and the deck has a sensible teaching arc.
- The "JEPA 輸在哪裡" slide and the disclosed checker loopholes are above average.

### Issues

#### Critical (truthfulness of records)

**C1. wiki/log.md timestamps are false (lines ~31–72).** Several entries carry times later than the commit that contains them:

| log entry | commit containing it | real evidence |
|---|---|---|
| 01:05 discuss | 61c25b4 @ 00:57:34 | already committed |
| 01:40 ingest, 01:50 check, 02:00, 02:05, 02:10 | 6a5474e @ 01:02:31 | wiki-pass1 mtime 00:59:45, pass3 01:01:53, table-check 01:02:31 |
| 02:30, 02:50, 03:00 | 8e2344e @ 01:17:48 | run-1 slides/semantic files 01:06–01:10, run-2 01:11–01:16 |

- Work after scaffolding took about 20 minutes. The log implies about 2 hours.
- A grader comparing `git log` with log.md will see impossible times. "REAL records" is the top-band criterion.
- Fix: the log is append-only, so append a correction entry. For example: 「## [2026-11-23 HH:MM] fix | 更正時間戳：本檔 01:05–03:00 各條的時間是事後填寫、與實際不符。依 git commit 與 logs/ 檔案時間，討論在 00:57:34 之前完成，Wiki 檢查 pass1–4 在 00:59:45–01:02:12，表格核對 01:02:31，run-1 簡報／語意檢查 01:06–01:10，run-2 01:11–01:17，線上檢查 12:45–12:47。」
- The 00:20, 00:40 and 00:55 entries cannot be checked from the repo. 00:55 is about 4 minutes after the run-0 log mtime (00:50:58). The 00:45 ingest is plausible: raw files are 00:46:43–00:47:35.

**C2. The run-1 "49 errors" breakdown is wrong** (submission.md §4 table and §5; logs/run-1/SUMMARY.md; wiki/log.md run-1 entry).
- Claimed: 未引用 18 / 數字 27 / 引文 3 / 其他 1.
- `logs/run-1/wiki-pass1.txt` gives **14 UNCITED_PARAGRAPH, 32 NUMBER_NOT_IN_QUOTE, 3 QUOTE_NOT_FOUND, 0 other**, which sums to 49. The 4 TABLE_NUMBER_UNVERIFIED lines are warnings.
- The reflection's 「最大宗是 AI 補充混寫」 is therefore false by count. Numbers are 32 of 49. Some of those are false positives; per log.md, the 「1.」 list markers and math numbers.
- Fix: 「未引用段落 14、數字不在引文 32（其中一部分是條列編號與數學式的誤報）、引文找不到 3」. Reflection: 「數量最多的是數字（32），其次是把 AI 解釋混進來源（14）」.

**C3. "run-2 證明這個修改有效，語意問題從 6 頁降到 3 頁" is not supported** (submission.md §4/§5; run-2/SUMMARY「學到的」; README "為什麼").
- Run-1 **pass 2**, before `check_outline.py` existed, was already 11/2/1, which is **3 problem pages**. Run-2's full check is also 3 (12/2/1).
- Like for like, there is no improvement. The 6→3 drop was made by the run-1 rewrite, and the denominators differ (14 vs 15 pages).
- The outline check cannot be credited for this result either. The deck diff 550fac2→0a7bc51 is mostly run-1 fixes plus the VICReg slide. Caveat text was added in one place (the I-JEPA slide).
- Run-2 also let the Hopper caveat through, and that is exactly the class the outline check targets. So 「剩下都是措辭」 is not accurate.
- Fix: 「run-1 第 2 次就已經是 3 頁（11/2/1），run-2 第 1 次也是 3 頁（12/2/1，多一頁），所以不能說語意問題因為大綱檢查而減少。可以確定的是：大綱檢查抓到 1 個漏但書；也放行了一個（Hopper）。」

**C4. The outline-check retro evidence is circular** (submission.md §4「8 列缺但書…在大綱階段就能攔下」; run-2/SUMMARY).
- The run-1 outline (550fac2) had **no 但書 column** (grep count 0). `outline-run1-retro.md` had an empty "—" column added before the run, so every row citing a 注意 page fails by construction: 8 of 15.
- Only 3 of those 8 correspond to pages the semantic check flagged. The other 5 were SUPPORTED. This is not disclosed.
- `check_outline` only needs a **non-empty cell**. I set the Hopper row's 但書 to 「沒空寫」 and it passed with errors=0.
- Fix: state that the column was added by hand, that 5 of 8 were false alarms, and that the check only forces someone to fill the cell.

#### Important

**I1. Wiki 頁 has caveats the workflow rule forbids.** CLAUDE.md §5 says 「理由不能是『放到別頁』」, and submission.md §5 lists that as a rule added. In slides/outline.md, rows 1, 3, 4 and 9 still use 「無：…放在『…』頁」. Slide 10 (V-JEPA) shows 81.9 / 72.2 / +21 with no caveat, although the V-JEPA 注意 is the one being deferred. Either write the caveats on those pages (add 「註：ImageNet 上輸給 OmniMAE（訓練方式不同）」), or change the rule to 「本頁要有但書，或明確說明為什麼可以移走」.

**I2. Several graph edges and loops never ran.**
- `git diff 550fac2..HEAD -- wiki/concepts wiki/sources` is empty: no wiki page changed after run-1.
- Per-page wiki checking, table checking at write time, and both H→E and K→E edges were therefore never exercised. run-2/SUMMARY's last line admits this only for per-page checking; submission.md presents all of them as working.
- The semantic check found the diagram and jepa.md at odds with ijepa.md. It was fixed only in HTML, and `wiki/concepts/jepa.md`「把被遮住的部分 y 編碼」 still contradicts ijepa.md:「遮住 target encoder 的輸出」. The deck now says 圖片（輸入不遮）, so deck and wiki disagree.
- Fix: edit the jepa.md target-encoder bullet to 「編碼整張圖，再取出 y 區域的輸出」. Say in the submission 「回頭邊與逐頁檢查是設計上的，本次 run-2 沒有實際觸發」. Add to both graphs the 線上檢查 → I back-edge that actually happened (favicon 404).

**I3. Over-claims in the submission.**
- 「每一句都附原文的逐字引文」 (§1, README): the rule is per block, and 16 AI_NOTE blocks have no citation by design. Use 「每個段落／條列項都有逐字引文；AI 補充另外標示」.
- 「所有原始輸出都在 logs/」: run-1 browser pass 1 (the cover overflow) was never committed, and `browser.txt` equals pass 3. The default outDir of `check_browser.mjs` is `logs/run-1`, so README's bare `node scripts/check_browser.mjs` overwrites run-1 evidence. Fix the default and the README line (pass `logs/rerun`). The 「15 個連結 200」 result also has no saved output (it is true; I re-checked).
- 「19 個數字都對」: 19 is the number of warning lines in wiki-pass4, with repeats. 4 of those are 500/800, which appeared only after the fix. Pass 3, before the fix, had 15. table-check.md has 11 distinct values plus 500/800. Use 「表格數字核對後…」 without the count, or 「約 15 筆警告」.
- 「部落格寫『2 million videos』」: the source is the V-JEPA **paper** (raw/vjepa/paper.txt:19). The blog's converted quote was 「two to 10」 → 「2 到 10」.
- 「人工對照」: the table error was found and fixed between 01:01:53 and 01:02:11, about 18 seconds. Table work was probably AI, not human; reword to 「逐一對照（由 AI 執行）」 unless a person did it.

**I4. Wiki vs raw: claims the cited quotes do not support.**
- `world model 的核心就是 JEPA` (world-model.md, jepa.md 2022 row, meta-lecun-blog.md; deck slide 14 and submission §1). Raw (meta-lecun-blog/page.txt:71,73): the *centerpiece is the predictive world model*, and JEPA is "*one key element of a solution*". The cited footnote (「trainable encoders…」) says nothing about core. Use 「JEPA 是 LeCun 方案的關鍵元素之一」. The deck's own speaker note 「候選做法」 is closer to the source.
- `Meta 自己承認／自己說 訓練 world model 是未來幾十年的主要挑戰` (meta-lecun-blog.md, world-model.md, deck slide 14). Raw 105 says "**it could be argued that** training world models…" Footnote [meta-lecun-blog-9] truncates the quote to drop the hedge. Use 「文章說『可以說』是主要挑戰」.
- `他主張關鍵是…`: raw 33 says world models "**may be the key**". Use 「可能是關鍵」.
- frozen-evaluation.md `JEPA 的優勢主要在凍結評估和低樣本`, cited only to ijepa-2 (the fine-tuning 87.1 sentence), supports neither frozen nor low-shot. This is on deck slide 11 and quiz answer 3. Cite ijepa Table 2, or mark it (AI 補充).
- pixel-vs-feature.md and vjepa.md `優勢主要在凍結評估`: V-JEPA Table 1 SSv2 frozen is 66.0 vs 66.2, essentially equal, while the paper says improvement in both frozen and fine-tuning. Qualify it: 「K400 凍結 73.7 vs 68.6，SSv2 幾乎沒差」.
- vjepa.md and deck slide 10 `SSv2 +21 分`: raw Table 6 caption says +21 compared to **image models**; the comparator is missing. Add 「（相較於影像模型，凍結評估）」.
- vjepa.md and slide 13 `影像模型仍然領先；V-JEPA 74.8% 對 OmniMAE 75.1%`: raw 426 says OmniMAE was **trained directly on ImageNet**, and V-JEPA is ViT-L/16 trained on video. "影像模型" mislabels OmniMAE. Add 「OmniMAE 直接用 ImageNet 訓練，不是公平對手」.
- collapse.md row `EMA target encoder + stop-gradient：I-JEPA、V-JEPA`, cited to a V-JEPA quote. The I-JEPA paper says only EMA; "stop-gradient" does not appear (grep). This is quiz Q2's answer (deck slide 16, 「I-JEPA、V-JEPA 用 EMA 加 stop-gradient」). Run-1 semantic pass 1 flagged it and pass 2 passed it because collapse.md supports it. Fix: 「I-JEPA 用 EMA target encoder；V-JEPA 用 EMA + stop-gradient」.
- The `Contrastive → SimCLR` row cites meta-lecun-blog-1, which does not mention SimCLR. Cite vicreg instead.

**I5. Semantic checks: one page each changes meaning of the evidence.** 12/2/1 and 8/4/2 are verified from the files. I cannot verify that the checker was an independent subagent given only the stated inputs; submission states this as fact. No prompt is saved in logs. Add the prompt text to logs if you have it.

#### Minor
- Deck slide 10 speaker note 「Kinetics-400 靠看物體就能答，SSv2 要看動作順序」 is not in the wiki (grep; it is in work/takeaways), so the note violates 只讀 Wiki. Slide 12's 「不講 pseudoinverse」 is also raw-only. Put the note's content in the wiki or drop it.
- Loss formula: the paper has Σ over patches in each target block and uses ‖·‖². The wiki/deck text says 「L2 距離」 and 「M 塊…取平均」. V-JEPA uses L1. Add 「（每塊再對 patch 加總；實際是平方 L2；V-JEPA 用 L1）」.
- JEPA 不預測下一張圖: submission §1 says 「預測下一張圖的每個像素」; I-JEPA masks one image. Use 「預測被遮住的部分」.
- Teaching clarity: 嵌入/表示 are never defined for beginners, and percentages (54.2, 66.9) never say "top-1 accuracy". linear probe and 凍結評估 appear on slides 8–10 before slide 11 explains them. Add one sentence on slide 4 or 5, and move slide 11 before slide 9 or add a footnote.
- world-model.md 「JEPA-Anything 給的寬鬆定義」: the cited quote is about anticipation, not the definition (raw 226 does support the idea). Cite raw 226's sentence.
- Speaker note on slide 14 「JEPA 是 world model 的候選做法」 is more correct than the slide body 「核心就是 JEPA」.
- quote-length rule 5–40 is not enforced: world-model.md meta-lecun-blog-2 has 41 words, and meta-lecun-blog.md-10 「It can be hypothesized」 has 4.
- Takeaways: vjepa.md holds 10 extra quotes inline after bullets that check_takeaways does not scan. They are all valid (I tested), so 「85 句全部」 is correct for what was checked, but there are 95.
- check_browser ignores horizontal overflow: a 3000px-wide paragraph passed with errors=0, while a 900px-tall one was caught. Review Focus item 5 is only half covered.

### Review Focus (plan)
1 ✓ (test_quote_normalization covers curly quotes and hyphen breaks). 2 ✓. 3 ✓. 4 ✓. 5 partly (see last Minor item); no unit test, but the mechanism works for vertical overflow.

### Claims verified as correct
- 85 takeaway quotes, 0 not found; 28 tests; Wiki 6 source + 9 concept pages; 49 total run-1 wiki errors; pass 2 =1, pass 3 =0, pass 4 =0.
- The three QUOTE_NOT_FOUND in pass 1 are the multi-column I-JEPA ones.
- Table 7 epochs 500 vs 800, 66.9/40.7; Table 6 54.2/15.5/20.2/17.6; Table 15 87.1 vs 87.8; V-JEPA 80.6→68.2 at 287→29; 85.4/85.6; VICReg 73.2 = Barlow Twins 73.2 (Table 1); Pong 34.83/12.90; Hopper favours standard JEPA; 10 dynamics tasks; 7 domains.
- Semantic counts 8/4/2, 11/2/1, 12/2/1; recheck 3/1 then slide 12 SUPPORTED; retro 8 rows; outline pass 1 = 2 errors (one real caveat, one 「第 13 頁」 false positive), pass 2 = 0; slides.txt 0 errors; run-2 and live browser runs 0 overflow; the live favicon 404 then fix (12:45:54 → 12:47:23, errors 1→0).
- Fixes the checker changes claim: list-marker, math and table tests exist; OUTLINE_TABLE_MISSING test exists; the 「22」 was a false positive.

### Declined to judge
- Whether the user's quoted replies are verbatim, and whether discussion preceded generation beyond commit order: needs the chat transcript, which I did not read.
- Whether the semantic checker was really blind/independent: not recorded.
- 「OpenReview 403」 and 「6 subagents read 全文」: no raw evidence kept.
- Full grading of design quality beyond the slides I screenshotted (5, 12): I only looked at those two screenshots; the rest I read as HTML.

### Assessment: With fixes
The engineering and correspondence are strong, but the false timestamps (C1), wrong error counts (C2) and the unsupported run-2 improvement claim (C3/C4) must be corrected before submission, because the grading rubric is about real records and honest reflection. All fixes are text edits to submission.md, README.md, wiki/log.md, the outline, a few wiki lines and two deck lines; no rebuild of the pipeline is needed. Read-only: checkout unchanged, git status clean.
