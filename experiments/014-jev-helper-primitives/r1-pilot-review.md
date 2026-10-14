# 014 – R1 matched pilot: retrospective review (EXPLORATORY; offline; 2026-10-14)

**What this is:** an analysis of the four exported runs of the [R1 matched development pilot](protocol-r1-pilot.md). It is **exploratory and retrospective**: none of it was part of the frozen pilot analysis, and the pilot's frozen findings and scores stand unchanged.

**What it involved:** no agents, no API calls and no ledger changes.

**Reproduce:** [`analysis/r1_pilot_review.py`](analysis/r1_pilot_review.py) (exported artifacts only).

**What happened, in plain language:**
- **Both B helpers did delegate.** For every new requirement, Claude's own code asked Jev about each current register entry and acted on the answers. Most decisions were right: 20 correct amend or retire decisions, no misses, and no wrong retirements.
- **Two kinds of avoidable mistake:** the helpers' broad "does this modify…?" question also caught entries that a new item only *triggers* or *mentions*, and the helpers turned those answers into amendments.
- **The extra cost had little to do with Jev:**
  - B's registers quoted requirement text verbatim from the first stage, before any Jev call;
  - B split each stage into more steps, each carrying a larger context;
  - one helper duplicated every amendment.

  Ordinary CLM paraphrased compactly and did code and register work in the same step.

## 1. The Jev-dependent decisions (both B runs; evaluator truth used after the runs)

**What was reconstructed:** all 288 (new item × current entry) decisions, from each helper's source and its printed log, with the exact question and answer. A decision is "correct" when the helper's action matches the item effect in the evaluator truth (replaces → retire, amends → amend, otherwise keep).

| Class | dev-3 B | dev-4 B | What it is | Likely source |
| --- | --- | --- | --- | --- |
| Correct keep | 175 | 82 | low answers; entry left alone | Jev and the logic both fine |
| Correct amend | 8 | 7 | partial change attached to the right entry | Jev and the logic both fine |
| Correct retire | 2 | 3 | full replacement or withdrawal moved to HISTORY | Jev's "completely replace?" answers (0.77–0.92) |
| Missed, wrongly retired, or replacement kept as amendment | 0 | 0 | — | — |
| **Activation recorded as amendment** | 2 | 2 | a change that *triggers* a dormant obligation (JSON → `exported_by`; a new confidential purpose → `confidential_count`) was appended to the obligation as if it modified it | **question breadth + editing logic.** "Conflict with or modify some part" (dev-3) and "modify, replace, override or withdraw any part … (same topic)" (dev-4) received 0.57–0.86. Strictly, the trigger does not modify the obligation, so this is partly a Jev overcall. But the helpers had no branch for "this makes the entry apply", and appended the item's full text |
| **Viewer change linked to scope** | 2 | 1 | "viewers now export only records they own" amended the scope rule ("other roles only their projects") and, in dev-3, the owner amendment S3.2 | **ambiguous.** The truth says the change affects only the viewer rule, but it does change what the scope rule's "any other role" covers for viewers, and A in dev-4 also merged it into its scope entry. Not counted as a clear Jev error |
| **Change questions applied to initial requirements** | 4 | 0 | dev-3's first helper version asked about stage-1 requirements against each other, and amended 2 entries (answers 0.55–0.67 on unrelated items) | **Claude's helper logic,** with Jev overcalling on a question that should not have been asked. Repaired by Claude's override (step 3) and a helper revision that limits questions to stages ≥ 3 |

**Other observations:**
- **dev-3, stage 7:** Claude's helper sent all CURRENT entries in one request (more than 20 items). The primitive rejected it as `invalid`, the helper logged `FALLBACK:` for S7.2 and S7.3, and Claude retired the withdrawn residency entries by override (step 25). The cause is Claude's helper logic (no chunking); the documented limit was enforced.
- **Claude's overrides (dev-3 only), what each repaired:**
  1. the stage-1 spurious amendments;
  2. the `exported_by` obligation, with the stated reason "S3.1 changes format (S1.1), not the exported_by obligation";
  3. the stage-7 fallback.

  None changed a correct Jev-governed decision.
