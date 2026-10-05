# 007 – Protocol (revised phase)

_Revision written on 2026-10-05, after the initial calibration and before any revised-phase paid run. This is a **documented protocol revision made after inspecting development data**, not the original pre-registered design. The original protocol and its calibration record are preserved unchanged in [`protocol-initial-phase.md`](protocol-initial-phase.md). Calibration, freezing and post-comparison notes for the revised phase are added below as they happen; earlier sections are not rewritten afterwards._

## Phases of experiment 007

| Phase | What it tested | Runs | Status |
| --- | --- | --- | --- |
| **Initial calibration** (comparison `20261005T061432`) | Whether merely *permitting* reusable context-management helpers (`clm_helpers`, optional) leads the model to create them | 6 development runs | Complete. No context-management helper appeared, so the original gate stopped that phase before evaluation |
| **Revised calibration** (a new comparison id) | Whether the apparatus works for the **instructed** reusable-function strategy (`clm_reuse`) | 6 development runs (+ at most 3 to validate an infrastructure fix) | This protocol |
| **Revised evaluation** (a new comparison id) | The three-condition comparison below | 24 runs (fallback 18) | This protocol |

**Phases are never pooled:**
- Every run carries a `phase` label in `experiment.json`, the manifest, the metrics and the report.
- Each comparison is labelled with its phase, and performance tables are per phase.
- The six initial runs are not relabelled as revised conditions. The initial direct-editing overflow stays recorded as an overflow.

## Revised question

**Does instructing a CLM agent to perform context edits through model-written reusable functions improve correctness or efficiency compared with direct CLM editing and the robust summary baseline?**

This comparison tests **instructed strategies**. Helper creation in condition C is instructed and is not described as spontaneous.

## What changed from the initial phase, and why

1. **Instructed, not just permitted.**
   - **What changed:** condition C's clause now instructs the model to perform its context edits through a reusable Python module it writes.
   - **Why:** in the initial phase, the optional permission produced no context-management helper. Both helpers-allowed runs edited inline, and one wrote only a task-analysis helper. That phase answered "do helpers appear spontaneously?" (here: no). It could not answer whether a reusable-function *strategy* helps.
2. **Simple functions count.**
   - **What changed:** a small reusable function that writes model-supplied notes is a valid implementation, and so is one with selection, filtering, deduplication or replacement logic.
   - **Why:** helpers are classified by what they do, not excluded for being simple, and sophisticated logic is not required.
3. **The spill defect is fixed for all revised conditions.**
   - **What changed:** `limits.spill_past_receipt = true` in `configs/exp007r.toml`.
   - **Why:** the initial calibration found that when a CLM step both edits the context and prints a large observation, the trailing edit receipt stopped the runtime from spilling that observation (initial run `…clm_direct…dev-1-b3a5` overflowed this way).
   - **Effect on the initial phase:** its config (`configs/exp007.toml`) keeps the original rule. The initial direct-editing overflow is not evidence that direct editing is intrinsically worse.

**Initial-phase provenance check:** all six initial runs used one source state (patch SHA-256 `3f43cd5d…`), prompt version `2026-10-05.1`, and the original spill rule (the setting did not exist yet). `configs/exp007.toml` now equals their frozen config again, after a post-calibration edit to it was moved to `exp007r.toml`.

**Unchanged:** the task family, scorer, instances, model, effort, budgets, limits, layout, caching, isolation, baseline policy and B's clause.

## Conditions (revised phase)

| | Condition | Mode | Condition-specific difference |
| --- | --- | --- | --- |
| A | Robust summary baseline | `summary` | `token-tail/1` with the rounds summariser instruction: recent history kept by token allowance, room-leaving summary sizing, separate summary calls |
| B | CLM, direct editing | `clm_direct` | Clause B (the same text as the initial phase) |
| C | CLM, reusable editing functions (instructed) | `clm_reuse` | Clause C (new) |

