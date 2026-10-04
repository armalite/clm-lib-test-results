# 005 – Protocol (draft; not frozen; not implemented)

## Proposed procedure

1. **Extend the coding generator** (a new generator version; `invoice-gen/1` stays unchanged for experiment 004):
   - interacting rules, more stages and longer change gaps, and changes stated by reference;
   - evaluator checks for interactions;
   - stale and regression detection kept as in experiment 004.
2. **Offline tests:**
   - stage visibility;
   - evaluator isolation;
   - scoring of correct, regressed, stale and interaction-failure solutions;
   - existing experiments unchanged.
3. **Development calibration:** a difficulty where some development runs fail, while both arms can complete the task and context management happens while work remains. Every attempt and change is recorded.
4. **Freeze, then run** a matched comparison on fresh evaluation instances with alternating arm order. All assigned runs are reported, with no reruns.

## Unresolved decisions

- **Workload:** which difficulty levers to use; the number of stages and rules; package size.
- **Limits:** whether `max_calls` / `max_output_tokens` need to change. Any change applies equally to both arms and is disclosed.
- **Difficulty target:** what failure rate counts as "informative". Decided before calibration from feasibility, not from which arm fails.
- **Sample size:** likely more instances and repetitions than experiment 004, if failures are rare events.
- **Budget:** not agreed. Experiment 004's unused authorisation does **not** carry over; a budget must be authorised for this experiment.
- **Metadata fix:** the exporter's `exported_with.current_scorer` should be fixed to report task-appropriate scorer versions before this experiment is exported (see clm-lib `docs/HANDOFF.md`).
