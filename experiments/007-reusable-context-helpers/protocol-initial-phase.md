# 007 – Protocol

_Design written on 2026-10-05, before any experiment-007 live run. Calibration, freezing and post-comparison notes are added below as they happen; earlier sections are not rewritten afterwards._

## Questions

1. Does CLM improve correctness or efficiency compared with the robust summary baseline on a longer, repetitive investigation task?
2. Does allowing the model to create and reuse context-management functions add value beyond direct context editing?
3. What reusable management logic, if any, does the model choose to create?

This is our own exploratory experiment, not a reproduction of the CLM paper's benchmarks.

## Conditions

| | Condition | Mode | What differs |
| --- | --- | --- | --- |
| A | Robust summary baseline | `summary` | `token-tail/1`: the runtime triggers summarisation at 70% of the budget, and the same model writes the summaries (separate summary calls) |
| B | CLM, direct editing (a deliberately restricted CLM condition) | `clm_direct` | The model edits its context with Python in each step, but is asked not to save context-management routines for later steps |
| C | CLM, reusable helpers allowed | `clm_helpers` | The same CLM capabilities, plus permission to save, call and revise context-management functions across steps. Optional |

**Comparisons:** B vs A, C vs A and C vs B are all reported.

**What C vs B measures:** the effect of *permitting* reusable routines under these instructions. It is not an isolated causal effect of each helper call.

### Exact condition-specific instructions

**Shared CLM text:** B and C share the experiment-001–006 CLM text (`prompts.CLM_INSTRUCTIONS`), with its one sentence about reusable helper modules removed (`prompts.CLM_SHARED`). Each adds one clause before the ordering rule.

**B (`clm_direct`):**

```
- Context-management code (this run): write the code that inspects or rewrites context.json
  within each step. You may define functions inside a step's code, but do not save
  context-management functions or scripts to files for importing, running or exec-ing in later
  steps. Saving notes and other non-executable files is fine, and so is saving code that only
  analyses task files.
```

**C (`clm_helpers`):**

```
- Context-management code (this run): you may also save reusable context-management functions
  in /task/workspace (for example as a Python module), call them in later steps and revise them.
  The working directory is importable. This is optional.
```

**What is not given:**
- No helper code, algorithm or example is provided, and helpers are never required or rewarded.
- The runtime never generates, schedules or invokes model-written code. Every execution is the model's own `execute` action.

**Enforcing B:** B's restriction is instruction-only and inspected afterwards (below). Nothing is blocked, deleted or failed to enforce it.

**The baseline (A):**
- It keeps the unchanged experiment-003 `token-tail/1` system text. It allows ordinary workspace files, including helper scripts for its own analysis.
- Its summariser gets a task-kind instruction for this task family (`SUMMARY_SYSTEM_TOKEN_TAIL_ROUNDS`). Like the coding variant used in experiments 004–006, it lists what to preserve: per-thread current and superseded causes, services, statuses, follow-ups, early facts, file:line references and rounds still to read. It is a fair, task-appropriate baseline, not a weakened one.

**Equal for all three:** task text, tools, sandbox, workspace persistence, evidence release and source access.

**Prompt version:** `2026-10-05.1` adds these texts. Earlier prompts are byte-identical (hash-tested).

## Task: incident over 10–12 evidence rounds (`incident-rounds-gen/1`)

- **Code:** clm-lib `src/clm_lib/rounds.py`.
- **Release mechanism, identical for all conditions:**
  - one hourly round per `advance` action;
  - files under `/task/fixtures/round-NN/` (read-only);
  - the release observation names the new directory (no file contents);
  - future rounds are absent until released, and released rounds never change and stay rereadable (rereads are ordinary executions and cost what they cost);
  - a final answer is accepted only after the last round.

**Each round contains:**
- **Service logs:** five services' structured logs (`logs/<service>.log`), about 55–95 lines each per round.
  - **Repeated observations:** routine health, heartbeat, request and slow-query lines.
  - **Format change:** from a seeded round (5–8) onward, the logs switch from key=value text to JSON lines.
- **`board.md`:** the incident board's updates for that hour. An update lists only what changed, and the latest update for a thread wins.
- **`changes.md`** (some rounds): APPLIED and PROPOSED change records.

**Storyline** (timings, services, causes, false alarm and follow-ups vary by seed):

