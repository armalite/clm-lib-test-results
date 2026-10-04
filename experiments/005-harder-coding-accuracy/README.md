# 005 – Harder coding accuracy comparison

**Status: stopped after calibration, as the protocol requires.** Both predefined workload levels gave strict success in **all 8 calibration runs** (4 per arm). Under the rule fixed before calibration, universal perfect scores at both levels mean the evaluation is not run, so there is **no evaluation comparison** and no evaluation instance was used.

## What problem did we test?

- **The task:** the experiment-004 coding scenario made harder. An agent writes a small Python package, an **invoice calculator**, while requirements arrive over **6 stages** (base workload) or **8 stages** (harder variant).
- **What changed from experiment 004:** the rules now **interact**, and later stages often change **only part** of an earlier rule.

The rules:
- **Bulk lines** (large quantities) get 10% off, and bulk lines are excluded from the customer's **tier discount**.
- **Shipping** (7.50 below 100.00) depends on the amount after discounts.
- **Tax** depends on the region, and later also applies to shipping.
- **Coupons** (harder variant) are applied after the tier discount, until a later stage moves them *before* it.
- **Refunds** (harder variant) recompute the invoice for the kept quantities with every rule in force.

**A concrete interacting change** (instance `coding2h-dev-1`):
- In **stage 2**, the agent is told "a line with qty ≥ 100 is a bulk line; its amount × 0.90", and the tier discount is introduced.
- **Stage 4** adds "bulk lines are not tier-eligible".
- **Stage 7** says only "a line is now a bulk line when qty ≥ 50. The 0.90 multiplier and everything else about bulk lines are unchanged."

So after stage 7, a 60-unit line gets 10% off but **loses** its tier discount. Its amount feeds the shipping threshold and the tax. A refund that returns 20 of the 60 units moves the line back under the threshold, so the kept line becomes tier-eligible again. Getting this right needs the stage-2, stage-4 and stage-7 rules together.

**Equal for both arms:**
- the code;
- every earlier requirement file (always rereadable);
- visible tests, rewritten at each stage for every rule then in force;
- the same tools.

**How it was scored:** hidden evaluator checks on different inputs, run on a copy of the submission in a fresh sandbox. The checks test:
- rules still in force from earlier stages (**retained**);
- changed behaviour, with detection of output that matches the old rule (**replaced**, stale rule);
- the unchanged part of a partially changed rule (**kept_part**);
- several rules at once (**interaction**);
- the last stage's new rule (**final_stage**);
- boundary inputs (thresholds, rounding ties, caps);
- exact return types (a `dict` of `str`, a `str`).

Copies of the workspace taken at each stage let a later failure of a retained rule be called a **regression** only if the rule had demonstrably worked earlier.

## How was it run?

- **Compared:** CLM (optional context editing) against the robust `token-tail/1` summary baseline.
- **Model and settings:** `claude-opus-5-5` at effort `low`, an 8,000-token budget per model request, and up to **45** calls (experiment 004: 30) and 4,096 output tokens per call. Prompt caching was not used.
- **Instances:** generator `invoice-gen/2`, scorer `invoice-checks/2`, one synthetic scenario.
- **Fixed in `protocol.md` before any live run:**
  - the workload, the harder variant and the rule for moving between them;
  - the evaluator and its offline validation;
  - the sample (6 instances × 3 repetitions × 2 arms = 36 runs, fallback 24);
  - the budget (USD 30 for this experiment, USD 10 for calibration).
- **Calibration:** both arms on two development instances per level, sequential, alternating which arm ran first.

## What happened?

| Calibration level | Arm | Runs | Strict success | Hidden checks passed | Mean cost (USD) | Mean elapsed | Mean calls | Summaries / edits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Base (6 stages) | token-tail/1 | 2 | 2 of 2 | 82 / 82 | 0.452 | 118 s | 18.5 (2.5 summary) | 5 summaries |
| Base (6 stages) | CLM | 2 | 2 of 2 | 82 / 82 | 0.301 | 92 s | 16.5 | 10 edits |
| Harder (8 stages) | token-tail/1 | 2 | 2 of 2 | 104 / 104 | 0.655 | 175 s | 24.5 (4 summary) | 8 summaries |
| Harder (8 stages) | CLM | 2 | 2 of 2 | 104 / 104 | 0.452 | 127 s | 23.5 | 13 edits |

**Checks by category:**
- Every category passed in every run:
  - retained: 40 of 40 per arm;
  - replaced: 80 of 80;
  - kept_part: 34 of 34;
  - interaction: 24 of 24;
  - final-stage refunds: 8 of 8;
  - boundary: 55 of 55.
