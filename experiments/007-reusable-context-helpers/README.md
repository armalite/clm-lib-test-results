# 007 – Reusable context-management helpers

**Status: complete (revised phase).** Experiment 007 ran in two phases, reported separately and never pooled:

1. **Initial calibration (helpers optional).** When CLM was merely *allowed* to save reusable context-management helpers, it did not create any, so the original gate stopped that phase. See [Initial calibration](#initial-calibration-helpers-optional) below and [`protocol-initial-phase.md`](protocol-initial-phase.md).
2. **Revised phase (strategy instructed).** A documented protocol revision, made after inspecting the development data, asks a practical question: does **instructing** a CLM agent to make its context edits through reusable functions it writes help, compared with direct CLM editing and the robust summary baseline? Its evaluation (24 runs) is the main result of this README.

## What did we test (revised phase)?

**Three conditions:**

| | Condition | What the model is told |
| --- | --- | --- |
| A | Robust summary baseline (`token-tail/1`) | The runtime summarises older context at 70% of the budget, and the same model writes the summaries in separate calls |
| B | CLM, direct editing | Edit the working context with code written fresh in each step; do not save context-management routines for later steps |
| C | CLM, reusable editing functions (**instructed**) | "Perform working-context edits through a reusable Python module that you create in the workspace. Define functions for the editing operations you need, and invoke the saved functions when you choose to edit context. Reuse them for later edits and revise them if useful. You decide what information to retain and how the functions work. You do not need to edit on every step." |

In C, helper creation is instructed, not spontaneous. The exact texts are in `protocol.md`.

**The task:** a multi-service production incident whose evidence arrives in **10–12 hourly rounds** (generator `incident-rounds-gen/1`).
- **Each round:** service logs (whose format switches to JSON part-way), incident-board updates (each update lists only what changed) and change records.
- **The answer must name:**
  - a resolved incident, whose earlier "mitigated" status is superseded;
  - an incident whose suspected cause is later revised, and which a partial update extends to a second service;
  - a late incident caused by a configuration value shipped in round 1 or 2, so it must be connected to an early fact;
  - the follow-ups still open.
- **Ignore:** false alarms.
- **Evidence:** each incident needs file:line references to its cause and status, and to the early change record where one applies.
- **Scoring:** 14 hidden, deterministic checks per run (scorer `rounds-score/1`).

**Settings, equal for all conditions:**
- `claude-opus-5-5` at effort `low`, an 8,000-token request budget and 4,096 output tokens;
- 60 task calls, with the baseline's summary calls counted separately (cap 20) but fully included in its cost, time and total calls;
- the cache-friendly request layout, 5-minute prompt caching, and a cold, isolated cache and workspace per run;
- the corrected spill and recovery behaviour (see [Runtime defects](#runtime-defects-found-and-fixed)).

**Instances and order:**
- **Evaluation:** 4 fresh instances (`rounds-eval-1..4`, never run before) × 2 repetitions × 3 conditions = **24 runs**, sequential.
- **Order:** each instance-and-repetition block ran all three conditions in a rotating order. Realised positions: A 3/2/3, B 3/3/2, C 2/3/3.
- **One family:** all instances are variants of one synthetic task family.

## What happened (revised evaluation, 24 runs)

All 24 runs completed and submitted an answer. There were no overflows, recoveries, repairs, retries or invalid runs.

| | A: summary baseline | B: CLM direct | C: CLM reusable functions |
| --- | --- | --- | --- |
| **Strict success** | **4 of 8** | **6 of 8** | **7 of 8** |
| Hidden checks passed | 108 / 112 | 107 / 112 | 111 / 112 |
| Failures | 4 runs, each missing one evidence reference (A's cause line ×2, C's status line ×2) | 1 run left out an incident entirely; 1 omitted the early change record | 1 run omitted the early change record |
| Stale causes or statuses | 0 | 0 | 0 |
| **Mean cost per run (USD)** | **0.582** (0.477–0.776) | **0.386** (0.314–0.502) | **0.361** (0.318–0.386) |
| of which summary calls | 0.274 (47%) | — | — |
| **Mean elapsed / provider time** | 249 s / 209 s | 187 s / 147 s | 187 s / 149 s |
| Task + summary calls (mean) | 32.5 + 9.0 = 41.5 | 34.0 | 33.0 |
| Context management (total) | 72 summaries | 108 edits | 92 edits |
| Mean tokens: uncached / cache read / cache write / output | 3,821 / 126,766 / 58,078 / 12,552 | 3,819 / 111,590 / 40,070 / 7,402 | 3,675 / 109,160 / 36,256 / 7,180 |
| Code written per run (characters) | — | 11,177 | 10,481 |

**Per block** (strict success S or failure F, cost in USD):

| Block | A | B | C |
| --- | --- | --- | --- |
| eval-1 rep 1 | F 0.483 | F 0.389 | S 0.377 |
| eval-2 rep 1 | F 0.668 | S 0.502 | S 0.360 |
| eval-3 rep 1 | F 0.481 | F 0.318 | S 0.360 |
| eval-4 rep 1 | S 0.594 | S 0.402 | F 0.318 |
| eval-1 rep 2 | S 0.606 | S 0.360 | S 0.368 |
| eval-2 rep 2 | S 0.571 | S 0.443 | S 0.384 |
| eval-3 rep 2 | F 0.776 | S 0.314 | S 0.340 |
| eval-4 rep 2 | S 0.477 | S 0.360 | S 0.386 |

## The three comparisons (8 matched blocks each)

| Comparison | Strict success | Cost | Elapsed time |
| --- | --- | --- | --- |
| **C vs A** (primary) | 7 vs 4. Both succeeded in 3 blocks, only C in 4, only A in 1 | C **38% cheaper** (USD 0.361 vs 0.582); cheaper in **8 of 8** blocks (−19% to −56%) | C 25% faster (187 s vs 249 s); faster in 8 of 8 |
| B vs A | 6 vs 4. Both in 4, only B in 2, only A in 0, neither in 2 | B 34% cheaper (0.386 vs 0.582); cheaper in 8 of 8 | B 25% faster; faster in 8 of 8 |
| **C vs B** | 7 vs 6. Both in 5, only C in 2, only B in 1 | C 6% cheaper on means (0.361 vs 0.386), but cheaper in only **4 of 8** blocks (−28% to +13%) | about the same: C slower in 6 of 8, +2% on average |

Cost differences are ratios of the condition means; the paired mean relative differences are −36%, −32% and −4%.

**Reading the comparisons:**
- **Against the baseline:** both CLM strategies were cheaper and faster than the baseline in every matched block.
- **Where the gap comes from:** most of it matches the baseline's separate summary calls (USD 0.274 per run). These calls also produce output tokens and extra time.
- **The baseline's accuracy failures:** all were missing evidence references; its causes, services, statuses and follow-ups were always right.
- **C vs B:** the differences are small and mixed (one more strict success, a 6% lower mean cost, cheaper in only half the blocks). With 8 blocks they do not establish an effect of instructing reusable functions.

## Helpers and adherence

**C followed the instruction in all 8 runs:**
- **Creation:** every C run wrote a small module `ctx.py` at **step 1** (310–459 characters) and never revised it.
- **Use:** its functions executed in **10–13 distinct steps** per run, and **every accepted context edit** (92 in all) happened in a step where they executed.
- **Write attribution:** each such write had helper code on the call stack, and each accepted revision was confirmed as the prefix of the next model request.
- **Mixed writes:** one run (eval-3 rep 1) also wrote the context inline after calling a helper, in 10 of its 13 edit steps.

**What the helpers did:**
- Every module had a `load` (reads only) and a `save` (writes a dict it is given).
- **4 runs:** the editing function only writes or replaces note content the model supplies, for example `keep_notes(body)` or `reset(notes)`, which replace the context with supplied notes. The model composed the note text in its step code each time.
- **4 runs:** the module also (or instead) had functions that select or remove existing entries, for example `keep_only(ids)`, `prune(keep)`, `setnote(id, body)` (which replaces one note and keeps the rest), or a `keep_notes` that keeps only existing notes. Each was confirmed by reading the code.
- **None** contained more substantial logic such as merging or deduplication.

**B followed its restriction in all 8 runs:** no saved context-management code and no reuse.

**Helper overhead:** the step that created the module cost about USD 0.022 per run, and that step also did the first round's investigation. Helper creation and use are included in C's totals.

**Example** (run `20261005T075320-clm_reuse-cacheon-rounds-eval-3-48d0`): the module the model wrote at step 1:

```python
def setnote(i,body):
    d=load(); d['entries']=[e for e in d['entries'] if e['id']!=i]; d['entries'].insert(0,{'id':i,'role':'note','body':body}); save(d)
def keep_only(ids):
    d=load(); d['entries']=[e for e in d['entries'] if e['id'] in ids]; save(d)
```

- **At step 4,** its code began with `ctx.keep_only(['n1'])`. The accepted revision dropped five entries (1,576 → 268 characters), and the step-5 request began with exactly the kept note `n1`, followed by step 4's own action and output.
- **The pattern:** the same call recurred through the run, interleaved with notes for each new round.

## What do the results tell us?

- **Against the robust baseline, on this task:** both CLM strategies were cheaper (about a third) and faster (about a quarter), in every matched block, with at least as many strict successes (C 7, B 6, A 4 of 8).
  - **Cost:** the efficiency gap is consistent with the baseline's separate summary calls.
  - **Accuracy:** the baseline's lower strict success came from missing evidence references only. It is a small-sample observation, not an established difference in memory or reasoning.
- **Instructed reusable functions vs direct editing:**
  - **What happened:** the model complied fully but wrote simple helpers, mostly note writers or entry filters. C and B performed similarly.
  - **What it shows:** there is no measurable benefit of the instructed strategy beyond direct editing in this sample. A cost or accuracy effect of that size cannot be distinguished from run-to-run variation with 8 blocks.
  - **What it does not show:** that helper reuse saves money. Any apparent advantage cannot be attributed to helper reuse as such, because the instruction also changes the model's strategy.
- **Scope:** these are exploratory findings for one synthetic task family, one model and effort, one instruction wording and 8 matched blocks (4 instances × 2). The repetitions are not independent designs.

## Runtime defects found and fixed

1. **Spill past a receipt** (found in the initial calibration):
   - **The defect:** when a CLM step both edited the context and printed a large observation, the trailing edit receipt stopped the runtime from spilling that observation.
   - **The fix:** `spill_past_receipt`.
   - **Affected run:** initial run `…clm_direct…dev-1-b3a5`, which overflowed.
2. **Pressure notice over the hard limit** (found in revised calibration block 1):
   - **The defect:** the runtime's own CLM pressure notice could push a request just over the hard limit, ending the run without spill or recovery.
   - **The fix:** `recheck_after_notice`.
   - **Affected run:** revised run `…clm_reuse…dev-1-9be4`, which overflowed at round 4 after fully following its instruction.

**Scope of the fixes:**
- Both fixes are on for every revised condition; earlier configs keep the original behaviour.
- Both affected runs are kept as recorded. Neither says anything about the strategies.
- A third revised calibration run was interrupted by us to apply the second fix. It is kept, and its cost is counted.

## Revised calibration (development evidence, 7 runs)

- **Instances:** `rounds-dev-1` and `rounds-dev-2`, already inspected and not fresh.
- **Block 1** (comparison `20261005T070400`):
  - A: 13/14, a missing evidence line;
  - B: strict;
  - C: overflowed from defect 2, after fully adhering;
  - a B run on dev-2 was interrupted to fix the defect.
- **Validation triplet** (comparison `20261005T072003`, fixed source):
  - B: strict;
  - C: 13/14, a 21-line reference range over the 20-line limit, with full adherence;
  - A: strict.
- **Conclusion:** these established that the corrected apparatus, scoring and instrumentation work and that both CLM conditions follow their instructions. They are not findings.

## Initial calibration (helpers optional)

Comparison `20261005T061432`, 6 development runs; the details are in [`protocol-initial-phase.md`](protocol-initial-phase.md).

- **Accuracy:** A 2/2, `clm_direct` 1/2 (the run that overflowed from defect 1), `clm_helpers` 2/2 strict successes.
- **Mean costs:** USD 0.550, 0.351 and 0.386.
- **Helpers:** with helpers merely permitted, **no context-management helper appeared**. Every edit was inline, and one run saved only a task-analysis function. The original gate therefore stopped that phase.
- **Separation:** these runs use the original runtime and the optional-helpers wording. They are not part of the revised comparison.

## Where is the evidence?

- `protocol.md`: the revised protocol (written before any revised run), the calibration records, the defects, the freeze and the post-evaluation notes. `protocol-initial-phase.md` holds the original protocol and initial calibration, unchanged.
- `report.md`, `metrics.json` / `metrics.csv`: every run, labelled by `phase` (`initial-calibration`, `revised-calibration`, `revised-evaluation`), with the helper and adherence columns (`helper_*`, `accepted_edit_steps`, `helper_attributed_edit_steps`, `adherence`).
- `artifacts/runs/calibration/` (both phases, by run id) and `artifacts/runs/evaluation/`: per-run step scripts, saved helper versions (`files/step-NNN/`), requests, context revisions and scores.
- `artifacts/comparisons/`:
  - `20261005T073045`: the evaluation, with the frozen settings, the 24-row schedule and the source patch;
  - `20261005T072003` and `20261005T070400`: the revised calibration;
  - `20261005T061432`: the initial calibration.

**Spend:**
- **Revised phase:** USD 13.281 (calibration 2.645 + evaluation 10.636) of its USD 30.
- **Initial phase:** USD 2.573.
- **Ledger:** USD 46.994 spent of a USD 63.713 ceiling.
