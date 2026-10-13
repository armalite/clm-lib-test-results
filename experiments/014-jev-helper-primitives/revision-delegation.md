# 014 – Development revision R1: an enforceable delegation contract (PROPOSED 2026-10-14; not frozen, not authorised, not run)

**Status:** a design for review.
- **The pilot it follows:** the completed W3 development pilot. Its frozen protocol ([protocol-comparison.md](protocol-comparison.md)), its runs and its conclusions are unchanged and are **not replaced** by this revision.
- **What this is:** R1 is a separately labelled *development revision* of condition B only.
- **What is unchanged:** the library, ordinary CLM and condition A. No new workload, scorer or task family is proposed.

## 1. Diagnosis

**What worked:** the integration. Claude wrote helpers, they called real Jev during their own executions (37 calls across 3 B runs), and the edits were validated and reached the next requests.

**What did not happen:** the intended delegation.
- **In every one of the 15 Jev-using executions, the caller supplied the register edits itself:**
  - **dev-1:** an `amendments` dict passed to `regmgr.apply`;
  - **dev-2:** `if l.startswith('CURRENT [S1.2]'): …` replacements followed by `regtool.set_entry`;
  - **the smoke:** literal `CURRENT [...]` / `HISTORY [...]` lines and `reg[i] = …` assignments.
- **The helpers only printed Jev's answers.** Replaying with the answers withheld produced identical context every time.

**What this establishes:** **non-delegation under that instruction and workload.** It is not evidence that answer-driven helpers cannot help.

**Why this was a failure of the configured condition, not a reasonable choice:**
- **In an optional-tool experiment,** Claude declining to delegate would be a legitimate outcome.
- **Here, B was meant to configure delegation.** But the instruction left an open path. It said to use the answers "to decide, for each register item, whether to keep it, amend it or move it to HISTORY". It also said "you may pass the helper text you write yourself", and it never forbade the caller from choosing the affected items.
- **Per-item text addressed to existing items *is* the selection.** So the configured behaviour was under-specified, and the protocol's mechanism criterion correctly reported it as not exercised.

**Example** (dev-1 B, stage 5; `scripts/step-013.py`, `jev_primitive/0012–0013.json`):

| | |
| --- | --- |
| Instruction | "…use clm_jev.judge to find which register items each newly released item affects, and use the answers in the helper's own logic to decide… you may pass the helper text you write yourself." |
| Caller's preselected edits | `regmgr.apply(c, [new items…], {'reg.S1.2': 'HISTORY [S1.2] viewer -> PermissionError; replaced by S5.2.', 'reg.S1.5': 'CURRENT [S1.5, S5.1] …', 'reg.S2.6': 'CURRENT [S2.6, S5.1] …'})` |
| Jev response | for S5.1: `reg.S1.5` 0.95, `reg.S2.6` 0.74; for S5.2: `reg.S1.2` 0.89, `reg.S1.3` 0.89, `reg.S3.2` 0.73 (the last two false positives) |
| Why the write was independent | `apply` writes every `amendments` entry unconditionally. It uses the answers only to `print('JEV FLAG', …)` for items *not* in `amendments`. Any answers produce the same context |

## 2. The contract for the revised B condition (R1)

**The boundary:**

| | Who | What |
| --- | --- | --- |
| Input | Claude (the caller) | the newly released stage (its number or file path); optional general parameters (thresholds, question wording); optional text **about the new items, keyed only by the new item ids** and never naming existing register items |
| Read | the helper | the current register from `context.json` itself, not from caller arguments |
| Judge | the helper → Jev | questions about the relationship between each new item and current register items |
| Decide | the helper's code | keep, amend or retire each register item, **governed by the returned judgments** |
| Write | the helper | `context.json` through the existing CLM mechanism (ordinary runtime validation; the edit appears in the next request) |

**Forbidden to the caller in R1:**
- a list of affected register item ids;
- per-item edits of existing register items;
- writing register items directly.

This restriction belongs to condition R1 only. It is not a library rule and does not apply to A or to ordinary CLM.

**Not provided to Claude:** a reference helper, the affected-item mappings, or any truth. Claude writes its own procedure, questions and thresholds.

**How replacement content is formed.** Jev returns judgments, not prose. The helper may use any of these; which one it used is reported:
1. **Quoting the update:** each stage file lists items as `- [Sk.n] text`, which code can parse, so a new CURRENT item can be `CURRENT [Sk.n] <quoted text>`.
2. **Keeping the old text with an explicit amendment:** for example `CURRENT [S1.3, S3.2] <old text> Amended by S3.2: <new text>`.
3. **Relabelling a retired item:** `HISTORY [S1.2] <old text> (replaced by S5.2)`.
4. **Text Claude writes about a new item:** keyed by the new id. This summarises the *new* item, but must not say which existing items it affects; otherwise the candidate preparation would already be the selection.

**What stays with Claude:**
- **Reading the notice and the context:** the notice enters the working context on release, so Claude has already read and paid for it before any helper call.
- **Implementing the code change,** which needs the same understanding of what changed.
- **Writing and maintaining the helper,** and optional summaries of new items.
- **Handling fallbacks and overrides.**