| Thread | What happens | Final truth |
| --- | --- | --- |
| A | A cause confirmed on the board for one service, with impact on a second. An APPLIED change, then the status goes "mitigated" and later "resolved" | Its cause, both services, **resolved** (the earlier "mitigated" is superseded) |
| B | Errors in one service with a **suspected** cause; a later update **revises** the cause (superseding the suspicion); a **partial update** adds an affected service ("cause and status unchanged"); later mitigated | The revised cause, both services, **mitigated** |
| C | A late symptom ("cause not yet identified"); its logs show `config validation failed key=K value=V build=B`; K=V and build B were shipped by a change record in **round 1 or 2** | `BAD_CONFIG_ROLLOUT`, its service, **ongoing**, citing the early change record |
| D (60% of instances) | Alerts for some cause, later closed by the board as a false alarm | Not an incident |
| Follow-ups | 4–5 opened at various rounds; 1–2 closed later | The still-open codes are the unresolved issues |

**Output contract** (in the task text):

```json
{"incidents": [{"cause": "<CAUSE_CODE>", "services": [...], "status": "ongoing|mitigated|resolved",
                "evidence_refs": ["round-NN/<file>:<line>", ...]}],
 "unresolved": ["<FOLLOW_UP_CODE>", ...], "summary": "..."}
```

**Code lists:** the task text lists the cause codes (9) and follow-up codes (7) with descriptions. Instance facts are not in the task text.

**Instances:**
- **Development (calibration only):** `rounds-dev-1` (10 rounds) and `rounds-dev-2` (11).
- **Evaluation:** `rounds-eval-1` (11), `-2` (12), `-3` (10) and `-4` (11). Their causes, services, timings, superseded causes, false-alarm presence, follow-ups, format-change round, origin round and config key all differ.
- **One family:** all are variants of **one synthetic task family**.

## Scorer (`rounds-score/1`), hidden and deterministic

**Checks per run (14 components):**
- **causes:** each real incident's cause is reported (3), plus one check that no other cause is reported.
  - Reporting B's superseded cause counts as **stale**.
  - Reporting D's false alarm is an error.
- **services:** an exact service set per found incident (3).
- **status:** an exact status per found incident (3). An earlier, superseded status is **stale**.
- **evidence:** per found incident (3), the references must be valid, exist, span at most 20 lines, and cover every evidence group:
  - **A and B cause:** the board's cause line, or any log line of that cause in the thread's services;
  - **C cause:** a `config validation failed` line;
  - **status:** the board line that set the current status;
  - **C origin:** the early change record.
- **unresolved:** exactly the open follow-up codes (1). Reporting a closed one is **stale**.

**Strict success:** all components pass and the answer was submitted.

**Counting:** components are parts of a run, not independent samples.

**Validation before live runs** (`tests/test_rounds.py`, all offline):
- **Correct answers:** strict on every instance.
- **Faulty answers fail in the intended category**, on every instance: a superseded cause, a stale status, a missed partial update, a missing incident, the early change record not cited, an invalid reference, a missing open follow-up, a closed follow-up reported, a false alarm reported, and no answer.
- **Evidence:** every required fact is shown to appear in the evidence.
- **End-to-end:** a sandbox run shows release visibility (future rounds absent, no hidden files) and scoring.

## Helper evidence (`helper_audit.py`) and direct-edit compliance

**Context-management code:** a workspace code file whose content refers to `context.json`.

**Tiers per file:**
1. **created:** such a file was written;
2. **executed:** a function or module body defined in it began executing in a successful step (in-container `sys.monitoring` record);
3. **repeated accepted edits:**
   - its code was on the call stack when `context.json` was written, and that step's edit was accepted;
   - in **at least two distinct steps**;
   - each such revision is confirmed as the prefix of the next request (edit evidence).
4. **substantive repeated:** tier 3, where the writing function contains its own selection, filtering, merging or replacement logic over existing entries.
   - A static AST heuristic classifies each writing function version as selection/filtering, merging/rewriting, replacement, or a **wrapper** that writes caller-supplied text.
   - Wrappers are valid behaviour, but are reported separately and are not substantive.
   - Ambiguous classifications are checked by reading the code.

**Code preservation:** every helper version is preserved (`files/step-NNN/`).

**Code volume:** generated code volume is the total characters of all executed step code, recorded per run.

**B compliance:** any later-step reuse of saved context-management code is flagged, including indirect reuse. The signals are:
- the runtime record: imported, executed or compiled;
- the code reading the file with `exec`/`compile`/`runpy`;
- a subprocess naming the file;
- an import in the code text.

Violations are recorded and reported with their outcomes. They are not excluded or rerun.

**Limits of the instrumentation:**
- code in child processes and `os.open`-level writes are not attributed;
- code-text checks are pattern-based;
- write attribution shows helper code performed the write, not that it alone chose the content.

## Shared settings and fairness

