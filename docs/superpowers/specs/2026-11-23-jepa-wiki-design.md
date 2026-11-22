# Design — JEPA LLM Wiki + 教學 HTML 簡報（TAICA w10）

Approved in conversation 2026-11-23. Deadline 2026-11-23 23:59.

## Intent
TAICA w10 作業：先建一個 LLM Wiki（先討論、後生成，≥5 篇 ingest），再只用 Wiki 當知識來源做一份教學型 HTML 簡報，並說明 loop/graph、附實際執行檢查紀錄與反思。評分 9–10 分的關鍵：Wiki↔簡報明確對應、有檢查紀錄、反思真實。

## Decisions (user)
- 主題：JEPA（Joint-Embedding Predictive Architecture）。使用者放棄電玩主題。
- 對象：TAICA 同學程度（知道 AI / 神經網路大概是什麼，沒學過 self-supervised learning）。
- 公開 repo `MikoAL/TAICA_w10` + GitHub Pages；可以自行 commit / push。

## Decisions (mine, stated to user)
- 做法 A：Claude Code 當各節點執行者；規則寫在 `CLAUDE.md`；確定性檢查用 Python 腳本；語意檢查用一個沒看過前文的 subagent。（B：LangGraph 程式，需 API key、檢查邏輯相同；C：純對話，無可重複檢查。皆不採用。）
- Wiki 格式依 Karpathy LLM Wiki：`raw/`（本機、gitignore，repo 只放 `SOURCES.md`）、`wiki/sources/`、`wiki/concepts/`、`wiki/index.md`、`wiki/log.md`；相對 markdown 連結（GitHub 可瀏覽）；每個說法標來源。
- 資料：LeCun 2022 立場論文被 OpenReview 人機驗證擋下 → 改用 Meta 2022 LeCun 構想文章 + Meta I-JEPA 部落格；加上 I-JEPA、V-JEPA、VICReg、JEPA-Anything 四篇論文原文，共 6 篇。
- 先討論：寫 Wiki 前一次列出 6 篇重點與擬建頁面給使用者回饋；使用者原話記入 `log.md`。
- 簡報：reveal.js 單頁 HTML，12–15 頁，繁中＋英文術語，每頁標「來源：Wiki › 頁名」連到 GitHub。JEPA-Anything 結果一律寫「論文報告…」（v1 預印本）。
- 寫簡報只讀 `wiki/`；缺資料 → 回頭補 Wiki（loop 回頭邊）。
- 檢查：slide→wiki（引用存在、數字一致）、wiki→raw（數字/引文出現在原文）、subagent 語意檢查；第一輪輸出存檔 → 依結果改流程 → 第二輪存檔。反思依實際結果寫。
- 繳交：`submission.md`（w9 格式）+ Mermaid 流程圖 + 兩輪檢查紀錄 + 反思。

## Non-goals
不深挖 JEPA-Anything 的七個實驗；不從零教神經網路；不靠模型記憶寫任何事實。
