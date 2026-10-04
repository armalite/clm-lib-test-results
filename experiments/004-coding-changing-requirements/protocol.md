# 004 – Protocol

_Design finalised on 2026-10-05, before any experiment-004 live run. Calibration, freezing and post-comparison notes are added below as they happen; earlier sections are not rewritten afterwards._

## Resolution of the earlier open decisions

| Earlier open decision | Resolution |
| --- | --- |
| Test runner in the sandbox | Standard-library `unittest` in the existing `python:3.12-slim` sandbox. No new image, no network. |
| Submission | A `final` action, `{"summary": "..."}`, accepted only after all stages are released. The workspace at that point is the submission. |
| Workload size | 4 stages with 2–3 rule changes each (below). Confirmed or adjusted in calibration. |
| Scoring | Strict success means every evaluator check passes **and** the agent submitted. Regressions and stale rules are reported separately. |
| Sample size and budget | USD 30 authorised for this experiment (below). Sample decided after calibration. |
| Baseline policy | `token-tail/1`, the robust baseline from experiment 003. |

## Task

- **Package:** a dependency-free Python package `invoice` (generator `invoice-gen/1`, in clm-lib `src/clm_lib/coding.py`). It provides:
  - `compute_invoice(lines, customer)`, which returns subtotal, discount, tax and total as 2-decimal strings;
  - `format_money(amount, currency)`.
- **Starting point:** the agent's writable workspace starts with a skeleton package.
- **Rule modules**, each with one or two versions:
  - rounding: per-line half-up, then exact amounts with half-even rounding;
  - tax: flat 10%, then regional rates;
  - tier discount: one rate table, then another;
  - bulk-line discount: one threshold scheme, then another;
  - tax exemption;
  - validation: `qty <= 0` rejected, then `qty == 0` lines skipped;
  - money formatting: plain, then with thousands separators.
- **Schedules:** each instance has its own schedule over 4 stages, saying which rules are introduced and which are later **replaced**. Rules that are never changed after being introduced **remain in force**.

**Instances.** Each instance is a different supersession structure, not just different numbers:

| Instance | Use | Rules replaced later | Rules retained unchanged | Introduced in the final stage |
| --- | --- | --- | --- | --- |
| `coding-dev-1` | calibration | ROUND, TAX, TIER | VALIDATE, BULK | FORMAT |
| `coding-dev-2` | calibration | FORMAT, TIER, TAX | ROUND, VALIDATE, EXEMPT | BULK |
| `coding-eval-1` | evaluation | ROUND, TAX, BULK | VALIDATE, TIER | EXEMPT, FORMAT |
| `coding-eval-2` | evaluation | TIER, VALIDATE, FORMAT | ROUND, TAX, BULK | EXEMPT |
| `coding-eval-3` | evaluation | ROUND, TAX, FORMAT, BULK | TIER, EXEMPT | VALIDATE |
| `coding-eval-4` | evaluation | ROUND, BULK, TIER, VALIDATE | TAX, FORMAT | EXEMPT |

All instances come from **one generator and one application scenario** (an invoice calculator). This is a limitation.

## Release, access and submission (the same for both arms)

- **At start:**
  - `/task/fixtures/stage-1/REQUIREMENTS.md`: the API, the base calculation and the stage-1 rules.
  - `/task/fixtures/current-tests/test_invoice.py`: visible `unittest` tests for the rules in force.
  - The editable skeleton in `/task/workspace/invoice/`.
  - Fixtures are read-only.
- **`advance`:**
  - releases `stage-N/REQUIREMENTS.md`, which lists only that stage's changes, each marked NEW or CHANGED;
  - rewrites `current-tests/test_invoice.py` to cover every rule then in force, so visible tests for replaced rules are updated, not left contradicting the new rule;
  - appends the requirement text to the working context.
