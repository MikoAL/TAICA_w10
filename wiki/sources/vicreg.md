---
title: VICReg 論文（Bardes, Ponce, LeCun, ICLR 2022）
type: source
sources: [vicreg]
---
# VICReg 論文（Bardes, Ponce, LeCun, ICLR 2022）

- 原文：VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning。[^vicreg-8]
- （AI 補充）角色：解釋 [collapse](../concepts/collapse.md) 以及一種**看得懂的**防法。

## 背景
很多方法用 joint embedding 架構：兩個網路對同一張圖的不同視角，產生相似的嵌入。[^vicreg-1] 最大的危險是 collapse：兩個分支乾脆忽略輸入，輸出一模一樣的常數向量。[^vicreg-2]

## 三個項（只講直覺）
- **Invariance（不變）**：同一張圖的兩個視角，嵌入要接近。這一項單獨用就會 collapse（附錄的消融表）。[^vicreg-9]
- **Variance（變異）**：同一批資料裡，不同樣本的嵌入必須不一樣。[^vicreg-4]
- **Covariance（共變異）**：嵌入的各個維度不要互相重複，防止「資訊上的 collapse」。[^vicreg-5]

## 重點
- 拿掉 variance 項，表示**立刻** collapse 成同一個向量；covariance 項救不了。[^vicreg-3]
- 其他方法（BYOL、SimSiam 的 momentum encoder、stop-gradient、predictor）也能避免 collapse，但為什麼有效並不完全清楚。[^vicreg-6] VICReg 改用明確、可解釋的限制。
- 準確度和當時最好的方法差不多，而且不需要 SimCLR 那種負樣本。[^vicreg-7]

## 注意
- VICReg 的主要賣點是**可解釋、模組化**，不是準確度大勝；ImageNet 上和 Barlow Twins 打平（表 1）。[^vicreg-7][^vicreg-10][^vicreg-11]

## 相關頁面
- [collapse](../concepts/collapse.md)、[生成式 vs 聯合嵌入](../concepts/generative-vs-joint-embedding.md)、[Meta LeCun 構想文](meta-lecun-blog.md)

## 引文
[^vicreg-1]: [vicreg](vicreg.md) — "Several recent approaches rely on a joint embedding architecture in which two networks are trained to produce similar embeddings for different views of the same image."
[^vicreg-2]: [vicreg](vicreg.md) — "a collapse in which the two branches ignore the inputs and produce identical and constant output vectors"
[^vicreg-3]: [vicreg](vicreg.md) — "Without variance regularization the representations immediately collapse to a single vector and the covariance term, which has no repulsive effect preventing collapse, has no impact."
[^vicreg-4]: [vicreg](vicreg.md) — "This term forces the embedding vectors of samples within a batch to be different."
[^vicreg-5]: [vicreg](vicreg.md) — "This term decorrelates the variables of each embedding and prevents an informational collapse in which the variables would vary together or be highly correlated."
[^vicreg-6]: [vicreg](vicreg.md) — "The dynamics of learning in these methods, and how they avoid collapse, is not fully understood"
[^vicreg-8]: [vicreg](vicreg.md) — "We introduce VICReg (Variance-Invariance-Covariance Regularization), a self-supervised method for"
[^vicreg-7]: [vicreg](vicreg.md) — "The performance of VICReg is on par with the state of the art without using the negative pairs of SimCLR"
[^vicreg-9]: [vicreg](vicreg.md) — "Inv 1 0 0 collapse"
[^vicreg-10]: [vicreg](vicreg.md) — "The main advantage of VICReg is the modularity of its objective function"
[^vicreg-11]: [vicreg](vicreg.md) — "avoiding collapse, while being clearer, more interpretable, and working with independent branches"
