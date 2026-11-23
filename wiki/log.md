# Wiki Log

時間序紀錄。格式：`## [日期 時間] 類型 | 標題`。類型：discuss / ingest / check / fix / workflow。只往後加。

## [2026-11-23 00:20] discuss | 選主題
- AI 提出四個候選主題（資料庫索引、RAG vs LLM Wiki、Prompt Injection、Vector Embeddings），推薦資料庫索引。
- 使用者：「Does it have to be something that... useful? What about video games?」
- AI：主題不需要實用，但「電玩」太大，請使用者收斂。
- 使用者：「What about https://arxiv.org/html/2609.20800v1 Would that work?」
- AI 讀了這篇（JEPA-Anything），說明它是 world model / JEPA 論文，不是遊戲論文。建議把主題設成 world model，這篇放最後。
- 使用者：「I am abandoning the game idea. what do you think about JEPA?」
- AI 分析 JEPA 當主題的優缺點（核心想法好教、資料脈絡清楚、有爭議可檢查；前置知識多、JEPA-Anything 很新）。
- 使用者：「TAICA classmates level is fine, go ahead.」
- **決定**：主題 JEPA；對象是 TAICA 同學程度。

## [2026-11-23 00:40] discuss | 做法與發布
- AI 提出做法 A（Claude Code + CLAUDE.md 規則 + Python 檢查程式 + subagent 語意檢查），不採用 LangGraph 和純對話。
- 使用者對「公開 repo + Pages」先回「no」，對「可以 commit/push」回「yes」。AI 追問簡報要放哪裡給助教看。使用者：「Okay, maybe a public repo is needed. Go ahead.」
- **決定**：公開 repo `MikoAL/TAICA_w10` + GitHub Pages。

## [2026-11-23 00:45] ingest | 取得原文
- 下載 6 篇（見 `raw/SOURCES.md`），每篇核對標題。
- LeCun 2022 立場論文：OpenReview 回 HTTP 403（人機驗證），改用 Meta 2022 年介紹同一構想的文章 `meta-lecun-blog`。

## [2026-11-23 00:55] check | 重點整理的引文檢查（run-0）
- 6 個 subagent 各讀一篇原文全文，整理重點，每點附逐字引文（`work/takeaways/`）。
- `scripts/check_takeaways.py`：85 句引文，0 句找不到（`logs/run-0/takeaways.txt`）。

## [2026-11-23 01:05] discuss | 先討論、後生成：6 篇重點
- AI 給使用者看：6 篇各一句話摘要、讀到的矛盾（部落格「2 到 10 倍 GPU 時數」沒說跟誰比；V-JEPA「drops by 12%」其實是 12 個百分點；JEPA 在微調、ImageNet、Hopper 上輸給別的方法）、擬建 6 個來源頁 + 9 個概念頁，以及 5 個問題：
  1. 主要範例用 I-JEPA，V-JEPA 一頁延伸？
  2. 數學只放 L2 距離，VICReg 只講直覺？
  3. 放一頁「JEPA 輸在哪裡」？
  4. JEPA-Anything 只講「切成因子」概念 + 1～2 個數字 + v1 提醒？
  5. LeCun 的 6 個模組一頁帶過？
- 使用者：「都照你的建議，開始做吧」
- **決定**：以上 5 點都照 AI 建議。

## [2026-11-23 01:40] ingest | 6 篇來源頁 + 9 個概念頁
- 寫 `sources/` 6 頁、`concepts/` 9 頁、`index.md`。

## [2026-11-23 01:50] check | Wiki 檢查 run-1 第 1 次（`logs/run-1/wiki-pass1.txt`）
- **49 errors / 4 warnings。** 分類：
  - 未引用段落 18：多數是 AI 自己加的解釋、角色說明（例如「直覺：把資料藏起來…」），混在來源事實中，看不出哪句沒有出處。
  - 數字不在引文 27：其中真的有問題的是表格數字沒標表號、單位換算（2 million → 200 萬、two to 10 → 2 到 10）、引錯來源（部落格頁引用了論文才有的「12 或 13 張」）、引的句子不含該數字（16 張 A100）。其餘是檢查程式誤報：條列編號「1.」和數學式裡的數字。
  - 引文找不到 3：都是 I-JEPA PDF 的**雙欄排版**，一句話在文字檔裡被另一欄的字插進中間。
