### [006 – Prompt-caching comparison](experiments/006-prompt-caching-comparison/README.md)

- **Problem:** does CLM's cost and speed advantage over the robust `token-tail/1` baseline persist when both can use ordinary provider prompt caching? This is not the CLM paper's suffix-cache reuse.
- **Design:** {baseline, CLM} × {caching off, on}, on the experiment-004 coding task. Its 4 evaluation instances were reused with fresh runs, 3 repetitions each, giving 48 runs in a Williams order.
  - **Layout:** all conditions share a new request layout, with the stable task first, one block per context entry and the status last.
  - **Caching:** explicit 5-minute breakpoints, used only when caching is on.
  - **Isolation:** a random per-run tag gives every run a cold, private cache.
- **Headline:** all 48 runs were strictly successful.
  - **Cost:** with caching **on**, CLM was **35% cheaper** (USD 0.136 vs 0.208 per run, cheaper in 12 of 12 blocks); with caching **off**, 27% cheaper (0.223 vs 0.305).
  - **Time:** CLM was about 20% faster either way.
  - **Caching within each approach:** it cut cost by 32% (baseline) and 39% (CLM), without changing elapsed time.
- **Main finding:** CLM's advantage persisted and widened. Caching made task calls cheap for both, while the baseline's separate summary calls gained almost nothing from caching (their prefix was mostly not yet cached) and became 37% of its cost.
- **Most important limitation:** one synthetic workload with reused instances, one model, one request layout and caching policy, and cold-start-per-run caches.
