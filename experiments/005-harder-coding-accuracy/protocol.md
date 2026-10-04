# 005 – Protocol

_Design finalised on 2026-10-05, before any experiment-005 live run. It replaces the draft plan committed earlier. Calibration, freezing and post-comparison notes are added below as they happen; earlier sections are not rewritten afterwards._

## Question

Does CLM affect correctness on a coding task with changing, interacting requirements, compared with the robust `token-tail/1` summary baseline? Experiment 004 exercised context management, but both arms passed every evaluator check. This experiment makes the task substantively harder. It is **not** designed or tuned to make CLM win.

## Task: invoice calculator, generator `invoice-gen/2`

- **Code:** clm-lib `src/clm_lib/coding2.py` (generator, checks, scoring) and `src/clm_lib/invoice_ref2.py` (reference rules). `invoice-gen/1` and experiment 004 are unchanged.
- **Same scenario as experiment 004:** the agent implements a dependency-free Python package `invoice` in its workspace, with requirements released in stages by `advance`.
- **API:**
  - `compute_invoice(lines, customer)` returns a dict with **exactly** the keys `subtotal`, `discount`, `shipping`, `tax` and `total`. Each value is a `str` with exactly 2 decimals.
  - The harder variant adds `compute_refund(lines, customer, returns)`, which returns a `str`.

### Rules

| Module | Version 1 | Version 2 (a partial or full change) |
| --- | --- | --- |
| ROUND | Round each line amount (half up) after adjustments; round each discount part and the tax as soon as computed | **Full replacement:** exact arithmetic; round subtotal, discount and tax at the end, half even |
| VALIDATE | `ValueError` for empty lines, qty not an integer > 0, or negative price | qty 0 lines are ignored (all ignored: `ValueError`); the rest is unchanged |
| BULK | qty ≥ 100 is a bulk line; amount × 0.90 | Threshold becomes qty ≥ 50; the multiplier is unchanged |
| TIER | Gold 5%, silver 2%, others 0%, applied to the tier-eligible amount | Gold becomes 8% and platinum 10% is new; silver and the rest are unchanged |
| STACK | Bulk lines are not tier-eligible | — |
| COUPON (harder only) | Coupon applied after the tier discount, capped at the amount left | **Order change:** coupon first (capped at the subtotal), then the tier rate on eligible − coupon |
| SHIP | 7.50 when subtotal − discount < 100.00; not taxed | Shipping is now taxed; fee and threshold unchanged |
| TAX | 10% for everyone | NZ 15%, US 0%; **other regions keep the earlier rate** |
| REFUND (harder only) | `compute_refund`: original total minus the total for kept quantities, both with every rule but no shipping; never negative; `ValueError` for bad returns | — |

**How the rules interact:**
- bulk status decides tier eligibility;
- the discount decides the shipping threshold;
- shipping may be taxed;
- coupons change the calculation order;
- refunds recompute both invoices, so a return can move a line across the bulk threshold.

**How changes are stated:**
- **Partial changes:** a CHANGED item names the stage it partly replaces (for example "partly replaces the stage-1 rates"). It states only what changed: the parts left in force are not restated.
- **Reading the documents:** earlier documents never change and stay readable.
- **Precision:** the exact text is in each instance's `artifacts/fixtures/<task>/stage-N/REQUIREMENTS.md`. Every rule is precise and every check follows from it; there is no padding or log noise.

### Workload levels, fixed before calibration

- **Base (`coding2-*`):**
  - **6 stages and 7 modules** (ROUND, VALIDATE, BULK, TIER, STACK, SHIP, TAX);
  - each instance changes 3–4 rules, with gaps of 1–5 stages between introducing and changing a rule.
- **Harder variant (`coding2h-*`):**
  - the same schedule plus **stages 7 and 8**;
  - adds COUPON, one further change, then REFUND and another change.
  - The result: **8 stages, 9 modules**, 5–6 changed rules and longer gaps.
- **Instances:**
  - **Calibration:** `dev-1` and `dev-2`.
  - **Evaluation:** `eval-1` … `eval-6`, each with its own order of introduction, changed rules and gaps.