- **What A did with the same activations:** dev-3 A wrote "Obligation (now triggered by S3.1, applies)", recording activation as a *status*, not an amendment.
- **Correction to the earlier write-up:** it said dev-4 B attached "the residency withdrawal" to the obligation entry. That was wrong. The S7.2 cited there is dev-4's `exported_by` change, a correct amendment, and the residency rule was correctly retired at stage 6.

### Trace 1: activation recorded as amendment (dev-4 B, stage 3; the fictional export-service task)

1. **The new requirement:** S3.1, "Exports are now JSON text…".
2. **The existing entry:** `reg.S2.4`, the dormant obligation "if a later stage changes the export format from CSV, every export … must include `exported_by`".
3. **The question:** "Does the NEW change item modify, replace, override or withdraw any part of this existing requirement (same topic, conflicting rule)?" → **0.69**, a hit.
4. **Then:** "…completely replace…?" → 0.20, so the helper takes its amend branch.
5. **The resulting context:** `CURRENT [S2.4, S3.1] Compliance obligation… AMENDED by S3.1: Exports are now JSON…`. Because S3.1 had hits, the helper did not add it as its own entry, so **the current format rule existed only inside the obligation entry.** (The CSV rule S1.1 was correctly retired: replace 0.85.)
6. **Later:** S7.1 ("records also have `project`") was attached to the same entry. That was correct relative to the entry's contents, because it held S3.1.
7. **The outcome:** the code implemented `exported_by` correctly (64/64), and the current register scorer reported no error. Read by hand, the register states a misleading relationship, though it had no observed downstream effect.
8. **The same case in dev-3:** the trigger was attached the same way (0.85), and Claude reversed it by override at step 11.

### Trace 2: an ambiguous link (dev-4 B, stage 5; the fictional export-service task)

1. **The new requirement:** S5.2, "Viewers no longer receive an error: a viewer now exports only the records they own…, in any project".
2. **The existing entry:** `reg.S1.2`, the scope rule "an admin may export any project; any other role exports only records whose project is in user['projects']…".
3. **The first question:** "modify, replace, override or withdraw any part…?" → **0.80**, a hit.
4. **The replacement question:** 0.16, so the helper amended the entry: `CURRENT [S1.2, S4.2, S5.2] Scope… AMENDED by S5.2: Viewers no longer receive an error…`.
5. **The same request for the viewer rule:** `reg.S2.1` 0.97, then replace 0.83, so it was retired (correct).
6. **The outcome:** the code was correct, and the current scorer reported no error.
7. **Why it is ambiguous:**
   - **For a false link:** the truth labels S5.2 as affecting only the viewer rule.
   - **For a valid link:** the scope rule's "any other role" clause does change for viewers, and ordinary CLM (dev-4 A) put S5.2 in its scope entry too.

   **The evidence does not establish an error.**

## 2. Larger registers and additional work

**Register size, in characters of CURRENT/HISTORY lines at each assessed stage:**

| Run | Stage 1 | 2 | 3 | 4 | 5 | 6 | 7 | Lines at stage 7 (CURRENT / HISTORY) | Verbatim lines | Duplicated amendments | Footer text glued on | Information items as CURRENT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dev-3 A | 715 | 1,341 | 1,599 | 1,789 | 2,089 | 2,244 | 2,356 | 12 / 8 | 0 | 0 | 0 | 0 |
| dev-3 B | 1,363 | 2,716 | 3,794 | 5,142 | 6,639 | 7,404 | 8,211 | 31 / 7 | 38 | 10 | 8 | 3 |
| dev-4 B | 1,075 | 2,279 | 2,889 | 3,441 | 3,891 | 4,026 | 4,372 | 8 / 8 | 16 | 0 | 0 | 0 |
| dev-4 A | 790 | 1,462 | 1,919 | 2,048 | 2,203 | 2,331 | 2,590 | 11 / 11 | 0 | 0 | 0 | 0 |

