# 004 – Coding with changing requirements (planned)

**Status: planned. Not implemented and not run.** The task design below is a proposal; workload size, sample size and settings will be set during development calibration.

## Question

Does model-controlled context editing help an agent implement changing requirements while preserving existing functionality?

## Why

Experiments 001–003 use incident investigation, where the agent mostly reads. A coding task adds a different pressure: the agent must remember which requirements are still in force, which have been superseded, and what it has already built, while its context fills with code, test output and requirement updates.

## Proposed task

- **Repository:** a small, self-contained Python package, for example an invoice or pricing calculator of a few modules, with no third-party dependencies.
- **Requirements arrive in stages,** like the staged evidence in experiment 002:
  - The first stage asks for core features.
  - Later stages add features and **supersede** some earlier rules, for example a changed rounding or discount rule.
  - Some stages state only the change, so the agent must keep track of what remains in force.
- **Visible tests:** at each stage the agent sees tests for that stage's requirements, and can run tests and edit files in its sandboxed workspace.
- **Evaluation:** independent evaluator tests check the **final, current** requirements plus **regressions** (earlier requirements that still apply). They also check that superseded behaviour was actually replaced. These tests and their expected results stay outside the agent workspace and are run only after the run ends.

## Comparison

- **Arms:** CLM versus a summary baseline, with the same model, repository access, editing tools, visible tests and limits.
- **Baseline policy:** to be chosen after experiment 003; most likely the more robust summary policy from that experiment.

## What will be measured

- **Correctness:** the evaluator-test pass rate on current requirements.
- **Task completion:** did the run finish with a submitted solution?
- **Regressions:** earlier, still-valid requirements now failing.
- **Superseded behaviour:** old rules still present.
- **Context management:** edits, summaries, overflows and recoveries, and when they happened.
- **Efficiency:** provider-reported tokens, cost, calls and elapsed time.

## What outcomes would and would not establish

- A difference in **regressions or superseded-rule errors** at similar cost would be evidence about keeping track of changing requirements on this task.
- **Equal correctness** with different efficiency is still informative.
- A small synthetic task cannot establish general coding benefit, and nothing here will be statistically definitive.

## Unresolved design decisions

See `protocol.md`.
