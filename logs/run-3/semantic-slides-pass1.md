# 語意檢查：簡報 → Wiki（run-3）

範圍：index.html 第 2–16 頁（第 1 頁封面略過），含講者備註、圖示、隱藏的測驗答案；不含 footer。只對照各頁 data-wiki 引用的 Wiki 頁。

| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 2 | 人 20 小時學會開車，AI 呢？ | SUPPORTED | 20 小時、上百萬／上十億筆標註、world model 兩個功能、「假說」「可能」的保留語氣都和 world-model.md、meta-lecun-blog.md 一致。 |
| 3 | 不用標註也能學：自監督學習 | SUPPORTED | 定義、能量說法、I-JEPA 論文統一各種方法都有對應。「把資料藏起來去猜」是 Wiki 的（AI 補充），本頁已放在 `.ai-note` 框內。 |
| 4 | 三種「猜」法 | MISLEADING | (1) 標題說三種「猜」法，但聯合嵌入（VICReg 類）並不做預測，是讓相容輸入的嵌入相近；初學者會以為三者都在「預測」。(2)「生成式的問題」整段把 Meta 部落格的批評當成一般事實，沒標是 Meta 的說法；Wiki 同頁還有「聯合嵌入的問題」（要資料增強、有 collapse 風險），本頁沒提，造成「生成式不好、其他比較好」的單邊印象。(3) 表中 y 沒有定義。其餘表格內容（decoder 重建、predictor 預測嵌入、代表方法）和 generative-vs-joint-embedding.md 一致。 |
| 5 | JEPA 的三個零件 | SUPPORTED | 圖與式子對得上 jepa.md、ijepa.md：context encoder 只處理看得到的部分、target encoder 輸入不遮而遮輸出、target encoder 是 EMA、loss 為平均 L2。小提醒（不扣分）：頁名泛稱 JEPA，但「遮輸出」「L2」是 I-JEPA 的做法（V-JEPA 改用 ℓ1，見 vjepa.md），只有式子標了「I-JEPA」。 |
| 6 | JEPA 的難點：collapse（表示崩塌） | SUPPORTED | 常數向量、能量地形平坦、四種防法與使用者、VICReg 消融、「為什麼有效還不完全清楚」皆在 collapse.md。「loss 永遠是零」是 Wiki 的（AI 補充），已放 `.ai-note`。 |
| 7 | 防 collapse 的一種做法：VICReg 的三個項 | UNSUPPORTED | 表格 Invariance 列「這是原本的目標」不在 vicreg.md（只寫「單獨用就會 collapse」），屬未標示的 AI 解釋，應刪除或放進 `.ai-note`。另外「擋住什麼」欄把 Variance 對應到「所有樣本變成同一個向量」，是把 collapse.md 的分類與 vicreg.md 的各項說明拼接，Wiki 沒有明寫這個一一對應（輕微）。其餘（立刻崩塌、covariance 救不了、可解釋／模組化、與 Barlow Twins 打平（表 1）、不需負樣本）皆有支持。 |
| 8 | 主要範例：I-JEPA（2023，圖片） | SUPPORTED | 方法、但書（只在圖片驗證、ViT-B/16、1% 標註）、表 6 的 54.2 vs 17.6 皆在 ijepa.md、masking-strategy.md。附註：格子圖（10×10、context 幾乎涵蓋整張圖、右側灰色「沒用到」欄）是示意，尺寸與比例不是 Wiki 內容，Wiki 只說「一塊夠有資訊量、分布夠廣的 context 與幾塊夠大的 target」。建議圖上標「示意」。 |
| 9 | 預測表示真的比較好？ | MISLEADING | 「效率：ViT-Huge 用 16 張 A100、不到 72 小時；比 MAE 少約 5 倍的迭代就收斂」緊接在「V-JEPA」那一條之後，讀起來像在說 V-JEPA；Wiki 寫的是 I-JEPA（ViT-Huge/14）。而且「不到 72 小時」沒有比較對象，放在「預測表示比較好嗎」的證據下，容易被當成表示優於像素的證據，其實 Wiki 只把「比像素重建方法收斂快」當效率證據。66.9 vs 40.7 的數字、500 vs 800 epoch、但書（表 7 只是消融、V-JEPA 微調差距小、SSv2 幾乎沒差）則皆支持。 |
| 10 | 從圖片到影片：V-JEPA（2024） | MISLEADING | 但書列「ImageNet 略輸 OmniMAE（74.8% 對 75.1%）」，但同一頁的「最大模型 ViT-H/16」數字旁沒有 ImageNet，而 vjepa.md 的 ViT-H/16 ImageNet 是 77.9%（用兩層 attentive probe，見 frozen-evaluation.md）。初學者會看不懂 74.8 是哪個模型、哪種 probe，也看不出 77.9 其實高於 75.1。應註明 74.8 的模型與評估設定。另外 vjepa.md 說這個比較是「凍結評估」，頁面沒寫。其餘（約 2 million 支影片、81.9%、72.2%、SSv2 +21 分是對影像模型、樣本較少是對預測像素方法、label-efficient、完整微調差距小）皆支持。 |
| 11 | 怎麼看這些數字 | SUPPORTED | 四種評估定義、I-JEPA 87.1 vs MAE 87.8、V-JEPA 表 1 的 73.7 vs 68.6、66.2 vs 66.0 皆在 frozen-evaluation.md。ai-note 為 Wiki 的（AI 補充）。小提醒：「凍結、低樣本：I-JEPA 贏過 MAE」省略了 Wiki 的限定（對象是「同樣不靠資料增強」「架構相近」的 MAE，且低樣本時訓練 epoch 較少）。 |
| 12 | JEPA-Anything（2026）：把目標拆開來預測 | MISLEADING | 右側圖把「一個目標」畫成方塊再切成四塊並排的色塊，像是空間上切碎；Wiki 的拆解是用學到的基底矩陣在表示空間拆成成分，因子數也沒有說是四個。初學者會誤以為是把圖切成四個區塊分別預測。文字部分（v1 預印本、論文報告、七個領域、34.8%、12.90%、Hopper 輸）皆支持。另：Wiki 的「34.83% 單一介入 vs 12.90% 組合介入」本頁已寫，但作者自己的提醒（正交因子不代表因果機制、生物證據樣本小）沒放，Interventional 的結果容易被讀成「因果發現」。 |
| 13 | JEPA 輸在哪裡 | SUPPORTED | 87.1 vs 87.8（epoch 少 5.3 倍）、74.8% vs 75.1%（OmniMAE 直接用 ImageNet 訓練）、Hopper「看環境而定」、「drops by 12%」是 287→29 張、80.6→68.2、12 個百分點、Meta 部落格「兩到 10 倍 GPU 時數」沒說跟誰比，全部與四個來源頁的「注意」一致。 |
| 14 | 回到大藍圖：LeCun 的六個模組 | SUPPORTED | 六模組描述、JEPA 是「一個關鍵元素」、Meta 稱 I-JEPA predictor 為「原始、受限的 world model」、「it could be argued」皆在 world-model.md，保留語氣沒被拿掉。 |
| 15 | 帶走四句話 | MISLEADING | 第 2 點「I-JEPA 的消融實驗裡，預測表示 66.9、預測像素 40.7」把數字放在「在抽象表示裡比較，可以忽略不重要的細節」之後，像是證實這個機制；而且省略了 Wiki 的限定：只用 1% 標註的線性評估、兩組訓練 epoch 不同（500 vs 800）、表 7 只是一組消融。這些但書在第 9 頁，但本頁單獨看會被當成一般性的勝負。第 3 點把 VICReg 正則化與 EMA、stop-gradient 並列為「JEPA 的防法」，VICReg 在 Wiki 是另一篇聯合嵌入論文提出的方法，屬輕微簡化。第 1、4 點皆支持。 |
| 16 | 自我檢測 | SUPPORTED | 三題答案（loss 在嵌入空間 vs 像素空間；collapse，I-JEPA 用 EMA、V-JEPA 另明寫 stop-gradient 與 predictor；87.1 vs 87.8）皆有 Wiki 支持。小提醒：第 3 題答案同樣省略「MAE 同樣不靠資料增強／架構相近」的限定。 |

## 統計
SUPPORTED 9 / UNSUPPORTED 1 / MISLEADING 5

非 SUPPORTED 的頁：4（MISLEADING）、7（UNSUPPORTED）、9（MISLEADING）、10（MISLEADING）、12（MISLEADING）、15（MISLEADING）。
