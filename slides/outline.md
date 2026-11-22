# 簡報大綱：JEPA：不預測像素，預測意義

規則：只讀 `wiki/`。每頁列出教學目的、要點、**但書**、引用的 Wiki 頁（= `data-wiki`）。
寫 HTML 之前先跑 `python3 scripts/check_outline.py`（run-2 加入）。
敘事線：**為什麼 → 怎麼學 → JEPA 是什麼 → 難在哪 → 實際例子 → 怎麼看數字 → 最新進展 → 誠實面 → 大藍圖 → 收尾**。

| # | 標題 | 教學目的 | 要點 | 但書 | 引用 Wiki |
|---|---|---|---|---|---|
| 0 | JEPA：不預測像素，預測意義 | 封面 | 主題、對象 | — | （封面，不引用） |
| 1 | 人 20 小時學會開車，AI 呢？ | 動機 | LeCun 的出發點：20 小時 vs 百萬到十億筆資料；world model：補資訊、預測未來 | 無：world model 頁的「注意」（研究方向、未來幾十年的挑戰）放在「大藍圖」頁 | `concepts/world-model.md#為什麼需要`、`#是什麼`、`sources/meta-lecun-blog.md#摘要` |
| 2 | 不用標註也能學：自監督學習 | 前置知識 | 從無標註資料學；把一部分藏起來猜（AI 補充框）；能量觀點一句話 | — | `concepts/self-supervised-learning.md#是什麼`、`#用能量來想` |
| 3 | 三種「猜」法 | 定位 JEPA | 三大流派表；生成式要補每個細節（人手）；JEPA 的位置 | 無：「像素 vs 表示」的但書放在「預測表示真的比較好？」頁 | `concepts/generative-vs-joint-embedding.md#自監督的三大流派生成式聯合嵌入jepa`、`#生成式的問題`、`#jepa-站在哪裡`、`concepts/pixel-vs-feature-prediction.md#生成式預測像素` |
| 4 | JEPA 的三個零件 | 核心概念 | context encoder / predictor / target encoder（EMA）；遮的是 target encoder 的輸出；L2 loss 一個式子 | 無：I-JEPA 頁的「注意」放在「JEPA 輸在哪裡」頁 | `concepts/jepa.md#三個零件`、`#一句話`、`concepts/collapse.md#怎麼防`、`sources/ijepa.md#方法` |
| 5 | JEPA 的難點：collapse | 難點 | 輸出常數向量就作弊（AI 補充：loss 為零）；三類防法表；拿掉 variance 立刻崩塌 | — | `concepts/collapse.md#是什麼`、`#怎麼防` |
| 6 | VICReg 的三個項（run-2 新增） | 把 collapse 的防法講具體 | invariance / variance / covariance 三個項的直覺；拿掉 variance 立刻崩塌 | VICReg 主要賣點是可解釋、模組化，不是準確度大勝；ImageNet 和 Barlow Twins 打平 | `sources/vicreg.md#三個項只講直覺`、`#重點`、`#注意` |
| 7 | 主要範例：I-JEPA | 具體化 | 一塊 context 預測幾塊 target；遮罩要大塊；不需人工資料增強；multi-block 54.2 vs random 17.6（1% 標註，表 6） | 只在圖片上驗證；消融多用 ViT-B/16 和 1% 標註 | `sources/ijepa.md#一句話`、`#方法`、`#注意jepa-不是全面勝出`、`concepts/masking-strategy.md#i-jepa-的-multi-block-masking` |
| 8 | 預測表示真的比較好？ | 證據 | 66.9 vs 40.7（像素版本 800 vs 500 epoch）；V-JEPA 一致；16 張 A100、72 小時、約 5 倍迭代 | 表 7 只是一組消融；V-JEPA 微調差距很小 85.4 vs 85.6 | `concepts/pixel-vs-feature-prediction.md#證據`、`#注意`、`sources/ijepa.md#結果` |
| 9 | 從圖片到影片：V-JEPA | 延伸 | 2 million 支影片；K400 81.9%、SSv2 72.2%；動作 +21；label-efficient | 無：V-JEPA 頁的「注意」放在「JEPA 輸在哪裡」頁 | `sources/vjepa.md#一句話`、`#結果` |
| 10 | 怎麼看這些數字 | 讀懂評估 | linear probe / 凍結 / 微調 / 低樣本（1% ≈ 12 或 13 張） | JEPA 優勢主要在凍結和低樣本，微調時變小 | `concepts/frozen-evaluation.md#linear-probe線性探測`、`#frozen-evaluation凍結評估`、`#fine-tuning微調`、`#low-shot低樣本`、`#為什麼要分清楚` |
| 11 | 最新進展：JEPA-Anything | 前沿 | 論文認為單一目標讓容易的結構主導；拆成正交因子；七個領域；Pong −34.8% | v1 預印本；和標準 JEPA 比；組合介入只有 12.90%；Hopper 輸（放在「JEPA 輸在哪裡」頁） | `concepts/orthogonal-predictive-factorization.md#核心想法概念版`、`sources/jepa-anything.md#問題`、`#論文報告的結果`、`#注意`、`concepts/orthogonal-predictive-factorization.md` |
| 12 | JEPA 輸在哪裡 | 批判思考 | 微調 87.1 vs 87.8；ImageNet 74.8 vs 75.1；Hopper；drops by 12%（287 → 29 張，80.6 → 68.2）；兩到 10 倍沒說跟誰比 | 本頁就是但書頁 | `sources/ijepa.md#注意jepa-不是全面勝出`、`sources/vjepa.md#注意`、`sources/jepa-anything.md#注意`、`sources/meta-ijepa-blog.md#注意` |
| 13 | 回到大藍圖：LeCun 的六個模組 | 收束到願景 | 六模組；world model 核心是 JEPA；predictor 是原始的 world model | 仍是研究方向，未來幾十年的主要挑戰 | `concepts/world-model.md#lecun-的六模組架構一頁帶過`、`#注意`、`#和-jepa-的關係` |
| 14 | 帶走四句話 | 複習 | 預測表示；忽略不重要的細節，66.9 vs 40.7；難點 collapse；不是全面勝出 | 第 4 句本身就是但書 | `concepts/jepa.md#一句話`、`#為什麼不預測像素`、`concepts/pixel-vs-feature-prediction.md#證據`、`concepts/collapse.md#怎麼防`、`sources/ijepa.md#注意jepa-不是全面勝出`、`sources/vjepa.md#注意`、`sources/jepa-anything.md#注意` |
| 15 | 自我檢測 | 檢查理解 | 3 題，答案用 fragment 顯示 | 第 3 題就是但書 | `concepts/generative-vs-joint-embedding.md#jepa-站在哪裡`、`concepts/pixel-vs-feature-prediction.md#生成式預測像素`、`concepts/collapse.md#怎麼防`、`concepts/frozen-evaluation.md#為什麼要分清楚` |

## 缺口（Wiki 沒有、簡報想用的）
- 無。第 2、5 頁的 AI 補充框對應 Wiki 裡標了（AI 補充）的內容。
