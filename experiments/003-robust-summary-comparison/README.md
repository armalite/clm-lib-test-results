# 003 – Robust summary comparison

**Status: complete.** This was a small exploratory comparison: 3 synthetic evaluation instances × 2 approaches × 2 repetitions.

## What problem did we test?

The task is the same as experiment 002's: a simulated outage investigation in which evidence arrives in three stages, sometimes superseding earlier information. The agent must track the facts that matter as its context fills, then report the cause, the **current** value of the faulty setting, a remedy, and three kinds of supporting citation (the symptom, the record that set the current value, and the stage-1 release-note line that started the problem). This experiment used fresh instances.

The question: **does CLM's efficiency and completion advantage from experiment 002 persist against a summary policy that handles large recent messages and leaves useful space for continued work?**

In experiment 002, the baseline kept its four most recent entries verbatim whatever their size. That caused one context overflow, and after pressure began it summarised on almost every step.

## How did the comparison work?

- **Robust summary baseline:** `token-tail/1`, a policy we implemented. The same Claude model writes the summaries it asks for.
  - When a model request reaches about 70% of its 8,000-token budget, older entries are replaced by a summary.
  - **What stays verbatim:** recent entries are kept up to a token allowance (15% of the budget), and the newest entry is kept if it fits 25%. Larger recent entries are summarised too.
  - **Summary size:** each summary is sized so the request drops to about 50% of the budget, leaving room to keep working.
  - **Summariser instructions:** the summariser is told to keep exact values, references, current versus superseded values, and unresolved work.
  - **Retries:** one retry; then an explicit overflow if the summary still doesn't fit.
- **CLM:** the same model, budget, tasks, evidence schedule and tools. The model may rewrite its working-context file with its own code, whenever it chooses, and gets a reminder at the same 70% point. Editing was optional and helpers were not requested.
- **Setup, the same for both:**
  - `claude-opus-5-5` at effort `low`;
  - an 8,000-token budget for each model request (instructions, task and working context together);
  - at most 20 calls and 2,048 output tokens per call;
  - the unchanged scorer, score/2.
- **Runs:** 3 fresh evaluation instances (`staged-eval-4..6`) × 2 repetitions × 2 approaches = **12 runs**, one after another, alternating which approach ran first.
  - Settings, instances, policy version, scorer and exact source were frozen first.
  - One matched calibration pair on a different instance checked that both approaches would activate.

## What happened?

**Both approaches managed context in every run, and neither failed.**
- **Baseline:** summarised 2–3 times per run. 15 summary calls produced 15 accepted summaries, every one fitting at the first attempt, each leaving the request at about 50% of the budget.
- **CLM:** made 2–5 accepted edits per run (16 in total, none rejected), starting in stage 1.
- **No overflows, recoveries or retries** in either approach.

**Outcomes**, 6 runs per approach:

| | Robust summary baseline | CLM |
| --- | --- | --- |
| **Completion:** reached a final answer | 6 of 6 | 6 of 6 |
| **Strict success:** met every requirement | 6 of 6 | 6 of 6 |
| **Factual correctness:** diagnosis, remedy and current value | 6 of 6 | 6 of 6 |
| **Evidence:** all three citation types, within the allowed range | 6 of 6 | 6 of 6 |
| Stale-value or stale-hypothesis errors | 0 | 0 |

**Efficiency**, per-run averages (totals for all 6 runs in brackets):

| | Robust summary baseline | CLM |
| --- | --- | --- |
| Cost per run (USD) | 0.306 (total 1.834) | 0.228 (total 1.369) |
| Elapsed time per run | 75 s (total 448 s) | 54 s (total 323 s) |
| Model calls per run | 12.5: 10.0 task + 2.5 summary (total 75) | 10.3, all task (total 62) |
| Code executions per run | 7.0 | 7.3 |
| Cumulative input tokens per run* | 56,644 | 44,472 |
| Cumulative output tokens per run | 3,955 | 2,514 |
| Cache read / write tokens | 0 / 0 | 0 / 0 |
| Largest single request, average (input tokens) | 5,966 | 5,748 |

\* Cumulative input tokens add up the input of every model call in a run, so they are much larger than any single request.

**When management happened:**
- **Baseline:** the first summary came at steps 3–5 (stage 1 in five runs, stage 2 in one), followed by 5–10 more action steps.
- **CLM:** the first edit took effect at steps 3–5, always in stage 1, followed by 7–10 more action steps. Only one CLM run reached the pressure point at all.

**Matched pairs**, same instance and repetition:

| Instance | Repetition | Baseline (USD) | CLM (USD) | CLM minus baseline (USD) |
| --- | --- | --- | --- | --- |
| staged-eval-4 | 1 | success, 0.278 | success, 0.201 | −0.077 |
| staged-eval-4 | 2 | success, 0.338 | success, 0.255 | −0.082 |
| staged-eval-5 | 1 | success, 0.331 | success, 0.220 | −0.111 |
| staged-eval-5 | 2 | success, 0.376 | success, 0.221 | −0.155 |
| staged-eval-6 | 1 | success, 0.253 | success, 0.247 | −0.006 |
| staged-eval-6 | 2 | success, 0.258 | success, 0.224 | −0.034 |

## What do the results tell us?

- **Against the robust baseline, CLM's quality and completion advantage disappeared.** Both approaches completed and strictly succeeded in every run.
  - This supports the experiment-002 explanation: that gap came from the old baseline's two failure modes (an overflow and an over-wide citation), not from better reasoning.
- **An efficiency advantage remained, smaller.**
  - CLM was about **25% cheaper** per run on average and took about **28% less time**. It was cheaper in all 6 matched pairs, though by very little in one.
  - The cost gap ($0.465 in total) is about the same as the baseline's spending on summary calls ($0.486). Leaving those out, the two approaches spent almost the same on task calls ($1.35 vs $1.37). CLM's saving therefore comes from not paying for separate summarisation, not from doing less investigation.
- **The robust baseline fixed the failures it targeted.**
  - Compared with experiment 002's baseline, it summarised less often (2–3 times per run, versus 2–5) and never overflowed.
  - This is context only, not a matched comparison: experiment 002 used different instances.
- **Retention looked similar.** In 5 of 6 runs per approach, the stage-1 origin reference was still held in the final request, in a summary or a note. All 12 answers cited it.

## What remains untested?

- **Statistical confidence:** 6 runs per approach, from one synthetic task family.
- **Other baselines:** cheaper summariser models, incremental summaries, retrieval.
- **Other conditions:** other models, effort levels and budgets.
- **Accuracy differences:** whether CLM's advantage changes on tasks hard enough to separate the approaches on accuracy. This task proved too easy for that against the robust baseline.
- **Helpers:** helper creation was neither requested nor observed.

## Where is the evidence?

- `protocol.md`: the plan written before the runs, the calibration record, the frozen settings and post-comparison notes.
- `report.md` and `metrics.json` / `metrics.csv`: every run's numbers.
- `manifest.json`: run roles, settings, source commit, the saved source patch and checksums.
- `artifacts/runs/evaluation/`: the 12 comparison runs.
- `artifacts/runs/calibration/`: the matched calibration pair.
- `artifacts/comparisons/20261004T094550/`: the comparison record, with frozen settings (including `summary_policy: token-tail/1`) and the exact source patch.
