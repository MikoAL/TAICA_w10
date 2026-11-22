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
