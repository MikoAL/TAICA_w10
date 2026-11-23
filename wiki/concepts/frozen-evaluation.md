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
- **Linear probe（凍結）**：I-JEPA 明顯贏過 MAE 這類同樣不靠資料增強的方法。[^ijepa-6]
- **低樣本**：只用 1% 標註時，I-JEPA 贏過架構相近的 MAE，而且訓練 epoch 比較少。[^ijepa-3][^ijepa-7][^ijepa-8]
- **完整微調**：I-JEPA 87.1，MAE 87.8（表 15），略輸。[^ijepa-2][^ijepa-9]
- **V-JEPA 的特徵 vs 像素（表 1）**：凍結評估時 K400 差距大（73.7 vs 68.6），SSv2 幾乎沒差（66.2 vs 66.0）；完整微調差距很小（85.6 vs 85.4）。論文自己的說法是凍結和微調都有進步。[^vjepa-4][^vjepa-5]
- **和 view-invariance 方法比**（ImageNet linear probe）：大模型才打平，不是大幅領先。[^ijepa-10]
- （AI 補充）合起來看：和 MAE、預測像素的做法比，JEPA 的優勢在凍結評估和低樣本比較明顯，完整微調時變小；但不是每個凍結任務都明顯，和 view-invariance 方法比也只是打平。
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
[^ijepa-6]: [ijepa](../sources/ijepa.md) — "we see that I-JEPA significantly improves linear probing"
[^ijepa-7]: [ijepa](../sources/ijepa.md) — "works best for each respective method. I-JEPA"
[^ijepa-8]: [ijepa](../sources/ijepa.md) — "forms MAE while requiring less pretraining epochs when"
[^ijepa-9]: [ijepa](../sources/ijepa.md) — "Table 15. Finetuning on the full ImageNet dataset. I-JEPA achieves competitive performance."
[^vjepa-4]: [vjepa](../sources/vjepa.md) — "Table 1 Pixels vs. Featurized Targets. We ablate the effect of computing the prediction loss in feature space vs pixel space."
[^vjepa-5]: [vjepa](../sources/vjepa.md) — "diction in both frozen evaluation of the video backbone,"
[^ijepa-10]: [ijepa](../sources/ijepa.md) — "larger I-JEPA model matches the performance of view-invariance"
