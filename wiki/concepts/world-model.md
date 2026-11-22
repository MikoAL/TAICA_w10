---
title: World model（世界模型）
type: concept
sources: [meta-lecun-blog, meta-ijepa-blog, jepa-anything]
---
# World model（世界模型）

## 是什麼
World model 是機器內部對「世界怎麼運作」的模型。[^meta-lecun-blog-1] 有了它，機器可以補上感官沒提供的資訊，也可以預測接下來合理的狀態。[^meta-lecun-blog-2]

JEPA-Anything 給的寬鬆定義：從「情境」（context）建立內部狀態，再預測同一系統的另一個狀態。[^jepa-anything-1]

## 為什麼需要
LeCun 的出發點：青少年大約 20 小時就學會開車。[^meta-lecun-blog-3] 自駕系統卻需要上百萬、上十億筆標註資料，還要在虛擬環境試上百萬次。[^meta-lecun-blog-4] 他認為差別在於人類靠觀察累積了大量「世界怎麼運作」的背景知識，也就是常識。[^meta-lecun-blog-5]

## LeCun 的六模組架構（一頁帶過）
| 模組 | 做什麼 |
|---|---|
| Configurator | 總指揮，依任務設定其他模組 [^meta-lecun-blog-6] |
| Perception | 從感測器估計目前世界的狀態 [^meta-lecun-blog-7] |
| World model | 補缺的資訊、預測未來狀態；最複雜的一塊 [^meta-lecun-blog-2] |
| Cost | 算出一個「不舒服程度」的數值 [^meta-lecun-blog-8] |
| Actor | 提出行動序列，找讓未來成本最低的那個 [^meta-lecun-blog-9] |
| Short-term memory | 記住目前與預測的狀態和成本 [^meta-lecun-blog-10] |

## 和 JEPA 的關係
- LeCun 架構中，world model 的核心就是 [JEPA](jepa.md)。[^meta-lecun-blog-11]
- Meta 把 I-JEPA 的 predictor 稱為一個原始、受限的 world model。[^meta-ijepa-blog-1]

## 注意
- 這是一個**研究方向**，Meta 自己說訓練 world model 是未來幾十年的主要挑戰。[^meta-lecun-blog-12]

## 相關頁面
- [JEPA](jepa.md)、[self-supervised learning](self-supervised-learning.md)、[Meta LeCun 構想文](../sources/meta-lecun-blog.md)

## 引文
[^meta-lecun-blog-1]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "internal models of how the world works"
[^meta-lecun-blog-2]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "The world model module constitutes the most complex piece of the architecture. Its role is twofold: (1) to estimate missing information about the state of the world not provided by perception, and (2) to predict plausible future states of the world."
[^meta-lecun-blog-3]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "a teenager who has never sat behind a steering wheel can learn to drive in about 20 hours"
[^meta-lecun-blog-4]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "millions or billions of pieces of labeled training data and millions of reinforcement learning trials in virtual environments"
[^meta-lecun-blog-5]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "It can be hypothesized that this accumulated knowledge may constitute the basis for what is often called common sense."
[^meta-lecun-blog-6]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "The configurator module performs executive control"
[^meta-lecun-blog-7]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "The perception module receives signals from sensors and estimates the current state of the world."
[^meta-lecun-blog-8]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "The cost module computes a single scalar output that predicts the level of discomfort of the agent."
[^meta-lecun-blog-9]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "The actor can find an optimal action sequence that minimizes the estimated future cost"
[^meta-lecun-blog-10]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "The short-term memory module keeps track of the current and predicted world state, as well as associated costs."
[^meta-lecun-blog-11]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "trainable encoders that extract abstract representations of them"
[^meta-lecun-blog-12]: [meta-lecun-blog](../sources/meta-lecun-blog.md) — "training world models constitutes the main challenge toward real progress in AI over the next decades"
[^meta-ijepa-blog-1]: [meta-ijepa-blog](../sources/meta-ijepa-blog.md) — "The predictor in I-JEPA can be seen as a primitive (and restricted) world-model"
[^jepa-anything-1]: [jepa-anything](../sources/jepa-anything.md) — "World modeling enables intelligence to anticipate consequences, guide interventions, and learn from interaction."
