# V-JEPA (Bardes et al., 2024) - pre-discussion note

## One-line summary
V-JEPA trains a video model only by predicting the *features* (not pixels) of masked video regions, and the frozen result works well on both motion and appearance tasks while training faster than pixel-reconstruction models.

## Key takeaways
- The whole recipe is one objective: predict features, with no pixel reconstruction, text, negative examples, or pretrained image encoder.
> "introduces V-JEPA, a collection of vision models trained solely using a feature prediction objective"
- The learned representation is "versatile": the same frozen backbone does motion tasks and appearance tasks, with no weight updates.
> "without adaption of the model’s parameters; e.g., using a frozen backbone."
- Predicting in feature space beat predicting pixels in the controlled ablation (same ViT-L/16, same data, same 90K iterations).
> "Predicting in feature space provide a consistent improvement over pixel space prediction."
- Naive feature prediction has a degenerate answer (constant output), so a collapse-prevention trick is needed: a stop-gradient plus a slowly updated (exponential-moving-average) target encoder.
> "would admit a trivial solution, where the encoder"
> "along with a stop-gradient and a predictor has"
- Masking design matters: hide large continuous spatio-temporal blocks so the task is hard enough to force semantic features (multi-block masking won the ablation).
> "Best performance obtained by using multiblock"
- Video pretraining gives motion understanding that image models lack, but image models stay ahead on appearance tasks.
> "V-JEPA shows a significant performance improvement on tasks requiring motion understanding (+21 points on SSv2)"
- More efficient than pixel methods: fewer samples seen and shorter schedules for similar or better results.
> "The V-JEPA results are achieved while processing significantly fewer examples during pretraining."
- Label-efficient: with few labels the gap over pixel-prediction baselines grows.
> "V-JEPA is more label-efficient than other models"

## Numbers
- Pretraining set VideoMix2M, ~2M public videos. > "The models are trained on 2 million videos collected from public datasets and are evaluated on downstream"
- ViT-H/16 (video only): K400 81.9%, SSv2 72.2%, ImageNet-1K 77.9%. > "Our largest model, a ViT-H/16 trained only on videos, obtains 81.9% on Kinetics-400, 72.2% on Something-Something-v2, and 77.9% on ImageNet1K."
- Table 1 (ViT-L/16, frozen K400): pixels 68.6 vs features 73.7; fine-tuned K400 85.4 vs 85.6 (table 1).
- Table 3: attentive pooling vs average pooling, +17 K400, +16.1 SSv2. > "improvement of +17 points on K400 and +16.1 points"
- Table 5 (ViT-L class, frozen): V-JEPA 80.8 K400, 69.5 SSv2, 25.6 AVA, 270M samples seen, 90K iterations, vs OmniMAE 2400M/1170K, VideoMAE 410M/400K, Hiera 770M/1500K (table 5). > "V-JEPA outperforms the baselines on all downstream tasks, except ImageNet, where the model achieves 74.8% compared to 75.1% of an OmniMAE model"
- Speed: roughly 2x pretraining wallclock speedup vs large pixel models. > "V-JEPA achieves this performance with a roughly 2×"
- ImageNet 77.9% needs a two-layer probe (77.4% with one layer). > "77.9% using a two-layer attentive probe."
- Table 7 (K400, 5% labels): V-JEPA 68.2 vs VideoMAE 62.3, MVD 62.6, VideoMAEv2 37.0. > "drops by 12% to 68.2% top-1 when we reduce the number"

## Concepts a beginner needs
- Feature (representation) space vs pixel space: predict an embedding vector, not raw colors; can discard unpredictable detail.
- JEPA: encoder plus predictor; predict y's representation from x's representation, with z saying what transformation links them.
- Masked modeling: hide parts of the clip, predict them from the rest (x = visible, y = masked).
- Representation collapse: encoder outputs a constant to make the loss trivially zero.
- Stop-gradient and EMA target encoder: the paper's collapse-prevention strategy (borrowed from BYOL).
- ViT / tokens: video cut into 16x16-pixel patches spanning 2 frames; each patch is a token.
- Frozen evaluation and attentive probe: freeze the encoder, train only a small head (cross-attention pooling) on labels.
- Appearance vs motion tasks: Kinetics-400 (objects suffice) vs Something-Something-v2 (needs temporal understanding).

## Proposed wiki pages
- `jepa` - architecture (encoder, predictor, z); this paper extends it to video.
- `v-jepa` - model, data, results.
- `pixel-vs-feature-prediction` - Table 1, efficiency, label-efficiency evidence.
- `collapse` - trivial-solution problem, stop-gradient + EMA.
- `masking-strategies` - multi-block vs tube vs causal.
- `frozen-evaluation-and-probing` - frozen vs fine-tune, attentive pooling.
- `label-efficiency` - Table 7.

## Caveats / limitations / things that might conflict with other sources
- Hype risk: "versatile" and "best" are task-dependent; DINOv2 and OpenCLIP beat V-JEPA on Kinetics-400 and ImageNet (Table 6). The paper admits the gap persists: > "and other video models are too constrained and lack the"
- Wallclock comparison is caveated by the authors: > "diction methods are actually obtained with small batch sizes"
- Headline "+6%" is vague about its comparison baseline. > "methods we consider (+6% accuracy) on the"
- Fine-tuned gains over pixel prediction are tiny (85.4 vs 85.6); the advantage is mainly under frozen probing, which is also the protocol the authors designed (attentive probe).
- "drops by 12%" is really about 12 points (80.6 to 68.2), not relative percent; same for other models.

## Questions for the human
1. Should the deck stress this paper's pixel-vs-feature evidence (Table 1, efficiency) or the collapse/EMA mechanics?
2. Include the Table 6 state-of-the-art comparison (including where V-JEPA loses) or keep to the pixel-prediction comparison?
3. Is the diffusion-decoder visualization (Fig 6) worth a slide?
