### [004 – Coding with changing requirements](experiments/004-coding-changing-requirements/README.md)

- **Problem:** an agent builds a small invoice-calculator package while requirements arrive in four stages. Later stages add rules and replace some earlier ones; every rule not replaced stays in force.
- **Compared:** CLM against the robust `token-tail/1` summary baseline from experiment 003.
- **Setup:** `claude-opus-5-5` (effort `low`), 8,000-token budget per model request, up to 30 calls per run. 4 instances (different add/replace schedules, one generator) × 3 repetitions per approach = 24 runs.
- **Headline:** both approaches got **12/12** strict successes (all 336 evaluator checks passed in each, no regressions, no stale rules). CLM was about **25% cheaper** per run (USD 0.225 vs 0.302) and cheaper in 11 of 12 matched pairs; elapsed time was about 15% lower.
- **Main finding:** correctness was equal; the efficiency gap again matches the baseline's spending on separate summary calls.
- **Most important limitation:** one synthetic application scenario that proved too easy to separate the approaches on correctness. Prompt caching was not tested.
