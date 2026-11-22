---
title: Meta 部落格：LeCun 的 world model 構想（2022）
type: source
sources: [meta-lecun-blog]
---
# Meta 部落格：LeCun 的 world model 構想（2022）

- 原文：Yann LeCun on a vision to make AI systems learn and reason like animals and humans，Meta AI 部落格，2022-02-23。[^meta-lecun-blog-1]
- （AI 補充）性質：構想預告，**沒有實驗結果**。

## 摘要
LeCun 指出人類學東西遠比 AI 有效率：青少年大約 20 小時就能學會開車。[^meta-lecun-blog-2] 他主張關鍵是讓機器學會「世界怎麼運作」的內部模型，也就是 [world model](../concepts/world-model.md)。[^meta-lecun-blog-3]

他提出一個由六個模組組成的架構。[^meta-lecun-blog-4] 其中 world model 的核心就是 [JEPA](../concepts/jepa.md)：把兩個輸入各自編碼成抽象表示，再從一個預測另一個。[^meta-lecun-blog-5]

訓練 JEPA 要防止 [collapse](../concepts/collapse.md)。文章說過去只能用 contrastive 方法，現在有 VICReg 這類 regularized 方法可用。[^meta-lecun-blog-6]

## 重點
- 常識可以看成一組 world model，告訴我們什麼可能、什麼合理、什麼不可能。[^meta-lecun-blog-7]
- JEPA 可以一層疊一層，學到更抽象、看得更遠的表示。[^meta-lecun-blog-8]
- Meta 自己也承認：怎麼訓練 world model 是未來幾十年 AI 的主要挑戰。[^meta-lecun-blog-9]

## 注意
- 嬰兒、動物的比較是假說，文章沒有給證據。[^meta-lecun-blog-10]
- （AI 補充）這篇只是預告，細節要看後來的論文（本 Wiki 沒有收錄原始立場論文，見 [SOURCES](../../raw/SOURCES.md)）。

## 相關頁面
- [world model](../concepts/world-model.md)、[JEPA](../concepts/jepa.md)、[collapse](../concepts/collapse.md)、[self-supervised learning](../concepts/self-supervised-learning.md)

## 引文
[^meta-lecun-blog-1]: [meta-lecun-blog](meta-lecun-blog.md) — "Yann LeCun on a vision to make AI systems learn and reason like animals and humans"
[^meta-lecun-blog-2]: [meta-lecun-blog](meta-lecun-blog.md) — "a teenager who has never sat behind a steering wheel can learn to drive in about 20 hours"
[^meta-lecun-blog-3]: [meta-lecun-blog](meta-lecun-blog.md) — "internal models of how the world works"
[^meta-lecun-blog-4]: [meta-lecun-blog](meta-lecun-blog.md) — "LeCun proposes an architecture composed of six separate modules."
[^meta-lecun-blog-5]: [meta-lecun-blog](meta-lecun-blog.md) — "trainable encoders that extract abstract representations of them"
[^meta-lecun-blog-6]: [meta-lecun-blog](meta-lecun-blog.md) — "Until recently, the only approach would have been to use contrastive methods"
[^meta-lecun-blog-7]: [meta-lecun-blog](meta-lecun-blog.md) — "common sense can be seen as a collection of models of the world that can guide on what is likely, what is plausible, and what is impossible"
[^meta-lecun-blog-8]: [meta-lecun-blog](meta-lecun-blog.md) — "This enables JEPAs to be stacked on top of one another so as to learn representations with higher levels of abstraction"
[^meta-lecun-blog-9]: [meta-lecun-blog](meta-lecun-blog.md) — "training world models constitutes the main challenge toward real progress in AI over the next decades"
[^meta-lecun-blog-10]: [meta-lecun-blog](meta-lecun-blog.md) — "It can be hypothesized"
