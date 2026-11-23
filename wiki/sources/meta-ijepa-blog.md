---
title: Meta 部落格：I-JEPA（2023）
type: source
sources: [meta-ijepa-blog]
---
# Meta 部落格：I-JEPA（2023）

- 原文：I-JEPA: The first AI model based on Yann LeCun's vision for more human-like AI，Meta AI 部落格，2023-06-13。[^meta-ijepa-blog-1]
- （AI 補充）性質：給一般讀者的介紹文，對應論文見 [I-JEPA 論文](ijepa.md)。

## 摘要
I-JEPA 學習的方式是比較圖片的抽象表示，而不是比較像素本身。[^meta-ijepa-blog-2] 它是 [self-supervised learning](../concepts/self-supervised-learning.md)：直接從沒有標註的資料學，不靠人工整理的標註資料集。[^meta-ijepa-blog-3]

文章批評 [生成式方法](../concepts/generative-vs-joint-embedding.md)：模型會試著補完每一個缺少的細節，但世界本來就無法完全預測。[^meta-ijepa-blog-4] 舉的例子是生成式模型很難把人手畫對。[^meta-ijepa-blog-5]

## 重點
- 架構：context encoder 是 Vision Transformer（ViT），只處理看得到的區塊。[^meta-ijepa-blog-6]
- predictor 可以看成一個原始、受限的 [world model](../concepts/world-model.md)。[^meta-ijepa-blog-7]
- 用多區塊遮罩（[multi-block masking](../concepts/masking-strategy.md)）引導模型學到語意特徵。[^meta-ijepa-blog-8]
- 訓練成本：一個 632M 參數的 ViT，用 16 張 A100 GPU，不到 72 小時。[^meta-ijepa-blog-9]
- 低樣本：每類只用 12 個標註範例就能分類 ImageNet。[^meta-ijepa-blog-10]
- 未來方向：把 JEPA 推到影片、圖文配對等更豐富的資料。[^meta-ijepa-blog-11][^meta-ijepa-blog-14]

## 注意
- 「其他方法通常要兩到 10 倍 GPU 時數」這句沒有說是跟哪些方法、在什麼設定下比。[^meta-ijepa-blog-12]
- 部落格說每類「12 個」標註範例；論文的說法是 1% 標註「大約每類 12 或 13 張」，見 [I-JEPA 論文](ijepa.md)。[^meta-ijepa-blog-10][^ijepa-1][^ijepa-2]
- 標題的「first」指的是 LeCun 構想中的**一個元件**，不是整個架構。[^meta-ijepa-blog-13]

## 相關頁面
- [I-JEPA 論文](ijepa.md)、[JEPA](../concepts/jepa.md)、[生成式 vs 聯合嵌入](../concepts/generative-vs-joint-embedding.md)

## 引文
[^meta-ijepa-blog-1]: [meta-ijepa-blog](meta-ijepa-blog.md) — "I-JEPA: The first AI model based on Yann LeCun’s vision for more human-like AI"
[^meta-ijepa-blog-2]: [meta-ijepa-blog](meta-ijepa-blog.md) — "learns by creating an internal model of the outside world, which compares abstract representations of images (rather than comparing the pixels themselves)"
[^meta-ijepa-blog-3]: [meta-ijepa-blog](meta-ijepa-blog.md) — "directly from unlabeled data such as images or sounds, rather than from manually assembled labeled datasets"
[^meta-ijepa-blog-4]: [meta-ijepa-blog](meta-ijepa-blog.md) — "the model tries to fill-in every bit of missing information, even though the world is inherently unpredictable"
[^meta-ijepa-blog-5]: [meta-ijepa-blog](meta-ijepa-blog.md) — "it is notoriously difficult for generative models to generate human hands accurately"
[^meta-ijepa-blog-6]: [meta-ijepa-blog](meta-ijepa-blog.md) — "The context encoder is a Vision Transformer (ViT) that only processes the visible context patches."
[^meta-ijepa-blog-7]: [meta-ijepa-blog](meta-ijepa-blog.md) — "The predictor in I-JEPA can be seen as a primitive (and restricted) world-model"
[^meta-ijepa-blog-8]: [meta-ijepa-blog](meta-ijepa-blog.md) — "the proposed multi-block masking strategy"
[^meta-ijepa-blog-9]: [meta-ijepa-blog](meta-ijepa-blog.md) — "we train a 632M parameter visual transformer model using 16 A100 GPUs in under 72 hours"
[^meta-ijepa-blog-10]: [meta-ijepa-blog](meta-ijepa-blog.md) — "with only 12 labeled examples per class"
[^ijepa-1]: [ijepa](ijepa.md) — "only 1% of the available ImageNet labels, corresponding"
[^ijepa-2]: [ijepa](ijepa.md) — "to roughly 12 or 13 images per class"
[^meta-ijepa-blog-11]: [meta-ijepa-blog](meta-ijepa-blog.md) — "It would be particularly interesting to advance JEPAs to learn more general world-models from richer modalities"
[^meta-ijepa-blog-12]: [meta-ijepa-blog](meta-ijepa-blog.md) — "Other methods typically take two to 10 times more GPU-hours and achieve worse error rates when trained with the same amount of data."
[^meta-ijepa-blog-13]: [meta-ijepa-blog](meta-ijepa-blog.md) — "We’re excited to introduce the first AI model based on a key component of LeCun’s vision."
[^meta-ijepa-blog-14]: [meta-ijepa-blog](meta-ijepa-blog.md) — "We look forward to working to extend the JEPA approach to other domains, like image-text paired data and video data."
