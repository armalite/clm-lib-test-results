### [003 – Robust summary comparison](experiments/003-robust-summary-comparison/README.md)

- **Problem:** the staged outage investigation from experiment 002 (evidence arriving in three stages), on fresh instances.
- **Compared:** CLM against a more robust summary baseline, `token-tail/1`. It keeps recent history by a token allowance instead of four fixed entries, summarises oversized recent entries too, and sizes summaries to leave about half the budget for further work.
- **Setup:** `claude-opus-5-5` (effort `low`), 8,000-token budget per model request. 3 fresh instances × 2 repetitions per approach = 12 comparison runs.
- **Headline:** both approaches got **6/6** strict successes with no failures. CLM was about **25% cheaper** per run (USD 0.228 vs 0.306) and about **28% faster** (54 s vs 75 s), and cheaper in all 6 matched pairs.
- **Main finding:** experiment 002's quality gap disappeared against the robust baseline. The remaining efficiency gap matches the baseline's spending on separate summary calls.
- **Most important limitation:** a small synthetic pilot with one task family and one model. The task was too easy to separate the approaches on accuracy.