| Instance | Base: changed rules (introduced → changed stage) | Harder: further changes (stage) |
| --- | --- | --- |
| dev-1 | TAX 1→4, TIER 2→5, ROUND 1→6, SHIP 3→6 | BULK (7), COUPON (8) |
| dev-2 | BULK 3→5, VALIDATE 2→5, TAX 3→6, TIER 1→6 | SHIP (7), ROUND (8) |
| eval-1 | BULK 1→4, SHIP 2→5, TAX 2→6 | TIER (7), VALIDATE (8) |
| eval-2 | TIER 1→4, VALIDATE 2→5, ROUND 1→6 | TAX (7), COUPON (8) |
| eval-3 | TAX 2→3, BULK 1→5, SHIP 4→6, TIER 1→6 | ROUND (7), VALIDATE (8) |
| eval-4 | TAX 1→4, ROUND 1→4, BULK 2→6, VALIDATE 3→6 | SHIP (7), TIER (8) |
| eval-5 | SHIP 1→4, TIER 2→5, TAX 2→6 | BULK (7), COUPON (8) |
| eval-6 | ROUND 1→4, TIER 1→5, VALIDATE 3→6, BULK 1→6 | TAX (7), SHIP (8) |

All instances come from **one generator and one synthetic scenario**. This is a limitation.

### Access, the same for both arms

- **At the start:**
  - `/task/fixtures/stage-1/REQUIREMENTS.md`;
  - visible tests at `/task/fixtures/current-tests/test_invoice.py`;
  - a skeleton package in the writable workspace.
- **Fixtures are read-only.**
- **On `advance`:**
  - the next stage document is released and also added to the working context;
  - the visible tests are rewritten for every rule then in force (2 tests per rule; for a changed rule, one of them tests the changed behaviour), so they never demand superseded behaviour.
- **Finishing:** `final` is accepted only after all stages are released.
- **Tools and limits:** the same tools, prompts and limits for both arms, as in experiment 004.

## Evaluator (`invoice-checks/2`)

- **How checks are made:** hidden checks are computed host-side by the reference implementation. They:
  - use inputs different from every visible test;
  - test only disclosed requirements: inputs use only fields disclosed by then (no coupons before the coupon rule);
  - stay in host memory during the run;
  - run against a copy of the submission **in a fresh sandbox**.
- **Check categories:**
  - **retained:** a rule introduced before the final stage and never changed (4 checks per rule).
  - **replaced:** behaviour that a CHANGED rule altered (4 checks per rule). Every replaced check records the old rule's result. A failure whose output equals the old result counts as a **stale rule**; other failures are general failures of the changed rule.
  - **kept_part:** the part of a partially changed rule that stayed in force, for example silver 2% after the gold change, or other regions' 10% after the NZ/US change (2 checks per such rule). Each check is chosen so that a plausible over-applied change fails it.
  - **interaction:** 6 inputs where at least three rules (or, for refunds, two besides the refund rule) affect the result together.
  - **final_stage:** a rule introduced in the final stage (4 checks; refunds in the harder variant).
- **Boundary flags:** these mark thresholds (qty at and one below the bulk threshold, exactly 100.00 and 99.99, a discount bringing the subtotal below 100.00), rounding ties, coupon caps, and refunds that cross the bulk or shipping threshold or would be negative.
- **Exact API and types:** `compute_invoice` must return a `dict` with exactly the five keys and `str` values. `compute_refund` must return a `str`. A missing function or a wrong type is a failure, recorded as a type error.
- **Snapshots (for regression claims):**
  - When the agent releases stage k+1, the runtime copies its workspace host-side, out of the agent's view.
  - After the run, each copy is tested in the sandbox against hidden snapshot checks for the rules in force at stage k.
  - A failed retained rule is called a **regression** only if its snapshot checks had all passed at an earlier stage. Otherwise it is a **retained-rule failure**.
- **Counting:** checks are components of a run, not independent samples.

### Validation before any live run

All of this was done offline, without the model:
- **Cross-check:** the reference agrees with an independently written implementation:
  - on every hidden check of all 16 instances;
  - on 150 random inputs per stage configuration (more than 10,000 comparisons).
- **Hand-worked example:** one interacting example was checked by hand.
- **Deliberate mistakes:** for every instance (host-side), each mistake fails at least one hidden check, in the expected category:
  - forgetting any rule;
  - keeping any outdated rule, which is detected as stale in ≥ 4 replaced checks;
  - each over-applied partial change, which fails kept_part checks;
  - three calculation-order mistakes;
  - three refund interaction mistakes.
- **In the sandbox:**
  - the independent implementation is strictly successful;
  - faulty submissions are detected: a forgotten earlier rule, an outdated rule kept, a partial change over-applied, a wrong calculation order and a refund interaction mistake;
  - returning `Decimal` instead of `str` is detected as a type error;
  - stage visibility and evaluator isolation hold;
  - snapshot regression labelling holds.