- 教訓：最多錯誤來自「寫 Wiki」這一步把 AI 的補充和來源混在一起。

## [2026-11-23 02:00] workflow | 檢查程式與規則修改
- 新規則：AI 自己加的解釋必須以「（AI 補充）」開頭 → 檢查程式改報 `AI_NOTE` 警告，不再是錯誤，但在 Wiki 和簡報都看得出來。
- 檢查程式：略過條列編號和 `$$` 數學式（新增測試 `test_list_markers_and_math_blocks_ignored`、`test_ai_note_is_warning_not_error`）。
- 表格數字：標「（表 N）」時，數字至少要出現在該來源原文中，否則 `TABLE_NUMBER_NOT_IN_SOURCE` 錯誤（`test_table_number_absent_from_source_is_error`）。

## [2026-11-23 02:05] fix | 修正內容 → run-1 第 2、3 次
- 雙欄引文拆成兩句單欄引文；補上表號與表格說明句引文；單位換算改成保留原文數字；部落格頁補引 I-JEPA 論文。
- 第 2 次：1 error（引文結尾留了斷行連字號 `per-`）；第 3 次：0 errors。

## [2026-11-23 02:10] check | 表格數字人工核對（`logs/run-1/table-check.md`）
- 19 個表格數字逐一對照原文表格列，全部數字正確。
- **但抓到一個語意錯誤**：Wiki 寫 I-JEPA 表 7「同樣的設定，只改目標」，實際兩組訓練 epoch 是 500 vs 800。數字對、敘述錯，確定性檢查抓不到。已修正（第 4 次：0 errors）。

## [2026-11-23 02:30] query | 擬大綱、寫簡報（run-1）
- 只讀 `wiki/` 擬 `slides/outline.md`（15 頁），再寫 `index.html`（reveal.js 6.0.2）。
- `check_slides.py` 第 1 次：1 error，式子的 `<sub>2</sub><sup>2</sup>` 被當成數字 22（誤報）→ 改成 Unicode ₂²。
- 語意檢查（獨立 subagent，只看簡報與被引用的 Wiki）第 1 次：**8 SUPPORTED / 4 UNSUPPORTED / 2 MISLEADING**，問題是漏但書、把「論文認為」寫成事實、引用範圍不足。修正後第 2 次：11 / 2 / 1，剩下最高級說法（「最大的陷阱」）、架構圖遮輸入／遮輸出不一致、把 AI 補充當事實。
- 瀏覽檢查：封面溢出；截圖看出背景色沒套用、predictor 被畫成箭頭 → 修正後 0 溢出。

## [2026-11-23 02:50] workflow | run-1 → run-2 的流程修改（`logs/run-1/SUMMARY.md`）
- 最常出錯的節點：寫 Wiki（49 個格式／出處錯誤），但最難抓的是寫簡報的語意錯誤（只有最後的語意檢查抓得到）。
- 把「但書」「引用範圍」「數字」的檢查往前移到大綱：新增 `check_outline.py`，寫 HTML 前執行。
- Wiki 格式檢查改成每頁寫完就跑。

## [2026-11-23 03:00] query | run-2：新增 VICReg 頁，照新流程跑（`logs/run-2/SUMMARY.md`）
- 用新檢查回頭檢查 run-1 大綱：8 列缺但書，其中 3 列對應 run-1 語意檢查的真實問題。
- 新大綱第 1 次：2 errors（1 真的漏但書、1 誤報）→ 第 2 次 0。
- 簡報檢查第 1 次就 0 errors。語意檢查 12 / 2 / 1（run-1 是 8 / 4 / 2）。
- 複查發現大綱檢查的漏洞：但書寫「放到別頁」也會被放行 → 改規則。

## [2026-11-23 12:45] check | 線上瀏覽檢查（`logs/run-2-live/`）
- 對 https://mikoal.github.io/TAICA_w10/ 跑 `check_browser.mjs`：16 頁 0 溢出，但有 1 個 console 錯誤（404）。
- 原因：沒有指定 icon，瀏覽器自動去網域根目錄抓 `/favicon.ico`。本機用 `file://` 開不會發生，**只有線上才看得到**。
- 修正：`<head>` 內嵌 SVG icon，重新發布後再跑一次。
