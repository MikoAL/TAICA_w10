---
title: V-JEPA 論文（Bardes et al., 2024）
type: source
sources: [vjepa]
---
# V-JEPA 論文（Bardes et al., 2024）

- 原文：Revisiting Feature Prediction for Learning Visual Representations from Video。[^vjepa-1]
- （AI 補充）角色：JEPA 從圖片延伸到**影片**。

## 一句話
V-JEPA 是一系列只用「特徵預測」目標訓練的視覺模型：不重建像素、不用文字、不用負樣本。[^vjepa-2]

## 方法
- 把影片遮掉一部分，從看得到的部分預測被遮住部分的特徵。
  在特徵空間預測，比在像素空間預測有一致的進步。[^vjepa-3] 見 [像素 vs 表示](../concepts/pixel-vs-feature-prediction.md)。
- 單純的特徵預測有一個偷懶解（encoder 輸出常數），也就是 [collapse](../concepts/collapse.md)。[^vjepa-4]
- 防法是 stop-gradient 加上 predictor，以及緩慢更新的 EMA target encoder。[^vjepa-5]
- 遮罩用大塊、連續的時空區塊，multi-block 表現最好。[^vjepa-6] 見 [masking strategy](../concepts/masking-strategy.md)。
- 評估時**凍結**模型參數，只訓練一個小的分類頭。[^vjepa-7] 見 [怎麼看數字](../concepts/frozen-evaluation.md)。

## 結果
- 訓練資料：約 2 million（兩百萬）支公開影片。[^vjepa-8]
- 最大的 ViT-H/16 只看影片：Kinetics-400 81.9%、Something-Something-v2 72.2%、ImageNet 77.9%。[^vjepa-9]
- 需要理解**動作**的任務特別強：SSv2 進步 +21 分。[^vjepa-10]
- 預訓練看的樣本明顯比較少。[^vjepa-11]
- 標註變少時，V-JEPA 掉得比其他模型少（label-efficient）。[^vjepa-12]

## 注意
- 論文寫「drops by 12%」：標註從每類約 287 張減到 29 張時，從 80.6 掉到 68.2（表 7），是 **12 個百分點**，不是相對 12%。[^vjepa-13][^vjepa-16][^vjepa-17]
- 只看外觀就能做的任務（如 ImageNet），影像模型仍然領先；V-JEPA 74.8% 對 OmniMAE 75.1%。[^vjepa-14]
- 完整微調時，預測特徵和預測像素差距很小：85.4 vs 85.6（表 1），優勢主要出現在凍結評估。[^vjepa-15][^vjepa-18]

## 相關頁面
- [JEPA](../concepts/jepa.md)、[I-JEPA 論文](ijepa.md)、[collapse](../concepts/collapse.md)、[怎麼看數字](../concepts/frozen-evaluation.md)

## 引文
[^vjepa-1]: [vjepa](vjepa.md) — "Revisiting Feature Prediction for Learning Visual Representations from Video"
[^vjepa-2]: [vjepa](vjepa.md) — "introduces V-JEPA, a collection of vision models trained solely using a feature prediction objective"
[^vjepa-3]: [vjepa](vjepa.md) — "Predicting in feature space provide a consistent improvement over pixel space prediction."
[^vjepa-4]: [vjepa](vjepa.md) — "would admit a trivial solution, where the encoder"
[^vjepa-5]: [vjepa](vjepa.md) — "along with a stop-gradient and a predictor has"
[^vjepa-6]: [vjepa](vjepa.md) — "Best performance obtained by using multiblock"
[^vjepa-7]: [vjepa](vjepa.md) — "without adaption of the model’s parameters; e.g., using a frozen backbone."
[^vjepa-8]: [vjepa](vjepa.md) — "The models are trained on 2 million videos collected from public datasets and are evaluated on downstream"
[^vjepa-9]: [vjepa](vjepa.md) — "Our largest model, a ViT-H/16 trained only on videos, obtains 81.9% on Kinetics-400, 72.2% on Something-Something-v2, and 77.9% on ImageNet1K."
[^vjepa-10]: [vjepa](vjepa.md) — "V-JEPA shows a significant performance improvement on tasks requiring motion understanding (+21 points on SSv2)"
[^vjepa-11]: [vjepa](vjepa.md) — "The V-JEPA results are achieved while processing significantly fewer examples during pretraining."
[^vjepa-12]: [vjepa](vjepa.md) — "V-JEPA is more label-efficient than other models"
[^vjepa-13]: [vjepa](vjepa.md) — "drops by 12% to 68.2% top-1 when we reduce the number"
[^vjepa-14]: [vjepa](vjepa.md) — "V-JEPA outperforms the baselines on all downstream tasks, except ImageNet, where the model achieves 74.8% compared to 75.1% of an OmniMAE model"
[^vjepa-15]: [vjepa](vjepa.md) — "Predicting in feature space provide a consistent improvement over pixel space prediction."
[^vjepa-16]: [vjepa](vjepa.md) — "287 examples per class to 29 examples per class"
[^vjepa-17]: [vjepa](vjepa.md) — "Table 7 Low-Shot Frozen Evaluation."
[^vjepa-18]: [vjepa](vjepa.md) — "Table 1 Pixels vs. Featurized Targets. We ablate the effect of computing the prediction loss in feature space vs pixel space."