- **Config:** `configs/exp007.toml`.
  - **Same as experiment 006:** `claude-opus-5-5`, effort `low`, an 8,000-token whole-request budget, a 70% pressure point, a 1,000-token recovery reserve, `max_output_tokens` 4,096, a 30 s execution timeout, `token-tail/1` (0.15 / 0.25 / 0.50), request layout `blocks/1`, run isolation `run-tag/1`.
  - **Caching:** prompt caching is **on for all three conditions**, with explicit 5-minute breakpoints.
- **Action allowance** (fixed before calibration):
  - `max_calls` **60 task calls**: actions, repairs and their API retries.
  - The baseline's **summary calls are counted separately**, with their own cap of 20 (`summary_calls_in_max_calls = false`), so summarising never uses up investigation steps.
  - 10–12 rounds need about 2–4 calls per round.
  - Earlier experiments (`summary_calls_in_max_calls = true`) are unchanged.
- **Accounting:** every call is in the ledger: task calls, summary calls, repairs, retries, helper-creation steps, failed executions, cache writes and reads, and output.
- **Isolation:** each run starts with a fresh workspace and a cold, run-tagged cache. Audit records (`events.jsonl`, evidence) live outside every mount.

## Calibration, fixed before calibration

**Runs:**
- `rounds-dev-1` and `rounds-dev-2` under all three conditions: **6 runs at most, and at most USD 8**.
- Command: `compare --tasks rounds-dev-1,rounds-dev-2 --reps 1 --conditions summary:on,clm_direct:on,clm_helpers:on`.
- Order: dev-1 A, B, C; dev-2 B, C, A. Each condition is in two different positions.

**Calibration must establish:**
- evidence release and scoring work;
- the task fits the limits;
- all three conditions manage context while substantial work remains;
- whether C produces meaningful reusable management logic.

**Gate:**
- **Stop** if neither C run reaches tier 4 (substantive helper logic reused across at least two accepted editing steps). Then report whether no helpers appeared, only wrappers appeared, or helpers were created but not reused. Instructions are **not** strengthened.
- **Otherwise,** if the pilot is valid, proceed **regardless of preliminary cost or accuracy**. Perfect correctness is acceptable.

**Defects:** concrete implementation defects may be fixed and the affected runs documented, within the 6-run cap. Every paid attempt is kept.

## Evaluation, fixed before calibration

**Sample:**
- **Target:** `rounds-eval-1..4` × 2 repetitions × 3 conditions = **24 runs**.
- **Fallback:** `rounds-eval-1..3` × 2 × 3 = **18 runs**.

**Cost rule:**
- Estimate = mean calibration cost per run × runs × 1.25.
- Choose 24 if it fits the remaining authorisation (USD 30 minus calibration spend), else 18, else stop with an estimate.
- The choice is made before any evaluation run.

**Order:**
- Each matched block (instance, repetition) runs all three conditions sequentially. Block b (repetitions outer) uses order b mod 6 of the six permutations (`cli.ORDERS_3`).
- **With 24 runs (8 blocks), the position counts are not exactly balanced:**
  - A in positions 1/2/3: 3, 2, 3;
  - B: 3, 3, 2;
  - C: 2, 3, 3.
- **With 18 runs (6 blocks),** each condition is in each position exactly twice.
- The schedule is written into the comparison's frozen block.

**Rules during the evaluation:**
- **Assigned conditions:** every scheduled run is reported in its assigned condition. C runs without helpers remain C runs.
- **Invalid runs** are labelled and kept, not replaced.
- **No changes:** no reruns, sample changes or stopping because of observed results.

## Analysis

**Per condition and paired by block:**
- strict success and each check category;
- mean cost;
- mean elapsed and provider time;
- task, summary and total calls;
- uncached input, cache reads and writes, and output;
- edits and summaries;
- helper tiers and revisions, and code volume;
- operational failures and protocol violations.

**Presentation:** individual runs are shown with the averages.

**Helper effort:** the cost of creating and revising helpers stays inside C's totals. A subgroup of helper-using C runs, if described, is explicitly secondary and not causal.

**Limits of the conclusions:** they are exploratory, and checks and repetitions are not independent task designs.

## Budget

- **Ledger at the start:** USD 31.140097 spent, ceiling USD 49.932944.
- **Authorised for experiment 007:** at most USD 30, covering calibration, evaluation and failed attempts.
  - The ceiling is set once, explicitly, to **USD 61.140097**.
  - Nothing is raised automatically, and earlier unused authorisation is not reused.
- **Calibration sub-limit:** USD 8 and 6 runs.

## Calibration record

