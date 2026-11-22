# 語意檢查（run-2）
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 2 | 人 20 小時學會開車，AI 呢？ | UNSUPPORTED | (1) 「LeCun 的答案：world model」：world-model.md#為什麼需要 只說 LeCun 認為差別在「人類靠觀察累積的背景知識（常識）」，沒有說 world model 是他對「20 小時 vs 上百萬筆」這個差距的「答案」；把「是什麼」與「為什麼需要」兩節接成因果是投影片自己的推論。(2) 「人類靠觀察累積大量背景知識，也就是常識」寫成事實，wiki 是「他認為…」（引文為 "It can be hypothesized that…"），丟掉了「LeCun 認為/假說」的限定。 |
| 3 | 不用標註也能學：自監督學習 | SUPPORTED | |
| 4 | 三種「猜」法 | SUPPORTED | |
| 5 | JEPA 的三個零件 | MISLEADING | 架構圖把「y 要猜的區域」直接畫成 Target encoder 的輸入，但同一張圖又寫「遮的是輸出，不是輸入」，兩者互相矛盾；初學者會以為 target encoder 只看到被遮住的那塊。wiki（sources/ijepa.md#方法）是「目標區塊是遮住 target encoder 的輸出」，jepa.md 的「把被遮住的部分 y 編碼」是簡化說法。建議圖改成 Target encoder 吃整張圖、再在輸出上取 y 區塊的表示。其餘文字（L2、公式、EMA）都有支持。 |
| 6 | JEPA 的難點：collapse（表示崩塌） | SUPPORTED | |
| 7 | 防 collapse 的一種做法：VICReg 的三個項 | SUPPORTED | |
| 8 | 主要範例：I-JEPA（2023，圖片） | SUPPORTED | |
| 9 | 預測表示真的比較好？ | SUPPORTED | |
| 10 | 從圖片到影片：V-JEPA（2024） | SUPPORTED | |
| 11 | 怎麼看這些數字 | SUPPORTED | |
| 12 | 最新進展：JEPA-Anything（2026） | UNSUPPORTED | 「v1 預印本，尚未經過同儕審查」：在 sources/jepa-anything.md 這句是「（AI 補充）性質」，不是來源原文（引文只支持 "arXiv…v1"），但投影片用一般文字寫，沒放進 ai-note 框。其餘（七個領域、34.8%、12.90%、「論文報告」標示）都有支持。 |
| 13 | JEPA 輸在哪裡 | SUPPORTED | |
| 14 | 回到大藍圖：LeCun 的六個模組 | SUPPORTED | |
| 15 | 帶走四句話 | SUPPORTED | |
| 16 | 自我檢測 | SUPPORTED | 見小建議第 5 點。 |

## 統計
SUPPORTED 12 / UNSUPPORTED 2 / MISLEADING 1

## 小建議（不影響判定）
1. 第 12 頁：左下 split 圖把目標切成並排的色塊，容易讓初學者以為「正交」是把狀態像切蛋糕一樣切成不重疊的片段。wiki 只說「用學到的基底矩陣拆成成分、互相正交」。建議圖說加一句「示意」，或避免暗示切成等分。
2. 第 12 頁：「同時介入多個變數時只降低 12.90%」，wiki（jepa-anything.md#注意）寫「改善較小」。「只」是投影片的詮釋，影響不大，但可改成「較小（12.90%）」。
3. 第 10 頁：「SSv2 +21 分」「預訓練看的樣本明顯比較少」沒寫比較對象，wiki 也沒寫；初學者可能誤解成對所有方法都如此。可加「相較於論文中的基準」。
4. 第 8 頁：右側 10x10 格子圖（context 佔 90% 區域、target 為其中挖出的洞）是投影片自己的示意，wiki 沒有這個配置。建議圖說標明「示意，不是論文實際比例」。
5. 第 16 頁：Q1「MAE 算在像素空間」的直接文字出處是 concepts/pixel-vs-feature-prediction.md#生成式預測像素，建議把它加進 data-wiki（目前 generative-vs-joint-embedding 只用腳註把 MAE 掛在「loss 在輸入空間」上）。
6. 第 9 頁：把「ViT-Huge 16 張 A100、不到 72 小時」放在「預測表示比較好」的證據下，但它是成本，不是表示 vs 像素的比較；建議標成「計算成本」。
