---
title: JEPA（Joint-Embedding Predictive Architecture）
type: concept
sources: [ijepa, meta-ijepa-blog, meta-lecun-blog, vjepa, jepa-anything]
---
# JEPA（Joint-Embedding Predictive Architecture）

## 一句話
JEPA 從訊號 x 的嵌入，預測相容訊號 y 的**嵌入**，而不是預測 y 本身。[^ijepa-1]

## 三個零件
- **Context encoder**：把看得到的部分 x 編碼成表示。I-JEPA 用 ViT，只處理看得到的區塊。[^meta-ijepa-blog-1]
- **Target encoder**：把被遮住的部分 y 編碼成「答案」表示。它是 context encoder 的指數移動平均（EMA）。[^ijepa-2]
- **Predictor**：從 x 的表示，預測 y 的表示。[^ijepa-1]

訓練目標：預測出的表示和目標表示之間的平均 L2 距離越小越好。[^ijepa-3]

$$\text{loss} = \frac{1}{M}\sum_{i=1}^{M}\lVert \hat{s}_{y_i} - s_{y_i} \rVert_2^2$$

（白話：M 塊目標區域，每塊「預測的表示」和「真正的表示」差多少，取平均。）[^ijepa-3]

## 為什麼不預測像素
世界很多細節本來就無法預測，生成式模型卻要補完每一個細節。[^meta-ijepa-blog-2] JEPA 在抽象表示裡比較，可以忽略不重要的細節。[^meta-ijepa-blog-3] 實驗證據見 [像素 vs 表示](pixel-vs-feature-prediction.md)。

## 演進
| 年份 | 名稱 | 重點 |
|---|---|---|
| 2022 | LeCun 構想 | JEPA 是 world model 的核心，可以一層疊一層 [^meta-lecun-blog-1] |
| 2023 | [I-JEPA](../sources/ijepa.md) | 第一個實作，用在圖片 [^meta-ijepa-blog-4] |
| 2024 | [V-JEPA](../sources/vjepa.md) | 延伸到影片，只用特徵預測 [^vjepa-1] |
| 2026 | [JEPA-Anything](../sources/jepa-anything.md) | 論文報告：把目標拆成正交因子，用在七個領域 [^jepa-anything-1] |

## 難點
預測表示有一個偷懶解：encoder 不管輸入都輸出同一個東西。這叫 [collapse](collapse.md)。[^vjepa-2]

## 相關頁面
- [生成式 vs 聯合嵌入](generative-vs-joint-embedding.md)、[collapse](collapse.md)、[masking strategy](masking-strategy.md)、[world model](world-model.md)、[orthogonal predictive factorization](orthogonal-predictive-factorization.md)

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "Joint-Embedding Predictive Architectures learn to predict the embeddings of a signal y from a compatible signal x"
[^ijepa-2]: [ijepa](../sources/ijepa.md) — "The use of an exponential moving average target-encoder"
[^ijepa-3]: [ijepa](../sources/ijepa.md) — "The loss is simply the average L2 distance between the predicted patch-level representations"
[^meta-ijepa-blog-1]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "The context encoder is a Vision Transformer (ViT) that only processes the visible context patches."
[^meta-ijepa-blog-2]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "the model tries to fill-in every bit of missing information, even though the world is inherently unpredictable"
[^meta-ijepa-blog-3]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "which compares abstract representations of images (rather than comparing the pixels themselves)"
[^meta-ijepa-blog-4]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "We’re excited to introduce the first AI model based on a key component of LeCun’s vision."
[^meta-lecun-blog-1]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "This enables JEPAs to be stacked on top of one another so as to learn representations with higher levels of abstraction"
[^vjepa-1]: [vjepa](../sources/vjepa.md) — "introduces V-JEPA, a collection of vision models trained solely using a feature prediction objective"
[^vjepa-2]: [vjepa](../sources/vjepa.md) — "would admit a trivial solution, where the encoder"
[^jepa-anything-1]: [jepa-anything](../sources/jepa-anything.md) — "We evaluate JEPA -Anything across seven domains"
