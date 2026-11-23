---
title: Self-supervised learning（自監督學習）
type: concept
sources: [ijepa, meta-ijepa-blog, meta-lecun-blog]
---
# Self-supervised learning（自監督學習）

## 是什麼
Self-supervised learning 是一種學「表示」（representation）的方法：系統自己學習輸入之間的關係。[^ijepa-1] 它直接從沒有標註的資料（圖片、聲音）學，不靠人工整理的標註資料集。[^meta-ijepa-blog-1]

（AI 補充）「表示」（representation，也叫嵌入 embedding）：模型把一張圖轉成的一串數字。意思相近的圖，這串數字也應該相近。

（AI 補充）直覺：把資料的一部分藏起來，讓模型從剩下的部分去猜。不需要人告訴它答案，因為答案就在資料裡。

## 用「能量」來想
I-JEPA 論文用 Energy-Based Model 的角度統一各種方法：相容的輸入給低能量，不相容的給高能量。[^ijepa-2] 三大流派見 [生成式 vs 聯合嵌入](generative-vs-joint-embedding.md)。

## 為什麼重要
LeCun 說人和動物似乎能靠觀察和極少量的互動，以不分任務的非監督方式學到大量背景知識。[^meta-lecun-blog-1][^meta-lecun-blog-2]

（AI 補充）自監督學習可以看成讓機器也這樣學。

## 相關頁面
- [生成式 vs 聯合嵌入](generative-vs-joint-embedding.md)、[JEPA](jepa.md)、[world model](world-model.md)

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "Common architectures for self-supervised learning, in which the system learns to capture the relationships between its inputs."
[^ijepa-2]: [ijepa](../sources/ijepa.md) — "The objective is to assign a high energy (large scaler value) to incompatible inputs, and to assign a low energy (low scaler value) to compatible inputs."
[^meta-ijepa-blog-1]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "directly from unlabeled data such as images or sounds, rather than from manually assembled labeled datasets"
[^meta-lecun-blog-1]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "through an incomprehensibly small amount of interactions in a task-independent, unsupervised way"
[^meta-lecun-blog-2]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "seem able to learn enormous amounts of background knowledge about how the world works through observation"
