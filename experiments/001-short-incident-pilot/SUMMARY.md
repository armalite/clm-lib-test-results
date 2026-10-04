### [001 – Short incident pilot](experiments/001-short-incident-pilot/README.md)

- **Problem:** an agent investigates a simulated service outage by searching logs, configs and change records, then names the root cause, the exact current value of the faulty setting, a remedy and supporting file:line evidence.
- **Compared:** the summary baseline and CLM.
- **Setup:** `claude-opus-5-5` (effort `low`), 8,000-token budget per model request. 3 task instances × 2 repetitions per approach = 12 comparison runs.
- **Headline:** both approaches got 6/6 strictly correct, after a disclosed scoring correction; before it, the baseline had 5/6. Average cost per run was USD 0.060 (baseline) and USD 0.074 (CLM).
- **Main finding:** the tasks were too short to test context management. Every run finished in 3–4 model calls, before either method activated: 0 summaries and 0 CLM edits.
- **Separate demonstration:** in an explicitly prompted run (not part of the comparison), the model did edit its context and reuse a helper it wrote.
- **Most important limitation:** this experiment says nothing about whether CLM helps, because neither method was exercised.