**Exact clauses** (in `prompts.CLM_CLAUSE`; prompt version `2026-10-05.2`, which adds only clause C):
- B and C share the CLM text without its helper sentence (`prompts.CLM_SHARED`), plus their clause inserted before the ordering rule.
- A uses the unchanged `token-tail/1` system text.
- The task text and released evidence are identical for all three conditions.

**B (`clm_direct`):**

```
- Context-management code (this run): write the code that inspects or rewrites context.json
  within each step. You may define functions inside a step's code, but do not save
  context-management functions or scripts to files for importing, running or exec-ing in later
  steps. Saving notes and other non-executable files is fine, and so is saving code that only
  analyses task files.
```

**C (`clm_reuse`):**

```
- Context-management code (this run): perform working-context edits through a reusable Python
  module that you create in /task/workspace (the working directory is importable). Define
  functions for the editing operations you need, and invoke the saved functions when you choose
  to edit context. Reuse them for later edits and revise them if useful. You decide what
  information to retain and how the functions work. You do not need to edit on every step.
```

This is the requested wording, adapted to the tool interface by naming the workspace path and noting that it is importable.

**What is not given:**
- No helper code, algorithm, target note content or list of facts to keep is given.
- The runtime never generates, schedules or invokes model-written code, and no other model makes editing decisions.
- No edits are forced.

## Helper evidence and adherence (`helper_audit.py`)

**What counts as context-management code:** a workspace code file that refers to `context.json`.

**Measured for each such file:**
- creation step and revision steps (every version is kept under `files/step-NNN/`);
- **execution:** steps in which its functions actually began executing (in-container `sys.monitoring`). Being imported, compiled or mentioned is not counted;
- **repeated execution:** execution in at least two distinct steps;
- accepted context edits whose `context.json` write had its code on the call stack, and whether each accepted revision is the prefix of the next request.

**Helper categories**, for each writing function and for every top-level function (a static AST heuristic, with ambiguous cases inspected by hand):
1. writes or replaces supplied note content;
2. selects, removes or reorganises existing entries;
3. more substantial management logic (selection combined with merging or text rebuilding).

**Adherence:**
- **C:**
  - **full:** every accepted edit happened in a step where saved context-management code executed;
  - **partial:** some did;
  - **none:** no edit did.
  - Attributed writes (helper code on the stack) are reported separately.
- **B:**
  - **adherent:** no later-step reuse of saved context-management code (by import, execution, compile, exec of a read file, subprocess or import text);
  - **non-adherent:** otherwise.

**Non-adherent runs** stay in their assigned conditions and are reported with their outcomes.

**Limits of the instrumentation:**
- child processes and `os.open`-level writes are not attributed;
- code-text checks are patterns;
- write attribution shows that helper code performed the write, not that it alone chose the content.

## Shared controls

- **Config:** `configs/exp007r.toml` is `configs/exp007.toml` (the initial-phase config, unchanged) plus `spill_past_receipt = true` and the revised-phase ceiling. A test confirms that nothing else differs.
- **The same for all three conditions:**
  - `claude-opus-5-5`, effort `low`, an 8,000-token whole-request budget, `max_output_tokens` 4,096;
  - 60 task calls (actions, repairs and their retries), with the baseline's summary calls counted separately (cap 20) but included in its cost, latency and total calls;
  - the 30 s execution timeout, evidence release, task tools, sandbox and workspace persistence;
  - the `blocks/1` layout with 5-minute prompt caching on and `run-tag/1` cold-cache isolation per run;
  - the corrected spill and recovery behaviour.
- **Isolation:** no helper files, notes or caches carry between runs. Evaluator truth and audit records stay outside the sandbox mounts.
- **Scorer and task:** the scorer (`rounds-score/1`) and the task family (`incident-rounds-gen/1`) are unchanged. Tests confirm that the revised condition does not change task text, visibility or scoring.

## Revised calibration

