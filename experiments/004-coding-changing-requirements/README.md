# 004 – Coding with changing requirements

**Status: complete.** This was a small exploratory comparison: 4 evaluation instances × 3 repetitions × 2 approaches = 24 runs.

## What problem did we test?

An AI agent writes and maintains a small Python package: an **invoice calculator** that computes subtotal, discount, tax and total, and formats money amounts. The requirements arrive in **four stages**, as they might over a project's life.

- **Stage 1** gives the API, the base calculation and a few rules, for example "round each line to 2 decimals", "tax is 10%" or "reject invalid quantities".
- **Later stages list only what changed.** Some add new rules, for example tier discounts, bulk-line discounts, tax exemption and money formatting. Others **replace** an earlier rule, for example "tax now depends on the region" or "line amounts are no longer rounded; use banker's rounding at the end". Every rule that is not replaced **stays in force**, even though it is never mentioned again.

So the agent has to keep track of which rules are current, which were superseded, and what it has already built, while its working context fills with code, test output and requirement updates.

- **What it can see:** a read-only folder holds each stage's requirements, which stay readable, and a visible `unittest` suite. The suite is updated at each stage, so visible tests never demand a superseded rule.
- **How it works:** the agent edits its own copy of the package and runs the tests from code it writes, inside a sandbox. It asks for each next stage when ready, and submits when all four are out.
- **How it is scored:** afterwards, **independent evaluator checks**, never visible to the agent, test the final requirements on different inputs. Each check is tagged:
  - **retained:** an earlier rule still in force. A failure is a **regression**.
  - **replaced:** a superseded rule must behave the new way. Reproducing the old result counts as a **stale rule**.
  - **final_stage:** a rule introduced in the last stage.
  - The submitted code is evaluated in a fresh sandbox; model-written code never runs on the host.

The question: **does model-controlled context editing help an agent implement changing requirements while preserving existing functionality?**

## How did the comparison work?

- **Summary baseline:** `token-tail/1`, the robust policy from experiment 003. When a model request reaches about 70% of its 8,000-token budget, older entries are replaced by a summary written by the same Claude model, with instructions specific to coding (keep the rules in force, superseded rules, files, test status and remaining work). Recent entries are kept up to a token allowance.
- **CLM:** the same model, budget, tasks, tools and access. The model may rewrite its working-context file with its own code, whenever it chooses, and gets a reminder at the same 70% point. Editing was optional and helpers were not requested.
- **Setup, the same for both:**
  - `claude-opus-5-5` at effort `low`;
  - an 8,000-token budget per model request (instructions, task and working context together);
  - at most **30** calls and **4,096** output tokens per call. Experiment 003 allowed 20 and 2,048; this four-stage coding task needs room to write and fix code.
  - **Prompt caching was not used.** It should be tested separately.
- **Instances:** 4 evaluation instances, each with a **different schedule** of which rules are added, replaced or kept. Examples:
  - `coding-eval-3` replaces rounding, tax, money formatting and bulk discounts;
  - `coding-eval-2` keeps rounding, tax and bulk discounts unchanged throughout.
- **Runs:** 3 repetitions per instance and approach: **24 runs**, one after another, alternating which approach ran first. Settings, instances, scorer and the exact source were frozen first.
- **Shared limitation:** all instances come from **one generator and one application scenario**.

## What happened?

**Both approaches managed context while coding work remained, and both succeeded every time.**
- **Baseline:** summarised in every run, 1–3 times (20 summaries from 20 summary calls), first at steps 6–8 (stages 2–4), followed by 2–7 more action steps.
- **CLM:** edited its context in every run, 2–3 times (33 accepted edits, none rejected), first taking effect at steps 3–6 (stages 1–2), followed by 6–10 more action steps. CLM never reached the 70% pressure point.
- **No problems:** no overflows, recoveries, retries, repairs or early submissions in either approach.

**Correctness**, 12 runs per approach; checks are parts of a run, not separate samples:

| | Robust summary baseline | CLM |
| --- | --- | --- |
| Completed (submitted) | 12 of 12 | 12 of 12 |
| Strict success (every evaluator check passed) | 12 of 12 | 12 of 12 |
| Evaluator checks passed, all runs | 336 / 336 | 336 / 336 |
| Retained-rule checks (regressions) | 108 / 108 (0 regressions) | 108 / 108 (0 regressions) |
| Replaced-rule checks (stale rules) | 168 / 168 (0 stale) | 168 / 168 (0 stale) |
| Final-stage-rule checks | 60 / 60 | 60 / 60 |

**Efficiency**, per-run averages (totals for all 12 runs in brackets):

