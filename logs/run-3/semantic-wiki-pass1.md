# 語意檢查：Wiki → 原文（run-3）

範圍：`wiki/concepts/*.md`（9 頁）、`wiki/sources/*.md`（6 頁），對照 `raw/`。每個有引用的段落、條列項、表格列算一個檢查項；（AI 補充）段落不計。數字與（表 N）已逐一對回原文表格列。

總計：檢查 148 項，SUPPORTED 128，PARTIAL 20，WRONG 0。

所有數字（87.1／87.8、40.7／66.9、54.2／15.5／20.2／17.6、73.7／68.6、66.2／66.0、85.6／85.4、80.6→68.2、74.8／75.1、34.83／12.90、632M、72 小時等）都和原文表格列一致，沒有發現數字或方向錯誤。PARTIAL 主要是：附的引文只支持該句的一部分、最高級／比較級被放大、原文的 hedge（may）被拿掉、或條件範圍沒寫。

## 有問題的項目

| 頁 | 行 | 判定 | Wiki 寫的 | 原文（附檔案:行） | 建議 |
|---|---|---|---|---|---|
| sources/ijepa.md | 12 | PARTIAL | 從一塊 context 預測幾塊 target 的表示，「不需要人工設計的資料增強」；附 [^ijepa-2] | 引文只涵蓋「不靠 hand-crafted augmentation」；「一塊 context 預測多塊 target」在 ijepa/paper.txt:~120、paper.txt:243（"Given a context block, predict the representations of various target blocks"）| 加一條引文：「given a context block, predict the representations of various target blocks」 |
| sources/ijepa.md | 16 | PARTIAL | 和生成式方法（如 MAE）「最大的差別」：loss 算在嵌入空間 | ijepa/paper.txt:187、194 兩處都寫 "a key difference"（一個關鍵差別），不是 the biggest／最大 | 改「一個關鍵差別」 |
| sources/ijepa.md | 19 | PARTIAL | 「為了避免 collapse」，target encoder 是 context encoder 的 EMA；附 [^ijepa-7] | 原文說避免 collapse 靠 "an asymmetric architecture between the x- and y-encoders"（paper.txt:201）；EMA 是 "has proven essential for training JEAs"（paper.txt:232），沒有直接說 EMA 的目的是防 collapse。引文只是片段「The use of an exponential moving average target-encoder」 | 改成「不對稱架構避免 collapse；EMA target encoder 對訓練是必要的」，引文換成 paper.txt:201 或 232 完整句 |
| sources/ijepa.md | 31 | PARTIAL | 「大模型才和 view-invariance 方法打平，不是大幅領先」 | 只適用 ImageNet linear（Table 1，paper.txt:266-282：ViT-H/14 79.3 < DINO 80.1，ViT-H/16-448 81.1 ≈ iBOT 81.0）。但同篇 Table 2（1%，paper.txt:270-284）ViT-H/14 73.3 已高於 iBOT 69.7、DINO 70.0；Table 4（低階任務）原文寫 "by a large margin"（paper.txt:~358） | 加上範圍「ImageNet linear probe」，並註明低樣本與低階任務上 I-JEPA 勝過 view-invariance 方法，避免讀者以為處處只打平 |
| sources/ijepa.md | 32 | PARTIAL | 「只在圖片上驗證；消融實驗多用 ViT-B/16 和 1% 標註」；附 [^ijepa-17]（Table 6 說明句） | 引文只支持「1% 標註」與 Table 6；「只在圖片上驗證」沒有被任何引文支持（原文 paper.txt:298 只說「可應用到不同模態」）；Table 7 用 ViT-L/16（paper.txt:495）所以「多用 ViT-B/16」要用 Table 6/8/9/10 的 "ViT-B/16 for 300 epochs" 引 | 改為（AI 補充）或補一條說明驗證範圍的引文；ViT-B/16 另引 Table 8 說明句 |
| sources/jepa-anything.md | 15 | PARTIAL | 「只有一個目標嵌入、一個 predictor 時，容易預測或變異大的結構會主導訓練」 | jepa-anything/paper.txt:115 是 "may dominate optimization"、"may receive conflicting gradients"，是可能性，不是肯定 | 補回「可能」，並寫「論文認為」 |
| sources/jepa-anything.md | 21 | PARTIAL | 「測試了七個領域：影像、生物、臨床、控制、分子動力學、物理場、天氣」；附 [^jepa-anything-6] | [^6] 的引文是「improves reported metrics on all 10 dynamics tasks … 34.8%」，沒有「seven domains」；七個領域在 paper.txt:32（摘要）。同頁 [^6] 同時掛在下面兩條，其中第一條掛錯 | 這條改引 "We evaluate JEPA -Anything across seven domains"（jepa.md 已有此引文）|
| sources/jepa-anything.md | 24 | PARTIAL | 分子模擬：四個系統的一步誤差和 100 步誤差「都最低」 | 摘要 paper.txt:39 是 "lowest … errors among compared methods"，是「在被比較的方法中」最低；wiki 沒寫比較範圍 | 補「在論文比較的方法中」 |
| sources/meta-ijepa-blog.md | 22 | PARTIAL | 未來方向：把 JEPA 推到影片、「聲音」等更豐富的資料 | meta-ijepa-blog/page.txt:76：richer modalities，例子是影片；audio／text 是「預測的條件提示」（"conditioning these predictions on audio or textual prompts"），不是要擴展到的資料；page.txt:78 另提 image-text 配對與影片 | 改為「影片、圖文配對等更豐富的資料；可用聲音或文字當條件」 |
| sources/meta-lecun-blog.md | 16 | PARTIAL | 「訓練 JEPA 要防止 collapse。文章說過去只能用 contrastive 方法…」 | meta-lecun-blog/page.txt:75 全文沒有出現 collapse；文章講的是 contrastive「在高維表示時不切實際」（impractical），regularized 方法是替代。防 collapse 是 VICReg／I-JEPA 論文的語言，不是這篇的 | 改成「文章只說 contrastive 在高維表示不實際」，或把 collapse 一句標為（AI 補充），並補引 "this is rather impractical when the representations are high-dimensional" |
| sources/vicreg.md | 15 | PARTIAL | Invariance 項「單獨用就會 collapse」；附 [^vicreg-3] | vicreg/paper.txt:1135：拿掉 variance 項、保留 invariance+covariance 會 collapse；沒有針對「invariance 單獨」的實驗，另有 paper.txt:1136 說 invariance 項 "absolutely necessary" | 改成「沒有 variance 項（只靠 invariance + covariance）就會立刻 collapse」 |
| sources/vicreg.md | 25 | PARTIAL | VICReg 的主要賣點是「可解釋、模組化」；附 [^vicreg-7] | vicreg/paper.txt:396 寫 "main advantage … is the modularity of its objective function and the applicability to multi-modal setups"；沒有「可解釋」；[^vicreg-7] 只支持「on par」 | 改成「模組化、可用在多模態」，並加引文 paper.txt:396 |
| sources/vjepa.md | 20 | PARTIAL | 遮罩用「大塊、連續」的時空區塊，multi-block 表現最好；附 [^vjepa-6] | [^6] 只支持「multiblock 最好」（vjepa/paper.txt:364，是和 random-tube、causal multi-block 比）。「大塊」不符合附錄：paper.txt:1183-1184 用 8 個 scale 0.15 的小塊加 2 個 scale 0.7 的塊，且附錄說「sampling several blocks … better than a single large block」（paper.txt:1437）；遮蔽比例約 90%（paper.txt:266） | 刪「大塊、連續」，改成「用多個時空區塊（short-range 與 long-range 兩種），遮掉約 90%」，並補引文；masking-strategy.md:17 同步改 |
| concepts/generative-vs-joint-embedding.md | 13 | PARTIAL | 表格「Generative … 代表 MAE」；附 [^ijepa-5]（"a key difference is that the loss function is applied in embedding space"） | 引文沒有提到 MAE。MAE 是生成式的例子見 ijepa/paper.txt:194、paper.txt:140 | 換成 "reminiscent of the generative masked autoencoders (MAE)" 之類的引文 |
| concepts/jepa.md | 20（公式） | PARTIAL | loss = (1/M) Σ‖ŝ − s‖²，白話「每塊預測的表示和真正的表示差多少」 | ijepa/paper.txt:~246：每一塊 i 的距離是對該塊內所有 patch j∈B_i 的 ‖ŝ_{y_j} − s_{y_j}‖² 加總，wiki 公式少了內層的 patch 加總（寫成每塊一個向量） | 公式補內層 Σ_{j∈B_i}，或在白話旁註明「每塊內逐 patch 加總」（標 AI 補充）|
| concepts/jepa.md | 31（表格 2026 列） | PARTIAL | 「論文報告：把目標拆成正交因子，用在七個領域」；附 [^jepa-anything-1] | 引文只有 "We evaluate JEPA -Anything across seven domains"，不含「拆成正交因子」（見 jepa-anything/paper.txt:128） | 補引 [^jepa-anything-3] 之類「learned basis matrices」那句 |
| concepts/masking-strategy.md | 9 | PARTIAL | 「遮哪裡、遮多大，決定題目難度，也決定模型學到的是語意還是細節」 | 引文只說預測夠大的語意目標區塊與夠資訊量的 context 很重要（ijepa/paper.txt:~120）；「題目難度」「語意還是細節」是 wiki 自己的推論，且沒標（AI 補充） | 加（AI 補充）開頭，或改成原文說法（multi-block 比 rasterized／block／random 好，見 Table 6） |
| concepts/masking-strategy.md | 17 | PARTIAL | 影片上遮「大塊、連續」的時空區塊，multi-block 最好 | 同 sources/vjepa.md:20：引文只支持「multiblock 最好」，「大塊」被附錄反駁（vjepa/paper.txt:1183-1184、1437） | 同上 |
| concepts/orthogonal-predictive-factorization.md | 11 | PARTIAL | 論文認為這樣「容易預測的結構會主導訓練，比較弱的結構被忽略或收到互相衝突的梯度」 | jepa-anything/paper.txt:115：容易預測「或高變異」的結構 "may dominate"；弱結構 "may receive conflicting gradients"。原文沒有「被忽略」，hedge「may」也被拿掉 | 刪「被忽略」、補「可能」 |
| concepts/self-supervised-learning.md | 19 | PARTIAL | 「LeCun 認為人類和動物主要靠觀察、以不分任務的非監督方式學到大量背景知識。自監督學習就是讓機器也這樣學。」 | meta-lecun-blog/page.txt:41：動物 "seem able to learn … through observation and through an incomprehensibly small amount of interactions"（有 "seem"，且是「觀察加極少量互動」）；引文 [^meta-lecun-blog-1] 不含 observation。第二句「自監督學習就是讓機器也這樣學」是 AI 的解釋，沒標（AI 補充）；原文 page.txt:49 說的是「用 self-supervised 方式學 world model」 | 補 "seem able" 與 observation 引文；第二句標（AI 補充） |


