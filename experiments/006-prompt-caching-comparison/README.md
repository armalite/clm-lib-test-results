# 006 – Prompt-caching comparison

**Status: complete.** This was an exploratory comparison: 4 task instances × 3 repetitions × 4 conditions = 48 evaluation runs, plus 4 calibration runs.

## What did we test?

- **Question:** in experiments 003 and 004, CLM was about 25% cheaper than the robust `token-tail/1` summary baseline, and the gap matched the baseline's spending on separate summary calls. Those runs used no prompt caching. Does CLM keep its cost and speed advantage when **both** approaches can use the provider's ordinary prompt caching?
- **Four conditions:** {summary baseline, CLM} × {caching off, caching on}.
- **Scope:** ordinary API prompt caching (`cache_control`), not the CLM paper's separate suffix-cache reuse optimisation.
- **Workload:**
  - the experiment-004 coding task: an invoice package whose requirements are added and replaced over four stages (`invoice-gen/1`, scorer `invoice-checks/1`);
  - its four evaluation instances `coding-eval-1..4`, **reused** with fresh runs. These are an established workload, not new unseen instances.
- **Settings, the same in all conditions:**
  - `claude-opus-5-5` at effort `low`;
  - an 8,000-token budget per model request;
  - up to 30 calls and 4,096 output tokens per call;
  - the same tools, prompts and request layout.

## How caching was set up

- **A new, shared request layout (`blocks/1`):**
  - **Before,** each request had the changing runtime status **before** the working context, so nothing after it could be reused.
  - **Now,** each request is split into text blocks in a fixed order: the stable task first, then **one block per working-context entry**, then the changing runtime status last.
  - **The same in all four conditions,** including caching-off, so the layout change is not confused with caching.
  - **Content:** the model sees the same section content; only the order changed.
- **Caching on:**
  - **What is marked:** two explicit 5-minute cache breakpoints on every task and summary request, one at the end of the stable task block and one at the end of the last context entry. The status block is never cached.
  - **How reuse works:** as the context grows, each request can read the previous request's prefix and pays to write only what was appended.
  - **After a change:** when a CLM edit or a baseline summary rewrites earlier entries, only the part before the change can be read.
- **Caching off:** the identical requests, with no cache markers.
- **No padding:** the stable prefixes (about 680–1,400 tokens) already exceed the 512-token minimum.
- **Run isolation:** every request in a run starts with a fixed-length random tag (`run-ref:` plus 32 random hex characters), stable within the run, in **all four** conditions.
  - **Why it works:** caching matches only an exact prefix from the start of the prompt, and every breakpoint lies after the tag. So a run can only reuse its own content and starts with a cold cache.
  - **What it contains:** no task information.
  - **Check:** all 52 runs' first calls read 0 cached tokens.
- **Order:** each instance-and-repetition block ran its four conditions sequentially in a Williams order, so each condition ran 3 times in each position.

## What happened?

All 48 runs completed and were valid. There were no failures, overflows, recoveries, retries, repairs or missing cells.

| | Baseline, caching off | Baseline, caching on | CLM, caching off | CLM, caching on |
| --- | --- | --- | --- | --- |
| Strict success | 12 of 12 | 12 of 12 | 12 of 12 | 12 of 12 |
| Evaluator checks | 336 / 336 | 336 / 336 | 336 / 336 | 336 / 336 |
| **Mean cost per run (USD)** | **0.305** | **0.208** | **0.223** | **0.136** |
| of which summary calls | 0.069 | 0.076 | — | — |
| Mean elapsed per run | 78 s | 79 s | 62 s | 63 s |
| Mean provider time per run | 66 s | 66 s | 50 s | 51 s |
| Mean calls per run | 12.0 (1.6 summary) | 12.1 (1.7 summary) | 11.2 | 11.1 |
| Context management | 19 summaries | 20 summaries | 41 edits | 41 edits |
| Mean uncached input tokens | 48,340 | 1,182 | 37,795 | 1,199 |
| Mean cache reads / writes | 0 / 0 | 30,345 / 17,518 | 0 / 0 | 25,176 / 10,690 |
| Share of input read from cache | — | 62% | — | 68% |
| Mean output tokens | 5,577 | 5,454 | 3,575 | 3,626 |