Delegation in W3 can therefore move the **register's selection and edits** into code. It cannot move Claude's **understanding** of the update, which the code change needs anyway.

**Fallback and overrides:**
- **When to fall back:** if Jev fails, or the helper cannot resolve an item.
- **What the fallback does:** the helper may add the new item as CURRENT and leave the other items unchanged, and must print a line starting `FALLBACK:`.
- **Overrides:** a later correction by Claude goes only through a helper function that prints `OVERRIDE:` with the item ids and the reason.
- **How they count:** both are allowed and reported separately. **Neither counts as delegation.** Nothing requires an edit merely to show dependence, or blind trust in Jev.

**What R1 adds over ordinary CLM:**
- a mandatory helper call per release;
- restricted caller arguments;
- no direct register writes;
- labelled fallbacks and overrides.

**What a future comparison would mean:** this deliberately configured approach against ordinary CLM, not a test of whether Claude would delegate unprompted. **Successful delegation would not imply savings:** it may cost more, or make worse edits than Claude would.

## 3. Proposed R1 instruction for B (exact text, for review)

```
CONFIGURED JEV-DELEGATED REGISTER MAINTENANCE (this run only; development revision R1):
- Write and save in /task/workspace a reusable Python helper that maintains your requirements
  register, and call it once each time a stage is released. Pass it only the newly released
  stage (its number or the path of its REQUIREMENTS.md) and, if you want, general parameters
  such as thresholds or question wording, and text you write about the new items keyed by the
  new item ids.
- The helper itself must read the current register from context.json, use clm_jev.judge to ask
  how each newly released item relates to the current register items, and let those answers
  decide which register items are kept, amended or moved to HISTORY. It then writes
  context.json.
- In this run that selection is the helper's job: do not pass the helper, or write yourself, a
  list of affected register items or edits to existing register items, and do not name
  existing register items in text you pass about new items.
- If Jev fails or the helper cannot resolve an item, the helper may add the new item as CURRENT
  and leave other items unchanged; it must then print a line starting "FALLBACK:" with the
  reason. If you later decide a register item is wrong, correct it only through a helper
  function that prints a line starting "OVERRIDE:" with the item ids and the reason.
- You choose the questions, thresholds and wording, and you may improve the helper between
  stages. Your changes to the exporter code are not affected by this.
```

**How it differs from the pilot's instruction:**
- it defines the caller's inputs;
- it requires the helper to read the register itself;
- it forbids caller-side selection;
- it defines labelled fallbacks and overrides.

It contains no ids, mappings, thresholds, wording or truth. A, if it is ever run again, keeps no extra instruction.

## 4. Illustrative worked example (hypothetical; not run, not real Jev output)

The inputs are taken from `w3-dev-1` stage 3. The register excerpt before the update:

```
CURRENT [S1.2] Viewers raise PermissionError; nothing is exported.
CURRENT [S1.3] Admin: any project; other roles only records whose project is in user['projects'].
CURRENT [S2.4] Obligation: if the format leaves CSV, every export includes exported_by = user name.
```

1. **The caller:** `reghelper.update(stage=3)`.
2. **The helper parses** `- [S3.2] Users whose role is neither 'admin' nor 'viewer' may now also export the records they own…, even outside their projects.`
3. **Q1,** one call with 3 items: "Does the new item change any part of the requirement in this entry?". *Hypothetical* answers: S1.2 0.21, S1.3 0.86, S2.4 0.06.
4. **Q2,** asked only for S1.3: "Does the new item replace the whole requirement in this entry, leaving no part in force?". *Hypothetical* answer: 0.12.
5. **The helper's own rule** (Q1 ≥ 0.5 and Q2 < 0.5 → amend; both ≥ 0.5 → retire; Q1 < 0.5 → keep) writes:
   `CURRENT [S1.3, S3.2] Admin: any project; other roles only records whose project is in user['projects']. Amended by S3.2: …own records even outside their projects.`
   S1.2 and S2.4 are left unchanged.

**What a wrong judgment would do:** a *hypothetical* Q2 of 0.80 would retire S1.3 to HISTORY. The register scorer would then report `incorrect_retirement` independently, and the replay with substituted answers would show which answer caused it.

## 5. The context-budget change (8,000 → 12,000), explained

**Where it was recorded before any paid call:**
- in the `configs/exp014c.toml` header comment, written during the offline development;
- in `protocol-comparison.md` §5, frozen before the smoke;
- in freeze record 1, which carries the config's SHA-256 prefix `c78388dee58e909c`.

`configs/exp014.toml` itself is unchanged.

**Why it was changed:**
- **The draft's figure was too small:** the design draft had estimated 5,430 tokens on the hand-written example.
- **The implemented W3 is larger:** a scripted offline probe (verbatim register, about 3,000 characters of code and 3,000 of output per step, transcript pruned) peaked at **about 7,800** estimated tokens.
- **The probe measured what the runtime measures:** it used the requests' `est_input_tokens`, which is the same estimate `prepare_request` uses for pressure (system prompt plus the user message with its status line).
- **The real runs agreed:**
  - A: 6,082 and 5,730;
  - B: 7,302 and 8,217;
  - the B smoke: 7,576.