**What the table shows:**
- **B was already 1.4–1.9× larger at stage 1,** before any Jev call. Both B helpers quoted the requirement text verbatim, while A paraphrased.
- **dev-3 B ended about 1.9× larger than dev-4 B,** because its helper also kept every new item as its own CURRENT entry next to the amendment line (10 duplicates). Its stage-file parser also attached the "Visible tests…" footer and treated "For information:" items as changes.
- **No HISTORY copies of copies** appeared in this pilot. Both helpers retired entries in place. That pattern was the R1 smoke's helper, not these.

**Main-model cost by step role:**

| Run | Helper setup (+ revision) | Helper-call steps | Override steps | Code / inspection / compaction steps | Advance steps | Register-edit steps (A) |
| --- | --- | --- | --- | --- | --- | --- |
| dev-3 A | — | — | — | 6 steps, USD 0.054 | 6, USD 0.071 | 7 steps, USD 0.161 (6,485 output tokens) |
| dev-3 B | USD 0.052 (+ 0.032) | 7 steps, USD 0.133 (3,084 output) | 2, USD 0.075 | **8 steps, USD 0.179** | 6, USD 0.085 | — |
| dev-4 B | USD 0.060 | 6 steps, USD 0.051 (1,367 output) | — | **10 steps, USD 0.232** | 6, USD 0.078 | — |
| dev-4 A | — | — | — | 6 steps, USD 0.058 | 6, USD 0.063 | 7 steps, USD 0.144 (5,574 output) |

(The final step is omitted.)

**What the step roles show:**
- **B's maintenance steps were cheaper than A's register-edit steps.** They had less output, because Claude no longer wrote the register text. That is the work delegation displaced.
- **But B split each stage into more steps:**
  - a helper call;
  - then a code change in a separate step;
  - often a separate compaction step.

  Every step paid for a larger, verbatim register in cache writes and reads.

**Recurring cost per change notice** (stages 3–7, including the advance steps):
- **A:** USD 0.031–0.055;
- **B:** USD 0.061–0.112.

**B's recurring cost was higher at every notice,** so on these traces a longer task would add cost for B faster than for A. **Amortising the setup is not supported** by what was observed.

**Attribution:**

| Behaviour | Source |
| --- | --- |
| A helper call per release that reads and writes the register itself; no caller-written register text | **required by the R1 instruction** |
| Verbatim quoting rather than Claude's summaries (summaries keyed by new id were allowed) | **chosen by Claude** when writing the helpers |
| Separate helper-call, code and compaction steps; inspection prints | **chosen by Claude** (the instruction did not require separate steps) |
| Duplicated amendments, no chunking, footer contamination, information items treated as changes, change questions at stage 1 | **chosen by Claude** in dev-3's helper code |
| The broad "does it modify…?" question, the thresholds, and appending full item text as the amendment | **chosen by Claude** |
| Activation and viewer–scope amendments | **consequences of Jev's answers to those broad questions,** combined with the editing logic above |
| 5 correct retirements, 15 correct amendments | **Jev's answers,** used appropriately |
| Whether the extra steps are a general cost of delegating (verifying what the helper did) or an artefact of these two runs | **not attributable** from n = 2 |
| Whether shorter, summarised entries would have changed Jev's accuracy | **not attributable** |

## 3. Why the register scorer reported no errors

**What `register-checks/1` scores** (unchanged; the original scores stand):
- it checks that each **in-force** item is cited in a CURRENT item, together with its in-force amendments;
- that replaced items are not cited as current without their successor;
- that obligations and exceptions are not lost;
- that the item's probe literal appears in its CURRENT text.

**What it does not score:**
- **extra citations:** a CURRENT item may cite additional items, which is how valid merging looks;
- **claimed relations** ("AMENDED by", "replaced by");
- **information items,** which are unscored;
- **duplication.**

So a misplaced amendment that keeps every item cited and stated passes. Earlier write-ups that said "register harm 0" mean **"passed the current register scorer"**.

