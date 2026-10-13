# 014 – Comparison phase protocol: Jev-assisted register maintenance on W3 (FROZEN 2026-10-14, before any paid call of this phase)

**Status:** frozen for the **development smoke and the four-run development pilot only**. The 32-run evaluation is proposed, not authorised. This phase is separate from 014's completed prompted demonstration ([protocol.md](protocol.md)), which is unchanged.
- **History:** this file replaces the unfrozen design draft of the same day, whose inspection and measurements are kept in sections 1–2 below. Any later change is appended as a dated "freeze record" at the end. Nothing above it is edited.

**The question:** does a **configured Jev-assisted approach** change correctness, cost or time against **ordinary CLM**? In that approach, Claude writes a reusable context-management procedure whose code calls Jev during the same execution and uses the answers to maintain a requirements register. And did B's helper actually make register changes that depended on Jev's answers?

**Approved design decisions (2026-10-14):**
1. **Same objective:** both conditions receive the same requirements-register objective.
2. **A is ordinary CLM:** CLM with helper capabilities; it chooses its own approach. No algorithm, no repeated full rewrites and no extra review steps are required of it.
3. **B:** the same task, plus the Jev primitive and a declared instruction to use it within a reusable context-management procedure.
4. **What is compared:** the complete configured approach against ordinary CLM. The comparison does not isolate Jev from the effects of the procedure instruction.
5. **The demonstration** stays unchanged and separate.

**The mechanism (B):**
1. Claude writes code.
2. That code calls `clm_jev.judge` during its own execution.
3. The same code uses the answers.
4. The code edits `context.json`.
5. The runtime validates the edit as usual.
6. The edited context appears in the next request.

There is no Claude review or confirmation turn, and no host-authored semantic edit.

## 1. What the demonstration showed (inspection, unchanged from the draft)

**What depended on Jev in the demonstration:** only which notes carried a fixed review prefix.

**What would have been identical without Jev's answers:**
- the notes, all of which Claude wrote itself;
- the transcript removal;
- the scripts' filters.

**What limited it:**
- **The helper's design:** its only action was the marker; a substring test for "historical" exempted a whole current note; and it asked one yes/no question per multi-rule note.
- **The instruction:** a per-note yes/no question, with no structure for the context.
- **The workload:** W2 has few rules, its changes name what they replace, and the code is the real state.

## 2. What ordinary CLM spent on maintenance (recorded runs, unchanged from the draft)

[`analysis/displaceable_work.py`](analysis/displaceable_work.py) reads exported runs only.

**How much of the output was maintenance text:**
- **Most of it, in some runs:** in 8 of 12 incident-workload runs, model-written note text was 42–76% of the output tokens, because Claude rewrote one cumulative note every round.
- **Much less with other strategies:** 13–15% in the append-only incident runs, and 7–11% on W2.

**Total cost did not follow it:** the append-only runs were not cheaper in total.

**Stale facts:** no earlier workload recorded a stale-fact error.

## 3. The workload: W3 (`export-gen/2`)

**Implementation:** `src/clm_lib/w3.py` in clm-lib. It extends W2's records-export service and reuses W2's tooling: staged release, read-only fixtures, visible tests per stage, hidden checks, and workspace snapshots at each release.

**Stages:** two stages of initial requirements, then five change notices (seven stages).
- Every requirement, change and note carries a visible item id (`S<stage>.<n>`).
- **Notice items do not say which earlier item they affect.** A change wins over anything earlier that it conflicts with, and everything it does not change stays in force.
- Notices have a "Changes" section and a "Notes" section (decision records and information).

**Relationships, varied per instance:**
- full replacements: CSV → JSON, and the viewer error → own records;
- partial amendments (scope, status, the confidential exception, date filter, region, record limit, titles, the `exported_by` obligation), including an amendment of an amendment (JSON records gain `project`);
- a withdrawal (the residency rule);
- an exception that is widened but survives;
- two obligations stated early that apply only once later items trigger them, and are never restated: `exported_by` when the format leaves CSV, and `confidential_count` when confidential records can be exported for a non-audit purpose;
- decision records that stay true as history;
- information items that share terminology with a requirement without changing it.

**What is visible to the agent:**
- the stage documents (each also added to the working context on release, as in W2);
- the visible tests for the latest stage;
- earlier stage files, which stay readable in both conditions;
- the task prompt.

**Evaluator-only** (host memory until scoring; never in prompts, fixtures, the workspace or Jev payloads):
- item effects;
- register truth per stage;
- semantic probes;
- hidden code checks.