**What 8,000 would have done:** at 8,000 the runtime signals pressure at ≥ 5,600. Above the hard limit of 7,000, it first spills the latest large entry to a workspace file, then gives one recovery request. It stops the run only if a request exceeds 8,000, or is still over 7,000 after that recovery opportunity.
- **It would not have prevented valid operation.** A compact register with a pruned transcript fits under 7,000 (A's peaks were 5.7–6.1k).
- **It would have triggered routine pressure notices,** and for B (larger helper code in its steps) spill and recovery requests. That is normal CLM context management, not failure.

**The honest reason for the change:** to avoid that routine pressure, which falls unevenly on the two conditions.

**Recommendation for R1: keep 12,000.**
- **The R1 smoke asks whether the helper's selection follows Jev's judgments.** Pressure notices are runtime-supplied prompts with a second trigger for edits, and would confound that attribution.
- **12,000 also keeps R1 comparable with the pilot's B runs.**
- **The register remains actively maintained at 12,000:** it is the object of study, so context management is not avoided.
- **A future A/B comparison** should use one budget for both conditions. It should state that pressure-triggered management is outside its question, and report pressure steps. Testing 8,000 would be a separate, declared condition, not a silent change.

## 6. Measurement for R1 (pilot replay evidence kept as is)

1. **The helper consumes the judgments in its selection logic:**
   - **A static audit** of every script that writes `context.json`: flag string literals that are register items (`CURRENT [` / `HISTORY [`), and caller arguments naming earlier item ids or register entry ids.
   - **A source check of the helper:** it reads the register from `context.json`, and its keep/amend/retire branches depend on `answers`.
2. **Substituted judgments change the selection, not just the control flow** (offline replay, sandbox, no paid calls, originals untouched):
   - **(a) recorded:** must reproduce the accepted revision.
   - **(b) withheld:** must take the declared `FALLBACK:` path with exit 0. A crash, an early exit or an unchanged context is reported as such, not as selection.
   - **(c) permuted:** each request's answers are rotated across its items, so different items cross the helper's threshold.
   - **What counts as substantive:** `substantive` requires label or content changes. Under (c), every changed register item must correspond to an item whose submitted judgment changed. Marker-only differences stay `marker_only`.
   - **To build:** variant (c) and the per-item consistency check are small additions to `replay.py`, implemented only if R1 is authorised.
3. **The actual edits are scored independently:**
   - `register-checks/1` at every assessed stage;
   - each Jev-governed edit classified against the evaluator truth after the run (correct amend, correct retire, correct keep, incorrect retirement, missed amendment);
   - Jev's own true and false positives;
   - the code by `export-checks/2`.
4. **Reported separately:**
   - `FALLBACK:` lines and Jev error statuses;
   - `OVERRIDE:` lines;
   - register writes by the caller that the audit flags;
   - edits made either way (transcript pruning).

   None of these counts as delegation.

**Never used in the helper or replay inputs:** hidden answers, mappings or probes. Substituted answers are derived only from the recorded answers.

## 7. Is one configured smoke worth it?

**It would meaningfully test the missing behaviour:** whether, under an explicit contract, Claude writes a procedure whose own Jev-governed selection produces register changes. It needs **no new workload:** `w3-smoke-1`, 5 stages, a development instance.

**It would not test benefit,** and a positive smoke would not imply savings.

**Proposed:** one R1 B smoke on `w3-smoke-1` with `configs/exp014c.toml` (budget 12,000; primitive 8/40/20), the R1 instruction above, and prompts otherwise unchanged. It would need its own frozen protocol section, and authorisation.
- **Estimate:** USD 0.25–0.40 (the pilot's B smoke cost USD 0.246; the R1 helper will be larger and make more Jev calls), plus under USD 0.005 for TypeSafe.
- **Authorisation:** USD 1 would cover one attempt, plus one more only after a genuine harness defect.

**Exact success criteria** (frozen before the run; all three needed):
1. **Contract held:**
   - in every Jev-using execution, the static audit finds no caller-supplied affected ids, per-item edits or direct register writes, except labelled `OVERRIDE:` calls;
   - and the helper reads the register from `context.json`.
2. **Reproducible:** the replay (a) reproduces every Jev-using execution.
3. **Delegated:**
   - at least 2 of the 3 change notices (stages 3–5) have an execution classified `substantive` under (b) or (c), with every changed item consistent with a changed judgment;
   - and under (b) the helper takes its declared fallback path with exit 0.

**Reported but not criteria:**
- code correctness;
- register harm and the correctness of the Jev-governed edits;
- fallback and override counts;
- cost, time, calls and Jev usage.

**If the smoke fails:** the result is recorded and R1 stops. There is no further rewording of the instruction to obtain delegation.
