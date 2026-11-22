# CLAUDE.md — JEPA LLM Wiki

這個檔案是 Wiki 的 schema，規定 AI（Claude Code）怎麼維護 Wiki、怎麼用 Wiki 做簡報。每次動手前先讀它。

## 1. 這是什麼
- 主題：**JEPA（Joint-Embedding Predictive Architecture）**，以及它背後的 world model 構想。
- 讀者：TAICA 同學。大概知道 AI、神經網路是什麼，沒學過 self-supervised learning。
- 語言：繁體中文；英文術語保留，第一次出現時附中文。
- 成果：`wiki/`（知識庫）與 `index.html`（教學簡報，GitHub Pages）。

## 2. 目錄
| 路徑 | 用途 | 誰能改 |
|---|---|---|
| `raw/` | 原始資料（本機，不進 git）。`raw/SOURCES.md` 是清單 | 只新增，不修改 |
| `wiki/sources/<id>.md` | 每篇資料一頁 | AI |
| `wiki/concepts/<slug>.md` | 概念頁 | AI |
| `wiki/index.md` | 所有頁面目錄，每頁一行摘要 | AI |
| `wiki/log.md` | 時間序紀錄：討論、ingest、檢查、修正 | AI（只往後加） |
| `slides/outline.md` | 簡報大綱（每頁目的、要點、引用的 Wiki 頁） | AI |
| `index.html` | reveal.js 簡報 | AI |
| `scripts/` | 檢查程式 | AI |
| `logs/run-N/` | 第 N 輪檢查的原始輸出 | 程式產生 |

## 3. Wiki 頁面格式
```markdown
---
title: JEPA
type: concept          # concept | source
sources: [ijepa, meta-ijepa-blog]
---
# JEPA（Joint-Embedding Predictive Architecture）

內文句子。[^ijepa-1]

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "exact quote from raw text"
```
規則：
1. **每個內文段落、每個條列項至少一個 `[^…]` 引用。** 表格列也算。標題、`## 引文` 區、`相關頁面` 條列除外。
2. footnote 定義必須是 `[^<source-id>-<n>]: [<source-id>](...) — "<引文>"`。引文要**逐字**來自 `raw/` 的文字檔，5–40 個英文字。
3. **內文出現的數字，必須出現在該段引用的某一句引文裡。** 表格數字沒有句子可引時，引文寫該表格的說明句，並在內文註明「（表 N）」。
4. 頁面之間用**相對 markdown 連結**（`[collapse](collapse.md)`），不用 `[[wikilink]]`（GitHub 不會轉成連結）。
5. 每頁結尾有 `## 相關頁面`。
6. 對 `jepa-anything`（v1 預印本）的結果一律寫「論文報告…」。
8. **AI 自己加的解釋、比喻、角色說明，必須以「（AI 補充）」開頭**，自成一段或一個條列項。檢查程式會把它列為 `AI_NOTE` 警告，不算錯誤，但讀者看得出哪些不是來源內容。（run-1 加入）
9. 表格數字標「（表 N）」，數字至少要出現在該來源原文；寫完後人工對照表格列，記錄在 `logs/run-N/table-check.md`。（run-1 加入）
7. 來源之間有矛盾或宣傳用語時，寫進該頁的「注意」段落，不要擇一抹平。

## 4. 操作
### Ingest（新增一篇資料）
1. 下載原文到 `raw/<id>/`，轉成文字檔，核對標題，登記到 `raw/SOURCES.md`。
2. **先討論**：整理重點（每點附逐字引文）、擬建頁面、要人決定的問題 → 給使用者看 → 使用者的回覆原文記進 `log.md`。
3. 寫 `wiki/sources/<id>.md`，再新增／更新相關 `concepts/` 頁。
4. 更新 `index.md`，在 `log.md` 加一筆。
5. 跑 `python3 scripts/check_wiki.py`，errors=0 才算完成。

### Query（用 Wiki 回答問題／做簡報）
- **只讀 `wiki/`，不讀 `raw/`、不靠記憶。** Wiki 沒有的東西，先回到 Ingest 補進 Wiki，再用。

### Lint
- `python3 scripts/check_wiki.py`：引文、來源 id、未引用段落、壞連結、數字。
- 孤兒頁（`index.md` 沒列到）、概念被提到但沒有頁面 → 補。

## 5. 簡報規則
- reveal.js 6.0.2（CDN：cdn.jsdelivr.net），單一 `index.html`。
- 12–15 頁，結構：為什麼 → 自監督 → 三大流派 → JEPA → collapse → I-JEPA（主要範例）→ V-JEPA → 怎麼看數字 → JEPA-Anything → JEPA 輸在哪裡 → LeCun 的大藍圖 → 總結 → 自我檢測。
- 每個內容頁 `<section data-wiki="concepts/jepa.md#錨點,...">`，頁尾 `<footer class="src">` 列出可點的 Wiki 頁（連到 GitHub）。
- 簡報裡的數字必須出現在它引用的 Wiki 頁。
- 數學只放一個式子（L2 距離）；VICReg 只講直覺。
- `python3 scripts/check_slides.py` errors=0、語意檢查無 UNSUPPORTED、`scripts/check_browser.mjs` 無溢出，才算完成。

## 6. 流程（loop / graph）
見 `README.md` 的流程圖。每輪檢查輸出存到 `logs/run-N/`，修正動作記進 `wiki/log.md`。