## 沒有發現的 WRONG 與抽查過、判定 SUPPORTED 的高風險項目
- 表 6（54.2 / 15.5 / 20.2 / 17.6）：對 ijepa/paper.txt:477-481 逐列相符。
- 表 7（66.9 @500 epoch、40.7 @800 epoch，ViT-L/16）：paper.txt:490-492 相符，wiki 寫「像素訓練的 epoch 較多」方向正確。
- 表 15（87.1 vs 87.8）：paper.txt:920-921 相符；註：MAE 是 ViT-H/14-448、I-JEPA 是 ViT-H/16-448，wiki 未寫架構差異，不算錯。
- V-JEPA 表 1（K400 73.7 vs 68.6；SSv2 66.2 vs 66.0；K400-ft 85.6 vs 85.4）：vjepa/paper.txt:288-292 相符；兩頁都有標「（表 1）」。
- V-JEPA 表 7（80.6 → 68.2，287 → 29 examples per class）：paper.txt:589-597 相符，80.6−68.2 = 12.4 個百分點，wiki「12 個百分點、不是相對 12%」正確（相對下降約 15%）。
- V-JEPA 74.8 vs OmniMAE 75.1（表 5，凍結評估，ViT-L/16）：paper.txt:426、435 相符。
- JEPA-Anything 34.83% / 12.90%（單一／組合介入）：paper.txt:748 順序相符；Hopper 屬於另一個 planning 實驗，和「10 個動態任務全部改善」不矛盾（paper.txt:927-937 與 1425-1437）。
- 全部 `jepa-anything` 結果皆以「論文報告」「v1 預印本」呈現，符合規則 6。