**Instances** (seeds and values are fixed by the generator):

| Instance | Role | Seed | Stages | Items per stage (module + version; D = decision record, I = information) | Values |
| --- | --- | --- | --- | --- | --- |
| `w3-smoke-1` | B smoke only, never compared | 8701 | 5 | 1: FORMAT1, SCOPE1, CONF1, D · 2: STATUS1, BY1, TITLE1 · 3: FORMAT2, SCOPE2, I · 4: STATUS2, TITLE2, D · 5: CONF2, BY2 | regulator, ch, 30 |
| `w3-dev-1` | pilot | 8501 | 7 | 1: FORMAT1, VIEWER1, SCOPE1, STATUS1, CONF1, D · 2: SINCE1, REGION1, LIMIT1, BY1, TITLE1, CC1 · 3: FORMAT2, SCOPE2, I · 4: STATUS2, REGION2, TITLE2 · 5: CONF2, VIEWER2, D · 6: BY2, LIMIT2, I · 7: FORMAT3, REGION0, I | litigation, ch, 25 |
| `w3-dev-2` | pilot | 8502 | 7 | 1: FORMAT1, SCOPE1, STATUS1, SINCE1, TITLE1, D · 2: VIEWER1, CONF1, LIMIT1, BY1, CC1, REGION1 · 3: FORMAT2, SINCE2, I · 4: CONF2, SCOPE2, D · 5: STATUS2, VIEWER2, LIMIT2 · 6: REGION0, I · 7: FORMAT3, BY2, D | legal, eu, 25 |

**Sizes:**
- **Hidden code checks:** 64 per development instance, plus 112 snapshot checks.
- **Per notice:** 1–3 items of the register in force are affected: 6–27% of items in the development instances (counting activations), and 22–50% in the smaller smoke instance.
- **The register at stage 7:** 17 CURRENT and 7 HISTORY items if kept one per item, about 4,100 characters verbatim.

**The register objective,** in the task prompt and identical in both conditions:

```
Requirements register (part of this task): keep, in your working context (context.json), a
register of the requirements. A register item starts with CURRENT or HISTORY at the start of an
entry body or of a line, cites in square brackets the item ids it covers (for example
[S1.3, S3.2]), and states what they say. CURRENT items state what is in force now, including
every part of an earlier item that later changes left in force. HISTORY items record items that
were replaced or withdrawn, and decision records. You decide how to organise, merge, word and
update the register, and how to maintain it. It is checked after you have processed each stage:
when you release the next stage, and at your final answer.
```

It prescribes labels and citations so that the register can be scored. It does not prescribe a helper, an algorithm, the wording, or any mapping.

## 4. Conditions and instructions

| | A: ordinary CLM | B: configured Jev-assisted approach |
| --- | --- | --- |
| Mode | `clm_helpers` | `clm_helpers` with `--jev-primitive on` |
| Task prompt (with the register objective), fixtures, source access, visible tests | identical | identical |
| System prompt | the ordinary CLM prompt (prompt version `2026-10-13.8`) | the same plus `JEV_PRIMITIVE_CLAUSE`, which describes `clm_jev.judge` and says its use is optional |
| Extra instruction | none (`run.json → extra_instruction` is null) | [`comparison-instruction-b.txt`](comparison-instruction-b.txt), SHA-256 prefix `1064862cd4246ffe`, appended to the task text and recorded in `run.json` |
| Model, effort, caching, layout, limits, budget, sandbox | identical (`configs/exp014c.toml`) | identical |

**B's instruction** (verbatim):
```
CONFIGURED JEV-ASSISTED CONTEXT MANAGEMENT (this run only):
- Maintain your requirements register through a reusable Python helper module that you write and
  save in /task/workspace, and use it each time a stage is released.
- Inside the helper, use clm_jev.judge to find which register items each newly released item
  affects, and use the answers in the helper's own logic to decide, for each register item,
  whether to keep it, amend it or move it to HISTORY. You choose the questions, thresholds and
  how new register items are written; you may pass the helper text you write yourself.
- You may improve the helper between stages.
```

**The only differences between the conditions:**
- the primitive is on;
- `JEV_PRIMITIVE_CLAUSE` is in the system prompt;
- the instruction above.

**What the instruction adds:**
- the use of a reusable procedure, and of Jev within it, so the effects of the two cannot be separated (decision 4);
- **no task information** (no ids, mappings, thresholds, wording or truth);
- **no review or confirmation turns.**

