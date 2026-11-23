# JEPA LLM Wiki + 教學簡報（TAICA w10）

- **簡報**：https://mikoal.github.io/TAICA_w10/ （reveal.js；方向鍵換頁，按 `S` 開講者備註）
- **Wiki**：[wiki/index.md](wiki/index.md)（6 篇來源頁 + 9 個概念頁；來源內容每段／每條都附逐字引文，AI 自己的解釋標「（AI 補充）」）
- **Wiki 規則（schema）**：[CLAUDE.md](CLAUDE.md)
- **時間序紀錄（討論、ingest、檢查、修正）**：[wiki/log.md](wiki/log.md)
- **檢查紀錄**：[logs/](logs/)（[run-1 總結](logs/run-1/SUMMARY.md)、[run-2 總結](logs/run-2/SUMMARY.md)、[run-3 總結](logs/run-3/SUMMARY.md)）

## 流程（graph）

### run-3 之後的版本（目前）

```mermaid
flowchart TD
    A[取得資料<br>下載原文、轉文字、核對標題] --> B[重點整理<br>5 個 subagent 讀 6 篇，附逐字引文]
    B --> C{引文檢查<br>check_takeaways.py}
    C -- 找不到 --> B
    C -- 通過 --> D[先討論<br>重點＋擬建頁面＋問題給使用者]
    D -- 使用者回饋 --> E[寫一頁 Wiki]
    E --> F{逐頁 Wiki 檢查<br>check_wiki.py＋表格數字對照}
    F -- 錯誤 --> E
    F -- 全部通過 --> W{Wiki 語意檢查 run-3 新增<br>新 subagent：引文真的支持這句話嗎？}
    W -- PARTIAL／WRONG --> E
    W -- 通過 --> G[擬大綱<br>每頁要點＋但書＋引用]
    G --> H{大綱檢查<br>check_outline.py}
    H -- 缺但書／但書推給別頁／數字／引用 --> G
    H -- Wiki 缺資料 --> E
    H -- 通過 --> I[寫簡報 HTML]
    I --> J{簡報檢查<br>check_slides.py}
    J -- 錯誤 --> I
    J -- 通過 --> K{簡報語意檢查<br>新 subagent：含講者備註、圖、測驗答案}
    K -- UNSUPPORTED／MISLEADING --> I
    K -- Wiki 本身錯 --> E
    K -- 通過 --> L{瀏覽檢查<br>check_browser.mjs 1280×720 量測＋截圖}
    L -- 溢出／畫面問題 --> I
    L -- 通過 --> M[發布 GitHub Pages]
    M --> N{線上檢查}
    N -- 線上才有的錯誤 --> I
    N -- 通過 --> R{獨立審查 run-3 新增<br>沒看過過程的 reviewer 看整個 repo}
    R -- 紀錄和 logs 不符 --> P[更正紀錄]
    R -- Wiki 錯 --> E
    R -- 簡報錯 --> I
    P --> Z[繳交]
    R -- 通過 --> Z
```

run-2 的版本是上圖拿掉「Wiki 語意檢查」「獨立審查」兩個節點，線上檢查也還沒有畫成節點。

**哪些邊真的走過**（截至 run-3）：

- 走過：F→E、W→E、H→G、J→I、K→I、K→E、L→I、N→I、R→P、R→E、R→I。
- K→E 到 run-3 才走到（簡報語意檢查指出 74.8% 沒說是哪個模型 → 先補 Wiki 的 V-JEPA 頁，再改簡報）。run-2 的簡報語意檢查也看到 Wiki 兩頁互相矛盾（遮輸入／遮輸出），但當時只改了簡報，那次該走而沒走。
- **沒走過**：C→B（第一次就 0 錯）、H→E（大綱沒有缺 Wiki 資料）。

### run-1 的版本（被修改前）

```mermaid
flowchart LR
    A[取得資料] --> B[重點整理] --> C{引文檢查} --> D[先討論] --> E[一次寫完全部 Wiki] --> F{Wiki 檢查} --> G[擬大綱<br>沒有檢查] --> I[寫簡報 HTML] --> J{簡報檢查} --> K{語意檢查} --> L{瀏覽檢查}
    F -- 錯誤 --> E
    J -- 錯誤 --> I
    K -- 問題 --> I
    L -- 問題 --> I
```

