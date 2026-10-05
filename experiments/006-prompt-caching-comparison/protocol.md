# 006 – Protocol

_Design finalised on 2026-10-05, before any experiment-006 live run. It replaces the draft plan committed earlier. Calibration, freezing and post-comparison notes are added below as they happen; earlier sections are not rewritten afterwards._

## Question

Does CLM's cost and speed advantage over the robust `token-tail/1` summary baseline persist when both approaches can use ordinary provider prompt caching?

**Scope:**
- This is the Messages API's `cache_control` prompt caching.
- It is **not** the CLM paper's separate suffix-cache reuse optimisation, which is out of scope.

## Conditions

| # | Approach | Prompt caching |
| --- | --- | --- |
| 1 | `token-tail/1` summary baseline | off |
| 2 | `token-tail/1` summary baseline | on |
| 3 | CLM | off |
| 4 | CLM | on |

**Shared across all four:** the same model, effort, task instances, tools, limits, request layout (`blocks/1`) and run-isolation convention. Only the necessary CLM/baseline differences remain: the system-prompt section on context management, editing versus automatic summaries, and the baseline's separate summary calls.

**Comparisons:**
- **Primary:**
  - CLM against the baseline with caching **on**;
  - the effect of enabling caching **within** each approach.
- **Also reported:** the fresh caching-**off** comparison.
- **Context only:** experiment 004's historical results, which are **not** the control group.

## Workload: reuse of an established task

- **Task:** the experiment-004 coding task (`invoice-gen/1`, scorer `invoice-checks/1`), unchanged.
- **Evaluation instances:** `coding-eval-1..4`. These are **instances already used in experiment 004**, run freshly here. This is a deliberate reuse of an established workload, not newly unseen instances.
- **Calibration:** development instance `coding-dev-1`.
- **Accuracy:** experiment 004 found both arms at 12/12. Equal, perfect accuracy is acceptable here, because this experiment measures efficiency.

## Settings

- **Config:** `configs/exp006.toml`. The settings are experiment 004's:
  - `claude-opus-5-5`, effort `low`;
  - an 8,000-token whole-request budget and a 70% pressure point;
  - `max_calls` 30 and `max_output_tokens` 4,096;
  - `token-tail/1` (ratios 0.15 / 0.25 / 0.50) and a 30 s execution timeout.
- **Prompt text:** prompt version `2026-10-04.1` is unchanged.
- **Additions:** the request layout and run isolation below, used in every condition.

## Provider facts checked (2026-10-05)

From the official prompt-caching documentation (platform.claude.com, `build-with-claude/prompt-caching`) and the installed SDK (`anthropic` 1.11.0, whose `cache_control` accepts `ttl: "5m" | "1h"`):

- **Minimum cacheable prompt** for `claude-opus-5-5`: **512 tokens**. Shorter prefixes silently do not cache.
- **TTL:**
  - The default is 5 minutes; 1 hour is optional.
  - The lifetime is measured from the start of the request that writes or reads the entry, and a read refreshes it at no cost.
- **Breakpoints:**
  - Up to 4 explicit `cache_control` breakpoints, or top-level automatic caching (a breakpoint on the last cacheable block).
  - A hit needs a 100% identical prefix up to and including the marked block. Prefixes are ordered tools → system → messages.
  - **Lookback:** each breakpoint looks back at most 20 blocks for an earlier write.
- **Usage fields:**
  - `input_tokens` is the **uncached remainder only**.
  - `cache_creation_input_tokens` counts tokens written; `cache_read_input_tokens` counts tokens read.
  - Total input = all three. `usage.cache_creation` splits writes by TTL.
- **Prices**, which match `configs/prices.toml` (retrieved 2026-10-04): input USD 4, 5-minute write USD 5 (1.25×), 1-hour write USD 8, read USD 0.20 (0.05×), output USD 20 per million tokens.
- **Isolation:** caches are isolated per workspace and never shared across organisations.
- **Concurrency:** an entry becomes readable once the first response begins.
- **Invalidation:** changing effort or thinking settings invalidates message caches. Both are fixed per run here.

## Request layout `blocks/1` (all four conditions)

**Before (`single-user/1`, experiments 001–005):**
- one system string;
- one user string ordered `<task>`, `<runtime_status>`, `<working_context>`.

The status changes on every call and sits **before** the context, so at most the system and task could ever repeat.

**Now (`blocks/1`, recorded as `request.layout` in every run and export row):**
- **`system`** is two text blocks:
  1. the run tag (below);
  2. the unchanged system prompt.
- **The user message** is text blocks:
  1. `<task>…</task>` plus the opening `<working_context>` tag (stable for the whole run);
  2. **one block per working-context entry** (the same escaped JSON line as before);
  3. last, `</working_context>` and the changing `<runtime_status>`.