**A may write helpers too;** helper use is recorded in both conditions.

## 5. Settings and source

**Config:** `configs/exp014c.toml`, identical to `configs/exp014.toml` except:
- **Ceiling:** 87.535602.
- **`context_budget_tokens` 12000 (was 8000):** a scripted offline probe, with a verbatim register, about 3,000 characters of code and 3,000 of output per step, peaked at about 7,800 estimated tokens. That is above the 8,000 budget's 70% pressure line (5,600), but under 12,000's (8,400), with no pressure steps.
- **`[jev_primitive]` 8 calls per execution and 40 per run (was 4 and 30):** a register of about 25 items needs 2 calls per question.

**The other settings:**
- **Main model:** `claude-opus-5-5`, effort low, structured output.
- **Caching:** prompt caching on (5-minute TTL), with `blocks/1` and `run-tag/1` isolation.
- **Limits:** 90 calls; a 30 s execution timeout; a 6,000-character output cap.
- **Jev:** `jev-1.13.0`, with a 15 s host timeout and 1 retry, every attempt ledgered; USD 0.042 per million input tokens, output free.

**Scorers:** code `export-checks/2`; register `register-checks/1`; replay `jev-replay/1`.

**Source:** clm-lib HEAD `0fb0334` plus the uncommitted 014-comparison implementation. The fingerprint is in the freeze record at the end of this file.

## 6. Scoring and measurements (frozen)

**Code** (`export-checks/2`, hidden checks in a fresh sandbox after the run):
- **Strict success:** all checks pass.
- **Checks by category:** retained, exception, replaced, amended, kept_part, deferred, interaction.
- **Stale results:** an output that matches the rule's previous version.
- **Snapshots** at each release.
- **Regressions.**

