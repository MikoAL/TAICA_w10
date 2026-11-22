# Meta AI blog: Yann LeCun's vision (Feb 23, 2022)

## One-line summary
LeCun argues that human-level AI needs machines that learn "world models" by self-supervised observation, and sketches a six-module architecture whose core is a (hierarchical) JEPA.

## Key takeaways
- Motivation: people learn far more efficiently than today's systems, so more data and bigger models may not be the answer.
> "a teenager who has never sat behind a steering wheel can learn to drive in about 20 hours"
- Proposed key: learn internal models of how the world works (world models).
> "internal models of how the world works"
- Common sense is framed as a set of world models that tell what is likely, plausible or impossible.
> "common sense can be seen as a collection of models of the world that can guide on what is likely, what is plausible, and what is impossible"
- The architecture has six modules (configurator, perception, world model, cost, actor, short-term memory), all assumed differentiable.
> "LeCun proposes an architecture composed of six separate modules."
- JEPA: encode both inputs into abstract representations and predict one from the other, instead of predicting raw detail.
> "trainable encoders that extract abstract representations of them"
- Training JEPA: contrastive methods are impractical in high dimensions, so regularized methods (e.g. VICReg) are the alternative.
> "Until recently, the only approach would have been to use contrastive methods"
- JEPAs can be stacked for higher abstraction and longer-term prediction (the "cook making crepes" example).
> "This enables JEPAs to be stacked on top of one another so as to learn representations with higher levels of abstraction"
- Training the world model is the open problem; Meta admits no guarantees.
> "training world models constitutes the main challenge toward real progress in AI over the next decades"

## Numbers
- Teen learns to drive in about 20 hours:
> "can learn to drive in about 20 hours"
- Autonomous driving systems' data needs:
> "millions or billions of pieces of labeled training data and millions of reinforcement learning trials in virtual environments"
- Four criteria for regularized JEPA training:
> "the method uses four criteria:"
- Babies learn intuitive physics at about nine months:
> "around nine months of age, babies learn intuitive physics"

## Concepts a beginner needs
- World model: an internal simulator of how the world works, used to predict, reason and plan.
- Self-supervised learning: learning from the world without task labels ("task-independent, unsupervised way").
- Configurator: executive control; sets up the other modules for the task.
- Perception: estimates current world state from sensors.
- World model module: fills in missing information and predicts plausible future states.
- Cost module: one scalar "discomfort"; intrinsic cost (fixed) plus trainable critic.
- Actor: proposes action sequences that minimize predicted cost.
- Short-term memory: tracks current/predicted state and costs.
- JEPA: predicts the representation s_y from s_x, optionally with latent variable z for uncertainty.
- Contrastive vs regularized training; VICReg (Variance, Invariance, Covariance Regularization).
- Hierarchical JEPA, model-predictive-control-style planning with subgoals.

## Proposed wiki pages
- `world-model` - central idea and motivation.
- `lecun-autonomous-intelligence-architecture` - the six modules.
- `jepa` - definition, latent variable, stacking.
- `self-supervised-learning` - framing as learning without labels.
- `contrastive-vs-regularized-training` - plus VICReg.
- `hierarchical-planning` - perception-action episode.
- `common-sense` - brief concept page.

## Caveats / things that might conflict with other sources
- It is a vision preview with no results; the post says details come in a later position paper.
- Animal/baby comparisons are asserted without evidence ("It can be hypothesized...").
- "Millions or billions" of data for driving is not sourced.
- Later JEPA sources (I-JEPA, V-JEPA) may define JEPA more narrowly; check the position paper for module names and the VICReg criteria wording.
- Blog says the latent variable z handles uncertainty; I-JEPA uses positional tokens instead.

## Questions for the human
- Should the deck spend time on all six modules, or only world model + JEPA?
- Include the hierarchical planning (perception-action episode) detail, or treat it as optional advanced material?
