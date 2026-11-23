# run-3：本輪新增／更動的表格數字對照（AI 用 grep 對照原文表格列，2026-11-23 16:27:15）

```
295:                                  Pixels    ViT-L/16    68.6          66.0         73.3            85.4
296:                                 Features   ViT-L/16    73.7          66.2         74.8            85.6
                                                           Frozen Evaluation                    Fine-Tuning
                                                       K400           SSv2      IN1K             K400-ft
                                 Target     Arch.      (16×1×1)   (16×1×1)                        (16×5×3)
920:                                           MAE [36]     ViT-H/14448     1600      87.8
921:                                           I-JEPA       ViT-H/16448      300      87.1
is competitive when fine-tuning on the full ImageNet dataset.


                                           Method       Arch.          Epochs    Top-1
                                           MAE [36]     ViT-H/14448     1600      87.8
                                           I-JEPA       ViT-H/16448      300      87.1

```

- 表 1（V-JEPA）：凍結 K400 68.6／73.7、SSv2 66.0／66.2；微調 K400 85.4（像素）／85.6（特徵）→ Wiki 的 frozen-evaluation、pixel-vs-feature、vjepa 三頁一致。
- 表 15（I-JEPA）：MAE 87.8（1600 epoch），I-JEPA 87.1 → 一致。