**Runs:**
- `rounds-dev-1` and `rounds-dev-2` (development instances already inspected, not fresh) × the three revised conditions = **6 runs**.
- Command: `compare --tasks rounds-dev-1,rounds-dev-2 --reps 1 --conditions summary:on,clm_direct:on,clm_reuse:on` with `configs/exp007r.toml`.
- Order: dev-1 A, B, C; dev-2 B, C, A.

**Checks:**
- all conditions operate under the corrected runtime;
- context management happens while work remains;
- the output contract and scoring work;
- whether B and C follow their editing instructions;
- whether the instrumentation captures the behaviour;
- the expected evaluation cost.

An accuracy difference, early savings, sophisticated helpers and spontaneity are **not** required.

**If C does not follow the instruction:**
- Inspect whether the capability description or interface is unclear, and record the finding.
- Do not strengthen the prompt repeatedly.
- Non-adherence alone is not a reason to discard runs or to declare success. If the apparatus works, proceed with the frozen strategy and measure adherence in the evaluation as well.

**If there is a concrete infrastructure defect:** stop and fix it. At most **one** extra development triplet (one run per condition) may validate the fix. Every affected attempt is kept. If validity is still unresolved, stop.

**Limits:** calibration may use at most USD 8 and 6 + 3 runs.

## Revised evaluation

**Instances:**
- `rounds-eval-1..4`, which have **never been run**. No run directory exists, and they did not tune the design.
- Disclosure: during implementation their generated structure (causes, services, round counts) was printed once, as a sanity check of the generator.

**Sample:**
- **Target:** 4 instances × 2 repetitions × 3 conditions = **24 runs**.
- **Fallback:** `rounds-eval-1..3` × 2 × 3 = **18 runs**.

**Cost rule:**
- Estimate = mean revised-calibration cost per run × runs × 1.25.
- Use 24 if it fits within the remaining revised-phase authorisation (USD 30 minus revised calibration spend), else 18, else stop with an estimate.
- The size is chosen before the evaluation and never changed in response to outcomes.

**Schedule:**
- Each matched block (instance, repetition) runs all three conditions. Block b (repetitions outer) uses order b mod 6 of the six permutations.
- **With 24 runs, the position counts are not exactly balanced:**
  - A in positions 1/2/3: 3, 2, 3;
  - B: 3, 3, 2;
  - C: 2, 3, 3.
- **With 18 runs,** each condition is in each position exactly twice.
- The schedule, prompts, settings, scorer and the full source patch (including untracked files) are frozen in the comparison record.

**Rules during the evaluation:**
- **One version:** the comparison uses one runtime and prompt version.
- **Defects:** if an infrastructure defect appears, halt and preserve the evidence before deciding whether a separately recorded rerun is needed.
- **No changes:** no reruns, no tuning after results, no sample changes.

## Analysis

**Comparisons:**
- **Primary:** C vs A.
- **Also reported:** B vs A and C vs B.

**Per condition:**
- strict success and categories;
- completed runs and failure reasons;
- mean cost, elapsed and provider time;
- task, summary and total calls;
- tokens, cache reads and writes;
- context-management activity;
- helper creation, execution, reuse, revisions, categories and adherence.

**Overheads included:** helper creation and revision cost stays inside C.

**Presentation:** individual runs and paired block differences are shown alongside the means.

**Early failures:**
- Their costs remain in the all-attempt totals, and the completion difference is made prominent.
- Lower spend caused by stopping early is not called efficiency.
- Any completed-run-only view is secondary and selection-affected.

**Interpretation:**
- **Not exact attribution:** helper "savings" are not attributed exactly, because C also changes instructions and strategy. Traces may illustrate mechanisms.
- **Calibration:** these observations are development evidence, not findings.
- **The sample:** small and exploratory, with repeated instances that are not independent designs.

## Budget

- **Ledger at the start of the revised phase:** USD 33.713095 spent; the initial phase spent USD 2.572998 of its own separate authorisation.
- **Authorised for the revised phase:** at most USD 30.
  - The ceiling is set once to **USD 63.713095** (spend at start + 30).
  - It is not combined with the initial phase's unused authorisation, and not raised automatically.
