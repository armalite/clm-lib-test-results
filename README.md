# clm-lib test results

[clm-lib](https://github.com/armalite/clm-lib) implements the core pattern of Context Language
Models (CLMs): the model sees its working context as a file and writes code to edit it, and the
runtime builds every later model request from the accepted edits. Without an edit, the context
simply accumulates.

This repository holds **our own experiments and evidence** with that library: small synthetic
pilots. It is **not** a reproduction of the CLM paper's benchmarks.

Each experiment documents its own methods, model, context budget and settings in its folder.

## Completed experiments

| Experiment | What it tested | Main finding |
| --- | --- | --- |
| [001](experiments/001-short-incident-pilot/README.md) | Short incident investigations | Neither context-management method activated in the comparison, so it did not test their relative effectiveness. |
| [002](experiments/002-staged-incident-context-pressure/README.md) | Incident investigations with evidence arriving in stages | Both methods managed context. CLM achieved higher strict task success, with lower cost and elapsed time, against this baseline. |
| [003](experiments/003-robust-summary-comparison/README.md) | The same staged investigations, against a more robust summary baseline | Both methods managed context and both got 6/6 strict successes. CLM remained about 25% cheaper and 28% faster, matching the baseline's spending on summary calls. |

### Methods compared in experiments 001 and 002

Experiment 003 used a different, more robust baseline; see its README.

Both experiments compared two context-management approaches. The model was the same (`claude-opus-5-5`, effort `low`), as were the 8,000-token budget per model request and the limits:
- **Summary baseline:** a policy we implemented; the same Claude model writes the summaries it asks for. When a model request reaches about 70% of its budget, Claude is asked to summarise the older working-context entries, and the summary replaces them. The four most recent entries are kept unchanged.
- **CLM:** the same model and budget, but the model may edit its working context itself, at any time, using code it writes. Editing is optional.

### [001 – Short incident pilot](experiments/001-short-incident-pilot/README.md)

- **Problem:** an agent investigates a simulated service outage by searching logs, configs and change records, then names the root cause, the exact current value of the faulty setting, a remedy and supporting file:line evidence.
- **Runs:** 3 task instances × 2 repetitions per approach = 12 comparison runs.
- **Headline:** both approaches got 6/6 strictly correct, after a disclosed scoring correction; before it, the baseline had 5/6. Average cost per run was USD 0.060 (baseline) and USD 0.074 (CLM).
- **Why it didn't test the methods:** every run finished in 3–4 model calls, before either method activated: 0 summaries and 0 CLM edits.
- **Separate demonstration:** in an explicitly prompted run (not part of the comparison), the model did edit its context and reuse a helper it wrote.

### [002 – Staged incident under context pressure](experiments/002-staged-incident-context-pressure/README.md)

- **Problem:** a simulated outage investigation in which new evidence arrives in three stages, sometimes superseding earlier information. The agent has to keep track of the facts that matter as its context fills up, and reach a diagnosis supported by citations.
- **Runs:** 3 instances of one synthetic task × 2 repetitions per approach = 12 comparison runs.
- **Headline:** CLM got **6/6** strict successes against the baseline's **4/6**. It had about **38% lower average cost** per run (USD 0.231 vs 0.372) and about **43% lower average elapsed time** (56 s vs 99 s). CLM edited its context in all 6 runs without being asked to.
- **Explanation:** most of CLM's cost advantage came from not needing separate summarisation calls. The baseline's two failures were one context overflow and one otherwise correct answer whose citation exceeded the allowed range. Every completed answer, in both approaches, had the correct diagnosis, remedy and current value.
- **Most important limitation:** these are promising results from a small synthetic pilot against this one baseline policy: one task family, one model, 6 runs per approach. Better reasoning or memory retention was not demonstrated, and a stronger baseline is untested.

### [003 – Robust summary comparison](experiments/003-robust-summary-comparison/README.md)

- **Problem:** the staged outage investigation from experiment 002 (evidence arriving in three stages), on fresh instances.
- **Compared:** CLM against a more robust summary baseline, `token-tail/1`. It keeps recent history by a token allowance instead of four fixed entries, summarises oversized recent entries too, and sizes summaries to leave about half the budget for further work.
- **Setup:** `claude-opus-5-5` (effort `low`), 8,000-token budget per model request. 3 fresh instances × 2 repetitions per approach = 12 comparison runs.
- **Headline:** both approaches got **6/6** strict successes with no failures. CLM was about **25% cheaper** per run (USD 0.228 vs 0.306) and about **28% faster** (54 s vs 75 s), and cheaper in all 6 matched pairs.
- **Main finding:** experiment 002's quality gap disappeared against the robust baseline. The remaining efficiency gap matches the baseline's spending on separate summary calls.
- **Most important limitation:** a small synthetic pilot with one task family and one model. The task was too easy to separate the approaches on accuracy.

## Planned experiments

These are plans only: nothing has been run, and their settings are not frozen.

| Experiment | Question | Status |
| --- | --- | --- |
| [004](experiments/004-coding-changing-requirements/README.md) | Does model-controlled context editing help an agent implement changing requirements while preserving existing functionality? | planned; not implemented |

## Navigating the raw evidence

Each experiment folder contains:
- `README.md`: what was tested, how, what happened, and what it means.
- `protocol.md`: what was planned before running, and what changed afterwards.
- `report.md`: generated per-run tables and context-edit evidence.
- `metrics.json` / `metrics.csv`: one row per run, machine-readable.
- `manifest.json`: run IDs and roles, settings, source provenance, fixture and ledger checksums.
- `SHA256SUMS`: checksums of the evidence and generated files. The hand-written `README.md`, `SUMMARY.md` and `protocol.md` are excluded, so they can be edited freely.
- `artifacts/runs/<role>/<run_id>/`: one run's evidence. Roles are:
  - `evaluation`: comparison runs;
  - `guided`: explicitly prompted demonstrations;
  - `calibration`: development runs used to check settings;
  - `smoke` and `access-failure`: connectivity checks.

  Inside a run folder:
  - `run.json`: configuration;
  - `events.jsonl`: chronological event log;
  - `requests/`: exact model requests (no headers);
  - `context/`: accepted context revisions and diffs;
  - `scripts/`: model-written code, saved before it ran;
  - `files/`: workspace files before and after each step;
  - `workspace/`: the final sandbox workspace;
  - `evaluator/`: ground truth and score, written after the run;
  - `summary.json`: metrics.
- `artifacts/fixtures/<task>/`: the task files the agent investigated.
- `artifacts/comparisons/`: comparison records, including frozen settings and source patches.

`ledger-snapshots/` holds historical copies of the spend ledger; the active ledger lives in
clm-lib. `notes/` holds the draft blog notes and an archived clm-lib results log.

## Who maintains what

- **Hand-written, maintained here:** this README, each experiment's `README.md`, `SUMMARY.md`
  and `protocol.md`, and `notes/`. Edit them directly in this repository. `clm-lib export`
  never overwrites them.
- **Generated by `clm-lib export`:** `manifest.json`, `report.md`, `metrics.*`, `SHA256SUMS`,
  `artifacts/` and [EXPORT_FORMAT.md](EXPORT_FORMAT.md). Run evidence is copied unchanged
  except for the redactions listed in each manifest, and is never silently replaced.
  `EXPORT_FORMAT.md` gives the full checksum policy.
