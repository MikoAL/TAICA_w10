# 語意檢查（run-1）

投影片依文件順序編號：第 1 頁為封面（略過），內容頁為第 2–15 頁。

| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 2 | 人 20 小時學會開車，AI 呢？ | SUPPORTED | |
| 3 | 不用標註也能學：自監督學習 | SUPPORTED | AI 框內容與 wiki 的（AI 補充）一致。 |
| 4 | 三種「猜」法 | UNSUPPORTED | 表格「在哪裡比較」欄寫生成式＝「像素」。所引的 generative-vs-joint-embedding.md 只寫生成式「用 decoder 直接重建訊號 y」，沒有寫「在像素空間比較」。「loss 算在像素」出現在 concepts/pixel-vs-feature-prediction.md#生成式預測像素（以及 sources/ijepa.md#方法），這兩頁都不在 data-wiki。建議補上 pixel-vs-feature-prediction.md。 |
| 5 | JEPA 的三個零件 | UNSUPPORTED | 小字「target encoder 是 context encoder 權重的緩慢平均版本」。jepa.md 只寫「context encoder 的指數移動平均（EMA）」，沒有「緩慢」，也沒有「權重」。「緩慢更新」只出現在 collapse.md#怎麼防（引 vjepa），該頁不在這頁的 data-wiki。這句也是沒標 AI 框的白話解釋。要嘛補引 collapse.md，要嘛改成 AI 框，要嘛刪除。 |
| 6 | 最大的陷阱：collapse（表示崩塌） | SUPPORTED | |
| 7 | 主要範例：I-JEPA（2023，圖片） | SUPPORTED | 備註：「一塊 context 預測幾塊 target 的表示」和「不需要人工設計的資料增強」在 sources/ijepa.md#一句話，不在 data-wiki 列出的錨點 #方法。頁面有引，內容有據。建議補上錨點。遮罩 54.2 對 17.6 有 masking-strategy.md 支持，條形長度比例也正確。 |
| 8 | 預測表示真的比較好？ | MISLEADING | 標題「預測表示真的比較好？」搭配 66.9 對 40.7 和「V-JEPA 一致的進步」。數字有據，但 wiki（pixel-vs-feature-prediction.md#注意）要求同時說明三件事：(1) 表 7 只是一組消融實驗，(2) 兩組 epoch 不同（這頁有提到 epoch），(3) V-JEPA 完整微調時差距很小，85.4 對 85.6，優勢主要在凍結評估。第 3 點沒有出現在這頁。初學者會以為預測表示在所有評估下都明顯勝出。 |
| 9 | 從圖片到影片：V-JEPA（2024） | SUPPORTED | |
| 10 | 怎麼看這些數字 | SUPPORTED | 備註：「凍結評估」「微調」兩列的內容在 frozen-evaluation.md#frozen-evaluation凍結評估 和 #fine-tuning微調，data-wiki 沒列這兩個錨點，建議補上。內容本身與 wiki 一致。 |
| 11 | 最新進展：JEPA-Anything（2026） | MISLEADING | (1)「34.8%」是單一介入的最佳結果，而且沒說是跟「條件相同的標準 JEPA」比。wiki（sources/jepa-anything.md#注意）同頁寫了組合介入只有 12.90%，且分子模擬、10 個任務等是「論文報告」。這頁只放最亮的一個數字。(2)「問題」欄「容易預測的結構會主導訓練」寫成事實。wiki 寫的是「論文認為／論文對標準 JEPA 的診斷」。頁首的「以下結果都是論文報告」只涵蓋結果，沒涵蓋這個診斷。(3) 這頁沒提到作者自己的警語：正交因子不代表因果機制。 |
| 12 | JEPA 輸在哪裡 | SUPPORTED | |
| 13 | 回到大藍圖：LeCun 的六個模組 | SUPPORTED | |
| 14 | 帶走四句話 | UNSUPPORTED | (a) 第 4 句「看外觀的任務、部分控制任務仍可能輸」的依據是 sources/vjepa.md#注意（ImageNet 74.8 對 75.1）和 sources/jepa-anything.md#注意（Hopper）。這兩頁都不在 data-wiki（只有 ijepa.md#注意，那裡只有微調），建議補上。(b) 第 2 句「好處是能忽略無法預測的細節」後面接 66.9 對 40.7，把原因和結果直接連起來。wiki 的說法是「忽略不重要的細節」（jepa.md／Meta 部落格）和（AI 補充）「可以只預測重要的部分」，沒有把「忽略無法預測的細節」當成這個分數差距的原因。也沒帶上「兩組 epoch 不同、只是消融」這個但書。 |
| 15 | 自我檢測 | UNSUPPORTED | 第 2 題答案「I-JEPA 用 EMA target encoder（V-JEPA 再加 stop-gradient）」暗示 I-JEPA 沒有 stop-gradient。wiki collapse.md#怎麼防 的表格把「EMA target encoder + stop-gradient」整組列給「I-JEPA、V-JEPA」，sources/ijepa.md 只提到 EMA，沒有明說 I-JEPA 不用 stop-gradient。「V-JEPA 再加」這個先後關係 wiki 沒有。另外第 1 題「MAE 算在像素空間」需要 pixel-vs-feature-prediction.md 才有明確依據（目前只能從 generative-vs-joint-embedding.md 推論）。 |

## 統計
SUPPORTED 8 / UNSUPPORTED 4 / MISLEADING 2（共 14 個內容頁，第 2–15 頁）
