# 語意複查（run-2，第 2、5、12、16 頁）

| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 2 | 人 20 小時學會開車，AI 呢？ | SUPPORTED | 先前問題已修正：data-wiki 已加入 sources/meta-lecun-blog.md#摘要，支持「LeCun 主張關鍵是 world model」；「LeCun 認為：差別在於人類靠觀察累積了大量背景知識」保留「認為」的保留語氣。其餘（20 小時、上百萬／上十億筆標註資料、補資訊與預測狀態）皆與 world-model.md 一致。 |
| 5 | JEPA 的三個零件 | SUPPORTED | 先前矛盾已修正：下排改為「圖片（輸入不遮）→ Target encoder → 取出 y 區域的表示（遮的是輸出）」，與 sources/ijepa.md「遮住 target encoder 的輸出，不是遮住輸入」一致。公式、L2、EMA、「下一頁 collapse」（第 6 頁確為 collapse）皆有據。 |
| 12 | 最新進展：JEPA-Anything（2026） | MISLEADING | (1) 「尚未經過同儕審查」已移除，改為「來源只有這一篇 v1 預印本」（OPF 頁的普通引言），先前問題已修正。(2) 新問題：只列出 34.8% 與 12.90% 的改善，漏掉 wiki「注意」節（已被 data-wiki 引用）的 Hopper 規劃任務是標準 JEPA 較好，初學者易以為 OPF 全面勝出。(3) 小問題：標題「最新進展」在 wiki 只出現在（AI 補充）「角色：JEPA 的最新進展」，投影片未放入 ai-note 框；建議改為中性標題或加框。 |
| 16 | 自我檢測 | SUPPORTED | 先前問題已修正：data-wiki 已加入 concepts/pixel-vs-feature-prediction.md#生成式預測像素，支持 MAE 在像素（輸入）空間算 loss。其餘答案（collapse、EMA+stop-gradient、凍結評估／低樣本優勢、I-JEPA 微調略輸 MAE）皆有據。 |

## 統計
SUPPORTED 3 / UNSUPPORTED 0 / MISLEADING 1

## 第 12 頁再複查
| 頁 | 標題 | 判定 | 問題 |
|---|---|---|---|
| 12 | JEPA-Anything（2026）：把目標拆開來預測 | SUPPORTED | 先前兩項問題皆已修正：(1) 已新增「也有輸的地方：Hopper 規劃任務是標準 JEPA 比較好」，並同時列出 34.8%（單一介入）與 12.90%（多變數介入），與 wiki「注意」節一致；(2) 標題已不含「最新進展」，改用中性標題，未使用（AI 補充）的「角色」句，也未使用（AI 補充）的「尚未經過同儕審查」與比喻。逐項核對（七個領域、matched baseline、三步驟、問題診斷）皆有 cited 頁面支持。輕微備註（不影響判定）：長條圖畫成四個等大因子，「四個」與等大是示意，wiki 只說「幾個成分」；圖說「一個目標 → 拆成互相正交的因子」本身無數量主張，可接受。 |
