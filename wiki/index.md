# JEPA LLM Wiki — 目錄

主題：**JEPA（Joint-Embedding Predictive Architecture）**：讓 AI 不預測像素、改預測「意義」的自監督學習架構，以及它背後的 world model 構想。
讀者：知道 AI、神經網路大概是什麼，沒學過 self-supervised learning 的同學。
規則見 [CLAUDE.md](../CLAUDE.md)，時間序紀錄見 [log.md](log.md)，原始資料清單見 [raw/SOURCES.md](../raw/SOURCES.md)。

## 建議閱讀順序
1. [world model](concepts/world-model.md)：為什麼要讓 AI 學「世界怎麼運作」
2. [self-supervised learning](concepts/self-supervised-learning.md)：不用標註怎麼學
3. [三大流派](concepts/generative-vs-joint-embedding.md)：生成式、聯合嵌入、JEPA
4. [JEPA](concepts/jepa.md)：核心概念頁
5. [預測像素 vs 預測表示](concepts/pixel-vs-feature-prediction.md)
6. [collapse](concepts/collapse.md)：最大的難點
7. [masking strategy](concepts/masking-strategy.md)
8. [怎麼看數字](concepts/frozen-evaluation.md)
9. [正交預測分解](concepts/orthogonal-predictive-factorization.md)：最新進展

## 概念頁（concepts）
| 頁面 | 摘要 |
|---|---|
| [world-model](concepts/world-model.md) | 機器內部對世界的模型；LeCun 的六模組架構 |
| [self-supervised-learning](concepts/self-supervised-learning.md) | 從無標註資料學表示；能量的觀點 |
| [generative-vs-joint-embedding](concepts/generative-vs-joint-embedding.md) | 自監督三大流派比較 |
| [jepa](concepts/jepa.md) | 三個零件、L2 loss、演進時間線 |
| [pixel-vs-feature-prediction](concepts/pixel-vs-feature-prediction.md) | 預測像素還是表示？證據與限制 |
| [collapse](concepts/collapse.md) | 表示崩塌與三類防法 |
| [masking-strategy](concepts/masking-strategy.md) | multi-block 遮罩為什麼重要 |
| [frozen-evaluation](concepts/frozen-evaluation.md) | linear probe、凍結評估、微調、低樣本 |
| [orthogonal-predictive-factorization](concepts/orthogonal-predictive-factorization.md) | JEPA-Anything 的核心想法 |

## 來源頁（sources）
| 頁面 | 摘要 |
|---|---|
| [meta-lecun-blog](sources/meta-lecun-blog.md) | 2022 Meta 部落格：LeCun 的 world model 構想 |
| [meta-ijepa-blog](sources/meta-ijepa-blog.md) | 2023 Meta 部落格：I-JEPA 白話介紹 |
| [ijepa](sources/ijepa.md) | I-JEPA 論文（主要範例） |
| [vjepa](sources/vjepa.md) | V-JEPA 論文（影片） |
| [vicreg](sources/vicreg.md) | VICReg 論文（collapse） |
| [jepa-anything](sources/jepa-anything.md) | JEPA-Anything 論文（2026，v1 預印本） |