### 哪些步驟會重複？
| 迴圈 | 重複什麼 | 什麼時候停 |
|---|---|---|
| 重點整理 ⇄ 引文檢查 | 引文找不到就重新從原文挑句子 | 85 句全部找得到（只檢查行首引文；`vjepa.md` 另有 10 句夾在條列裡沒算到，獨立審查另外驗過都存在） |
| 寫 Wiki ⇄ Wiki 檢查 | **每寫完一頁**就檢查、修正 | `check_wiki.py` errors=0 |
| Wiki 語意檢查 → 寫 Wiki | 引文支持不了那句話時，改句子或換引文 | 沒有 WRONG，PARTIAL 都處理過 |
| 擬大綱 ⇄ 大綱檢查 | 補但書、修數字、修引用 | `check_outline.py` errors=0 |
| 大綱／語意檢查 → 寫 Wiki | Wiki 缺資料或 Wiki 本身寫錯，就回到 Wiki 修 | 回頭邊 |
| 寫 HTML ⇄ 簡報／語意／瀏覽檢查 | 重寫該頁 | 三種檢查都通過 |
| 獨立審查 → 紀錄／Wiki／簡報 | 對照 logs、git 和原文，把不符的地方改掉 | 嚴重和重要問題都處理過 |

### 為什麼這樣設計？
- **程式檢查一直重跑，語意檢查只放在關口**：程式檢查又快又便宜，每改一頁就跑；語意檢查每次都要開新的 subagent，比較貴，所以只放在 Wiki 寫完後和簡報寫完後。
- **語意檢查用「沒看過前文」的 subagent**：寫的人會不自覺補上腦中的知識，看不出自己漏寫了什麼。檢查者被指示只讀簡報和 Wiki（這是 prompt 的指示，沒有技術上的隔離；prompt 在 `logs/run-3/prompts/`）。
- **為什麼 run-3 又在前面加 Wiki 語意檢查**：簡報語意檢查只拿 Wiki 當標準。Wiki 寫錯時，它會把錯的判成對的，甚至把對的簡報改錯（run-1 的 stop-gradient 就是）。所以「Wiki → 原文」的語意也要先檢查。
- **寫簡報只能讀 Wiki**（規則）：這樣「簡報 → Wiki → 原文」每一段都能檢查。但寫簡報的是同一個對話，之前已經讀過原文的重點，所以這條規則靠檢查把關，不是靠隔離。Wiki 每段有逐字引文可以比對原文，簡報每頁有 `data-wiki` 可以比對 Wiki。
- **run-2 把檢查往前移**：見 [run-1 總結](logs/run-1/SUMMARY.md)。語意問題在 HTML 寫完後才被發現，每修一次就要重寫、重新語意檢查，所以把「但書有沒有填」「引用和數字存不存在」的檢查移到大綱（它不會判斷但書的內容對不對）；Wiki 的格式檢查也從「整批寫完」改成「每頁寫完」。

## 目錄
| 路徑 | 內容 |
|---|---|
| `wiki/` | LLM Wiki（`index.md`、`log.md`、`sources/`、`concepts/`） |
| `raw/SOURCES.md` | 原始資料清單（原文檔不放進 repo） |
| `work/takeaways/` | 討論前的每篇重點整理（subagent 產出） |
| `slides/outline.md` | 簡報大綱 |
| `index.html` | 簡報 |
| `scripts/` | 檢查程式；`tests/` 是它們的測試 |
| `logs/run-N/` | 每輪檢查的原始輸出與截圖 |
| `docs/superpowers/` | 設計文件與實作計畫 |

## 重跑檢查
```bash
python3 -m unittest discover tests
python3 scripts/check_wiki.py      # 需要本機 raw/（見 raw/SOURCES.md 下載）
python3 scripts/check_outline.py
python3 scripts/check_slides.py
npm install && node scripts/check_browser.mjs   # 需要 Chromium；輸出到 logs/local（不進 git）
```
