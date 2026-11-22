# I-JEPA (Assran et al., CVPR 2023, arXiv 2301.08243)

## One-line summary
I-JEPA learns image representations by predicting the *representations* (not pixels) of hidden image blocks from one visible context block, with no hand-crafted augmentations.

## Key takeaways
- **Three SSL families, one framework.** Joint-Embedding (make two views similar), Generative (reconstruct), JEPA (predict the embedding of y from x); all framed as Energy-Based Models.
> "Joint-Embedding Predictive Architectures learn to predict the embeddings of a signal y from a compatible signal x"
- **Key difference from generative methods like MAE: where the loss lives.**
> "a key difference is that the loss function is applied in embedding space, not input space"
- **Predicting abstract targets beats pixels (the paper's ablation).**
> "predicting in pixel-space leads to a significant degradation in the linear probing performance"
- **Masking strategy is the core design choice:** 4 large target blocks (scale 0.15-0.2), one big context block (0.85-1.0) with overlap removed.
> "we find that it is important to predict several relatively large (semantic) target blocks, and to use a sufficiently informative (spatially distributed) context block."
- **Targets come from masking the target encoder's output, not its input.**
> "the target blocks are obtained by masking the output of the target-encoder, not the input"
- **Collapse is still a risk; avoided with an asymmetric design:** target encoder is an EMA of the context encoder.
> "The use of an exponential moving average target-encoder"
- **No augmentations, yet competitive and cheaper.**
> "I-JEPA requires less compute than previous methods"
- **Keeps local information:** visualizations show object parts and pose kept, low-level detail dropped.
> "The I-JEPA predictor is correctly capturing positional uncertainty and producing high-level object parts with a correct pose"

## Numbers
- ImageNet-1K linear probe (Table 1, 300 ep unless noted): I-JEPA ViT-H/16-448 81.1, ViT-H/14 79.3; MAE ViT-H/14 (1600 ep) 77.2; iBOT ViT-L/16 81.0; DINO ViT-B/8 80.1. (table 1, not quotable)
> "larger I-JEPA model matches the performance of view-invariance"
- ImageNet 1% labels (Table 2): I-JEPA ViT-H/16-448 77.3, ViT-H/14 73.3; MAE ViT-H/14 71.5. (table 2, not quotable)
- Compute: ViT-H/14 in under 72 h on 16 A100s; about 7% slower per iteration than MAE but ~5x fewer iterations.
> "train a ViT-Huge/14 on ImageNet using 16 A100 GPUs in"
> "under 72 hours to achieve strong downstream performance"
> "I-JEPA converges in roughly 5×"
- Clevr/Dist (Table 4): I-JEPA 72.4 vs DINO 53.4, iBOT 62.8. (table 4, not quotable)
- IN1k to IN22k pretraining improves CIFAR100 87.5 to 89.5 (Table 5).
> "I-JEPA benefits from larger more diverse datasets."
- Targets (Table 7): encoder output 66.9 vs pixels 40.7. (table 7, not quotable)
- Masking (Table 6, ViT-B/16, 1% labels): multi-block 54.2; rasterized 15.5; block 20.2; random 17.6. (table 6, not quotable)
> "The proposed multi-block masking strategy is helpful for guiding I-JEPA to learn semantic representations."
- Target blocks (Table 10): 1 block 9.0, 4 blocks 54.2.
> "Increasing the number of target blocks improve the low-shot accuracy."
- Full fine-tune (Table 15): I-JEPA 87.1 vs MAE 87.8.
> "I-JEPA achieves 87.1 top-1 accuracy."

## Concepts a beginner needs
- **Self-supervised learning:** learn relationships within the input, no labels.
- **Energy-Based Model view:** low energy for compatible pairs, high for incompatible.
- **Invariance-based (Joint-Embedding):** similar embeddings for augmented views.
> "produce similar embeddings for two or more views"
- **Representation collapse:** encoder outputs a constant.
> "wherein the energy landscape is flat"
- **Context block, target blocks, predictor:** visible region; hidden regions; narrow ViT predicting targets from positional mask tokens.
- **EMA target encoder:** slow-moving copy of the context encoder producing targets.
- **Linear probing / 1% low-shot:** frozen encoder plus linear classifier / adaptation with few labels.
- **Loss:** average L2 distance between predicted and target patch representations.
> "The loss is simply the average L2 distance between the predicted patch-level representations"

## Proposed wiki pages
- `jepa` - architecture family and the "predict in embedding space" idea.
- `i-jepa` - this paper's method and results.
- `self-supervised-learning` - background and three families.
- `joint-embedding-vs-generative` - comparison.
- `collapse` - problem and EMA/asymmetry fix.
- `masking-strategy` - multi-block ablations.
- `representation-space-prediction` - pixel vs embedding argument.

## Caveats / limitations / things that might conflict with other sources
- Hype-like framing ("simple", "highly scalable"); efficiency compares GPU hours across different setups.
> "we find I-JEPA to be highly scalable"
- Not a clean win: iBOT (81.0) roughly ties I-JEPA 81.1, which needed 448 resolution; DINO/iBOT still beat it on iNat18; MAE beats it on Clevr/Count (90.5 vs 86.7).
- Larger patches hurt local tasks.
> "the ViT-G/16 uses larger input patches"
- MAE still slightly better after full fine-tuning (87.8 vs 87.1).
- "Representation space is better" is a conjecture backed by one ablation (Table 7) with different epochs (500 vs 800).
- Weight-decay trade-off.
> "However, this also leads to a degradation of performance in linear evaluation."
- Only images evaluated; ablations use ViT-B/16 and 1% labels. Other sources' "JEPA" (video, world models) is broader than this instance.

## Questions for the human
1. Should I-JEPA be the main worked example of JEPA in the deck, or a short case study?
2. How deep into the energy-based-model framing for beginners, or just the three-way comparison?
