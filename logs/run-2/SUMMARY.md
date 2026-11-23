# run-2 總結：修改後的流程實際跑一次

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
| 回頭檢查：用 `check_outline.py` 檢查 **run-1 的大綱** | 8 列缺但書。run-1 語意檢查抓到的 6 頁問題中，有 3 頁（證據、JEPA-Anything、總結）屬於漏掉但書，**在大綱階段就能攔下**；另外 3 頁（引用範圍、用詞、答案措辭）大綱檢查抓不到 | `outline-retro.txt` |
| 大綱檢查（新大綱）第 1 次 | 2 errors：1 個真的漏了但書（第 3 頁引用「像素 vs 表示」但沒處理它的注意）；1 個誤報（但書欄寫「第 13 頁」被當成數字） | `outline-pass1.txt` |
| 大綱檢查第 2 次 | 0 errors | `outline-pass2.txt` |
| 簡報檢查 | 第 1 次就 0 errors（16 頁） | `slides.txt` |
| 語意檢查（整份 15 個內容頁） | **12 SUPPORTED / 2 UNSUPPORTED / 1 MISLEADING**（run-1 第 1 次是 8 / 4 / 2） | `semantic.md` |
| 語意複查（修過的 4 頁） | 3 SUPPORTED / 1 MISLEADING（第 12 頁：只列改善，沒寫 Hopper 輸） | `semantic-recheck.md` |
| 第 12 頁再複查 | **SUPPORTED**（補上 Hopper 的但書、標題改成中性說法） | `semantic-recheck.md` |
| 瀏覽檢查 | 16 頁 0 溢出、0 console error | `browser.txt`、`shots/` |
| Wiki 檢查／單元測試 | errors=0；28 個測試全過 | `wiki.txt`、`tests.txt` |
| 線上瀏覽檢查 | 第 1 次 1 個 console 404（`/favicon.ico`，只有線上才會出現）→ 內嵌 icon 後 0 錯誤；頁尾 15 個 Wiki 連結全部 200 | `../run-2-live/` |

## 學到的
- **往前移有用，但不是萬能**：大綱檢查擋住了「漏但書」這一類，語意問題從 6 頁降到 3 頁。剩下的都是**措辭**問題（把「認為」寫成事實、圖和文字矛盾），只有語意檢查抓得到。
- **檢查本身有漏洞**：第 12 頁的但書在大綱寫成「放到別頁」，`check_outline.py` 把它當成合格的「無：理由」放行，語意檢查卻判它 MISLEADING。`CLAUDE.md` 的規則已改成：引用頁的注意，**本頁也要寫**（這條目前靠語意檢查把關，`check_outline.py` 沒有擋）。
- run-2 沒有新增 Wiki 頁，所以「Wiki 逐頁檢查」這個修改這輪還沒實際跑到，只寫進了流程。