**Register** (`register-checks/1`):
- **When:** stage k is assessed on the accepted revision live **when the agent releases stage k+1**, after it has had its turns to process stage k. The last stage is assessed on the revision live **at the accepted final answer**. A missing assessment, such as one lost to an early stop, is reported as missing.
- **Which items count:** only lines that start with CURRENT or HISTORY, in entries the runtime did not write. Merged items, a single note with CURRENT/HISTORY sections, and replaced items cited in a CURRENT item together with their successor are all accepted.
- **Categories per released item:**
  - `retained`;
  - `amended_ok`;
  - `represented_uncited`;
  - `history_kept`;
  - **harm:** `stale_superseded`, `stale_unamended`, `lost_obligation`, `lost_exception`, `incorrect_retirement`;
  - **history errors:** `history_as_current`, `history_lost`;
  - **incomplete:** `omitted`, and `content_missing` (cited, but the CURRENT text lacks the item's distinctive literal, such as a field name or value).
- **Its limits:** labels, citations and probe literals are evidence of meaning, not proof of it. **The final register of every pilot run is also read by hand,** and any disagreement with the scorer is reported.
- **Kept apart:** register errors are kept separate from code failures and from harness defects.

**Jev dependence** (`jev-replay/1`, offline; `clm-lib replay-jev <run dir>`):
- **The method:** each B execution that called Jev is re-executed in the sandbox:
  - on an isolated copy of the recorded pre-execution workspace (`workspace_pre/step-NNN.json`);
  - with the fixtures as released at that step;
  - with scripted responses: (a) recorded, which must reproduce the accepted revision; (b) withheld (an error status, no answers); (c) inverted (1 − p).
- **Safeguards:** no paid calls; original artifacts are not modified.
- **Classes:**
  - `substantive` (label or content changes);
  - `marker_only`;
  - `no_register_dependence`;
  - `crash_without_answers` and `no_edit_without_answers`, reported separately and **not** counted as substantive;
  - `not_reproduced`.
- **What it shows:** dependence of the helper's behaviour on its inputs, not correctness or benefit.
- **Edits made either way** (for example transcript removal) are listed as independent of the answers.

**Also reported per run:**
- **Totals:** cost by provider; elapsed time; main-model calls (actions, repairs, retries); executions.
- **Tokens:** uncached input, cache reads and writes, output.
- **Jev:** calls, items, latency, failures and cost; the questions, submitted items and answers.
- **Helpers:** creation, revision and reuse.
- **Requirement rereads:** executions whose code opens requirement files, from the runtime's `requirement_reads`, plus a scan of the scripts for earlier stage folders.
- **Extra work:** pressure steps, spills and repairs.
- **Maintenance text:** model-written register characters per accepted edit.

**Interpretation:** Claude has already received its context and the latest update before it writes a helper call, so no saving of that input is credited to Jev.

## 7. Live sequence, budget and rules

**Budget:**
- **At the start:** spent USD 84.535602.
- **The authorisation:** USD 3 new, both providers, including smoke, pilot and retries, with earlier unused allowances not stacked. The new ceiling is **87.535602**, set with `budget --set-ceiling` before the first call.
- **Before each run:** the remaining allowance must be at least USD 0.60, otherwise stop and report. This allows for a W3 run of about USD 0.25–0.40, estimated from W2's USD 0.155 per 5-stage run. The ledger's per-request reservations still apply.

**The sequence, each run once:**
1. **B smoke** on `w3-smoke-1`.
2. **Pilot,** `w3-dev-1`: A, then B.
3. **Pilot,** `w3-dev-2`: B, then A.

**The commands** (the key file is loaded in the same shell; credential values are never printed):
```
clm-lib --config configs/exp014c.toml run --task w3-smoke-1 --mode clm_helpers --jev-primitive on --extra-instruction-file <comparison-instruction-b.txt> --label "014 comparison: B smoke (configured; excluded)"
clm-lib --config configs/exp014c.toml run --task w3-dev-1 --mode clm_helpers --jev-primitive off --label "014 comparison pilot: A dev-1 (position 0)"
clm-lib --config configs/exp014c.toml run --task w3-dev-1 --mode clm_helpers --jev-primitive on --extra-instruction-file <...> --label "014 comparison pilot: B dev-1 (position 1)"
clm-lib --config configs/exp014c.toml run --task w3-dev-2 --mode clm_helpers --jev-primitive on --extra-instruction-file <...> --label "014 comparison pilot: B dev-2 (position 0)"
clm-lib --config configs/exp014c.toml run --task w3-dev-2 --mode clm_helpers --jev-primitive off --label "014 comparison pilot: A dev-2 (position 1)"
```

**Rules:**
- **Every attempt is kept and exported.** There are no silent replacements, no cherry-picking, and no repeats to obtain substantive use or a positive outcome.
- **A genuine harness defect** is a runtime, scorer or recording fault that invalidates the run's evidence; agent choices do not count.
  - The attempt is kept and the defect documented.
  - It is fixed and re-verified offline, and a new freeze record is appended before any further call.
  - A further smoke attempt must stay within the same USD 3 and must not be used to tune for a result.
- **Not invalid runs:** ordinary agent mistakes, poor helper choices, task failures, an unused or marker-only primitive, a register not followed, and running out of calls are all results.
- **B's instruction is never strengthened** after seeing the results. If Jev is unused or marker-only, that is recorded and the phase stops before the evaluation.
- **Reruns** happen only after an infrastructure failure before the first model response (once, both kept), or after a genuine harness defect.

## 8. Readiness, mechanism and analysis

**Offline readiness:** confirmed before this freeze; see the freeze record.
- **Task and scorer:** the reference matches an independent implementation on every hidden and snapshot check. The visible tests pass on it, and it is strictly successful in the sandbox. Targeted faulty solutions each fail their category: a forgotten rule, a stale previous version, an amendment applied as a replacement, a lost exception, and a lost obligation, which fails only the obligation checks.
- **Register scorer:** correct registers in three representations score no error at every stage of every instance. Planted faults are each detected: stale superseded, stale unamended, incorrect retirement, lost obligation, lost exception, history as current, content missing, and omitted.
- **Assessment timing:** tested with a scripted run whose register stops being updated after stage 3. Stages 1–3 are clean and stages 4–5 show harm.
- **Information boundary:** no evaluator field, hidden case, effect or probe appears in the prompts, fixtures, stage texts or requests. Jev receives only what B's code sends, and the host adds nothing (§25 of the clm-lib SPEC).
- **Jev batching and limits:** over-limit and invalid requests get explicit error responses, never silent omissions. A stage-7 register fits in 2 calls per question within 8 per execution.
- **Request size and pressure:** understood (section 5).
- **Replay:** a scripted B run is reproduced and classified (`substantive`, and `marker_only` for a marker helper), with the run folder byte-identical afterwards.
- **Historical compatibility:** the full test suite passes. All new behaviour is opt-in (W3 tasks, the `replay-jev` command, exp014c), and earlier configs, prompts and evidence are unchanged.

**The mechanism is counted as exercised in a B run when:**
- a helper is created and reused at two or more stage updates;
- Jev is called in two or more executions;
- every Jev-using execution is reproduced by the replay;
- at least one execution is classified `substantive`.

This is reported per B run. It decides nothing automatically: the evaluation remains unauthorised.

**Pilot analysis** (descriptive only; no inferential claims from 2 instances):
- per run and per A/B pair: the measurements in section 6;
- B's Jev-dependent edits, listed with their correctness against the truth (evaluator-only, after the run);
- one traced example: update → Jev judgment → helper decision → accepted context → next request.
- **If every run is correct,** efficiency is still reported, and no accuracy advantage is claimed.
- **If B is worse,** that is reported and explained.

**A future evaluation (proposed, not authorised):** 8 fresh instances × 2 repetitions × A/B = 32 runs. These sizes are a **practical exploratory choice** (cost about USD 9–14), **not a powered design**, and no detectable effect size is claimed. Its instances would be generated afterwards and not opened before its own freeze.

## Freeze records

_(Appended below; earlier records are never edited.)_

### Freeze record 1 (2026-10-14, before the B smoke; no paid call of this phase made yet)

- **Source:** clm-lib HEAD `0fb0334` plus uncommitted changes.
  - **Tracked diff** (`git diff HEAD`): SHA-256 prefix `c90dc1265b38789a`. This includes the session-18 documentation edits.
  - **File prefixes:**
    - `w3.py` `67cf4b38ddc50afd`;
    - `register_score.py` `e77cbc1ab5d2d375`;
    - `replay.py` `a42701815672bb00`;
    - `runner.py` `a8aecb8ec383c3dd`;
    - `tasks.py` `331314ad26a5bdfb`;
    - `cli.py` `3431bb9e4972223e`;
    - `jev_primitive.py` `3408dee1dd1a9e81` (unchanged since the demonstration);
    - `executor.py` `34d8416b757ac037` (unchanged);
    - `prompts.py` `01375b848c223f50` (unchanged; prompt version `2026-10-13.8`);
    - `configs/exp014c.toml` `c78388dee58e909c`;
    - `tests/test_w3.py` `18d34e47cbf5b419`;
    - `tests/w3_solutions.py` `b5456c3f928da09a`.
- **B instruction:** `comparison-instruction-b.txt`, prefix `1064862cd4246ffe`.
- **Verification:**
  - ruff and ruff format are clean, and mypy reports no issues in 33 source files;
  - pytest: **291 passed** (all, Docker-backed included), with 21 new W3 tests;
  - the offline readiness items in section 8 are confirmed.
- **Fixture fingerprints:** `w3-smoke-1` `021c631ee4b3e70c`, `w3-dev-1` `301baf8a5ae90300`, `w3-dev-2` `3dacfbcd3aa25795`. The W3 task prompt prefix is `e7dd6a71e096f7c7`.
- **Ledger before the ceiling change:** spent USD 84.535602, ceiling 85.351732.

### Result record (appended after the runs; nothing above was changed)

- **Runs** (each once, in the frozen order; no retries, reruns or harness defects):
  - **smoke B:** `20261013T143429-clm_helpers-cacheon-jprim-w3-smoke-1-8797`;
  - **dev-1 A:** `20261013T143716-clm_helpers-cacheon-w3-dev-1-495e`;
  - **dev-1 B:** `20261013T143929-clm_helpers-cacheon-jprim-w3-dev-1-4a83`;
  - **dev-2 B:** `20261013T144206-clm_helpers-cacheon-jprim-w3-dev-2-d925`;
  - **dev-2 A:** `20261013T144446-clm_helpers-cacheon-w3-dev-2-36fe`.

  The run ids carry the machine clock (UTC).
- **The smoke** exposed no harness defect: the recording, scoring, replay and accounting were complete. Its helper printed Jev's decisions and Claude wrote the edits. That is agent behaviour, recorded as such, and **B's instruction was not changed.**
- **Outcome:** all 5 runs code-correct, and register harm 0 at every assessed stage.
- **Mechanism:** Jev was called in every B run (9, 17 and 11 calls). The replay reproduced all 15 Jev-using executions, and **all were `no_register_dependence`.** **The mechanism was not exercised** under the criteria of section 8.
- **Cost:** B minus A was +USD 0.060 (+19%) and +USD 0.096 (+32%).
- **Spend:** USD 1.646743 for the phase. The ledger moved from 84.535602 to 86.182345, against the 87.535602 ceiling.
- **Next:** the phase stops before the evaluation, which is not run.
- **Details:** in the [README](README.md#comparison-phase-w3-development-pilot-results).