**Notes on the table:**
- **Totals:** costs over 12 runs were USD 3.66, 2.49, 2.67 and 1.63 respectively.
- **Input:** total input per run was about the same with and without caching (about 49K tokens baseline, 37K CLM); caching changes how it is billed.
- **Management happened while work remained:**
  - the baseline first summarised at stage 2–4 of 4, with 3–7 action steps after;
  - CLM first edited at stage 1–2, with 5–12 action steps after.

**CLM against the baseline:**

| Comparison (12 matched blocks) | Cost | Elapsed time |
| --- | --- | --- |
| Caching **off** | CLM **27% cheaper** (USD 0.223 vs 0.305); cheaper in 11 of 12 blocks | CLM **20% faster** (62 s vs 78 s); faster in 10 of 12 |
| Caching **on** | CLM **35% cheaper** (USD 0.136 vs 0.208); cheaper in 12 of 12 blocks | CLM **20% faster** (63 s vs 79 s); faster in 9 of 12 |

**Caching within each approach:**

| Approach | Cost with caching on vs off | Elapsed time |
| --- | --- | --- |
| Baseline | **32% cheaper**; cheaper in 12 of 12 blocks | about the same (+1%) |
| CLM | **39% cheaper**; cheaper in 12 of 12 blocks | about the same (+1%) |

Percentages are ratios of the condition means. The mean paired differences are similar: −31% and −25% for CLM against the baseline with caching on and off, and −33% and −39% for caching on against off within the baseline and CLM.

**By instance (mean cost, USD):**

| Instance | Baseline off | Baseline on | CLM off | CLM on |
| --- | --- | --- | --- | --- |
| coding-eval-1 | 0.255 | 0.164 | 0.249 | 0.127 |
| coding-eval-2 | 0.290 | 0.179 | 0.212 | 0.123 |
| coding-eval-3 | 0.334 | 0.231 | 0.218 | 0.153 |
| coding-eval-4 | 0.341 | 0.255 | 0.213 | 0.141 |

## Where the difference comes from

- **Summary calls barely benefit from caching:**
  - **Why:** a summary request has its own instructions, so the **first** summary in a run has nothing cached to read.
  - **Observed:** 12 of the 20 summary calls read nothing. The other 8 (later summaries) read only the stable summariser prefix, about 800 tokens. Summary calls mostly *write* cache (about 4,000 tokens each, at 1.25× the input price).
  - **Effect on cost:** summary calls cost slightly *more* with caching on (USD 0.076 vs 0.069 per run), so their share of the baseline's cost rose from 23% to 37%.
- **Task calls cost about the same:** with caching on, the baseline's task calls cost USD 0.131 per run and CLM's 0.136. CLM's whole advantage with caching comes from not making separate summary calls. Without caching, CLM's task calls were also slightly cheaper (USD 0.223 vs 0.236).
- **Edits and summaries both cut reuse, but differently:**
  - **After a CLM edit:** the next request read on average 1,723 tokens (the stable prefix) and wrote 1,167. In an ordinary growth step it read 3,100 and wrote 674. CLM edited often (41 edits over 12 runs), each time shortening the context.
  - **After a baseline summary:** the next request read 1,429 and wrote 2,339, against 3,850 read and 658 written in ordinary steps.
  - **"Lost" reuse** (a descriptive figure, not an exact causal measurement): the previous request's size minus what was read afterwards averaged about 2,100 tokens per CLM edit and 3,850 per baseline summary.
- **Time:** caching did not measurably change elapsed time on these short requests (at most about 6,500 tokens). CLM's time advantage comes from fewer output tokens and no summary calls.

## Examples of observed reuse (caching on, instance `coding-eval-3`, repetition 1)

**A CLM edit** (run `20261004T235401-clm-cacheon-coding-eval-3-1fc1`):
- At step 2, the model's code replaced its first two entries (2,625 characters: its step-1 code and output, which listed and printed the task files) with a 193-character note.
- **The step-3 request:**
  - It repeated the previous request only up to the stable prefix: `common_blocks` 3 (run tag, system prompt, task), with the first changed block being the first context entry.
  - It **read 1,721** cached tokens (the stable prefix), **wrote 1,164** (the note plus the new entries) and paid uncached for 108 (the status).