## 每頁統計

| 頁 | 檢查項數 | SUPPORTED | PARTIAL | WRONG |
|---|---|---|---|---|
| sources/ijepa.md | 16 | 11 | 5 | 0 |
| sources/jepa-anything.md | 13 | 10 | 3 | 0 |
| sources/meta-ijepa-blog.md | 12 | 11 | 1 | 0 |
| sources/meta-lecun-blog.md | 8 | 7 | 1 | 0 |
| sources/vicreg.md | 9 | 7 | 2 | 0 |
| sources/vjepa.md | 17 | 16 | 1 | 0 |
| concepts/collapse.md | 11 | 11 | 0 | 0 |
| concepts/frozen-evaluation.md | 9 | 9 | 0 | 0 |
| concepts/generative-vs-joint-embedding.md | 7 | 6 | 1 | 0 |
| concepts/jepa.md | 12 | 10 | 2 | 0 |
| concepts/masking-strategy.md | 5 | 3 | 2 | 0 |
| concepts/orthogonal-predictive-factorization.md | 7 | 6 | 1 | 0 |
| concepts/pixel-vs-feature-prediction.md | 7 | 7 | 0 | 0 |
| concepts/self-supervised-learning.md | 3 | 2 | 1 | 0 |
| concepts/world-model.md | 12 | 12 | 0 | 0 |
| **合計** | **148** | **128** | **20** | **0** |