- **Calibration sub-limit:** USD 8.

## Revised calibration record

**Before calibration:**
- **Ceiling:** the ledger ceiling was set once, as authorised, from USD 61.140097 to **USD 63.713095** (spend at the change: USD 33.713095).
- **Source:** HEAD `c391457` plus uncommitted changes, patch SHA-256 `c7d1cbdf…`.

### Revised block 1: comparison `20261005T070400` (stopped)

**Runs:**

| Order | Run | Condition | Result | Calls | Cost (USD) | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `20261005T070400-summary-cacheon-rounds-dev-1-b73b` | A | completed, **not strict** (13/14) | 30 task + 9 summary | 0.537 | Thread A's references cited its status lines and the mitigation change, but no line establishing its cause. A genuine answer error under the output contract |
| 2 | `20261005T070816-clm_direct-cacheon-rounds-dev-1-d5f6` | B | strict 14/14 | 31 | 0.334 | 11 inline edits; adherent (no saved context-management code) |
| 3 | `20261005T071052-clm_reuse-cacheon-rounds-dev-1-9be4` | C | **context overflow** at step 11 (round 4 of 10), no answer | 10 | 0.114 | **Runtime defect, below.** Before it, the run followed the instruction **fully**: it created `ctx.py` at step 1 (`load`, `save`, `keep_notes(note_id, body)`), and all 4 accepted edits (steps 2, 4, 5 and 8) were made by these saved functions |
| 4 | `20261005T071143-clm_direct-cacheon-rounds-dev-2-9275` | B | **interrupted** by us (SIGINT) at step 11 | 11 | 0.259 | Stopped to fix the defect. The in-flight call was charged its full reservation (USD 0.141, assumed); kept as recorded |

**Runs 5 and 6** (C and A on dev-2) were not started.

**Defect 2: the pressure notice pushes a request over the hard limit.**
- **Where it happened:** in run 3 at step 11, the request was estimated at 6,993 tokens, which is above the pressure point (5,600) but just under the hard limit (7,000). So neither spill nor the recovery request applied.
- **The defect:** the runtime then added its CLM-only "PRESSURE" notice to the status block. That made the request about 7,059 tokens, and the final size check ended the run, with no spill or recovery handling.
- **Who it affects:** CLM conditions only. The baseline summarises at that point instead.
- **The fix:** `limits.recheck_after_notice` (true in `configs/exp007r.toml`, false keeps the original behaviour for earlier configs) re-checks after the notice: spill first, then the CLM recovery request.
- **Test:** a regression test reproduces the defect with the flag off and shows the fix with it on.
- **Affected runs:** run 3 is kept and reported as an overflow. It is **not** evidence about the reuse strategy.

**Audit refinement (reporting only):** the helper audit labels non-writing helper functions (such as `load`) as "reads or utility (no context write)" rather than as note writers. This changes no run or score.

**Next:** one validation triplet (the at-most-one extra triplet allowed), `rounds-dev-2` with B, C, A in the dev-2 order planned above. It uses the fixed source under a new comparison id. The revised calibration then has 4 + 3 = 7 runs.

### Revised block 2: the validation triplet, comparison `20261005T072003` on `rounds-dev-2`, fixed source

**Source:** patch SHA-256 `22333795cd3f133ec9229da6a4c7a2004afd5cd0d5ecbd891991a450f850478d`.

