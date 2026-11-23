---
title: Collapse（表示崩塌）
type: concept
sources: [vicreg, vjepa, ijepa, meta-lecun-blog]
---
# Collapse（表示崩塌）

## 是什麼
如果目標只是「讓兩個表示接近」，模型可以偷懶：不管輸入是什麼，都輸出同一個常數向量。[^vicreg-1]

（AI 補充）這樣兩個表示永遠一模一樣，「讓它們接近」的 loss 永遠是零，模型什麼都沒學到。

V-JEPA 也明說，單純的特徵預測有這個偷懶解。[^vjepa-1][^vjepa-4]

用能量的說法：能量地形變得完全平坦。[^ijepa-1]

## 兩種崩塌（VICReg 的分法）
- **完全崩塌**：所有樣本都變成同一個向量。[^vicreg-1]
- **資訊崩塌**：表示的各個維度一起變動、高度相關，等於很多維度在重複同樣的資訊。[^vicreg-2]

## 怎麼防
| 方法 | 直覺 | 誰用 |
|---|---|---|
| Contrastive（對比） | 把不同樣本的表示推開；Meta 2022 文章說以前只能這樣做 [^meta-lecun-blog-1][^vicreg-6] | SimCLR [^vicreg-7] |
| 不對稱架構（target encoder 用 EMA） | x 和 y 的 encoder 不對稱；[^ijepa-4][^ijepa-5] 答案由 target encoder 給，它的權重是 context encoder 的 EMA [^ijepa-2][^ijepa-3] | I-JEPA（論文沒有說自己用 stop-gradient） |
| EMA + stop-gradient + predictor | 答案由 EMA 的 encoder 給，並且明寫不讓梯度流回答案那一邊 [^vjepa-2][^vjepa-3] | V-JEPA |
| Variance + Covariance 正則化 | 強迫一批樣本彼此不同、各維度不重複 [^vicreg-3] | VICReg |

- VICReg 的消融：拿掉 variance 項，表示立刻崩塌；covariance 項救不了。[^vicreg-4]
- EMA、stop-gradient 這類技巧為什麼能避免崩塌，VICReg 論文說還不完全清楚。[^vicreg-5]

## 相關頁面
- [VICReg 論文](../sources/vicreg.md)、[JEPA](jepa.md)、[生成式 vs 聯合嵌入](generative-vs-joint-embedding.md)

## 引文
[^vicreg-1]: [vicreg](../sources/vicreg.md) — "a collapse in which the two branches ignore the inputs and produce identical and constant output vectors"
[^vicreg-2]: [vicreg](../sources/vicreg.md) — "prevents an informational collapse in which the variables would vary together or be highly correlated."
[^vicreg-3]: [vicreg](../sources/vicreg.md) — "This term forces the embedding vectors of samples within a batch to be different."
[^vicreg-4]: [vicreg](../sources/vicreg.md) — "Without variance regularization the representations immediately collapse to a single vector and the covariance term, which has no repulsive effect preventing collapse, has no impact."
[^vicreg-5]: [vicreg](../sources/vicreg.md) — "The dynamics of learning in these methods, and how they avoid collapse, is not fully understood"
[^vjepa-1]: [vjepa](../sources/vjepa.md) — "would admit a trivial solution, where the encoder"
[^vjepa-2]: [vjepa](../sources/vjepa.md) — "along with a stop-gradient and a predictor has"
[^ijepa-1]: [ijepa](../sources/ijepa.md) — "wherein the energy landscape is flat"
[^meta-lecun-blog-1]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "Until recently, the only approach would have been to use contrastive methods"
[^vicreg-6]: [vicreg](../sources/vicreg.md) — "other samples and their distortions are pushed away"
[^vicreg-7]: [vicreg](../sources/vicreg.md) — "given by the current batch of data as in SimCLR"
[^ijepa-2]: [ijepa](../sources/ijepa.md) — "The use of an exponential moving average target-encoder"
[^ijepa-3]: [ijepa](../sources/ijepa.md) — "are updated at each iteration via an exponential moving average of"
[^vjepa-3]: [vjepa](../sources/vjepa.md) — "does not backpropagate through its argument"
[^vjepa-4]: [vjepa](../sources/vjepa.md) — "puts a constant representation, regardless of its input."
[^ijepa-4]: [ijepa](../sources/ijepa.md) — "JEPAs; we leverage an asymmetric architecture between the"
[^ijepa-5]: [ijepa](../sources/ijepa.md) — "x- and y-encoders to avoid representation collapse."
