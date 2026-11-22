# 語意檢查（run-1 第 2 次）
（頁碼依文件順序，第 1 頁為封面，略過。）

| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 2 | 人 20 小時學會開車，AI 呢？ | SUPPORTED | 小提醒：左欄「需要上百萬、上十億筆標註資料」在 wiki（world-model.md#為什麼需要）是「LeCun 的出發點」，投影片沒標出處是 LeCun/Meta 部落格，但右欄標題有「LeCun 的答案」，可接受。 |
| 3 | 不用標註也能學：自監督學習 | SUPPORTED | AI 補充框與 self-supervised-learning.md 的（AI 補充）一致。 |
| 4 | 三種「猜」法 | SUPPORTED | 表格各欄與 generative-vs-joint-embedding.md、pixel-vs-feature-prediction.md 一致。 |
| 5 | JEPA 的三個零件 | MISLEADING | 圖中「y 被遮住的部分 → Target encoder」。jepa.md#三個零件 確實這樣寫，但 ijepa.md#方法 說「目標區塊是遮住 target encoder 的輸出，不是遮住輸入」（第 7 頁講者備註才提到）。初學者會以為遮住的輸入被送進 target encoder。建議在圖或文字補一句，且 data-wiki 加上 sources/ijepa.md#方法。其餘（EMA、L2、公式、白話）皆有支持。 |
| 6 | 最大的陷阱：collapse（表示崩塌） | UNSUPPORTED | 標題「最大的陷阱」：wiki 只說「難點」（jepa.md#難點）、「偷懶解」，沒有說是「最大」。其餘內容（AI 補充框、防法表、VICReg 拿掉 variance 項立刻崩塌、EMA 原因尚不清楚）皆有支持。 |
| 7 | 主要範例：I-JEPA（2023，圖片） | SUPPORTED | 54.2 vs 17.6（表 6）見 masking-strategy.md。小提醒：ijepa.md 另寫「其他遮法 15.5–20.2」且消融多用 ViT-B/16，投影片只列 random，無害。 |
| 8 | 預測表示真的比較好？ | SUPPORTED | 66.9（500 epoch）/ 40.7（800 epoch）、V-JEPA、效率、但書皆與 pixel-vs-feature-prediction.md、sources/ijepa.md#結果 一致。 |
| 9 | 從圖片到影片：V-JEPA（2024） | SUPPORTED | 數字與 sources/vjepa.md#結果 一致。 |
| 10 | 怎麼看這些數字 | SUPPORTED | 與 frozen-evaluation.md 一致。 |
| 11 | 最新進展：JEPA-Anything（2026） | SUPPORTED | v1 預印本與「論文報告」標示保留；34.8% / 12.90% 與 jepa-anything.md#注意 一致（wiki 原寫 34.83%）。 |
| 12 | JEPA 輸在哪裡 | SUPPORTED | 87.1 vs 87.8、74.8 vs 75.1、Hopper、80.6→68.2、Meta 部落格「沒說跟誰比」皆有支持。小提醒：「drops by 12%」一列沒交代是標註從每類約 287 張減到 29 張（vjepa.md#注意），讀者不知道為何掉分。 |
| 13 | 回到大藍圖：LeCun 的六個模組 | SUPPORTED | 六模組、「原始、受限的 world model」、「未來幾十年的主要挑戰」皆與 world-model.md 一致。 |
| 14 | 帶走四句話 | UNSUPPORTED | (1) 第 3 點「最大難點是 collapse」：wiki 只說「難點」，沒說「最大」。(2) 第 2 點「在表示空間比較，可以忽略無法預測的細節」：jepa.md#為什麼不預測像素 寫的是「忽略不重要的細節」（Meta 部落格）；「只預測重要的部分，不用管無法預測的細節」在 pixel-vs-feature-prediction.md 是（AI 補充），投影片把它當事實寫、又沒放 AI 補充框。其餘（66.9/40.7 且註明消融實驗、EMA/stop-gradient/VICReg、微調與看外觀任務會輸）皆有支持。 |
| 15 | 自我檢測 | SUPPORTED | 三題答案與 generative-vs-joint-embedding.md、collapse.md、frozen-evaluation.md 一致。 |

## 統計
SUPPORTED 11 / UNSUPPORTED 2 / MISLEADING 1