| Order | Run | Condition | Result | Calls | Cost (USD) | Management and adherence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `20261005T072003-clm_direct-cacheon-rounds-dev-2-93fb` | B | strict 14/14 | 33 | 0.416 | 15 inline edits from round 1, with 31 action steps after; adherent |
| 2 | `20261005T072252-clm_reuse-cacheon-rounds-dev-2-daac` | C | completed, **not strict** (13/14) | 34 | 0.335 | **Full adherence**: `ctx.py` was created at step 1, and all 13 accepted edits were made by its saved `keep_notes` (which replaces the context with a note the caller supplies), executed in 13 distinct steps. Thread C's cause reference was a 21-line range (`round-11/logs/search-api.log:4-24`), over the 20-line limit in the output contract. A genuine answer error |
| 3 | `20261005T072543-summary-cacheon-rounds-dev-2-6431` | A | strict 14/14 | 32 task + 10 summary | 0.651 | 10 summaries, the first at round 2 of 11 |

**What calibration established (development evidence, not findings):**
- **The corrected runtime:** all three conditions operate under it. No spills, recoveries or overflows were needed in block 2. Every first call read 0 cached tokens. Nothing was pending or assumed, apart from the one reservation charged for the interrupted block-1 call.
- **Context management** happened while most of the work remained.
- **The output contract and scorer** work; the two non-strict answers each failed one evidence check, for genuine reasons.
- **Adherence:**
  - B was adherent in all its revised runs.
  - C followed its instruction **fully** in both revised runs: once before the defect ended run 3, and once in the validation run.
  - The helpers were simple: a note writer, and in dev-1 a note writer that also dropped non-note entries.
- **Instrumentation:** it captured creation, execution in each step, write attribution and next-request confirmation.

**Decisions:**
- **Proceed to the evaluation.** One infrastructure fix was made (`recheck_after_notice`), and the single validation triplet validated it. No prompt was changed.
- **Sample:** the revised calibration spent USD 2.645 over 7 runs (USD 0.378 per run). The estimate for 24 runs is USD 0.378 × 24 × 1.25 = USD 11.34, within the remaining USD 27.36, so the **24-run** evaluation is used.

## Frozen (revised evaluation)

**Command:** `configs/exp007r.toml` with

```
compare --tasks rounds-eval-1,rounds-eval-2,rounds-eval-3,rounds-eval-4 --reps 2 --conditions summary:on,clm_direct:on,clm_reuse:on --max-usd 27.3
```

**The comparison record's frozen block holds:**
- the full config: model, effort, limits including `spill_past_receipt` and `recheck_after_notice`, the baseline policy and request settings;
- prompt version `2026-10-05.2`;
- generator `incident-rounds-gen/1` and scorer `rounds-score/1`;
- the 24-row schedule;
- HEAD `c391457` and the complete uncommitted source patch, including untracked files.

**Source:** the evaluation uses the same source as the validation triplet (patch SHA-256 `22333795…`, rechecked before launch).

## After the revised evaluation

- **Cells:** all 24 cells of comparison `20261005T073045` completed, with none invalid, missing or halted. No runs were repeated.
- **Isolation:** every run's first call read 0 cached tokens.
- **Runtime:** no overflows, spills or recovery requests were needed; there were no repairs or API retries.
- **Source:** the frozen source patch is `22333795…`, the same as the validation triplet. No scorer, prompt, setting or runtime code changed after the results.
- **Order balance (realised):** A in positions 1/2/3: 3, 2, 3; B: 3, 3, 2; C: 2, 3, 3.
- **Adherence:**
  - **B** was adherent in all 8 runs: no saved context-management code.
  - **C** fully adhered in all 8 runs. Each created `ctx.py` at step 1, never revised it, ran its functions in 10–13 distinct steps, and made every accepted edit (92 in all) in steps where its functions executed. Each such write had helper code on the call stack and was confirmed as the next request's prefix.
  - **One C run** (eval-3, rep 1) also wrote the context inline after a helper call in 10 of its 13 edit steps.
- **Spend:**
  - **Revised phase:** USD 13.281 = calibration USD 2.645 (7 runs, including the interrupted one) + evaluation USD 10.636. This is within the USD 30 authorisation.
  - **Initial phase:** USD 2.573, separately.
  - **Ledger:** USD 46.994 spent of the USD 63.713 ceiling.
