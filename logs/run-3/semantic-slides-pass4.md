# 語意檢查：簡報 → Wiki（run-3 第 4 次，第 14、16 頁）

編號依文件順序（第 1 頁為標題頁）：第 14 頁 = 「回到大藍圖：LeCun 的六個模組」，第 16 頁 = 「自我檢測」。

| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 14 | 回到大藍圖：LeCun 的六個模組 | SUPPORTED | 六個模組的描述都對得上 `world-model.md#LeCun 的六模組架構` 表（Configurator 總指揮、Perception 估計狀態、World model 補資訊與預測、Cost「不舒服程度」、Actor 找最低未來成本、Short-term memory 記狀態與成本）。「難題是表示多種合理的預測，JEPA 是解法的一個關鍵元素」對應 `#和 JEPA 的關係`；「原始、受限的 world model」保留 Meta 的限定語；「仍是研究方向／可以說（it could be argued）／未來幾十年的主要挑戰」對應 `#注意`，沒有丟掉但書。講者備註「JEPA 不等於整個 world model」是由「一個關鍵元素」推得，不算新事實。無數字、無最高級、無未標記的 AI 補充。小提醒（不扣分）：「原文」指 Meta LeCun 文章，頁面沒寫出處名稱。 |
| 16 | 自我檢測 | SUPPORTED | Q1：JEPA loss 在嵌入空間、MAE 在像素（輸入）空間，對應 `generative-vs-joint-embedding.md#JEPA 站在哪裡` 與 `pixel-vs-feature-prediction.md#生成式：預測像素`。Q2：Collapse、I-JEPA 不對稱架構（target encoder 為 context encoder 的 EMA）、V-JEPA 的 EMA + stop-gradient + predictor，皆對應 `collapse.md#怎麼防`，且沒有說 I-JEPA 用 stop-gradient。Q3：linear probe 贏過同樣不靠資料增強的 MAE、低樣本贏過架構相近的 MAE、微調 87.1 vs 87.8 略輸、與 view-invariance 方法比大模型才打平，皆對應 `frozen-evaluation.md#為什麼要分清楚`；數字都出現在該頁。小提醒（不扣分）：答案略去了「I-JEPA 訓練 epoch 較少（低樣本、微調皆是，5.3 倍）」這個但書，且把「明顯贏過」簡化為「贏過」，方向仍正確，未形成誤導；但這個問答的重點是「先問比什麼」，若要更保險可補一句 epoch 差異。 |

## 統計
SUPPORTED 2 / UNSUPPORTED 0 / MISLEADING 0
