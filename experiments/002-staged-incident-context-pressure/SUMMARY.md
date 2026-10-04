### [002 – Staged incident under context pressure](experiments/002-staged-incident-context-pressure/README.md)

- **Problem:** a simulated outage investigation in which new evidence arrives in three stages, sometimes superseding earlier information. The agent has to keep track of the facts that matter as its context fills up, and reach a diagnosis supported by citations.
- **Compared:** the summary baseline and CLM.
- **Setup:** `claude-opus-5-5` (effort `low`), 8,000-token budget per model request. 3 instances of one synthetic task × 2 repetitions per approach = 12 comparison runs.
- **Headline:** CLM got **6/6** strict successes against the baseline's **4/6**. It had about **38% lower average cost** per run (USD 0.231 vs 0.372) and about **43% lower average elapsed time** (56 s vs 99 s). CLM edited its context in all 6 runs without being asked to.
- **Main finding:** most of CLM's cost advantage came from not needing separate summarisation calls. The baseline's two failures were one context overflow and one otherwise correct answer whose citation exceeded the allowed range. Every completed answer, in both approaches, had the correct diagnosis, remedy and current value.
- **Most important limitation:** these are promising results from a small synthetic pilot against this one baseline policy: one task family, one model, 6 runs per approach. Better reasoning or memory retention was not demonstrated, and a stronger baseline is untested.
