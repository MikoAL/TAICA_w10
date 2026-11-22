---
title: JEPA-Anything 論文（Cui et al., 2026，v1 預印本）
type: source
sources: [jepa-anything]
---
# JEPA-Anything 論文（Cui et al., 2026，v1 預印本）

- 原文：JEPA-Anything: Learning Predictive Models across Different Worlds，arXiv v1。[^jepa-anything-1]
- （AI 補充）性質：**v1 預印本，尚未經過同儕審查**。本 Wiki 一律寫「論文報告…」。
- （AI 補充）角色：JEPA 的最新進展。

## 問題
預測模型通常是一個領域做一個。論文問：有沒有一個共同的學習原則，能在截然不同的系統上做 [world modeling](../concepts/world-model.md)？[^jepa-anything-2]

論文對標準 [JEPA](../concepts/jepa.md) 的診斷：只有一個目標嵌入、一個 predictor 時，容易預測或變異大的結構會主導訓練，比較弱的結構會收到互相衝突的梯度。[^jepa-anything-3]

## 核心想法：正交預測分解（OPF）
用學到的基底矩陣把目標狀態拆成多個成分，每個成分由專屬的分支來預測。[^jepa-anything-4] 這些成分互相**正交**，所以不重疊、能穩定地組回完整的狀態。[^jepa-anything-5] 詳見 [orthogonal predictive factorization](../concepts/orthogonal-predictive-factorization.md)。

## 論文報告的結果
- 測試了七個領域：影像、生物、臨床、控制、分子動力學、物理場、天氣。[^jepa-anything-6]
- 和條件相同的標準 JEPA 比，在 10 個動態預測任務上指標全部改善。[^jepa-anything-6]
- Interventional Pong 單一介入的預測誤差降低 34.8%。[^jepa-anything-6]
- 分子模擬：四個系統的一步誤差和 100 步誤差都最低。[^jepa-anything-7]
- 由因子提名的生物介入（藥物組合），後續濕實驗有支持的結果。[^jepa-anything-8]

## 注意
- **標準 JEPA 也有贏的地方**：機器人 Hopper 的規劃任務是標準 JEPA 比較好，論文自己說規劃表現「看環境而定」。[^jepa-anything-9]
- 同時介入多個變數時改善較小：單一介入 34.83%、組合介入 12.90%。[^jepa-anything-10]
- 生物證據樣本小：三個類器官、三個腫瘤組織樣本。[^jepa-anything-11]
- 作者自己提醒：正交因子本身不代表因果機制，共用架構也不保證不同領域的表示對齊。[^jepa-anything-12]

## 相關頁面
- [orthogonal predictive factorization](../concepts/orthogonal-predictive-factorization.md)、[JEPA](../concepts/jepa.md)、[world model](../concepts/world-model.md)

## 引文
[^jepa-anything-1]: [jepa-anything](jepa-anything.md) — "arXiv:2609.20800v1 [cs.CL] 17 Sep 2026"
[^jepa-anything-2]: [jepa-anything](jepa-anything.md) — "Yet predictive models remain domain-specific: can a common learning principle support world modeling across radically different systems?"
[^jepa-anything-3]: [jepa-anything](jepa-anything.md) — "easily predicted or high-variance structure may dominate optimization, several latent directions may serve similar roles, and weaker predictive structure may receive conflicting gradients."
[^jepa-anything-4]: [jepa-anything](jepa-anything.md) — "A collection of learned basis matrices analyzes each target state into multiple components, and a dedicated branch predicts each component from the shared context representation."
[^jepa-anything-5]: [jepa-anything](jepa-anything.md) — "Orthogonality therefore turns multiple prediction outputs into a complete, non-overlapping, and numerically stable world-state interface."
[^jepa-anything-6]: [jepa-anything](jepa-anything.md) — "Against matched JEPA baselines, JEPA -Anything improves reported metrics on all 10 dynamics tasks and reduces single-intervention prediction error on Interventional Pong by 34.8%"
[^jepa-anything-7]: [jepa-anything](jepa-anything.md) — "JEPA -Anything produces the lowest one-step MAE and 100-step RMSD on all four molecular systems."
[^jepa-anything-8]: [jepa-anything](jepa-anything.md) — "Wet-lab studies subsequently supported this prediction, showing enhanced antitumor activity in Huh7–PBMC co-culture, patient-derived organoids and tumor fragments, and immunocompetent mice."
[^jepa-anything-9]: [jepa-anything](jepa-anything.md) — "Hopper favors standard JEPA. Planning performance is therefore environment-dependent."
[^jepa-anything-10]: [jepa-anything](jepa-anything.md) — "The corresponding reductions are 34.83%, 12.90%, and 8.58%, respectively."
[^jepa-anything-11]: [jepa-anything](jepa-anything.md) — "Across three organoid specimens and three tumor-fragment specimens"
[^jepa-anything-12]: [jepa-anything](jepa-anything.md) — "Orthogonal factors do not by themselves establish causal mechanisms, and a shared predictive architecture does not guarantee aligned representations across domains."