- Nothing failed in other ways: no stale rules, retained-rule failures or regressions, and no type errors.
- Every stage snapshot passed its checks.

**Completion and harness:**
- every run submitted;
- no overflows, recoveries, retries, repairs or premature final answers;
- no evaluation errors.

**Context management happened while work remained:**
- **Baseline:** it summarised 2–4 times per run, first at stage 3–4 of 6 or stage 4 of 8, followed by 7–14 more action steps.
- **CLM:** it edited its context 5–7 times per run (23 accepted, none rejected), with the first edit effective at stage 1–2, followed by 12–23 more action steps. CLM rarely reached the 70% pressure point.

**An actual CLM edit** (run `20261004T225826-clm-coding2h-dev-1-ce5f`):
- At step 18, at the end of stage 6 of 8, the model's code replaced seven entries (4,014 characters) with this 592-character note. The step-19 request (`requests/0019.json`) began with exactly that note, followed by only that step's action, output and receipt:

  > Stages1-6 done in invoice/core.py (tests pass): r2, _validate, tier_rate(gold .08, silver .02, platinum .10), tax_rate(NZ .15, US 0, else .10 by customer region), compute_invoice: amounts (bulk qty>=100 x0.90 before round), subtotal, elig=sum non-bulk amounts, discounts list [tier*elig], discount=sum r2, shipping 7.50 if subtotal-discount<100 else 0, tax=r2((subtotal-discount)*rate), total. Returns str dict subtotal/discount/shipping/tax/total. Read stage files for reqs. Stage6: no intermediate rounding, half-even final round of subtotal/discount/tax; tax on subtotal-discount+shipping.

- Stages 7 and 8 (coupons, refunds and two changes) were still to come.
- The note records what the code does, and points back to the requirement files.

**Visible tests rarely failed:**
- Across the 8 runs, the agents ran the visible tests 57 times. Only once did any test fail: run H1b, stage 5, 6 of 14 tests after the tier change, fixed in the next step.
- In every other case the code passed at the first run of each stage.

## What do the results tell us?

- **No informative accuracy comparison was possible at these difficulty levels.** Both approaches solved every calibration instance perfectly at both levels, so the planned evaluation was not run, as the protocol requires. **No claim is made about CLM's effect on correctness.** Equal perfect scores on 2 instances per level are not evidence of better or worse memory for either arm.
- **Why the task stayed easy (an interpretation, not separately tested):**
  - The agent kept the rules in its **code**: it updated one module stage by stage, so neither arm needed its working context to remember old requirements.
  - Earlier requirement files stayed **readable**, and changed rules **named the stage** they modified.
  - Visible tests were **rewritten for every rule in force** at each stage.
  - The model wrote the rules **correctly on the first attempt**; the visible tests only caught one transient mistake.
  - The 8,000-token budget **did not bind tightly**: the largest requests were about 5,300–6,500 tokens.
- **Efficiency (calibration only, 2 runs per arm and level, not an evaluation):** CLM was cheaper in all 4 matched calibration pairs, at about 31–33% lower mean cost. The pattern is consistent with experiments 003 and 004, but this sample is too small for a separate efficiency claim.

## What would make an accuracy comparison informative?

These are directions for a future design, **not tested here and not decided**:
- **Less visible test coverage:** for example, tests only for the rules changed in the current stage.
- **Requirements only in the working context:** released requirements that are not left as readable files. This directly tests what each arm retains.
- **A larger code base:** one where rereading the code is itself expensive in context.
- **A tighter request budget, or a smaller model or lower effort.**

Each changes what is being measured, and would need its own design and budget.

## What remains untested?

- CLM's effect on correctness under conditions where runs fail.
- Generality beyond one synthetic scenario and one generator.
- Prompt caching (planned as experiment 006).

## Where is the evidence?

- `protocol.md`: the design written before the runs, the offline evaluator validation, the calibration record and the stop decision.
- `report.md` and `metrics.json` / `metrics.csv`: every calibration run's numbers, including per-category and boundary check results.
- `manifest.json`: run roles, settings, source provenance and checksums. Its `exported_with.current_scorer` reads `invoice-checks/2`.
- `artifacts/runs/calibration/`: the 8 calibration runs. Each `evaluator/` folder holds:
  - the hidden checks and snapshot checks (`truth.json`);
  - the recorded submission (`submission/`);
  - the stage snapshots (`snapshots/`);
  - the evaluator output and the score.
- `artifacts/fixtures/`: every stage's requirement documents and visible tests for the 4 calibration instances.

**Spend:** USD 3.719 of the USD 30 authorisation, all calibration. The ledger stands at USD 19.933 spent of a USD 46.214 ceiling. The unused USD 26.28 is not authorisation for further experiments.
