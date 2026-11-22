# 簡報大綱：JEPA：不預測像素，預測意義

規則：只讀 `wiki/`。每頁列出教學目的、要點、引用的 Wiki 頁（= `data-wiki`）。
敘事線：**為什麼 → 怎麼學 → JEPA 是什麼 → 難在哪 → 實際例子 → 怎麼看數字 → 最新進展 → 誠實面 → 大藍圖 → 收尾**。

| # | 標題 | 教學目的 | 要點 | 引用 Wiki |
|---|---|---|---|---|
| 0 | JEPA：不預測像素，預測意義 | 封面 | 主題、對象 | （封面，不引用） |
| 1 | 人 20 小時學會開車，AI 呢？ | 動機 | 20 小時 vs 百萬到十億筆資料；關鍵是 world model：補資訊、預測未來 | `concepts/world-model.md#為什麼需要`、`#是什麼` |
| 2 | 不用標註也能學：自監督學習 | 前置知識 | 從無標註資料學；把一部分藏起來猜（AI 補充）；能量觀點一句話 | `concepts/self-supervised-learning.md#是什麼` |
| 3 | 三種「猜」法 | 定位 JEPA | 三大流派表；生成式要補每個細節（人手） | `concepts/generative-vs-joint-embedding.md#自監督的三大流派生成式聯合嵌入jepa`、`#生成式的問題` |
| 4 | JEPA 的三個零件 | 核心概念 | context encoder / target encoder(EMA) / predictor；L2 loss 一個式子 | `concepts/jepa.md#三個零件` |
| 5 | 最大的陷阱：collapse | 難點 | 輸出常數向量就作弊；三類防法表 | `concepts/collapse.md#是什麼`、`#怎麼防` |
| 6 | 主要範例：I-JEPA | 具體化 | 一塊 context 預測幾塊 target；遮罩要大塊；multi-block 54.2 vs random 17.6 | `sources/ijepa.md#方法`、`concepts/masking-strategy.md#i-jepa-的-multi-block-masking` |
| 7 | 證據：預測表示真的比較好？ | 證據 | 66.9 vs 40.7（且像素多訓練 800 vs 500 epoch）；V-JEPA 也一致；16 張 A100、72 小時 | `concepts/pixel-vs-feature-prediction.md#證據`、`sources/ijepa.md#結果` |
| 8 | 從圖片到影片：V-JEPA | 延伸 | 2 million 支影片；動作任務 +21；K400 81.9 / SSv2 72.2 | `sources/vjepa.md#結果` |
| 9 | 怎麼看這些數字 | 讀懂評估 | linear probe / 凍結 / 微調 / 低樣本（1% ≈ 12–13 張） | `concepts/frozen-evaluation.md#linear-probe線性探測`、`#low-shot低樣本`、`#為什麼要分清楚` |
| 10 | 最新進展：JEPA-Anything | 前沿 | 單一目標的問題；拆成正交因子；論文報告 Pong −34.8%；v1 預印本 | `concepts/orthogonal-predictive-factorization.md#核心想法概念版`、`sources/jepa-anything.md#論文報告的結果` |
| 11 | JEPA 輸在哪裡 | 批判思考 | 微調 87.1 vs MAE 87.8；ImageNet 74.8 vs 75.1；Hopper；「drops by 12%」是百分點 | `sources/ijepa.md#注意jepa-不是全面勝出`、`sources/vjepa.md#注意`、`sources/jepa-anything.md#注意` |
| 12 | LeCun 的大藍圖 | 收束到願景 | 六模組，一頁帶過；world model 是核心；仍是未來幾十年的挑戰 | `concepts/world-model.md#lecun-的六模組架構一頁帶過`、`#注意` |
| 13 | 總結 | 複習 | 4 句話帶走 | `concepts/jepa.md#一句話`、`concepts/collapse.md#是什麼`、`concepts/pixel-vs-feature-prediction.md#證據` |
| 14 | 自我檢測 | 檢查理解 | 3 題，答案用 fragment 顯示 | `concepts/jepa.md#三個零件`、`concepts/collapse.md#怎麼防`、`concepts/frozen-evaluation.md#為什麼要分清楚` |

## 缺口（Wiki 沒有、簡報想用的）
- 無。第 2 頁「把一部分藏起來猜」是 Wiki 裡標了（AI 補充）的內容，簡報照樣標示。
