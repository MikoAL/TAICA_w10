---
title: Meta 部落格：LeCun 的 world model 構想（2022）
type: source
sources: [meta-lecun-blog]
---
# Meta 部落格：LeCun 的 world model 構想（2022）

- 原文：Yann LeCun on a vision to make AI systems learn and reason like animals and humans，Meta AI 部落格，2022-02-23。[^meta-lecun-blog-1]
- （AI 補充）性質：構想預告，**沒有實驗結果**。

## 摘要
LeCun 指出人類學東西遠比 AI 有效率：青少年大約 20 小時就能學會開車。[^meta-lecun-blog-2] 他提出，關鍵**可能**是讓機器學會「世界怎麼運作」的內部模型，也就是 [world model](../concepts/world-model.md)。[^meta-lecun-blog-3]

他提出一個由六個模組組成的架構。[^meta-lecun-blog-4] 架構的中心是 world model。[^meta-lecun-blog-11] 難題是怎麼表示多種合理的預測、又忽略不重要的細節，[JEPA](../concepts/jepa.md) 是解法的「一個關鍵元素」：[^meta-lecun-blog-12] 把兩個輸入各自編碼成抽象表示，再從一個預測另一個。[^meta-lecun-blog-5][^meta-lecun-blog-13]

怎麼訓練 JEPA？文章說過去只能用 contrastive 方法，但表示維度很高時不實際；[^meta-lecun-blog-16] 近兩年出現了 regularized 方法，VICReg 是其中一種。[^meta-lecun-blog-6][^meta-lecun-blog-14][^meta-lecun-blog-15]

## 重點
- 常識可以看成一組 world model，告訴我們什麼可能、什麼合理、什麼不可能。[^meta-lecun-blog-7]
- JEPA 可以一層疊一層，學到更抽象、看得更遠的表示。[^meta-lecun-blog-8]
- 文章說得有保留：「可以說」（it could be argued）怎麼訓練 world model 是未來幾十年 AI 的主要挑戰。[^meta-lecun-blog-9]

## 注意
- 「累積的背景知識可能是常識的基礎」是假說，原文用 can be hypothesized。[^meta-lecun-blog-10]
- （AI 補充）嬰兒、動物的例子，文章沒有附實驗證據。
- （AI 補充）這篇只是預告，細節要看後來的論文（本 Wiki 沒有收錄原始立場論文，見 [SOURCES](../../raw/SOURCES.md)）。

## 相關頁面
- [world model](../concepts/world-model.md)、[JEPA](../concepts/jepa.md)、[collapse](../concepts/collapse.md)、[self-supervised learning](../concepts/self-supervised-learning.md)

## 引文
[^meta-lecun-blog-1]: [meta-lecun-blog](meta-lecun-blog.md) — "Yann LeCun on a vision to make AI systems learn and reason like animals and humans"
[^meta-lecun-blog-2]: [meta-lecun-blog](meta-lecun-blog.md) — "a teenager who has never sat behind a steering wheel can learn to drive in about 20 hours"
[^meta-lecun-blog-3]: [meta-lecun-blog](meta-lecun-blog.md) — "internal models of how the world works — may be the key"
[^meta-lecun-blog-4]: [meta-lecun-blog](meta-lecun-blog.md) — "LeCun proposes an architecture composed of six separate modules."
[^meta-lecun-blog-5]: [meta-lecun-blog](meta-lecun-blog.md) — "Inputs x and y are fed to trainable encoders that extract abstract representations of them"
[^meta-lecun-blog-6]: [meta-lecun-blog](meta-lecun-blog.md) — "Until recently, the only approach would have been to use contrastive methods"
[^meta-lecun-blog-7]: [meta-lecun-blog](meta-lecun-blog.md) — "common sense can be seen as a collection of models of the world that can guide on what is likely, what is plausible, and what is impossible"
[^meta-lecun-blog-8]: [meta-lecun-blog](meta-lecun-blog.md) — "This enables JEPAs to be stacked on top of one another so as to learn representations with higher levels of abstraction"
[^meta-lecun-blog-9]: [meta-lecun-blog](meta-lecun-blog.md) — "it could be argued that training world models constitutes the main challenge toward real progress in AI over the next decades"
[^meta-lecun-blog-10]: [meta-lecun-blog](meta-lecun-blog.md) — "It can be hypothesized that this accumulated knowledge may constitute the basis for what is often called common sense."
[^meta-lecun-blog-11]: [meta-lecun-blog](meta-lecun-blog.md) — "The centerpiece of the architecture is the predictive world model."
[^meta-lecun-blog-12]: [meta-lecun-blog](meta-lecun-blog.md) — "One key element of a solution is the Joint Embedding Predictive Architecture (JEPA)."
[^meta-lecun-blog-13]: [meta-lecun-blog](meta-lecun-blog.md) — "A predictor module is trained to predict s y from s x"
[^meta-lecun-blog-14]: [meta-lecun-blog](meta-lecun-blog.md) — "An alternative training strategy has emerged in the last two years: regularized methods."
[^meta-lecun-blog-15]: [meta-lecun-blog](meta-lecun-blog.md) — "One way is the VICReg method"
[^meta-lecun-blog-16]: [meta-lecun-blog](meta-lecun-blog.md) — "But this is rather impractical when the representations are high-dimensional."