- **Earlier experiments:** `invoice-gen/1` fixtures still match experiment 004's exported hashes, and incident prompts are byte-identical.

## Arms and settings

- **Comparison:** CLM (optional, model-controlled context editing, with the usual reminders and no forced edits or helpers) against `token-tail/1` with the coding summariser instruction. Prompts are unchanged from experiment 004 (`2026-10-04.1`).
- **Config:** `configs/exp005.toml`, which is experiment 004's configuration except:
  - **`max_calls` 45** (was 30): 6–8 stages need more write/test steps;
  - **`min_run_reserve_usd` 1.50** (was 0.75): a harder run costs more, so a run is not started without room to finish.
- **Unchanged from experiment 004:** `claude-opus-5-5`, effort `low`, the 8,000-token whole-request budget, a 70% pressure point, `max_output_tokens` 4,096, and token-tail ratios 0.15 / 0.25 / 0.50.
- **Prompt caching:** disabled; that is experiment 006.
- **Limits:** identical for both arms and both workload levels.

## Budget

- **Ledger at the start:** USD 16.213524 spent, ceiling USD 38.916744.
- **Authorised for experiment 005:** at most USD 30, covering calibration, evaluation, retries and any other live calls.
  - The ceiling is set once, explicitly, to **USD 46.213524** (spend at start + 30).
  - Previous entries are preserved and nothing is raised further automatically.
- **Calibration sub-limit:** USD 10.
- **If the budget runs out:** results are preserved and the comparison is reported incomplete.

## Calibration procedure, fixed before calibration

**Runs:**
- Each workload level gets four runs: both arms on `dev-1` and on `dev-2`, sequential, with the arm order alternating (summary first on `dev-1`, CLM first on `dev-2`).
- At most **8 calibration runs** in all, within USD 10.

**Assessment.** It is pooled over the 4 runs, never per arm:
1. **Harness fault:** for example evaluation errors, executor failures, repeated output truncation or repair loops, or accounting problems. Diagnose and fix the harness, record it, and do not escalate difficulty for this reason. A fix that needs reruns uses the same 8-run cap.
2. **Infeasible:** at least 3 of 4 runs do not submit, or no run passes at least 50% of its checks. Diagnose the cause, for example a limit or an unclear requirement. Do not escalate; report.
3. **Ceiling:** all 4 runs are strictly successful. Move to the harder variant and calibrate it the same way.
4. **Otherwise** the level is used for evaluation: feasible, with some correct behaviour and not all runs perfect.

**At the harder level**, outcome 3 or 2 means **stop before the evaluation** and report what prevented an informative experiment.

**Context management:** whether summaries or edits happen while coding work remains is recorded. It is not a condition on either arm, and edits and helpers are never forced.

## Planned evaluation, fixed before calibration

**Sample:**
- **Target:** `eval-1..6` at the chosen level × 3 repetitions × 2 arms = **36 runs**, sequential.
- **Order:** `--order balanced`. The arm that runs first alternates across instances and across repetitions within each instance, which gives 2:1 within an instance and 18:18 overall.
- **Cost rule:**
  - Estimate = mean calibration cost per run at the chosen level × runs × 1.25.
  - If the estimate for 36 runs exceeds the remaining authorisation (USD 30 minus calibration spend), use the fallback `eval-1..4` × 3 × 2 = **24 runs**.
  - If neither fits, stop with preparation complete and report the estimate.

**Rules during the evaluation:**
- **Invalid runs:** runs with an infrastructure, executor or accounting status, or an evaluation error, are labelled invalid. They are kept and not replaced.
- **Halts:** a budget or accounting halt leaves the remaining cells missing, and they are reported.
- **No changes:** no reruns, no tuning after results, no sample expansion.

**Reporting:**
- **Primary outcome:** strict success (all hidden checks pass **and** the agent submitted), per arm, per instance and per run.
- **Secondary outcomes:**
  - check pass rate by category, boundary checks, stale-rule errors, retained-rule failures and regressions (with snapshot evidence), type errors;
  - completion and failure reasons;
  - edits, summaries, overflows and recoveries, and their timing relative to remaining work;
  - calls, tokens, cost and elapsed time.
- **Interpretation:** repeated runs of one instance are not independent task designs. Findings are exploratory.

## Calibration record (development instances only)