- **Step 4** grew normally again: read 2,885, wrote 473.
- The model kept editing every one to three steps, so the read drop to the stable prefix recurs through the run.

**A baseline summary** (run `20261004T235526-summary-cacheon-coding-eval-3-0cce`):
- **Before the summary:** at step 5 the action call read 4,662 and wrote 473.
- **The step-6 summary call** (replacing 8 older entries) read 0 and wrote 4,522; nothing with the summariser prefix existed yet.
- **The next action request** read 1,428 (stable prefix) and wrote 2,271.
- **The run's second summary** (step 10) read 815 tokens: the summariser prefix written by the first summary call.

Per-request evidence is in each run's `requests/*.json` (`meta.prefix`) and `events.jsonl` (`response.usage`, `latency_s`).

## What do the results tell us?

- **CLM's efficiency advantage persisted, and widened, with prompt caching** on this workload:
  - **Cost:** 35% cheaper with caching on, against 27% with caching off. CLM was cheaper in all 12 matched blocks with caching on.
  - **Time:** about 20% faster either way.
- **Caching helped both approaches substantially** (32% and 39% cheaper), with no accuracy change.
- **Why the gap widened:** caching made task calls cheap for both, while the baseline's summary calls stayed mostly uncacheable. They became a larger share of its cost.
  - This follows from the shared layout and caching policy (summaries keep their own instructions).
  - A different design could change it, for example summary requests that reuse the action prefix. That design was deliberately not used, because it changes the baseline. It is untested.
- **CLM's frequent edits did cost cache reuse,** each time back to the stable prefix. This did not offset the absence of summary calls here.

**Limits of these conclusions:** they apply to this model, this one synthetic coding workload (4 reused instances), this request layout, explicit 5-minute breakpoints and a cold cache per run. 12 matched blocks per comparison are not independent task designs. The findings are exploratory.

## Relation to earlier experiments

Experiment 004's caching-off numbers (CLM USD 0.225 vs baseline 0.302) are close to this experiment's fresh caching-off control (0.223 vs 0.305), but they are context only, not the control. That experiment used the old layout.

## Deviations and limitations

- **Workload reuse:** the evaluation instances were reused from experiment 004.
- **Post-evaluation change (reporting only):** the report's edit-evidence parser could not read the new block layout. It was fixed after the evaluation, with a test, and changes no run or score.
- **Layout change:** `blocks/1` moves the runtime status after the working context in all conditions. Its effect on behaviour was not separately measured, since there is no single-user-layout control in this experiment. The caching-off results are similar to experiment 004's.
- **Latency:** provider latency is per call, measured client-side around the API request. The slowest single call was 14.5 s; no outliers were removed.
- **Untested:** 1-hour TTL, cross-run cache sharing (deliberately prevented), other models and other workloads.

## Where is the evidence?

- `protocol.md`: the design written before the runs, the provider facts checked, the calibration record and decisions, and the frozen settings.
- `report.md` and `metrics.json` / `metrics.csv`: every run.
  - The condition is in the `request_layout`, `prompt_caching`, `cache_ttl` and `run_isolation` columns.
  - There are per-kind cost, cache and latency columns, plus first-call cache reads.
- `manifest.json`: run roles, settings, provenance and checksums.
- `artifacts/runs/evaluation/` (48 runs) and `artifacts/runs/calibration/` (4 runs).
  - Run ids contain `cacheon` / `cacheoff`.
  - `run.json → request` records the layout, caching, TTL and run tag.
  - `summary.json → request` holds usage, cost and latency by call kind.
- `artifacts/comparisons/20261004T234408/`: the evaluation record with the frozen settings, the 48-row Williams schedule and the exact source patch. `artifacts/comparisons/20261004T233901/` is the calibration record.

**Spend:** USD 11.207 for this experiment (calibration 0.757, evaluation 10.450) of the USD 30 authorised. The ledger stands at USD 31.140 spent of a USD 49.933 ceiling. The unused USD 18.79 is not authorisation for other work.
