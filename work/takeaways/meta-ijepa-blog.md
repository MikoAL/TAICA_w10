# Meta AI blog: I-JEPA (Jun 13, 2023)

## One-line summary
I-JEPA is the first model built on a piece of LeCun's vision: it predicts abstract representations of masked image regions rather than pixels, and Meta claims strong, efficient results.

## Key takeaways
- I-JEPA compares representations, not pixels.
> "learns by creating an internal model of the outside world, which compares abstract representations of images (rather than comparing the pixels themselves)"
- Self-supervised means learning from unlabeled data.
> "directly from unlabeled data such as images or sounds, rather than from manually assembled labeled datasets"
- Generative methods are criticized for predicting every detail.
> "the model tries to fill-in every bit of missing information, even though the world is inherently unpredictable"
- Example offered: hands.
> "it is notoriously difficult for generative models to generate human hands accurately"
- Design: one context block predicts several target blocks; multi-block masking guides semantic features.
> "the proposed multi-block masking strategy"
- Architecture: ViT context encoder sees only visible patches; the target encoder is an exponential moving average of it.
> "The context encoder is a Vision Transformer (ViT) that only processes the visible context patches."
- The predictor is framed as a primitive world model.
> "The predictor in I-JEPA can be seen as a primitive (and restricted) world-model"
- Future directions: video, audio and text.
> "It would be particularly interesting to advance JEPAs to learn more general world-models from richer modalities"

## Numbers
- Training cost and model size:
> "we train a 632M parameter visual transformer model using 16 A100 GPUs in under 72 hours"
- Low-shot ImageNet:
> "with only 12 labeled examples per class"
- Compute comparison:
> "Other methods typically take two to 10 times more GPU-hours and achieve worse error rates when trained with the same amount of data."
- Figure caption (1% labels):
> "approximately 12 labeled images per class"
- Venue:
> "Our paper on I-JEPA will be presented at CVPR 2023 next week"

## Concepts a beginner needs
- Representation / embedding: abstract encoding of an input.
- Self-supervised learning: no manual labels.
- Joint-embedding (invariance-based) architectures: similar embeddings for compatible inputs.
- Generative architectures: reconstruct missing pixels/words with a decoder.
- JEPA: predict the embedding of y from x with a predictor.
- Context block / target blocks / masking.
- Vision Transformer (ViT), exponential moving average target encoder.
- Linear probing, low-shot classification (evaluation terms; not explained).

## Proposed wiki pages
- `i-jepa` - the model.
- `jepa` - three-way comparison (joint-embedding vs generative vs JEPA).
- `self-supervised-learning` - definition.
- `generative-vs-joint-embedding` - motivation.
- `multi-block-masking` - design choice.
- `world-model` - link as "primitive world model".
- `representation-learning-evaluation` - linear probe, low-shot.

## Caveats / things that might conflict with other sources
- Marketing tone: "first AI model", "state-of-the-art", "strong performance" with no table of numbers in the text; check the paper.
- "Two to 10 times more GPU-hours" and "worse error rates" are not sourced to specific baselines.
- Much is phrased as hope ("the hope is for the JEPA to avoid the biases") rather than shown.
- Hands example is anecdotal.
- Post says "first" model of LeCun's vision, but only a component; compare to the paper's own claims.

## Questions for the human
- How much evaluation vocabulary (linear probing, low-shot) should the slides explain?
- Should the generative vs JEPA comparison be central, or secondary to explaining I-JEPA mechanics?