- **Same content:** the model sees the same section content as before; only the order of `<runtime_status>` and `<working_context>` changed.
- **Unchanged mechanism:**
  - the CLM context file still alone decides the entries of the next request;
  - the ordering rule and validation are unchanged;
  - the task and protected instructions stay outside the file.
- **Summary requests (baseline):** the same convention. The run tag and the summariser instructions come first, then `<task>` plus the opening transcript tag, one block per entry to summarise, and last the closing tag with the length instruction. The summary text the summariser sees is byte-identical to the earlier layout.
- **Repair requests** append their notice as a final block.
- **Old layouts:** `single-user/1` remains the default for every earlier config. Their payloads are unchanged, as tested.

## Caching policy (identical for both approaches)

**When caching is on, explicit breakpoints with `ttl: "5m"` go on:**
1. **the task block.** The cached prefix is the run tag, system prompt and task. It stays readable whatever happens later in the context.
2. **the last working-context entry block** (or, in a summary request, the last entry to summarise). As the context grows, the next request's breakpoint finds this write within the 20-block lookback, because a step appends 2–3 entries.

**Rules:**
- **Never marked:** the status block, the repair notice and the summary length instruction.
- **Where caching applies:** every action, repair and summary call.
- **Caching off:** the same blocks, with no `cache_control` anywhere.

**Why explicit breakpoints rather than automatic caching:**
- Automatic caching marks the **last** block, which here is the per-call runtime status.
- Every request would then write an entry ending in a unique status, and the next request could not read it. Its context end sits at a different position, and the earlier write ended after the old status.
- That would pay write premiums with little reuse. The explicit pair (stable prefix plus growing tail) is the documented robust pattern for agent loops.

**No padding:**
- **Estimated stable prefixes:**
  - CLM about 4,100 characters (≈ 1,200–1,350 tokens);
  - baseline about 3,250 (≈ 930–1,080);
  - summariser about 2,400 (≈ 680–800).
- All exceed 512 tokens. No content is added to reach the minimum, and calibration records whether writes actually happen.

**Summary calls:**
- A summary call's prefix differs from the action prefix (different instructions). So the **first** summary in a run is expected to write and read nothing; later summaries can read the stable summariser prefix.
- This is reported as observed. No reuse is engineered between action and summary prompts, since that would change the baseline.

**TTL:**
- 5 minutes. Steps are seconds to about a minute apart, so a 1-hour TTL would only add write cost.

## Run isolation, the same in all four conditions

- **The tag:** the first system block of **every** request in a run (action, repair and summary) is `run-ref: <32 random hex characters>`. It is fixed-length, generated with `secrets.token_hex(16)` for each run, and stable within the run.
- **What it contains:** nothing about the task, mode, answers or hidden data. It is recorded in `run.json → request.run_tag`.
- **Why it isolates runs:**
  - Cache matching is an exact prefix match starting from the beginning of the prompt, and every breakpoint lies after the tag.
  - So every cache entry a run writes or reads includes its own tag, and runs cannot read each other's entries. No sleeps between runs are relied on.
- **Caching-off runs** carry a tag too, so the layout is identical.
- **Checks:**
  - Every run's first call records its cache reads (`request.first_call_cache`).
  - Any non-zero first-call read in calibration is investigated before evaluation; in the evaluation it is reported.

## Accounting and measurements

**Cost:**
- **Pricing:** cost = uncached × input + 5-minute writes × 1.25 input + 1-hour writes × 1-hour rate + reads × read rate + output × output rate.
- **No double-counting:** `input_tokens` excludes cached tokens.
- **Reservations:** each call's reservation assumes every input token at the dearest applicable input-side rate (5-minute write) plus `max_tokens` output. Each response is checked against the bound using total input (all three fields).
- **Ledger:** every call is recorded, including retries, summaries and calibration.

**Context budget:** whole-request size, pressure and the chars-per-token estimate all use **total** input including cached tokens. Cheap cached tokens still occupy context.

