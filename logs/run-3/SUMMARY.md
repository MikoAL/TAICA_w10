# run-3 總結：獨立審查 → 更正紀錄 → 補上 Wiki 語意檢查

時間是檔案和 `date` 的實測值；數字從檢查輸出複製。

## 起因
run-2 和線上檢查都通過後，開一個**沒看過過程**的 reviewer 看整個 repo（審查 commit 3691f33，原文在 `independent-review.md`）。所有程式檢查都是 0 errors，它還是找到：

| 類別 | 問題 | 查證 | 處理 |
|---|---|---|---|
| 紀錄 | `wiki/log.md` 的時刻和 git commit 對不上 | 屬實。log 的 00:20–03:00 是事後估的。實際：第一則訊息 00:32:12，run-1 和 run-2 在 01:18 前就做完 | `log.md` 加更正 |
| 紀錄 | 49 errors 的分類寫錯（18／27／3／1） | 屬實。`wiki-pass1.txt` 是 14／32／3 | 改正 |
| 紀錄 | 「語意問題 6 → 3 證明大綱檢查有效」 | 不成立。加大綱檢查前的 run-1 第 2 次就是 3 頁 | 改寫 |
| 紀錄 | 用大綱檢查回頭檢查 run-1 大綱是循環論證 | 屬實。「但書」欄是事後補的空欄，必然報錯；8 列中 5 列當時是 SUPPORTED | 改寫 |
| Wiki | 引文存在，但支持不了那句話（「JEPA 是核心」、漏掉 it could be argued、+21 沒寫比較對象、I-JEPA 用 stop-gradient…） | 屬實 | 修 Wiki，再修簡報 |
| 流程 | 規則寫「但書不能放到別頁」，大綱自己有 4 列違反 | 屬實 | `check_outline.py` 加規則 |
| 工具 | `check_browser.mjs` 預設會覆蓋 run-1 的紀錄 | 屬實 | 預設改成 `logs/local` |

reviewer 看不到對話，所以有些地方要自己補查：00:20／00:40／00:55 三個時刻它說無法查證，逐字稿顯示也不對；subagent 是 5 個不是 6 個（它也無法查證）。

## 流程修改
1. **新節點「Wiki 語意檢查」**（擬大綱之前）：逐項問「引文真的支持這句話嗎？」。原因：`check_wiki.py` 只能確認引文存在。
2. **簡報語意檢查擴大**：加上講者備註、圖、測驗答案，而且不告訴檢查者改過什麼。
3. **大綱檢查擋「但書放到別頁」**（`OUTLINE_CAVEAT_DEFERRED`，先寫測試，失敗後才實作；測試 28 → 32 個）。
4. **新節點「獨立審查」**（發布之後）：對照 logs、git、原文看整個 repo。
5. 紀錄規則：時間用 `date`，數字從輸出複製。

## 結果
| 節點 | 結果 | 紀錄 |
|---|---|---|
| 舊大綱 × 新規則 | 4 errors（第 1、3、4、9 列把但書推給別頁）→ 修完 0 | `outline-pass1.txt`～`outline-pass4.txt` |
| 逐頁 Wiki 檢查 | 第一批有 2 errors（引文帶到斷行連字號、漏引 1% 的出處）。那一批的腳本沒有在出錯時停下，等於還是「一次寫三頁」；後來改成一出錯就停 | `wiki-per-page.txt` |
| **Wiki 語意檢查**（全部 15 頁） | **148 項：128 SUPPORTED／20 PARTIAL／0 WRONG** | `semantic-wiki-pass1.md` |
| 　查證 20 項 PARTIAL | 2 項是檢查者看漏（VICReg 附錄的表有「只用 Inv → collapse」；`more interpretable` 在原文第 866 行），改成補正確引文；其餘照原文改 | `wiki-changes.diff` |
| 　Wiki 語意複查（只看改過的，非盲測） | 約 48 SUPPORTED／2 PARTIAL／0 WRONG（48 是檢查者的概數），2 項已修 | `semantic-wiki-recheck.md` |
| **簡報語意檢查** 第 1 次（盲測、含備註） | **9 SUPPORTED／1 UNSUPPORTED／5 MISLEADING** | `semantic-slides-pass1.md` |
| 　第 2 次（盲測） | 14／0／1（第 11 頁） | `semantic-slides-pass2.md` |
| 　第 3 次（只看第 11、14、16 頁） | 1 SUPPORTED／1 UNSUPPORTED／1 MISLEADING（第 16、14 頁）→ 修正後第 4 次（第 14、16 頁）2／0／0 | `semantic-slides-pass3.md`、`semantic-slides-pass4.md` |
| 瀏覽檢查 | 過程中 3 頁溢出（第 8、12 頁，後來第 11 頁）→ 修完 16 頁 0 errors | `browser-pass2-overflow.txt`、`browser-pass4-overflow.txt`、`browser.txt` |
| 程式檢查 | Wiki errors=0、大綱 errors=0、簡報 errors=0、32 個測試全過 | `wiki.txt`、`outline.txt`、`slides.txt`、`tests.txt` |
| 線上檢查 | LIVERESULT | `live/browser.txt` |

（第 3、4 次只複查改過的頁，沒有再跑一次整份盲測；第 2 次之後改的是第 11、14、16 頁和對應的 Wiki。）

（run-3 的「9／1／5」不能和 run-2 的「12／2／1」直接比：這次檢查範圍比較大，簡報和 Wiki 也都改了。）

## 學到的
- **檢查者會繼承標準的錯誤。** Wiki 把 I-JEPA 寫成用 stop-gradient。run-1 的測驗答案原本寫「I-JEPA 用 EMA（V-JEPA 再加 stop-gradient）」，比 Wiki 正確，簡報語意檢查卻因為和 Wiki 不一致判 UNSUPPORTED，結果被改成錯的（`../run-1/semantic-pass1.md` 第 15 頁）。簡報檢查得再嚴，Wiki 錯就沒用。
- **0 errors 只代表程式檢查的那幾件事沒錯。** 引文存在 ≠ 引文支持；欄位有填 ≠ 填得對。
- **紀錄也要檢查。** 這次最嚴重的問題不在簡報，在紀錄：憑記憶寫的時間、數字和因果。
- **檢查者也會錯**：PARTIAL 要先查原文再改。

## 還沒做的
- `check_browser.mjs` 只量垂直溢出，沒有量水平溢出。
- 「引文 5–40 字」的規則沒有程式檢查。
- 大綱檢查只確認但書欄有填、沒有推給別頁，不判斷內容。
- 語意檢查的「只讀某些檔案」是 prompt 的指示，沒有技術隔離。
- 凍結評估這些名詞在第 8–10 頁先出現，第 11 頁才解釋（目前在第 9 頁加了提示，沒有調順序）。