- **Re-reading:** earlier requirement files never change and stay readable to both arms. Neither arm is told to re-read or not to.
- **Work:** the agent edits code and runs the visible tests from its own Python code (`python -m unittest discover -s /task/fixtures/current-tests`) inside the sandbox.
- **Finishing:** `final` is accepted only after all 4 stages are released; an earlier `final` gets a neutral "not accepted" notice.

## Evaluation (evaluator-only, outside the agent's view)

- **Checks:** each instance has data-driven checks: 4 per rule in force at the end, 24–28 in total.
  - They are generated host-side with a reference implementation, on inputs **different** from the visible tests, and cover only disclosed requirements.
  - They exist only in host memory during the run.
- **Where they run:** after the run, the submitted workspace is copied, and the checks run against the copy **in a fresh sandbox container**. Model-written code never runs on the host. The visible tests are read-only and are not used for scoring, so editing them cannot affect evaluation.
- **Categories**, one per check, by the rule it targets:
  - **retained:** a rule introduced before the final stage and never changed. Failures here are **regressions**.
  - **replaced:** a rule that was superseded. Each check also records the old rule's result; if the code reproduces it, the check counts as a **stale rule**.
  - **final_stage:** a rule introduced in the last stage.
- **Outcomes:**
  - **Strict success:** every check passes and the agent submitted.
  - **Other run outcomes:** `failed_checks`, `no_submission`, `correct_unsubmitted` and `evaluation_error`. An evaluator infrastructure failure counts as an invalid run.
- **Counting:** checks are task components, not independent samples. The unit of analysis is the run.
- **Limitation:** checks target one rule each, but are computed with all rules active, so a bug in one rule can occasionally fail another rule's check.

## Arms and settings (identical for both arms)

