---
title: 自監督的三大流派：生成式、聯合嵌入、JEPA
type: concept
sources: [ijepa, meta-ijepa-blog, vicreg]
---
# 自監督的三大流派：生成式、聯合嵌入、JEPA

I-JEPA 論文把 [self-supervised learning](self-supervised-learning.md) 的架構分成三種。[^ijepa-1]

| 流派 | 做法 | 代表 |
|---|---|---|
| Joint-Embedding（聯合嵌入） | 相容的輸入給相似的嵌入，不相容的給不同的嵌入 [^ijepa-2] | VICReg 等 [^vicreg-1] |
| Generative（生成式） | 用 decoder 直接**重建**訊號 y [^ijepa-3] | MAE [^ijepa-7] |
| JEPA | 用 predictor 預測訊號 y 的**嵌入** [^ijepa-4] | I-JEPA、V-JEPA |

## 生成式的問題
生成式模型想補完每一個缺少的細節，但世界本來就無法完全預測。[^meta-ijepa-blog-1] Meta 舉的例子：生成式模型很難把人手畫對。[^meta-ijepa-blog-2]

## 聯合嵌入的問題
聯合嵌入常常要對同一張圖做不同「視角」（資料增強），讓兩個嵌入接近。[^vicreg-1] I-JEPA 主打不需要這種人工設計的資料增強。[^ijepa-6] 聯合嵌入還有 [collapse](collapse.md) 的風險。

## JEPA 站在哪裡
JEPA 像生成式一樣「從一部分預測另一部分」，但像聯合嵌入一樣在**嵌入空間**比較：loss 算在嵌入空間，不是像素空間。[^ijepa-5] 見 [JEPA](jepa.md)、[像素 vs 表示](pixel-vs-feature-prediction.md)。

## 相關頁面
- [JEPA](jepa.md)、[self-supervised learning](self-supervised-learning.md)、[collapse](collapse.md)

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "Common architectures for self-supervised learning, in which the system learns to capture the relationships between its inputs."
[^ijepa-2]: [ijepa](../sources/ijepa.md) — "Joint-Embedding Architectures learn to output similar embeddings for compatible inputs x, y and dissimilar embeddings"
[^ijepa-3]: [ijepa](../sources/ijepa.md) — "Generative Architectures learn to directly reconstruct a signal y from a compatible signal x, using a decoder"
[^ijepa-4]: [ijepa](../sources/ijepa.md) — "tures learn to predict the embeddings of a signal y from a compatible signal x, using a predictor network"
[^ijepa-5]: [ijepa](../sources/ijepa.md) — "a key difference is that the loss function is applied in embedding space, not input space"
[^ijepa-6]: [ijepa](../sources/ijepa.md) — "learning semantic image representations without relying on hand-crafted data augmentations"
[^meta-ijepa-blog-1]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "the model tries to fill-in every bit of missing information, even though the world is inherently unpredictable"
[^meta-ijepa-blog-2]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "it is notoriously difficult for generative models to generate human hands accurately"
[^vicreg-1]: [vicreg](../sources/vicreg.md) — "Several recent approaches rely on a joint embedding architecture in which two networks are trained to produce similar embeddings for different views of the same image."
[^ijepa-7]: [ijepa](../sources/ijepa.md) — "By reconstructing missing patches in pixels space, MAE"
