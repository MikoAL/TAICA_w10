---
title: I-JEPA 論文（Assran et al., CVPR 2023）
type: source
sources: [ijepa]
---
# I-JEPA 論文（Assran et al., CVPR 2023）

- 原文：Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture。[^ijepa-1]
- （AI 補充）角色：本 Wiki 的**主要範例**。

## 一句話
從圖片中**一塊看得到的區域**（context block），預測**幾塊被遮住區域的表示**（target blocks），而且不需要人工設計的資料增強。[^ijepa-2][^ijepa-20]

## 方法
- JEPA 學習從訊號 x 預測相容訊號 y 的嵌入（embedding）。[^ijepa-3]
- 和生成式方法（如 MAE）一個關鍵差別：loss 算在**嵌入空間**，不是輸入（像素）空間。[^ijepa-4] 見 [像素 vs 表示](../concepts/pixel-vs-feature-prediction.md)。
- 遮罩設計很關鍵：要預測幾塊夠大的（語意層級）目標區塊，並給一個夠有資訊量、分布夠廣的 context 區塊。[^ijepa-5] 見 [masking strategy](../concepts/masking-strategy.md)。
- 目標區塊是遮住 target encoder 的**輸出**，不是遮住輸入。[^ijepa-6]
- 為了避免 [collapse](../concepts/collapse.md)，x 和 y 兩邊的 encoder 用**不對稱**的架構。[^ijepa-21][^ijepa-22] target encoder 的權重是 context encoder 的指數移動平均（EMA），論文說這對訓練是必要的。[^ijepa-7][^ijepa-23][^ijepa-24]
- loss 就是預測出的 patch 表示和目標 patch 表示之間的平均 L2 距離。[^ijepa-8]

## 結果
- 低樣本 ImageNet：只用 1% 標註，大約每類 12 或 13 張圖。[^ijepa-9][^ijepa-19]
- 預測像素 vs 預測表示：像素 40.7（訓練 800 epoch）、表示 66.9（訓練 500 epoch），在像素空間算 loss 語意品質明顯下降（表 7）。[^ijepa-10]
- 計算成本：ViT-Huge/14 用 16 張 A100、不到 72 小時。[^ijepa-16][^ijepa-11]
- 比 MAE 少約 5 倍的迭代次數就收斂。[^ijepa-12]
- 遮罩策略：只用 1% 標註時，multi-block 54.2，其他遮法只有 15.5–20.2（表 6）。[^ijepa-13][^ijepa-17]

## 注意（JEPA 不是全面勝出）
- 完整微調（fine-tune）時 I-JEPA 87.1，MAE 87.8（表 15），I-JEPA 略輸，但訓練 epoch 少 5.3 倍。[^ijepa-14][^ijepa-18]
- ImageNet linear probe：大模型才和 view-invariance 方法打平，不是大幅領先。[^ijepa-15]
- 低樣本（1% 標註）：最大的、解析度 448 的模型才超過這些方法。[^ijepa-25][^ijepa-28][^ijepa-9]
- 低階任務（物件計數、深度預測）：贏過 view-invariance 方法。[^ijepa-26]
- 表 6 的消融實驗用 ViT-B/16 和 1% 標註，表 7 用 ViT-L/16（表 6、表 7）。[^ijepa-17][^ijepa-10][^ijepa-27]
- （AI 補充）這篇的實驗都在圖片上；影片要看 [V-JEPA](vjepa.md)。

## 相關頁面
- [JEPA](../concepts/jepa.md)、[Meta I-JEPA 部落格](meta-ijepa-blog.md)、[masking strategy](../concepts/masking-strategy.md)、[collapse](../concepts/collapse.md)、[怎麼看數字](../concepts/frozen-evaluation.md)

## 引文
[^ijepa-1]: [ijepa](ijepa.md) — "Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture"
[^ijepa-2]: [ijepa](ijepa.md) — "learning semantic image representations without relying on hand-crafted data augmentations"
[^ijepa-3]: [ijepa](ijepa.md) — "Joint-Embedding Predictive Architectures learn to predict the embeddings of a signal y from a compatible signal x"
[^ijepa-4]: [ijepa](ijepa.md) — "a key difference is that the loss function is applied in embedding space, not input space"
[^ijepa-5]: [ijepa](ijepa.md) — "we find that it is important to predict several relatively large (semantic) target blocks, and to use a sufficiently informative (spatially distributed) context block."
[^ijepa-6]: [ijepa](ijepa.md) — "the target blocks are obtained by masking the output of the target-encoder, not the input"
[^ijepa-7]: [ijepa](ijepa.md) — "The use of an exponential moving average target-encoder"
[^ijepa-8]: [ijepa](ijepa.md) — "The loss is simply the average L2 distance between the predicted patch-level representations"
[^ijepa-9]: [ijepa](ijepa.md) — "only 1% of the available ImageNet labels, corresponding"
[^ijepa-10]: [ijepa](ijepa.md) — "Table 7. Ablating targets. Linear evaluation on ImageNet-1K"
[^ijepa-11]: [ijepa](ijepa.md) — "under 72 hours to achieve strong downstream performance"
[^ijepa-12]: [ijepa](ijepa.md) — "I-JEPA converges in roughly 5×"
[^ijepa-13]: [ijepa](ijepa.md) — "The proposed multi-block masking strategy is helpful for guiding I-JEPA to learn semantic representations."
[^ijepa-14]: [ijepa](ijepa.md) — "I-JEPA achieves 87.1 top-1 accuracy. Its performance is less than 1% away from the best MAE model despite I-JEPA being trained for 5.3 times less epochs than MAE."
[^ijepa-16]: [ijepa](ijepa.md) — "train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in"
[^ijepa-17]: [ijepa](ijepa.md) — "Table 6. Ablating masking strategy. Linear evaluation on ImageNet-1K using only 1% of the available labels"
[^ijepa-18]: [ijepa](ijepa.md) — "Table 15. Finetuning on the full ImageNet dataset."
[^ijepa-19]: [ijepa](ijepa.md) — "to roughly 12 or 13 images per class"
[^ijepa-15]: [ijepa](ijepa.md) — "larger I-JEPA model matches the performance of view-invariance"
[^ijepa-20]: [ijepa](ijepa.md) — "Architecture uses a single context block to predict"
[^ijepa-21]: [ijepa](ijepa.md) — "JEPAs; we leverage an asymmetric architecture between the"
[^ijepa-22]: [ijepa](ijepa.md) — "x- and y-encoders to avoid representation collapse."
[^ijepa-23]: [ijepa](ijepa.md) — "are updated at each iteration via an exponential moving average of"
[^ijepa-24]: [ijepa](ijepa.md) — "has proven essential for training JEAs with Vision"
[^ijepa-25]: [ijepa](ijepa.md) — "trained at resolution 448 surpasses previous methods"
[^ijepa-26]: [ijepa](ijepa.md) — "ing pretraining and outperforms view-invariance based methods"
[^ijepa-27]: [ijepa](ijepa.md) — "a ViT-B/16 for 300 epochs. Comparison of proposed multi-block masking strategy."
[^ijepa-28]: [ijepa](ijepa.md) — "Table 2. ImageNet-1%. Semi-supervised evaluation on"