**Separating the findings:**

| Kind | Examples | Observed effect |
| --- | --- | --- |
| Redundant but semantically valid | dev-3 B's duplicated amendments; verbatim text; HISTORY entries for notes | size and cost only |
| Misleading relationship | the activation-as-amendment cases (the format rule held inside the obligation entry in dev-4 B); information items labelled CURRENT (dev-3 B); stage-file footer text inside items | **none observed** (the code was correct; nothing later relied on the relationship) |
| Ambiguous | the viewer → scope links | none observed |
| Affected later behaviour | dev-3's stage-1 spurious amendments and its activation amendment: Claude spent override steps repairing them; the stage-7 fallback needed an override | extra steps and cost; final state repaired |

**Checks a revised scorer would need** (described only; not implemented, and old runs are not rescored):
1. **Claimed-relation check:**
   - an explicit relation claim (`AMENDED by N`, `replaced by N`, `superseded … by N`) attached to an item X where N has no effect on X should be flagged as `misleading_relation`. This would catch both dev-4 activation cases;
   - an activation stated as status ("now applies, triggered by S3.1", as dev-3 A wrote) should pass;
   - merged summaries without a relation claim should pass.
2. **Information items presented as CURRENT requirements:** `information_as_current`. This would catch dev-3 B's S3.3, S6.3 and S7.3.
3. **Duplicated statements:** the same item text in two or more CURRENT items should be flagged as `duplicate_statement`, a quality warning, not harm. dev-3 B has 10.

**Each needs labelled examples** in the scorer tests, including the ambiguous viewer → scope case, which should not be flagged as harm.

## 4. Is one follow-up justified?

**The strongest candidate:** a helper that asks a narrower question, separating "does N change the rule stated in X?" from "does N make X apply or relate to it?", and records activation as status rather than as an amendment.

**How it measures up:**
- **What it addresses:** 4 of the 7 questionable decisions (the activations), and possibly the 3 ambiguous links.
- **What Jev would still do:** the same per-entry judgments, with narrower questions.
- **What stays with Claude:** reading the update, implementing the code, writing the helper and its wording.
- **New risks:** more questions per item (latency, more invalid-request risk), and possible under-calls on real amendments.
- **What it does not address: the cost.** The overhead came from verbatim registers, fragmented steps and larger contexts, none of which Jev's question changes. Ordinary CLM can also deduplicate and paraphrase, so fixing those would not establish Jev's value.
- **It would be instruction tuning:** making it happen would mean telling Claude which questions to ask, or rewording the instruction after seeing results.
- **Recurring costs:** B's per-notice costs exceeded A's, so a longer task would not plausibly amortise setup on this evidence.

**Recommendation: B. Further paid work on this configuration is not justified by the current evidence.**
- Delegation works, and its semantic judgments were mostly right. But its observed costs come from how the delegated procedure manages text and steps, not from a Jev limitation that one narrow change would remove.
- Correctness was already at the scorer's ceiling for ordinary CLM.
- This recommendation does not authorise anything. It does not show that Jev cannot help CLM in general.

## 5. Programme status (014)

- **Established:**
  - the mechanism works: Claude's code calls Jev during an execution and edits context with the answers (demonstration);
  - non-delegation happens under a loose instruction (W3 pilot);
  - delegation happens under an explicit contract (R1 smoke and matched pilot);
  - the delegated judgments were mostly correct;
  - in two matched pairs the approach was correct but 61–98% more expensive, mainly through larger, verbatim registers and fragmented steps.
- **Untested:**
  - a workload where ordinary CLM makes register errors;
  - delegation with compact, Claude-summarised entries;
  - other models or effort levels;
  - the revised register checks above.
- **The next step:** none proposed for paid work. The revised scorer checks are the only concrete follow-up, and they are offline.
- **Deferred:** the 008–013 directions (advisory review, edit checking, result screening, Claude-directed screening) stay as concluded in the [programme review](../jev-programme-review.md). They are not reopened.
