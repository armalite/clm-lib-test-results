# 004 – Protocol (draft; not frozen; not implemented)

## Proposed procedure

1. **Implement a task generator** for the coding task, with stages, visible tests and evaluator-only tests. Evaluator-only material lives outside the sandbox mounts, as with experiment 002's ground truth.
2. **Offline tests:**
   - stage visibility;
   - evaluator isolation (no evaluator file visible in the sandbox);
   - scoring of correct, regressed and stale-rule solutions.
3. **Development calibration:** check that context pressure arises while work remains, and that both arms can complete the task.
4. **Freeze, then run a small matched comparison:** fresh evaluation instances, with arm order alternating across pairs. Report all assigned runs.

## Unresolved design decisions

- **Test runner in the sandbox:** the current image (`python:3.12-slim`) has no pytest. Options are `unittest`, or a prebuilt image with pytest. Either way there is no network access during runs.
- **Submission:** how the agent signals completion, for example a `final` action with a short change summary.
- **Workload size:** the number of stages, the requirements per stage, and how much code and test output each stage produces, chosen so that pressure occurs while work remains.
- **Scoring:** whether strict success means all evaluator tests passing, and how regressions and superseded-rule failures are reported separately.
- **Sample size and budget:** depend on the remaining ledger balance after experiment 003. Additional funding may be needed.
- **Baseline policy:** decided after experiment 003.