| | Robust summary baseline | CLM |
| --- | --- | --- |
| Cost per run (USD) | 0.302 (total 3.626) | 0.225 (total 2.701) |
| Elapsed time per run | 79 s (total 942 s) | 67 s (total 804 s) |
| Model calls per run | 12.0: 10.3 task + 1.7 summary | 11.3, all task |
| Code executions per run | 6.3 | 7.3 |
| Cumulative input tokens per run* | 47,744 | 38,050 |
| Cumulative output tokens per run | 5,560 | 3,645 |
| Cache read / write tokens | 0 / 0 | 0 / 0 |
| Largest single request, average (input tokens) | 5,425 | 4,747 |

\* Cumulative input tokens add up the input of every model call in a run, so they are much larger than any single request.

**By instance**, averages over 3 runs each:

| Instance | Baseline cost / time / summaries (all 3 runs) | CLM cost / time / edits (all 3 runs) |
| --- | --- | --- |
| coding-eval-1 | USD 0.248 / 65 s / 3 | USD 0.241 / 88 s / 7 |
| coding-eval-2 | USD 0.286 / 74 s / 4 | USD 0.213 / 58 s / 9 |
| coding-eval-3 | USD 0.359 / 92 s / 7 | USD 0.212 / 59 s / 9 |
| coding-eval-4 | USD 0.315 / 83 s / 6 | USD 0.234 / 63 s / 8 |

- **Matched pairs:** CLM was cheaper in **11 of 12**. The exception, `coding-eval-1` repetition 3, cost USD 0.265 against 0.234.
- **Elapsed-time outlier:** one CLM run (`coding-eval-1` repetition 3) took 137 s because a **single model response took 77 s**; its code executions took 1–4 s. Without it, CLM's mean elapsed time would be 61 s.
- Per-run results are in `report.md` and `metrics.csv`.

**An edit and the next request** (CLM, `coding-eval-3` repetition 1, run `20261004T111927-clm-coding-eval-3-6f2e`):
- At step 3, still in stage 1, the model's code replaced its first four entries (3,237 characters, mostly the printed stage-1 requirements and its first test run) with one 207-character note:
  `Stage1 implemented in invoice/core.py: _r half-up, discount_rate(lines,customer,subtotal)=0, tax_rate(customer)=0.10, format_money with PREFIX dict (NZ$,A$,US$), neg sign before prefix, ValueError otherwise.`
- The step-4 request (`requests/0004.json`) began with exactly that note, followed by the step's own action, output and receipt.
- The model rewrote the note after stages 2 and 3, each time again removing about 3.1–3.3K characters of history.
- The note recorded *what the code does*, not the requirement text. The requirements stayed in readable files and in the code itself.

## What do the results tell us?

- **Correctness:** **the same.** Both approaches implemented every final requirement in every run. Neither regressed a retained rule or kept a superseded one.
  - On this task and model, **no benefit of CLM for correctness, regressions or stale rules was observed**, because there were no failures to reduce.
  - This does not show better memory or retention in either approach.
- **Efficiency:** **CLM was cheaper.** It cost about **25% less** per run on average and was cheaper in 11 of 12 matched pairs.
  - Most of the gap is the baseline's separate summary calls: they cost USD 0.888, against a total gap of USD 0.925. Leaving them out, the two approaches spent almost the same on task calls (USD 2.74 vs 2.70).
  - The gap was smallest on the instance where the baseline summarised least (`coding-eval-1`), and largest where it summarised most (`coding-eval-3`). This is consistent with that explanation, which is inferred from cost accounting and not separately tested.
- **Elapsed time:** about 15% lower for CLM on average, partly masked by one slow provider response.
- **Relation to experiments 002 and 003:** the pattern resembles experiment 003 on a different task family. It is not a matched comparison.
  - Against a robust baseline, quality is equal.
  - CLM's remaining advantage is efficiency, from not paying for separate summarisation.

## What remains untested?

- **Harder coding work:** this task proved too easy to separate the approaches on correctness, since every run succeeded. Longer projects, larger code bases, tighter budgets or less capable models might separate them.
- **Generality:** one application scenario and one generator. 4 instances × 3 repetitions is still a small sample, so no statistical claims are made.
- **Prompt caching:** it might narrow or change the cost gap (summary calls and repeated context both affect it). It was not tested here.
- **Other baselines and models:** other summary policies, models, efforts and budgets.

## Where is the evidence?

- `protocol.md`: the design written before the runs, the calibration record, the frozen settings and post-comparison notes.
- `report.md` and `metrics.json` / `metrics.csv`: every run's numbers, including per-category check results.
- `manifest.json`: run roles, settings, source commit, the saved source patch and checksums.
- `artifacts/runs/evaluation/`: the 24 comparison runs. Each `evaluator/` folder holds the hidden checks (`truth.json`), the recorded submission (`submission/`), the evaluator output and the score.
- `artifacts/runs/calibration/`: the 4 calibration runs.
- `artifacts/comparisons/20261004T111345/`: the comparison record with frozen settings and the exact source patch.
- `artifacts/fixtures/`: every stage's requirement documents and the final visible tests.