**Before calibration:**
- **Ceiling:** the ledger ceiling was set once, as authorised, from USD 49.932944 to **USD 61.140097** (spend at the change: USD 31.140097).
- **Source:** clm-lib HEAD `c391457` plus uncommitted changes, patch SHA-256 `3f43cd5d4e9d3d387b4b4b573472bd13ef8f087efba6512488ceeb298f55e452`. This equals the comparison's frozen hash.

**Runs:** comparison `20261005T061432`, all six runs with caching on.

| Block / position | Run | Condition | Result | Task / summary calls | Cost (USD) | Elapsed / provider time | Management |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dev-1 / 1 | `20261005T061432-summary-cacheon-rounds-dev-1-4a35` | A baseline | strict 14/14 | 27 / 7 | 0.501 | 213 s / 186 s | 7 summaries, the first at stage 2 of 10, with 23 action steps after |
| dev-1 / 2 | `20261005T061804-clm_direct-cacheon-rounds-dev-1-b3a5` | B direct | **context overflow**, no answer | 29 / 0 | 0.321 | 151 s / 124 s | 12 edits from stage 1; ended at step 30 with all 10 rounds released |
| dev-1 / 3 | `20261005T062036-clm_helpers-cacheon-rounds-dev-1-34cd` | C helpers | strict 14/14 | 30 / 0 | 0.354 | 164 s / 138 s | 13 edits from stage 1, with 28 action steps after |
| dev-2 / 1 | `20261005T062320-clm_direct-cacheon-rounds-dev-2-fd51` | B direct | strict 14/14 | 34 / 0 | 0.381 | 180 s / 145 s | 12 edits from stage 1, with 31 action steps after |
| dev-2 / 2 | `20261005T062620-clm_helpers-cacheon-rounds-dev-2-066e` | C helpers | strict 14/14 | 34 / 0 | 0.417 | 163 s / 130 s | 16 edits from stage 1, with 32 action steps after |
| dev-2 / 3 | `20261005T062903-summary-cacheon-rounds-dev-2-2a08` | A baseline | strict 14/14 | 34 / 9 | 0.599 | 242 s / 204 s | 9 summaries, the first at stage 2 of 11, with 31 action steps after |

**What calibration established:**
- **Release and scoring:** evidence release and scoring work. The five completed runs scored 14/14.
- **Limits:** the task fits them. Task calls were 27–34 of 60, summary calls 7–9 of 20, and the peak request was 6,460–6,863 tokens of 8,000.
- **Context management:** all three conditions managed context while most of the work remained.
- **Caching and isolation:** every run's first call read 0 cached tokens.
- **Accounting:** nothing was pending or assumed.

**Helper evidence:**

| C run | Context-management code files | Other saved code | Tier reached |
| --- | --- | --- | --- |
| dev-1 | none | none | none |
| dev-2 | none | `h.py`: `scan(n)` prints board, change and warning/error lines of round n. It executed in 7 steps, but never reads or writes `context.json` | none (a task-analysis helper, not context management) |

- **How edits were made:** in both C runs, every context edit was inline step code. The model condensed findings into note entries (one rewritten running note, or one short note per round) and dropped the raw entries. The B runs edited the same way.
- **Direct-edit compliance (B):** no B run saved any code file, and the audit found no reuse of saved code. Both B runs complied.

**A defect found in calibration, run B dev-1:**
- **What happened:** at step 29 the model edited its context *and* printed a 6,000-character observation. The runtime appended the step's observation and then its edit receipt.
- **Why it overflowed:** the spill rule, which moves an oversized latest observation into a file when the request exceeds the hard limit, looked only at the **last** entry, which was the receipt. The observation could not be spilled, and the next request (about 8,136 tokens) exceeded the 8,000-token budget, so the run ended as a context overflow.
- **Who it affects:** only CLM runs; the baseline gets no receipts.
- **The fix:** `limits.spill_past_receipt` (true in `configs/exp007.toml` from now on; false keeps the original rule for earlier configs), with a test.
- **The affected run** is kept and reported as a context overflow. It was not rerun, since the six-run calibration allowance was used.

**Decision:**
- **Stop before the evaluation.** By the pre-registered gate, neither C run showed substantive context-management helper logic reused across editing steps. In fact, **no context-management helper appeared at all**; one C run created a reusable evidence-scanning helper.
- **Instructions were not strengthened, and no evaluation run was made.**
- **Calibration spend:** USD 2.573 of the USD 8 sub-limit, 6 of 6 runs.
- **Ledger:** USD 33.713 spent of the USD 61.140 ceiling. The unused USD 27.43 of experiment 007's authorisation is not carried over.
