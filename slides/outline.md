# 簡報大綱：JEPA：不預測像素，預測意義

規則：只讀 `wiki/`。每頁列出教學目的、要點、**但書**、引用的 Wiki 頁（= `data-wiki`）。
寫 HTML 之前先跑 `python3 scripts/check_outline.py`（run-2 加入）。
敘事線：**為什麼 → 怎麼學 → JEPA 是什麼 → 難在哪 → 實際例子 → 怎麼看數字 → 最新進展 → 誠實面 → 大藍圖 → 收尾**。

| # | 標題 | 教學目的 | 要點 | 但書 | 引用 Wiki |
|---|---|---|---|---|---|
| 0 | JEPA：不預測像素，預測意義 | 封面 | 主題、對象 | — | （封面，不引用） |
| 1 | 人 20 小時學會開車，AI 呢？ | 動機 | LeCun 的出發點：20 小時 vs 百萬到十億筆資料；world model：補資訊、預測未來 | 本頁寫明是「可能的關鍵」和「假說」，不是已證實的結論 | `concepts/world-model.md#為什麼需要`、`#是什麼`、`sources/meta-lecun-blog.md#摘要` |
| 2 | 不用標註也能學：自監督學習 | 前置知識 | 從無標註資料學；把一部分藏起來猜（AI 補充框）；能量觀點一句話 | — | `concepts/self-supervised-learning.md#是什麼`、`#用能量來想` |
| 3 | 三種流派 | 定位 JEPA | 先講「表示」是什麼（AI 補充框）；三大流派表；Meta 對生成式的批評（人手）；聯合嵌入的問題；JEPA 的位置 | 無：只用定義和定位（三種做法在哪裡算 loss），沒有用到實驗結果 | `concepts/generative-vs-joint-embedding.md#自監督的三大流派生成式聯合嵌入jepa`、`#生成式的問題`、`#聯合嵌入的問題`、`#jepa-站在哪裡`、`concepts/pixel-vs-feature-prediction.md#生成式預測像素`、`concepts/self-supervised-learning.md#是什麼` |
| 4 | JEPA 的三個零件 | 核心概念 | context encoder / predictor / target encoder（EMA）；遮的是 target encoder 的輸出；L2 loss 一個式子 | 無：只用方法定義（零件、loss、遮輸出），沒有用到實驗結果 | `concepts/jepa.md#三個零件`、`#一句話`、`concepts/collapse.md#怎麼防`、`sources/ijepa.md#方法` |
| 5 | JEPA 的難點：collapse | 難點 | 輸出常數向量就作弊（AI 補充：loss 為零）；三類防法表；拿掉 variance 立刻崩塌 | — | `concepts/collapse.md#是什麼`、`#怎麼防` |
| 6 | VICReg 的三個項（run-2 新增） | 把 collapse 的防法講具體 | invariance / variance / covariance 三個項的直覺；拿掉 variance 立刻崩塌 | VICReg 主要賣點是可解釋、模組化，不是準確度大勝；ImageNet 和 Barlow Twins 打平 | `sources/vicreg.md#三個項只講直覺`、`#重點`、`#注意` |
| 7 | 主要範例：I-JEPA | 具體化 | 一塊 context 預測幾塊 target；遮罩要大塊；不需人工資料增強；multi-block 54.2 vs random 17.6（1% 標註，表 6） | 表 6 的消融用 ViT-B/16 和 1% 標註，不是所有設定；實驗都在圖片上（AI 補充框） | `sources/ijepa.md#一句話`、`#方法`、`#注意jepa-不是全面勝出`、`concepts/masking-strategy.md#i-jepa-的-multi-block-masking` |
| 8 | 預測表示真的比較好？ | 證據 | 66.9 vs 40.7（像素版本 800 vs 500 epoch）；V-JEPA 一致；16 張 A100、72 小時、約 5 倍迭代 | 表 7 只是一組消融；V-JEPA 微調差距很小 85.4 vs 85.6，凍結時 SSv2 也幾乎沒差 66.0 vs 66.2 | `concepts/pixel-vs-feature-prediction.md#證據`、`#注意`、`sources/ijepa.md#結果` |
| 9 | 從圖片到影片：V-JEPA | 延伸 | 2 million 支影片；K400 81.9%、SSv2 72.2%；SSv2 +21（和影像模型比）；樣本較少（和預測像素的方法比）；label-efficient | +21 是和影像模型比、凍結評估；ViT-L 比較時 ImageNet 略輸 OmniMAE（74.8% 對 75.1%），77.9% 是更大的 ViT-H/16；完整微調時特徵和像素差距很小 | `sources/vjepa.md#一句話`、`#結果`、`#注意` |
| 10 | 怎麼看這些數字 | 讀懂評估 | linear probe / 凍結 / 微調 / 低樣本（1% ≈ 12 或 13 張） | 和 view-invariance 方法比只是打平；優勢不是每個凍結任務都明顯（V-JEPA 表 1 的 SSv2 66.2 vs 66.0）；微調 87.1 vs 87.8 略輸；總結句是 AI 補充，放 AI 補充框 | `concepts/frozen-evaluation.md#linear-probe線性探測`、`#frozen-evaluation凍結評估`、`#fine-tuning微調`、`#low-shot低樣本`、`#為什麼要分清楚` |
| 11 | JEPA-Anything：把目標拆開來預測 | 前沿 | 論文認為單一目標讓容易的結構主導；拆成正交因子；七個領域；Pong −34.8% | v1 預印本；和標準 JEPA 比；組合介入只有 12.90%；正交因子不代表因果機制、生物證據樣本小；Hopper 輸（本頁也要寫，不能只放到別頁） | `concepts/orthogonal-predictive-factorization.md#核心想法概念版`、`sources/jepa-anything.md#問題`、`#論文報告的結果`、`#注意`、`concepts/orthogonal-predictive-factorization.md` |
| 12 | JEPA 輸在哪裡 | 批判思考 | 微調 87.1 vs 87.8；ImageNet 74.8 vs 75.1（OmniMAE 直接用 ImageNet 訓練）；Hopper；drops by 12%（287 → 29 張，80.6 → 68.2）；兩到 10 倍沒說跟誰比 | 本頁就是但書頁 | `sources/ijepa.md#注意jepa-不是全面勝出`、`sources/vjepa.md#注意`、`sources/jepa-anything.md#注意`、`sources/meta-ijepa-blog.md#注意` |
| 13 | 回到大藍圖：LeCun 的六個模組 | 收束到願景 | 六模組；架構以 world model 為中心，JEPA 是一個關鍵元素；predictor 是原始的 world model | 仍是研究方向；原文是「可以說」是未來幾十年的主要挑戰 | `concepts/world-model.md#lecun-的六模組架構一頁帶過`、`#注意`、`#和-jepa-的關係` |
| 14 | 帶走四句話 | 複習 | 預測表示；忽略不重要的細節，66.9 vs 40.7；難點 collapse（I-JEPA 不對稱架構）；不是全面勝出 | 第 2 句註明 1% 標註、一組消融、epoch 不同；第 4 句本身就是但書 | `concepts/jepa.md#一句話`、`#為什麼不預測像素`、`concepts/pixel-vs-feature-prediction.md#證據`、`concepts/collapse.md#怎麼防`、`sources/ijepa.md#注意jepa-不是全面勝出`、`sources/vjepa.md#注意`、`sources/jepa-anything.md#注意` |
| 15 | 自我檢測 | 檢查理解 | 3 題，答案用 fragment 顯示 | 第 3 題就是但書 | `concepts/generative-vs-joint-embedding.md#jepa-站在哪裡`、`concepts/pixel-vs-feature-prediction.md#生成式預測像素`、`concepts/collapse.md#怎麼防`、`concepts/frozen-evaluation.md#為什麼要分清楚` |

## 缺口（Wiki 沒有、簡報想用的）
- 無。第 2、3、5、10 列的 AI 補充框對應 Wiki 裡標了（AI 補充）的內容。
