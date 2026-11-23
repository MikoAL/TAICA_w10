---
title: 預測像素 vs 預測表示
type: concept
sources: [ijepa, vjepa, meta-ijepa-blog]
---
# 預測像素 vs 預測表示

## 問題
（AI 補充）從看得到的部分，預測被遮住的部分。要預測的是**像素**，還是**表示**（embedding）？

## 生成式：預測像素
生成式方法（如 MAE）在輸入空間、也就是像素上算 loss。[^ijepa-1] 缺點是模型要花力氣補完不可預測的細節。[^meta-ijepa-blog-1]

## JEPA：預測表示
JEPA 在嵌入空間算 loss。[^ijepa-1]

（AI 補充）所以它可以只預測重要的部分，不用管無法預測的細節。

## 證據
- **I-JEPA**：只用 1% 標註做線性評估，預測表示 66.9，預測像素只有 40.7；而且像素版本訓練了 800 epoch，比表示版本的 500 epoch 還多（表 7）。[^ijepa-2]
- **V-JEPA**：在特徵空間預測，比在像素空間預測有一致的進步。[^vjepa-1]
- **效率**：I-JEPA 比像素重建方法收斂得快。[^ijepa-3]

## 注意
- V-JEPA 完整微調時，兩者差距很小：像素 85.4、特徵 85.6（表 1）。凍結評估時 K400 差距較大（68.6 vs 73.7），SSv2 幾乎沒差（66.0 vs 66.2）（表 1）。[^vjepa-1][^vjepa-2]
- I-JEPA 的表 7 只是一組消融實驗，兩組的訓練 epoch 也不同（表 7）。[^ijepa-2]

## 相關頁面
- [JEPA](jepa.md)、[生成式 vs 聯合嵌入](generative-vs-joint-embedding.md)、[怎麼看數字](frozen-evaluation.md)

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "a key difference is that the loss function is applied in embedding space, not input space"
[^ijepa-2]: [ijepa](../sources/ijepa.md) — "Table 7. Ablating targets. Linear evaluation on ImageNet-1K"
[^ijepa-3]: [ijepa](../sources/ijepa.md) — "I-JEPA converges faster than pixel reconstruction methods"
[^vjepa-1]: [vjepa](../sources/vjepa.md) — "Predicting in feature space provide a consistent improvement over pixel space prediction."
[^vjepa-2]: [vjepa](../sources/vjepa.md) — "Table 1 Pixels vs. Featurized Targets. We ablate the effect of computing the prediction loss in feature space vs pixel space."
[^meta-ijepa-blog-1]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "the model tries to fill-in every bit of missing information, even though the world is inherently unpredictable"