- **Comparison:** CLM (optional, model-controlled context editing, with the usual reminders) against the `token-tail/1` summary baseline (experiment 003's policy, with a coding-specific summariser instruction).
- **Config:** `configs/exp004.toml`, which is experiment 003's configuration except as noted.
  - The same: `claude-opus-5-5`, effort `low`, an 8,000-token whole-request budget, a 70% pressure point, a 1,000-token reserve, 30 s per execution, and token-tail ratios 0.15 / 0.25 / 0.50.
  - **Changed for this coding task:** `max_calls` 30 (was 20) and `max_output_tokens` 4,096 (was 2,048). Four requirement stages need code-writing, test and fix steps, and one action may write a whole module.
- **Prompt caching:** disabled. No `cache_control` is sent; it should be tested separately.

## Budget

- **Ledger before this experiment:** USD 8.916744 spent, USD 10 ceiling.
- **Authorised additional spend:** USD 30. The ledger ceiling is raised once, explicitly and with a recorded reason, to USD 38.916744. All prior spend records are preserved.
- **Cap:** never exceeded. If funds run out, outcomes are preserved and the comparison is reported incomplete.

## Calibration plan and stopping rules

- **Instances:** `coding-dev-1`, then `coding-dev-2` if needed. Matched pairs (both arms).
- **Checks:**
  - Is the task feasible within the limits?
  - Does pressure arise **while coding work remains**, and do summaries or edits occur before the final stage?
  - Are there avoidable infrastructure failures, such as output truncation or repair loops?
- **Adjustments:** if management is not exercised, or the task is infeasible, adjust the **development** workload or shared settings, with each change and the reason recorded, and recalibrate.
  - No adjustment is chosen because one arm wins.
  - **Stop calibration** after at most 3 matched pairs, or USD 8 of calibration spend, whichever comes first, and report if no functioning setting is found.

## Planned comparison

- **Sample:** after freezing, `coding-eval-1..4` (4 distinct structures) × 2 arms × 2 repetitions = 16 runs, sequential, alternating arm order across matched pairs, if the cost estimate from calibration fits the remaining authorisation. Otherwise 3 instances × 2 × 2, with the reason recorded.
- **Reporting:** all assigned runs are reported. Invalid runs (infrastructure or evaluation errors) are labelled and kept, not replaced.
- **No changes after results:** no scorer, prompt or setting changes after seeing evaluation results.

## Calibration record (development instances only)

The ledger ceiling was raised once beforehand, as authorised: from USD 10 to USD 38.916744 (spend at the change: USD 8.916744). The change is recorded in the ledger's `ceiling_history`, and all 360 prior entries are unchanged.

| # | Run | Instance | Arm | Result | Management observed |
| --- | --- | --- | --- | --- | --- |
| 1a | `20261004T110623-summary-coding-dev-1-3c5d` | coding-dev-1 | token-tail/1 | strict 24/24, 11 calls, USD 0.259 | one summary at step 7 (stage 3); 4 action steps after (2 executions, 1 advance) |
| 1b | `20261004T110755-clm-coding-dev-1-9116` | coding-dev-1 | CLM | strict 24/24, 11 calls, USD 0.228 | 2 unprompted edits (effective at steps 5 and 8, stages 2–3), each shrinking about 4.3–4.9K chars of history to a 300–400-char note; 7 action steps after; pressure never reached |
| 2a | `20261004T110921-summary-coding-dev-2-4e2e` | coding-dev-2 | token-tail/1 | strict 28/28, 11 calls, USD 0.261 | one summary at step 8 (stage 4); 3 action steps after |
| 2b | `20261004T111036-clm-coding-dev-2-189d` | coding-dev-2 | CLM | strict 28/28, 12 calls, USD 0.221 | 3 unprompted edits, the first effective at step 4 (stage 1); 9 action steps after |

**Findings:**
- The task is feasible within the limits, with no truncation, repair or infrastructure problems.
- Both methods manage context **before the final submission, while coding work remains**.
- The pressure is **modest**: the model writes compact code and uses one or two executions per stage. The baseline needed only one summary per run, and peak requests were about 4.6–5.6K tokens of the 8K budget.

**Decision:** no workload or setting change (the protocol's condition for change, management not being exercised, did not occur). Calibration spend was USD 0.969.

**Sample size, decided from calibration cost only:**
- At about USD 0.25 per run, the planned 16 runs would use about USD 4 of the remaining authorisation.
- Because differences may be mainly in efficiency, extra repetitions improve the estimate of run-to-run variability.
- The final sample is therefore **4 evaluation instances × 3 repetitions × 2 arms = 24 runs**, estimated at USD 6–7. This replaces the planned 2 repetitions. It is decided before any evaluation run.

## Frozen

Comparison `20261004T111345`, launched on 2026-10-04 (UTC) with `configs/exp004.toml`. The frozen block records:
- `claude-opus-5-5`, effort `low`, prompt version `2026-10-04.1` (coding task-kind variant);
- generator `invoice-gen/1`, summary policy `token-tail/1`;
- the full config (`max_calls` 30, `max_output_tokens` 4096, 8,000-token budget);
- git HEAD `9e843c2`, the SHA-256 of the uncommitted source (`20261004T111345.patch`, which includes the new `coding.py` and `configs/exp004.toml`).

Evaluation instances `coding-eval-1..4` had not been run before.

**Provenance note:** the frozen block's `scorer_version` field reads `score/2`, the incident scorer's constant. The coding runs were scored by `invoice-checks/1`, as every run's `evaluator/score.json` records. The field is wrong; scoring is unaffected.

## After the comparison

- All 24 cells completed; none were missing, invalid or halted. No runs were repeated.
- No scorer, prompt, setting or code changes were made to the evaluated system after the comparison.
  - The frozen-block `scorer_version` recording was corrected in clm-lib afterwards, for future comparisons only.
- **Costs:** evaluation USD 6.327; calibration plus evaluation USD 7.297, within the USD 30 authorisation.
- **Ledger after the experiment:** USD 16.214 spent of the USD 38.917 ceiling.
