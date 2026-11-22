# JEPA-Anything (arXiv 2609.20800v1, Sept 2026)

## One-line summary
JEPA-Anything keeps the standard JEPA recipe (predict a latent target from context) but splits the target embedding into several orthogonal "factors", each with its own predictor, and claims one such design works across seven very different domains (vision, cells, patients, control, molecules, PDE fields, weather).

## Key takeaways
- The problem: predictive models are usually built per domain; the paper asks whether one learning principle can cover very different systems.
> "Yet predictive models remain domain-specific: can a common learning principle support world modeling across radically different systems?"
- The diagnosis of standard JEPA: a single target embedding and single predictor lets easy or high-variance structure dominate training.
> "easily predicted or high-variance structure may dominate optimization, several latent directions may serve similar roles, and weaker predictive structure may receive conflicting gradients."
- Core idea (OPF, orthogonal predictive factorization): learned projections cut the target into components, and a dedicated branch predicts each one.
> "A collection of learned basis matrices analyzes each target state into multiple components, and a dedicated branch predicts each component from the shared context representation."
- Orthogonality is the key ingredient: it stops factors from duplicating each other and lets the predicted pieces be recombined into one stable latent state (checked on CITRIS Pong; Table 5 numbers stripped).
> "Orthogonality therefore turns multiple prediction outputs into a complete, non-overlapping, and numerically stable world-state interface."
- Beyond accuracy, factor coordinates are used for science: a factor-nominated drug combination (IL-18 plus CD73 blockade) was supported in wet-lab tests.
> "Wet-lab studies subsequently supported this prediction, showing enhanced antitumor activity in Huh7–PBMC co-culture, patient-derived organoids and tumor fragments, and immunocompetent mice."

## Numbers
- Overall claim (vs matched standard-JEPA baselines, same data/encoder/budget):
> "improve the reported metrics across the ten-task matched dynamics benchmark and all four molecular systems"
- CITRIS Interventional Pong (5 seeds): one-step single-intervention MSE 0.009541 to 0.006218; combined 0.009441 to 0.008223; six-step rollout 0.009478 to 0.008665.
> "The corresponding reductions are 34.83%, 12.90%, and 8.58%, respectively."
- APEBench Burgers (MLP):
> "The Burgers errors decrease by approximately 49.5% on the held-out late segment and 44.7% over six rollout steps, with improvement in every seed."
- Kuramoto-Sivashinsky (chaotic PDE):
> "KS late-state prediction improves by approximately 13.2%, also in every seed."
- Molecules (water, quartz, paracetamol, benzene; 100-step free rollout; Table 9): e.g. water RMSD 3.331 (scratch), 2.536 (TrajCast-JEPA), 2.459 (JEPA-Anything) Angstrom. The Benzene MAE row is blank in the extracted text.
> "JEPA -Anything produces the lowest one-step MAE and 100-step RMSD on all four molecular systems."
- Single cell (Table 4, not quotable): PBMC zero-shot AvgBIO 0.5288 (scGPT) vs 0.7752 (JEPA-Anything).
> "attains the highest value on both PBMC clustering metrics and both perturbation-response datasets."
- Orbital: latent modes recover the Kepler scaling relation (slope value stripped from the text; Figure 9, not quotable).

## Concepts a beginner needs
- JEPA: a context encoder, a target encoder and a predictor that predicts the target in representation space, not raw pixels.
- Latent / world model: a model that builds a hidden state from context and predicts another state of the same system.
- EMA target encoder and stop-gradient: the target network is a slow moving average that gets no gradient.
- OPF (with orthogonality and activity penalties): the target is analyzed into orthogonal subspaces ("factors"), each predicted separately, then synthesized back (via pseudoinverse) into a full state.
- OOD, rollout, intervention: unseen conditions; feeding predictions back (errors compound); predicting after a variable is changed.
- Matched baseline: same data, encoder, budget; only the predictive loss differs.

## Proposed wiki pages
- `jepa-anything` (source page): summary, results, status as latest frontier.
- `orthogonal-predictive-factorization`: the core new mechanism.
- `jepa` (update): add the "monolithic target" critique and this extension.
- `latent-world-models`: the paper's broad definition and rollout/planning use.
- `ai-for-science-with-jepa`: wet-lab and Kepler examples.

## Caveats / limitations / things that might conflict with other sources
- Standard JEPA wins somewhere:
> "Planning performance is therefore environment-dependent."
  (Hopper favors standard JEPA.)
- Gains shrink over longer horizons and for harder cases: combined interventions 12.90% vs 34.83% single; Burgers gain:
> "although it narrows from H20 to H50."
- Biology evidence is small-scale:
> "Across three organoid specimens and three tumor-fragment specimens"
- The authors themselves caution:
> "Orthogonal factors do not by themselves establish causal mechanisms, and a shared predictive architecture does not guarantee aligned representations across domains."
- Requires a real context-target dependence ("The interface requires a meaningful predictive relation"), and baselines are re-run by the authors; the paper reports no significance tests beyond the Figure 6 confidence intervals.
- Version status:
> "arXiv:2609.20800v1 [cs.CL] 17 Sep 2026"
  A v1 preprint, not peer reviewed; labeled cs.CL despite its scope. Check against other sources: its framing of JEPA may differ from the original I-JEPA/LeCun description (e.g. it uses regression to the target, not only similarity).

## Questions for the human
1. Should the deck show the factorization idea only conceptually (one target split into orthogonal pieces), or also the pseudoinverse and orthogonality math?
2. Which result gets the most slide space: the Pong intervention gains, the molecular rollouts, or the wet-lab discovery story?
3. Should the Hopper loss and v1 status be a visible "caution" slide, or just a footnote?
