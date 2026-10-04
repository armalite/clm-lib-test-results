# 005 – Harder coding accuracy comparison (planned)

**Status: draft plan. Not implemented and not run.** Nothing below is frozen, and workload, sample size and budget are not agreed.

## Question

Does CLM affect correctness when changing requirements create a more demanding coding task?

## Why

Experiments 001–004 already measured accuracy, but in experiments 003 and 004 they hit a ceiling: against the robust baseline, both arms passed every evaluator check. In experiment 004, all 336 checks passed per arm, with no regressions and no stale rules. A task where some runs fail is needed to tell the approaches apart on correctness. The goal is a more informative accuracy comparison, **not** a guaranteed CLM advantage.

## Task and comparison (proposed)

- **Task:** extend the experiment-004 coding task family, rather than build a new one. Candidate ways to make it more demanding with substantive work, not artificial padding:
  - more interacting rules, where one rule's output feeds another (for example discounts that depend on tax region, or rounding that interacts with bulk tiers);
  - more stages, and longer gaps between a rule and its later change, so a superseded rule was introduced well before its replacement;
  - changes stated only by reference ("the stage-2 discount now also applies to …");
  - a somewhat larger package, with several modules and more functions.
- **Arms:** CLM against the robust `token-tail/1` summary baseline. The same model, effort, file access, tools, visible tests and limits for both.
- **Instances:** development instances for calibration only; fresh evaluation instances with distinct add/replace/interaction structures.

## What will be measured

- **Correctness:** strict success; current-requirement correctness (all checks); retained-rule failures (regressions); superseded-rule failures (stale rules); interaction-check failures, if added.
- **Completion:** whether the run submitted.
- **Context management:** edits, summaries, overflows and recoveries, and when they happened.
- **Efficiency:** provider-reported tokens, cost, calls and elapsed time.

## What outcomes would and would not establish

- A correctness difference at a non-ceiling difficulty would be evidence about this task family and model, in either direction.
- Equal correctness at a non-ceiling difficulty would also be informative.
- One scenario and a small sample cannot establish general coding benefit.

## Rules for calibration and evaluation

- Calibrate difficulty on development instances only, aiming for a task that is feasible but not always solved.
- Do not select settings because CLM wins, and do not tune against held-out results.
- Freeze the workload, scoring, instances and sample before evaluation.

## Unresolved decisions

See `protocol.md`.
