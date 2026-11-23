# 語意複查：run-3 改過的 Wiki 內容 → 原文

| 頁 | 行 | 判定 | Wiki 寫的 | 原文（檔案:行） | 建議 |
|---|---|---|---|---|---|
| wiki/sources/ijepa.md | 「ImageNet linear probe…／低樣本和低階任務…贏過它們」條列（引 ijepa-25, ijepa-26） | PARTIAL | 同一條先說 ImageNet linear probe「大模型才和 view-invariance 打平，不是大幅領先」，再說低樣本「贏過它們」，引文用 "trained at resolution 448 surpasses previous methods" | raw/ijepa/paper.txt:290-291（表 1 說明：ViT-H/16 448 "surpasses previous methods including methods that leverage extra hand-crafted data-augmentations"，同頁另一句才說 "matches the performance of view-invariance"）；低樣本見 :343-361、:379；物件計數／深度見 :333-336、:359-361 | 引文只說 surpasses previous methods，沒有指明是低樣本；且與同條前半「只打平」有張力。建議拆成兩條，低樣本那條改引 Table 2 說明句，並註明比的是 ViT-H/16 448 |
| wiki/concepts/world-model.md、wiki/concepts/jepa.md、wiki/sources/meta-lecun-blog.md | 「JEPA 是建立 world model 的『一個關鍵元素』」（引 meta-lecun-blog-11/12/14） | PARTIAL | JEPA 是建立 world model 的一個關鍵元素 | raw/meta-lecun-blog/page.txt:71-73：原文是 "One key element of a solution is JEPA"，這個 solution 指的是「讓 world model 表示多種合理預測」這個關鍵挑戰，不是整個 world model | 比 run-2 的「核心」已保守很多；建議補「（用來處理多種合理預測的難題）」，或維持現狀並接受輕微放寬 |

（其餘已查對照：V-JEPA 表 1 的 68.6/73.7/66.0/66.2/85.4/85.6 對 vjepa/paper.txt:295-296；ℓ1 :183-184；short/long-range :258-266；OmniMAE 74.8 vs 75.1 且「trained directly on ImageNet」:426；ViT-L／Hiera-L :421；樣本較少 :428；SSv2 +21 與 image models 比較 :447-449；I-JEPA 87.1 / 87.8 表 15 :914-923；target 遮輸出 :239；EMA :184, :231；非對稱 encoder :201；損失式 :221；VICReg Inv collapse :1161、主要優點 :396；JEPA-Anything 七領域 :32、最低誤差 :39、:1031、容易預測結構可能主導 :115-117；Meta 部落格 key element/centerpiece/could be argued/hypothesized/impractical/regularized 皆在 page.txt:33-87；meta-ijepa-blog 圖文配對 :78。「論文沒有說自己用 stop-gradient」：ijepa/paper.txt 全文搜尋 stop-grad 無結果，成立。）

小提醒（不計入 PARTIAL）：jepa.md 把 jepa-anything-2 的引文 "complementary factors" 用來支持「正交因子」；原文 :28, :60-61 確實有 orthogonal，所以內容成立，只是該引文本身沒有 orthogonal 一詞。

## 統計
SUPPORTED 48 / PARTIAL 2 / WRONG 0
