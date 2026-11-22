---
title: 怎麼看數字：凍結評估、linear probe、低樣本
type: concept
sources: [ijepa, vjepa]
---
# 怎麼看數字：凍結評估、linear probe、低樣本

（AI 補充）自監督模型訓練時沒有標註，那怎麼知道它學得好不好？論文常用以下幾種評估。

## Linear probe（線性探測）
訓練完後把 encoder 的權重**凍結**，只在上面訓練一個線性模型。[^ijepa-1][^ijepa-4]

（AI 補充）表示越好，簡單的線性模型就越能用它分類。

## Frozen evaluation（凍結評估）
V-JEPA 強調不調整模型參數、直接用凍結的骨幹網路。[^vjepa-1] 它用一個小的 attentive probe 當分類頭。[^vjepa-2]

## Fine-tuning（微調）
整個模型連同 encoder 一起用標註資料再訓練。I-JEPA 微調後是 87.1。[^ijepa-2]

## Low-shot（低樣本）
只用 1% 的 ImageNet 標註，大約每類 12 或 13 張圖。[^ijepa-3][^ijepa-5]

（AI 補充）看模型能不能用很少的標註學會。

## 為什麼要分清楚
- JEPA 的優勢主要在**凍結評估**和**低樣本**；完整微調時優勢變小，I-JEPA 甚至略輸 MAE。[^ijepa-2]
- V-JEPA 的 ImageNet 77.9% 是用兩層 attentive probe 量的。[^vjepa-3]

## 相關頁面
- [I-JEPA 論文](../sources/ijepa.md)、[V-JEPA 論文](../sources/vjepa.md)、[像素 vs 表示](pixel-vs-feature-prediction.md)

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "using a linear probe. After pretraining, the encoder weights"
[^ijepa-4]: [ijepa](../sources/ijepa.md) — "are frozen and a linear model is trained on top to"
[^ijepa-2]: [ijepa](../sources/ijepa.md) — "I-JEPA achieves 87.1 top-1 accuracy. Its performance is less than 1% away from the best MAE model despite I-JEPA being trained for 5.3 times less epochs than MAE."
[^ijepa-3]: [ijepa](../sources/ijepa.md) — "only 1% of the available ImageNet labels, corresponding"
[^ijepa-5]: [ijepa](../sources/ijepa.md) — "to roughly 12 or 13 images per class"
[^vjepa-1]: [vjepa](../sources/vjepa.md) — "without adaption of the model’s parameters; e.g., using a frozen backbone."
[^vjepa-2]: [vjepa](../sources/vjepa.md) — "downstream performance of the frozen backbones with an attentive probe"
[^vjepa-3]: [vjepa](../sources/vjepa.md) — "77.9% using a two-layer attentive probe."
