# run-1：表格數字人工核對（TABLE_NUMBER_UNVERIFIED）

檢查程式只能確認「這個數字有出現在原文某處」，不能確認它在表格的哪一列、哪一欄。以下逐一對照 `raw/` 文字檔的表格列。

| Wiki 位置 | 數字 | 原文位置 | 結果 |
|---|---|---|---|
| ijepa.md / pixel-vs-feature | 66.9、40.7（表 7） | ijepa/paper.txt:492-493：`Target-Encoder Output ViT-L/16 500 66.9`、`Pixels ViT-L/16 800 40.7` | 數字正確。**但 Wiki 寫「同樣的設定，只改目標」是錯的：兩組 epoch 是 500 vs 800。** 已修正 |
| ijepa.md / masking-strategy | 54.2、15.5、20.2、17.6（表 6） | ijepa/paper.txt:476-479（multi-block / rasterized / block / random） | 正確 |
| ijepa.md | 87.8（表 15） | ijepa/paper.txt:920 `MAE ViT-H/14448 1600 87.8` | 正確 |
| vjepa.md | 80.6、68.2（表 7） | vjepa/paper.txt:596 ViT-H/16_384 列，50% 欄 80.6、5% 欄 68.2；文中 287 → 29 examples per class | 正確（差 12.4 個百分點，相對約 15%） |
| vjepa.md / pixel-vs-feature | 85.4、85.6（表 1） | vjepa/paper.txt:295-296 Pixels / Features 列，最後一欄（fine-tune K400） | 正確 |
