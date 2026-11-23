# 語意檢查：簡報 → Wiki（run-3 第 3 次，第 11、14、16 頁）

範圍：只檢查 `index.html` 依文件順序的第 11、14、16 頁（含 speaker notes、版面、隱藏答案），對照各頁 `data-wiki` 引用的 Wiki 頁。

| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 11 | 怎麼看這些數字 | SUPPORTED | 表格四列、87.1 / 87.8、73.7 vs 68.6、66.2 vs 66.0、「1% 標註、每類 12 或 13 張」、「大模型才打平」都能在 `concepts/frozen-evaluation.md` 找到。AI 補充的總結放在 `.ai-note` 框內，位置正確。小瑕疵（不影響判定）：(1) 凍結評估列寫「只訓練小的分類頭」，Wiki 只說「不調整模型參數、用凍結骨幹、用小的 attentive probe 當分類頭」，「只訓練」是合理推論，不是原文。(2) 第一個要點「凍結、低樣本：I-JEPA 贏過同樣不靠資料增強的 MAE」把兩個比較併在一起。Wiki 的低樣本比較對象是「架構相近的 MAE」，而且 I-JEPA 訓練 epoch 較少；簡報沒有這個但書，但沒有誇大。(3) speaker notes 說「下一頁會看到，換一種評估，JEPA 就不一定贏」。下一頁（第 12 頁 JEPA-Anything）講的是 Hopper 規劃輸給標準 JEPA，不是換評估方式。「換一種評估就不一定贏」這句話本身有 Wiki 支持（完整微調略輸），但「下一頁」指錯頁，建議改成「本頁微調那一條」或「第 13 頁」。 |
| 14 | 回到大藍圖：LeCun 的六個模組 | MISLEADING | 六個模組的說明、「一個關鍵元素」、Meta 稱 I-JEPA 的 predictor 為「原始、受限的 world model」、「可以說」（it could be argued）的研究方向但書，全部有 `concepts/world-model.md` 支持，沒有 UNSUPPORTED。問題在初學者可能誤讀：(1) World model 那格寫「JEPA 是解法的『一個關鍵元素』」，沒說「解法」是解什麼。Wiki 的上下文是：要讓 world model 能表示多種合理的預測，JEPA 是解法的一個關鍵元素。缺了這個指涉，初學者容易讀成「JEPA 就是 world model 的解法」。(2) speaker notes 說「重點是中間那格」，但版面是 3 欄 grid，World model 排在第一列最右邊（第三格），不是中間，只靠 `.core` 外框強調。(3) 「稱為」比原文 "can be seen as"（可以被看作）稍強，但 Wiki 本身就寫「稱為」，所以只當措辭提醒。(4) 六個格子只是並排，沒有箭頭或關係，不會誤導，但也看不出模組之間怎麼互動，Wiki 沒有這方面內容，不要補。 |
| 16 | 自我檢測 | UNSUPPORTED | 第 1、2 題與答案符合 `pixel-vs-feature-prediction.md` 和 `collapse.md`（I-JEPA 不對稱架構加 EMA；V-JEPA 用 EMA、stop-gradient、predictor，沒有說 I-JEPA 用 stop-gradient，正確）。問題在第 3 題答案：(1) 「和 view-invariance 方法比（ImageNet linear probe）則是打平」丟掉了「大模型才打平，不是大幅領先」。Wiki 原意是只有較大的 I-JEPA 才追平，小模型沒有。這是丟掉限定語，讀起來像 I-JEPA 一般都能和這類方法打平。(2) 「凍結和低樣本時 I-JEPA 贏過 MAE」沒有寫比較對象：Wiki 是「同樣不靠資料增強的 MAE」和「架構相近的 MAE」，低樣本還有 epoch 較少。題目問的是「跟哪個 MAE 比？」，答案卻沒有回答這件事，答案本身就是在示範「說出比較對象」。(3) 「完整微調 87.1 略輸 MAE 的 87.8」有 Wiki 支持（表 15），但 87.8 是「最好的 MAE 模型」，簡報沒標。建議第 3 題答案補上「大模型才」和「不靠資料增強的 MAE」。 |

## 統計
SUPPORTED 1 / UNSUPPORTED 1 / MISLEADING 1