**Before calibration:**
- **Ceiling:** the ledger ceiling was set once, as authorised, from USD 38.916744 to **USD 46.213524** (spend at the change: USD 16.213524). The change is recorded in `ceiling_history`, and all 684 prior entries are unchanged.
- **Source:** clm-lib HEAD `817198b` plus uncommitted changes, patch SHA-256 `8325b1e23ce4deded81835cf0eaaae40a11c3debc87a56ee8ed4c04da39dc76f`.
- **Run settings:** each calibration run used `clm-lib --config configs/exp005.toml run` with `--max-usd 3`.

### Base workload (`coding2-dev-*`, 6 stages)

| # | Run | Instance | Arm | Result | Calls | Cost (USD) | Management observed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1a | `20261004T224741-summary-coding2-dev-1-7820` | dev-1 | token-tail/1 | strict, 40/40 checks | 17 (2 summary) | 0.410 | 2 summaries, the first at step 9 (stage 4 of 6), followed by 7 action steps (4 executions, 2 advances) |
| B1b | `20261004T224934-clm-coding2-dev-1-e39f` | dev-1 | CLM | strict, 40/40 | 17 | 0.308 | 5 accepted edits, the first effective at step 3 (stage 1), followed by 15 action steps (9 executions, 5 advances); pressure never reached |
| B2a | `20261004T225109-clm-coding2-dev-2-e628` | dev-2 | CLM | strict, 42/42 | 16 | 0.293 | 5 accepted edits, the first effective at step 5 (stage 2), followed by 12 action steps (7 executions, 4 advances) |
| B2b | `20261004T225247-summary-coding2-dev-2-4c47` | dev-2 | token-tail/1 | strict, 42/42 | 20 (3 summary) | 0.494 | 3 summaries, the first at step 8 (stage 3 of 6), followed by 10 action steps (6 executions, 3 advances) |

**Findings:**
- No harness faults: no truncation, repairs, retries, overflows, recoveries or evaluation errors.
- Context management happened while substantial work remained in all 4 runs.
- All snapshot checks passed at every stage.

**Decision:** rule 3 (ceiling) applies, since all 4 runs were strictly successful. The protocol therefore moves to the predefined **harder variant** (`coding2h-*`), with no other change. Base calibration spend was USD 1.505.

### Harder variant (`coding2h-dev-*`, 8 stages)

| # | Run | Instance | Arm | Result | Calls | Cost (USD) | Management observed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1a | `20261004T225529-summary-coding2h-dev-1-caad` | dev-1 | token-tail/1 | strict, 52/52 checks | 24 (4 summary) | 0.645 | 4 summaries, the first at step 8 (stage 4 of 8), followed by 13 action steps (8 executions, 4 advances) |
| H1b | `20261004T225826-clm-coding2h-dev-1-ce5f` | dev-1 | CLM | strict, 52/52 | 25 | 0.469 | 7 accepted edits, the first effective at step 3 (stage 1), followed by 23 action steps (15 executions, 7 advances); pressure never reached |
| H2a | `20261004T230046-clm-coding2h-dev-2-5f50` | dev-2 | CLM | strict, 52/52 | 22 | 0.435 | 6 accepted edits, the first effective at step 5 (stage 2), followed by 18 action steps (11 executions, 6 advances) |
| H2b | `20261004T230250-summary-coding2h-dev-2-05a6` | dev-2 | token-tail/1 | strict, 52/52 | 25 (4 summary) | 0.666 | 4 summaries, the first at step 8 (stage 4 of 8), followed by 14 action steps (9 executions, 4 advances) |

**Findings:**
- No harness faults.
- Every category passed in every run: retained, replaced, kept_part, interaction and final-stage (refund) checks, and all 17 boundary checks.
- There were no stale rules, type errors or retained-rule failures.
- All snapshot checks passed at every stage.
- Context management happened while substantial work remained.
- Visible tests failed only once in the 8 calibration runs (H1b, step 13, stage 5: 6 of 14 tests after the tier change). The next step fixed it. Otherwise the agents' code passed the visible tests on the first run at each stage.

**Decision:** at the harder level, rule 3 (ceiling) means **stop before the evaluation**: universal perfect scores at both predefined levels.
- **No evaluation run** was made, and evaluation instances `coding2*-eval-*` were never run.
- **Calibration spend** was USD 3.719 (base 1.505 + harder 2.214) of the USD 10 sub-limit; 8 of 8 calibration runs were used.
- **Ledger after calibration:** USD 19.933 spent of the USD 46.214 ceiling. The unused experiment-005 authorisation (about USD 26.28) is not carried over to other work.
