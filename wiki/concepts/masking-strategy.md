---
title: Masking strategy（遮罩策略）
type: concept
sources: [ijepa, vjepa, meta-ijepa-blog]
---
# Masking strategy（遮罩策略）

## 為什麼重要
JEPA 的訓練題目是「從看得到的部分，猜被遮住部分的表示」。遮哪裡、遮多大，決定題目難度，也決定模型學到的是語意還是細節。[^ijepa-1]

## I-JEPA 的 multi-block masking
- 預測**幾塊夠大**的目標區塊（語意層級），並給一塊**資訊夠多、分布夠廣**的 context 區塊。[^ijepa-1]
- 目標區塊數量越多，低樣本準確度越好。[^ijepa-2]
- 遮罩方式比較：只用 1% 標註時，multi-block 54.2，random 17.6（表 6）。[^ijepa-3][^ijepa-9]

## V-JEPA 的做法
- 影片上遮大塊、連續的時空區塊，multi-block 最好。[^vjepa-1]

## 相關頁面
- [I-JEPA 論文](../sources/ijepa.md)、[V-JEPA 論文](../sources/vjepa.md)、[JEPA](jepa.md)

## 引文
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "we find that it is important to predict several relatively large (semantic) target blocks, and to use a sufficiently informative (spatially distributed) context block."
[^ijepa-2]: [ijepa](../sources/ijepa.md) — "Increasing the number of target blocks improve the low-shot accuracy."
[^ijepa-3]: [ijepa](../sources/ijepa.md) — "The proposed multi-block masking strategy is helpful for guiding I-JEPA to learn semantic representations."
[^ijepa-9]: [ijepa](../sources/ijepa.md) — "Table 6. Ablating masking strategy. Linear evaluation on ImageNet-1K using only 1% of the available labels"
[^vjepa-1]: [vjepa](../sources/vjepa.md) — "Best performance obtained by using multiblock"
