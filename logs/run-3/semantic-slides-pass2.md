# 語意檢查：簡報 → Wiki（run-3 第 2 次）

範圍：`index.html` 第 2–16 頁（第 1 頁封面略過），含講者備註、圖示、隱藏答案；只對照各頁引用的 Wiki 頁。

| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 2 | 人 20 小時學會開車，AI 呢？ | SUPPORTED | 數字、「可能關鍵」「假說」的保留語氣都和 world-model.md / meta-lecun-blog.md 一致。 |
| 3 | 不用標註也能學：自監督學習 | SUPPORTED | 直覺說明已放 `.ai-note`，對應 Wiki 的（AI 補充）。 |
| 4 | 自監督的三種流派 | SUPPORTED | 「表示／嵌入」說明在 `.ai-note` 內。表格「在哪裡比較」欄是把 Wiki 的「做法」欄整理成一欄，內容沒有走樣。 |
| 5 | JEPA 的三個零件（以 I-JEPA 為例） | SUPPORTED | 架構圖（輸入不遮、遮的是 target encoder 輸出、EMA）、L2 式子與白話都和 jepa.md、ijepa.md 一致。 |
| 6 | JEPA 的難點：collapse | SUPPORTED | 「loss 永遠是零」在 `.ai-note` 內。四種防法對應表和 collapse.md 一致。 |
| 7 | 防 collapse 的一種做法：VICReg 的三個項 | SUPPORTED | 三個項、「表 1 打平」「可解釋、模組化」都有出處。備註把「為什麼有效還不清楚」說成 EMA，Wiki 原句指的是 BYOL／SimSiam 的 momentum encoder、stop-gradient、predictor 這類技巧。意思相同，只是比較簡略。 |
| 8 | 主要範例：I-JEPA（2023，圖片） | SUPPORTED | 54.2 vs 17.6（表 6）與 ViT-B/16、1% 標註的但書都有出處，長條比例約 32%，也對得上。格子圖標「示意」，備註已補一句「遮的是輸出，不是遮輸入」。 |
| 9 | 預測表示真的比較好？ | SUPPORTED | 66.9／40.7、500／800 epoch、訓練成本、V-JEPA 85.4／85.6 與 66.0／66.2 都對得上。「表 7 只是一組消融」的但書有寫。 |
| 10 | 從圖片到影片：V-JEPA（2024） | SUPPORTED | 數字與比較對象（影像模型／預測像素的方法）都有交代。74.8 vs 75.1 及 OmniMAE 用 ImageNet 訓練的但書也有。 |
| 11 | 怎麼看這些數字 | MISLEADING | 「合起來看：JEPA 的優勢在凍結評估和低樣本比較明顯」放在 `.ai-note` 內，標示正確。但頁面只引用 frozen-evaluation.md。ijepa.md「注意」另寫了 ImageNet linear probe 對 view-invariance 方法只有大模型才打平、不是大幅領先，這一點沒有出現。第一條條列有寫「贏過 MAE」，初學者讀完仍可能以為凍結評估下 JEPA 普遍明顯領先。建議補上這個但書，或把 `.ai-note` 改成「相對 MAE」。 |
| 12 | JEPA-Anything（2026）：把目標拆開來預測 | SUPPORTED | 「論文報告」「v1 預印本」、34.8%、12.90%、Hopper、作者提醒都有出處。輕微挑剔：分解示意圖圖說的「不是切圖，也不是固定四個」是簡報自己加的，Wiki 只說「拆成幾個成分」，沒有這兩點。方向是保守的，不算錯。 |
| 13 | JEPA 輸在哪裡 | SUPPORTED | 87.1／87.8（5.3 倍）、74.8／75.1、Hopper「看環境而定」、「drops by 12%」是百分點、Meta「沒說跟誰比」都有出處。 |
| 14 | 回到大藍圖：LeCun 的六個模組 | SUPPORTED | 六模組、「一個關鍵元素」、「原始、受限的 world model」、「it could be argued」都有出處。備註的「不等於整個 world model」是簡報的推論，和 Wiki 不衝突。 |
| 15 | 帶走四句話 | SUPPORTED | 數字與但書和前面各頁一致。第 4 點「看外觀的任務仍可能輸」是 V-JEPA 只「縮小差距」加上 ImageNet 略輸 OmniMAE 的概括，有「可能」保留。 |
| 16 | 自我檢測 | SUPPORTED | 三個答案都有出處。第 3 題「凍結和低樣本時 I-JEPA 贏過 MAE」同第 11 頁的挑剔：比較對象是 MAE，沒有說對 view-invariance 方法只是打平。 |

## 統計
SUPPORTED 14 / UNSUPPORTED 0 / MISLEADING 1
