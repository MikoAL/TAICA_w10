---
title: Orthogonal predictive factorization（正交預測分解，OPF）
type: concept
sources: [jepa-anything]
---
# Orthogonal predictive factorization（正交預測分解，OPF）

> 來源只有 [JEPA-Anything](../sources/jepa-anything.md)，v1 預印本。以下結果都是「論文報告」。[^jepa-anything-1]

## 它想解決什麼
標準 [JEPA](jepa.md) 只有一個目標嵌入、一個 predictor。論文認為這樣容易預測的結構會主導訓練，比較弱的結構被忽略或收到互相衝突的梯度。[^jepa-anything-2]

## 核心想法（概念版）
1. **拆**：用學到的基底矩陣，把目標狀態拆成幾個成分（因子）。[^jepa-anything-3]
2. **分頭預測**：每個因子有自己專屬的預測分支。[^jepa-anything-3]
3. **正交**：因子之間互相垂直、不重疊，所以能穩定地組回完整狀態。[^jepa-anything-4]

（AI 補充）比喻：與其讓一個人同時猜「球的位置、顏色、速度」，不如分給三個人各猜一項，而且規定三人不能猜重複的東西。

## 論文報告的效果
- Interventional Pong 單一介入誤差降低 34.8%。[^jepa-anything-5]
- 但 Hopper 的規劃任務是標準 JEPA 比較好。[^jepa-anything-6]

## 相關頁面
- [JEPA-Anything 論文](../sources/jepa-anything.md)、[JEPA](jepa.md)

## 引文
[^jepa-anything-1]: [jepa-anything](../sources/jepa-anything.md) — "arXiv:2609.20800v1 [cs.CL] 17 Sep 2026"
[^jepa-anything-2]: [jepa-anything](../sources/jepa-anything.md) — "easily predicted or high-variance structure may dominate optimization, several latent directions may serve similar roles, and weaker predictive structure may receive conflicting gradients."
[^jepa-anything-3]: [jepa-anything](../sources/jepa-anything.md) — "A collection of learned basis matrices analyzes each target state into multiple components, and a dedicated branch predicts each component from the shared context representation."
[^jepa-anything-4]: [jepa-anything](../sources/jepa-anything.md) — "Orthogonality therefore turns multiple prediction outputs into a complete, non-overlapping, and numerically stable world-state interface."
[^jepa-anything-5]: [jepa-anything](../sources/jepa-anything.md) — "reduces single-intervention prediction error on Interventional Pong by 34.8%"
[^jepa-anything-6]: [jepa-anything](../sources/jepa-anything.md) — "Hopper favors standard JEPA. Planning performance is therefore environment-dependent."
