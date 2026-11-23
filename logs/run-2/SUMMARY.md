# run-2 總結：修改後的流程實際跑一次

> **更正（run-3）**：本檔原本寫「大綱檢查讓語意問題從 6 頁降到 3 頁」「有 3 頁在大綱階段就能攔下」。獨立審查指出證據不支持，下面已改寫。`browser.txt` 是 12:45:47 加 icon 後重跑的版本。

## 改了什麼（依 run-1 結果）
1. **新節點「大綱檢查」**（`scripts/check_outline.py`，7 個測試）放在寫 HTML **之前**：
   - 引用的 Wiki 頁和錨點要存在。
   - 大綱裡的數字要在引用頁裡找得到。
   - 引用頁有「注意」段落時，「但書」欄必填（或寫「無：理由」）。
2. **Wiki 檢查改成逐頁**：每寫完一頁就跑 `check_wiki.py`，不等整批寫完（寫進 `CLAUDE.md` 的 Ingest 步驟）。
3. 新規則寫進 `CLAUDE.md`：
   - 簡報不能有 Wiki 沒有的最高級說法。
   - Wiki 的（AI 補充）在簡報要放 AI 補充框。

## 這一輪做了什麼
新增一頁「VICReg 的三個項」，並在 I-JEPA 頁補上但書。照新流程走：大綱 → 大綱檢查 → HTML → 簡報檢查 → 語意檢查 → 瀏覽檢查。全部檢查重新跑一次。

## 結果
| 節點 | 結果 | 紀錄 |
|---|---|---|
| 回頭檢查：用 `check_outline.py` 檢查 **run-1 的大綱** | 8 列缺但書。但 run-1 的大綱本來**沒有「但書」欄**，是為了回頭檢查才補上空欄，所以引用到「注意」的 8 列必然全部報錯。其中 3 列（證據、JEPA-Anything、總結）和 run-1 第 1 次語意檢查有問題的頁重疊，另外 5 列當時是 SUPPORTED。**不能拿來證明大綱檢查有效** | `outline-retro.txt` |
| 大綱檢查（新大綱）第 1 次 | 2 errors：1 個真的漏了但書（第 3 頁引用「像素 vs 表示」但沒處理它的注意）；1 個誤報（但書欄寫「第 13 頁」被當成數字） | `outline-pass1.txt` |
| 大綱檢查第 2 次 | 0 errors | `outline-pass2.txt` |
| 簡報檢查 | 第 1 次就 0 errors（16 頁） | `slides.txt` |
| 語意檢查（整份 15 個內容頁） | **12 SUPPORTED / 2 UNSUPPORTED / 1 MISLEADING**（run-1 第 1 次 8 / 4 / 2、第 2 次 11 / 2 / 1） | `semantic.md` |
| 語意複查（修過的 4 頁） | 3 SUPPORTED / 1 MISLEADING（第 12 頁：只列改善，沒寫 Hopper 輸） | `semantic-recheck.md` |
| 第 12 頁再複查 | **SUPPORTED**（補上 Hopper 的但書、標題改成中性說法） | `semantic-recheck.md` |
| 瀏覽檢查 | 16 頁 0 垂直溢出、0 console error | `browser.txt`、`shots/` |
| Wiki 檢查／單元測試 | errors=0；28 個測試全過 | `wiki.txt`、`tests.txt` |
| 線上瀏覽檢查 | 第 1 次 1 個 console 404（`/favicon.ico`，只有線上才會出現）→ 內嵌 icon 後 0 錯誤；頁尾 15 個 Wiki 連結全部 200 | `../run-2-live/` |

## 學到的
- **不能說大綱檢查讓語意問題變少**：
  - 加入大綱檢查之前，run-1 第 2 次就已經是 3 頁有問題（11 / 2 / 1）；run-2 也是 3 頁（12 / 2 / 1，多一頁）。6 → 3 是 run-1 改簡報造成的。
  - 各次的判定也不穩定：第 2 頁的「LeCun 的答案」「人類靠觀察累積大量背景知識」兩句沒改，run-1 第 2 次判 SUPPORTED，run-2 判 UNSUPPORTED。所以頁數不能直接比。
- **可以確定的**：大綱檢查第 1 次抓到 1 個真的漏但書（第 3 列），也放行了 1 個（Hopper）。
- **檢查本身有漏洞**：第 12 頁的但書在大綱寫成「放到別頁」，`check_outline.py` 把它當成合格的「無：理由」放行，語意檢查卻判它 MISLEADING。`CLAUDE.md` 的規則已改成：引用頁的注意，**本頁也要寫**（run-2 時只靠語意檢查把關；run-3 已加進 `check_outline.py`）。
- run-2 沒有新增或修改 Wiki 頁，所以「Wiki 逐頁檢查」和兩條回到 Wiki 的回頭邊這輪都沒有實際跑到，到 run-3 才跑到。
- 語意複查（4 頁、第 12 頁）的 prompt 有告訴檢查者「上次抓到什麼」，所以複查**不是**盲測；完整 prompt 見 `../run-3/prompts/earlier-prompts.md`。
