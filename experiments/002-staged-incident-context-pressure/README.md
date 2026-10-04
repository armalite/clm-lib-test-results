# 002 – Staged incident under context pressure

## What problem did we test?

An AI agent investigates a simulated production outage where **new evidence arrives over time**, in three stages, as it would during a real incident. The agent asks for the next stage when it is ready.

- **Stage 1:** a new software build is deployed and requests start timing out. The build's release notes contain about 15 routine items. One of them quietly lowers the database connection-pool size; that is an easy-to-miss **early fact**.
- **Stage 2:** an on-call engineer fixes the timeout, so the obvious first theory is now **out of date**. Errors continue, now from the database pool running out of connections.
- **Stage 3:** someone raises the pool size part-way, which **supersedes** the earlier value. Errors persist. A proposal to raise it further was never applied, which is a distractor.

To succeed, the agent must:
- keep track of what still matters while its context fills up;
- diagnose the incident as it stands at the end (the database pool, not the timeout);
- report the **current** pool size;
- give a remedy;
- cite three pieces of evidence: the current symptom, the record that set the current value, and the stage-1 release-note line that started the problem.

Earlier files stay readable throughout, and future stages are not visible until released.

The question: when useful information has to survive sustained context pressure, does letting the model **edit its own context** (CLM) change results or cost compared with **automatic summarisation**?

## How did the comparison work?

- **Summary baseline (our implemented policy):** when a model request reaches about 70% of its 8,000-token budget, Claude is asked, in a separate call, to summarise the older working-context entries, and the summary replaces them. The 4 most recent entries are kept unchanged. If the summary still doesn't fit, it gets one retry, then the run stops with an explicit "context overflow".
- **CLM:** the same model, budget, tasks, evidence schedule and tools. The model may rewrite its working-context file with code it writes, whenever it chooses, and receives a reminder at the same 70% point.
  - Editing was **optional**. Creating reusable helpers was **not requested**.
  - An edit made during one step takes effect in the **next** model request.
- **Setup, the same for both:**
  - `claude-opus-5-5` at effort `low`;
  - an 8,000-token budget for each model request (instructions, task and working context together);
  - at most 20 model calls per run.
- **Runs:** 3 instances of one synthetic task family × 2 repetitions × 2 approaches = **12 comparison runs**, one after another, alternating which approach ran first.
  - Settings, task instances and code were frozen before the comparison.
  - Two earlier calibration runs used different instances, to confirm both methods would actually activate.
- **Scoring:** a run is a **strict success** only if it gets the diagnosis, remedy and exact current value right **and** cites all three evidence types, with each citation within the allowed range of at most 20 lines.

## What happened?

**Both context-management methods were active in every run.**
- Every CLM run edited its context: 2–6 accepted edits per run, 20 in total, none rejected. The first edits were made during stage 1, at steps 2–4, and took effect in the next request.
- Every baseline run summarised. 23 summary calls produced 20 accepted summaries; the other 3 attempts were too large to fit, all in the run that overflowed.
- No reusable helper was created in any run.

**Outcomes**, 6 runs per approach:

| | Summary baseline | CLM |
| --- | --- | --- |
| **Completion:** reached a final answer | 5 of 6 | 6 of 6 |
| **Strict success:** met every requirement | 4 of 6 | 6 of 6 |
| **Factual correctness** (of completed answers): diagnosis, remedy and current value all correct | 5 of 5 | 6 of 6 |
| Cited the stage-1 early fact (of completed answers) | 5 of 5 | 6 of 6 |

**Efficiency**, per-run averages (totals for all 6 runs in brackets):

| | Summary baseline | CLM |
| --- | --- | --- |
| Cost per run (USD) | 0.372 (total 2.229) | 0.231 (total 1.386) |
| Elapsed time per run | 99 s (total 595 s) | 56 s (total 338 s) |
| Model calls per run | 12.0: 8.2 task + 3.8 summary (total 72) | 10.2, all task (total 61) |
| Cumulative input tokens per run* | 56,000 | 44,060 |
| Cumulative output tokens per run | 7,377 | 2,741 |
| Largest single request (input tokens) | 6,346 | 6,005 |

\* Cumulative input tokens add up the input of **every** model call in a run. Most of the context is re-sent on each call, so this is much larger than any single request; it is not the size of one context window. The last row shows the largest single request, which stayed under the 8,000-token budget in every run. The runtime makes its budget decisions using its own calibrated token estimate. Its internal hard limit (7,000 tokens, which keeps 1,000 in reserve) is therefore applied to that estimate, and one provider-reported request reached 7,280 tokens.