**Per run, measured:**
- strict success, check pass rate and completion;
- total cost, with action, repair and summary cost (`request.by_kind`);
- uncached input, cache writes, cache reads and output tokens, per kind;
- end-to-end elapsed time and summed provider-call latency (each response's `latency_s`);
- calls, edits, summaries, overflows and recoveries;
- the first call's cache usage.

**Reuse around edits and summaries:**
- **Evidence per request:**
  - every saved request records `meta.prefix`: its block count, the breakpoint blocks, the number of leading blocks identical to the previous request of the same family (`common_blocks`), the first changed block, and the identical character prefix;
  - every response records the cache usage;
  - with the saved payloads, this relates each CLM edit or baseline summary to the cache reads and writes that followed.
- **Not an exact causal measure:** a "lost reuse" figure (tokens of the previous request no longer read) is descriptive. Breakpoint placement, the lookback and the 512-token minimum also govern reads.

**Timing:** cold-start costs stay in each run's total, and slow responses are not removed from headline timings.

## Calibration procedure, fixed before calibration

**Runs:**
- One four-condition block on `coding-dev-1`, run with `compare --conditions summary:off,summary:on,clm:off,clm:on --tasks coding-dev-1 --reps 1` (Williams row 0: summary/off, summary/on, CLM/on, CLM/off).
- At most one more block, only to resolve a **concrete** issue.
- At most **8 calibration runs** and **USD 8** within the total budget.
- Every attempt and change is recorded.

**What calibration must establish:**
1. **Context management while work remains:** both approaches manage context before the final stage, with action steps after.
2. **Caching works:** caching-on requests show cache writes and later reads.
3. **Off means off:** caching-off runs record zero cache reads and writes.
4. **Isolation:** each run's first call reads 0 cache tokens.
5. **Accounting:** the ledger settles to the sum of call costs, bounds hold, and nothing is assumed or pending.
6. **Scoring:** coding scoring works.

**If 2, 4 or 5 cannot be established** after the allowed second block, stop before the evaluation and report the blocker.

**No arm-based tuning:** the caching policy is never tuned on which approach wins.

## Planned evaluation, fixed before calibration

**Sample and order:**
- **Target:** `coding-eval-1..4` × 3 repetitions × 4 conditions = **48 runs**, sequential, with no concurrent live commands.
- **Command:** `compare --tasks coding-eval-1,coding-eval-2,coding-eval-3,coding-eval-4 --reps 3 --conditions summary:off,summary:on,clm:off,clm:on`.
- **Williams schedule:**
  - Instance i in repetition r runs its 4 conditions in Williams row (i + r − 1) mod 4.
  - Each condition appears **3 times in each of the 4 positions**, each instance gets 3 different orders, and each ordered adjacent pair occurs equally often.
  - The full schedule is written into the comparison record's frozen block before the first run.

**Cost rule:**
- Estimate = mean calibration cost per run × 48 × 1.25.
- If it exceeds the remaining authorisation (USD 30 minus calibration spend), use the fallback **4 instances × 2 repetitions × 4 conditions = 32 runs**, chosen before the evaluation.
- If neither fits, stop with preparation complete and report the estimate.

**Rules during the evaluation:**
- **Invalid runs:** infrastructure, executor or accounting statuses and evaluation errors are labelled invalid, kept and not replaced.
- **Halts:** a budget or accounting halt leaves the remaining cells missing; they are reported.
- **No changes:** no reruns, no tuning after results, no sample expansion.

**Analysis:**
- **Per condition:** means and per-run values of cost, time, calls and cache tokens.
- **Paired differences:** within each instance and repetition block, CLM − baseline at the same caching setting, and caching on − off within each approach.
- **Interpretation:** the 12 blocks are not independent task designs, since there are 4 instances. Findings are exploratory and limited to this model, workload, layout and cold-start-per-run policy.

## Budget

- **Ledger at the start:** USD 19.932944 spent, ceiling USD 46.213524.
- **Authorised for experiment 006:** at most USD 30, covering calibration, evaluation, retries and any live verification.
  - The ceiling is set once, explicitly, to **USD 49.932944** (spend at start + 30).
  - Previous entries are preserved, and nothing is raised automatically.
- **No stacking:** unused authorisations from earlier experiments are not added.

## Calibration record

**Before calibration:**
- **Ceiling:** the ledger ceiling was set once, as authorised, from USD 46.213524 to **USD 49.932944** (spend at the change: USD 19.932944). Prior entries are unchanged.
- **Source:** clm-lib HEAD `e486cae` plus uncommitted changes, patch SHA-256 `c4db53b41c7d270a415b910f04b0bb1625d6ab97ea9c1fde5053ec30f0ed6f4d`.

### Block 1: comparison `20261004T233901` on `coding-dev-1`, Williams row 0

| Order | Run | Condition | Result | Calls | Cost (USD) | Uncached / read / write / output tokens | First call read / write | Management |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `20261004T233901-summary-cacheoff-coding-dev-1-8371` | baseline, off | strict 24/24 | 11 (1 summary) | 0.267 | 43,846 / 0 / 0 / 4,564 | 0 / 0 | summary at step 7 (stage 3 of 4); 4 action steps after |
| 2 | `20261004T234009-summary-cacheon-coding-dev-1-b2b6` | baseline, on | strict 24/24 | 11 (1 summary) | 0.161 | 1,114 / 30,049 / 12,509 / 4,398 | 0 / 1,430 | summary at step 7 (stage 3); 4 action steps after |
| 3 | `20261004T234117-clm-cacheon-coding-dev-1-3845` | CLM, on | strict 24/24 | 11 | 0.117 | 1,187 / 27,952 / 8,980 / 3,076 | 0 / 1,726 | 2 edits, effective at steps 5 and 8 (stage 2 onwards); 7 action steps after the first |
| 4 | `20261004T234211-clm-cacheoff-coding-dev-1-55d8` | CLM, off | strict 24/24 | 11 | 0.213 | 37,398 / 0 / 0 / 3,148 | 0 / 0 | 2 edits, effective at steps 5 and 8; 7 action steps after |

**Findings against the criteria:**
1. **Context management while work remained:** both approaches managed context while stages remained to be released (the summary at stage 3 of 4; CLM edits from stage 2).
2. **Cache writes, then reads:**
   - **Stable prefix:** each caching-on run wrote it on its first call (1,430 tokens baseline, 1,726 CLM).
   - **Later calls:** these read the growing prefix and wrote only the newly appended entries, the documented healthy-loop pattern. For example, the CLM steps 2–4 read 1,726, 2,908 and 3,583 tokens.
   - **Uncached remainder:** about 108 tokens per action call, which is the runtime-status block after the last breakpoint.
3. **Off means off:** both caching-off runs recorded 0 cache reads and 0 writes.
4. **Isolation:** every run's first call read 0 tokens.
   - The two caching-on runs here use different system prompts (baseline vs CLM), so this block alone cannot show that the tag is needed.
   - In the evaluation, same-condition runs follow each other within the 5-minute TTL. There, first-call reads of 0 are the isolation check.
5. **Accounting:**
   - each run's ledger total matches its recorded cost (to rounding, at most USD 0.000001);
   - every entry has the `provider_usage` basis;
   - nothing was pending or assumed;
   - every response held the reservation bound.
6. **Scoring:** works; all four runs were strictly successful.

**Reuse around management, as observed:**
- **After each CLM edit** (steps 5 and 8), the next request matched the previous one only up to the stable prefix (`first_changed_block` = the first entry block). It read 1,726 tokens, the stable prefix, and wrote the rewritten context (935 and 1,222 tokens).
- **After the baseline summary**, the next action request read 1,430 (its stable prefix) and wrote 2,376.
- **The summary call itself** read 0 and wrote 3,832, because its prefix (summariser instructions) had never been written before in the run. This is expected, and is reported rather than engineered.

**Decisions:**
- **No second calibration block** is needed. No setting or layout was changed.
- **Calibration spend:** USD 0.757 (4 runs).
- **Cost estimate:** mean USD 0.189 per run × 48 × 1.25 = USD 11.36, within the remaining USD 29.24. The full **48-run** evaluation is used; the fallback is not needed.

## Frozen

The evaluation is launched with `configs/exp006.toml` and:

`compare --tasks coding-eval-1,coding-eval-2,coding-eval-3,coding-eval-4 --reps 3 --conditions summary:off,summary:on,clm:off,clm:on --max-usd 29.2`

**The comparison record's frozen block records:**
- the model, effort and full config: limits, `token-tail/1`, `request.layout` `blocks/1`, TTL 5m, `run-tag/1`;
- prompt version `2026-10-04.1`;
- generator `invoice-gen/1` and scorer `invoice-checks/1`;
- the 48-row Williams schedule;
- git HEAD and the uncommitted source patch.

**Fixed for the evaluation:**
- **Prices:** `configs/prices.toml` (retrieved 2026-10-04, rechecked against the caching docs on 2026-10-05).
- **Stopping and invalid-run rules:** as planned above.
- **Spend cap:** `--max-usd 29.2` caps this process at the remaining authorisation.

## After the comparison

- **Cells:** all 48 cells of comparison `20261004T234408` completed, with none invalid or missing and no halt. No runs were repeated.
- **Isolation:** every run's first call read 0 cached tokens, so no cross-run cache hit was observed.
- **Calls:** no repairs, API retries or premature final answers occurred in any of the 48 runs.
- **Source:** the frozen source patch SHA-256 equals the calibration patch (`c4db53b4…`). No scorer, prompt, setting or runtime code was changed after the results.
- **One post-evaluation change, reporting only:** `report.context_entries` now also reads `blocks/1` payloads. Before the fix, the edit-evidence section of the generated report failed on them. A test was added. The change affects no run, score or measurement.
- **Spend:** calibration USD 0.757 plus evaluation USD 10.450 is USD 11.207, within the USD 30 authorisation. The ledger after the experiment shows USD 31.140 spent of the USD 49.933 ceiling.
