# 原始資料清單（raw sources manifest）

原文檔只存在本機 `raw/<id>/`，不放進 repo（避免授權問題）。下載日期皆為 2026-11-23。
文字版由 `pdftotext -layout`（PDF）或去除 HTML 標籤（網頁）產生；檢查程式比對的就是這些文字檔。

| id | 標題 | 類型 | URL | 比對用文字檔 |
|---|---|---|---|---|
| `meta-lecun-blog` | Yann LeCun on a vision to make AI systems learn and reason like animals and humans (2022-02-23) | Meta AI 部落格 | https://ai.meta.com/blog/yann-lecun-advances-in-ai-research/ | `page.txt` |
| `meta-ijepa-blog` | I-JEPA: The first AI model based on Yann LeCun's vision for more human-like AI (2023-06-13) | Meta AI 部落格 | https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/ | `page.txt` |
| `ijepa` | Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture（Assran et al., CVPR 2023） | 論文 | https://arxiv.org/abs/2301.08243 (v3) | `paper.txt` |
| `vjepa` | Revisiting Feature Prediction for Learning Visual Representations from Video（Bardes et al., 2024） | 論文 | https://arxiv.org/abs/2404.08471 (v1) | `paper.txt` |
| `vicreg` | VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning（Bardes, Ponce, LeCun, ICLR 2022） | 論文 | https://arxiv.org/abs/2105.04906 (v3) | `paper.txt` |
| `jepa-anything` | JEPA-Anything: Learning Predictive Models across Different Worlds（Cui et al., 2026, v1 預印本） | 論文 | https://arxiv.org/abs/2609.20800 (v1) | `paper_html.txt`（另有 `paper.txt`） |

未採用：LeCun〈A Path Towards Autonomous Machine Intelligence〉(OpenReview `BZ5a1r-kVsf`)。下載時 OpenReview 要求人機驗證（HTTP 403 `ChallengeRequiredError`），改用 Meta 2022 年介紹同一構想的文章（`meta-lecun-blog`）。