**The two baseline failures, plainly:**
1. **Context overflow** (`staged-eval-1`, repetition 2). One recent observation of 6,105 characters sat among the four entries the baseline always keeps unchanged. Even after summarising everything older (and one retry), the request couldn't fit the budget, so the run stopped without an answer. The policy behaved as designed.
2. **Citation outside the allowed range** (`staged-eval-2`, repetition 2). The answer was correct: the right diagnosis, remedy and current value, and a correct citation of the stage-1 fact. But its symptom citation covered 24 lines where the task allows at most 20. The range did contain the right lines. The rule was the same for both approaches and was not relaxed afterwards.

**Matched pairs**, same instance and repetition:

| Instance | Repetition | Summary baseline | CLM | CLM cost minus baseline cost (USD) |
| --- | --- | --- | --- | --- |
| staged-eval-1 | 1 | success, 0.434 | success, 0.247 | −0.187 |
| staged-eval-1 | 2 | context overflow, 0.344 | success, 0.231 | −0.113 |
| staged-eval-2 | 1 | success, 0.470 | success, 0.223 | −0.247 |
| staged-eval-2 | 2 | citation out of range, 0.350 | success, 0.196 | −0.154 |
| staged-eval-3 | 1 | success, 0.256 | success, 0.205 | −0.051 |
| staged-eval-3 | 2 | success, 0.375 | success, 0.284 | −0.092 |

**Example of an edit and the next request** (run `20261004T081056-clm-staged-eval-1-ed3b`):
- During step 2, still in stage 1, the model's code replaced its first action and a 6,106-character observation (6,606 characters together) with one 329-character note. The note kept the exact early fact, starting: `Stage1: release notes stage-1/deploy/release-notes-8.19.0-ff7b.md:9 risk-score timeout 2500->800; :15 db.pool.max_size 60->14 …`.
- The step-3 request began with exactly that note, and its size fell from 6,017 to 4,017 input tokens.
- The model kept rewriting the note as new stages arrived. Its final answer cited `release-notes-8.19.0-ff7b.md:15` and the current value 24.

## What do the results tell us?

These are promising results from a **small synthetic pilot against this particular baseline**:
- CLM completed and strictly succeeded in every run.
- It cost about **38% less** on average, took about **43% less** time, and was cheaper in every matched pair.
- **Where the saving came from:** mostly from not needing separate summarisation calls, which made up 46% of the baseline's cost. CLM actually made *more* task calls and code executions than the baseline.
- **Where the quality gap came from:** the baseline's two failures were mechanical, an overflow and an over-wide citation. Every completed answer, in both approaches, had the correct diagnosis, remedy and current value, and cited the early fact.

So **better factual reasoning or memory retention was not demonstrated.** What the pilot does suggest is that, on this kind of task, letting the model manage its own context avoided this baseline's summarisation overhead and its overflow failure mode.

## What remains untested?

- **Statistical confidence:** there are only 6 runs per approach, with 3 instances of one synthetic task family repeated twice.
- **Stronger baselines:** for example, a token-limited recent tail, incremental summaries or a cheaper summarising model.
- **Other conditions:** other task families, models and effort levels.
- **Helpers:** whether CLM's behaviour includes helper creation when not prompted. It was neither required nor observed here.

## Where is the evidence?

- `protocol.md`: the plan written before the runs, the two calibration runs, and confirmation that nothing changed after the comparison.
- `report.md` and `metrics.json` / `metrics.csv`: every run's numbers.
- `manifest.json`: run roles, settings, source commit, the saved source patch and checksums.
- `artifacts/runs/evaluation/`: the 12 comparison runs, with requests, context revisions, model-written code and scores.
- `artifacts/runs/calibration/`: the 2 calibration runs.
- `artifacts/comparisons/20261004T080858/`: the comparison record, with its frozen settings and the exact source patch used.
  - **Provenance note, added later:** that record's `frozen.generator_version` field reads `incident-gen/1`. This is a recording mistake: the field was filled from the single-stage generator's constant. The runs themselves used `staged-incident-gen/1`, as each run's `run.json` (`generator_version`) and `manifest.json` show. The recorded evidence is left unchanged; experiment 003 onwards records each task's actual generator version.
- `artifacts/fixtures/`: the task files, all three stages.
