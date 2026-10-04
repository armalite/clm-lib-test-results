# 001 – Short incident pilot

## What problem did we test?

An AI agent investigates a simulated production outage. It searches through about 250,000 characters of logs, configuration files, change records, metrics and on-call notes, then reports:
- the **root cause**;
- the **exact current value** of the faulty setting;
- a **remedy**;
- **file:line citations** supporting the cause and the value.

Each task has a trap: an outdated value (for example in a config file or an early note) that a later, authoritative change record overrides.

The question: when the agent's working context is limited, does letting the model **edit its own context** (CLM) change results or cost compared with **automatic summarisation**?

## How did the comparison work?

- **Summary baseline (our implemented policy):** when a model request reaches about 70% of its 8,000-token budget, Claude summarises the older working-context entries, and the summary replaces them. The 4 most recent entries are kept unchanged.
- **CLM:** the same model, budget and tools. The model may rewrite its working-context file with code it writes, whenever it chooses. Editing is optional.
- **Setup, the same for both:**
  - `claude-opus-5-5` at effort `low`;
  - an 8,000-token budget for each model request (instructions, task and working context together);
  - at most 20 model calls per run.
- **Runs:** 3 task instances, each with a different root cause, × 2 repetitions × 2 approaches = **12 comparison runs**, one after another, alternating which approach ran first.
- **Scoring:** a run is a **strict success** only if the cause, remedy and exact current value are all correct and the citations cover both the cause and the value.

Separately, and not part of the comparison:
- a **prompted demonstration**, in which the model was explicitly asked to build and reuse a context-editing helper;
- one **calibration run**, checking that the budget could create pressure.

## What happened?

**The comparison tasks finished before either context-management method activated.** Every run took 3–4 model calls. The baseline never summarised, and CLM never edited its context.

Per-run averages, 6 runs per approach:

| | Summary baseline | CLM |
| --- | --- | --- |
| Reached a final answer | 6 of 6 | 6 of 6 |
| Strict success, original scorer (score/1) | 5 of 6 | 6 of 6 |
| Strict success, corrected scorer (score/2) | 6 of 6 | 6 of 6 |
| Average cost per run (USD) | 0.060 | 0.074 |
| Average elapsed time per run | 15 s | 17 s |
| Average model calls per run | 3.0 | 3.2 |
| Summaries / CLM edits (all runs) | 0 summaries | 0 edits |

Totals across all 6 runs per approach: USD 0.363 (baseline) and USD 0.446 (CLM).

- **Scoring correction (disclosed, after seeing results).**
  - One baseline answer gave the value as `clients.pricing-core.timeout_ms=750`. That is correct, written in the form used by the authoritative record. The original scorer wanted the bare `750`.
  - The corrected scorer also accepts `setting=value`, applied identically to every run. Both results are kept: `score/1` in each run's `evaluator/score.json`, `score/2` in `metrics.json`, `metrics.csv` and `report.md`.
  - No runs were repeated.
- **Prompted demonstration** (run `20261004T065342-guided-dev-a667`).
  - When asked to, the model wrote `helpers/ctx.py::compact(note)` and called it in two later steps. Each call replaced the working context with a short note.
  - The next model request contained exactly the edited context: 3,435 → 212 characters, then 2,853 → 267.
  - This shows the mechanism working with a real model **when prompted**. It is not evidence of spontaneous behaviour or of benefit.
- **Total spend for this experiment:** USD 1.055. That covers the comparison, the demonstration, the calibration run and a smoke check, all from provider-reported usage.

## What do the results tell us?

- **About the implementation:** context replacement works end to end with a real model (the demonstration).
- **About CLM versus summarisation:** **nothing.** Neither method was exercised in the comparison.
- **About cost:** CLM's slightly higher cost reflects its longer instructions (about 350 extra tokens per call) and normal run-to-run variation. It is not a cost of editing, since no edits happened.

## What remains untested?

- Whether CLM helps when context actually fills up. Experiment 002 was designed to test this.
- Other task families, models and baselines. There were only 2 repetitions per cell, so no statistical claims are made.

## Where is the evidence?

- `protocol.md`: planned procedure versus later changes, including the scorer correction and the added calibration run.
- `report.md` and `metrics.json` / `metrics.csv`: every run's numbers, with both scorer versions.
- `manifest.json`: run roles, settings, source commit and checksums.
- `artifacts/runs/evaluation/`: the 12 comparison runs.
- `artifacts/runs/guided/`: the prompted demonstration.
- `artifacts/runs/calibration/`, `smoke/` and `access-failure/`: supporting checks.
- `artifacts/comparisons/20261004T065603/`: the comparison record with its frozen settings.
- `artifacts/source/`: the scorer-correction patch.
