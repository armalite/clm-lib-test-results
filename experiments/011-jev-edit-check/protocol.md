# 011 – Planned protocol: Jev check of a proposed context edit (strategy 3)

**Status: PLANNED. Not implemented, not run, and no paid calls are authorised.** Written on 2026-10-13 as part of the [roadmap](../jev-assistance-roadmap.md). Any implementation would first freeze a revised version of this protocol and a new diagnostic.

## Question

**Before Claude applies a context edit, does a Jev check for narrow, specific risks help Claude catch mistakes in the edit?**

## Design

**Both arms get a defined check opportunity.**
1. When Claude's code writes a `context.json` that is valid and **removes or rewrites** at least one entry, the runtime holds it as a *proposed* revision instead of committing it at once.
2. The next observation shows the proposed change: the removed and rewritten entries, before and after.
3. Claude replies `apply`, revises the edit, or withdraws it.

Edits that only add entries are committed as today.

**The arms:**
- **A (control):** the same check opportunity, without Jev.
- **B (assisted):** the same, plus Jev's answers to a few narrow questions about the proposed change.

**The Jev judgment, which is new and untested:** it differs from affected-entry detection, so **the 008/009 question is not assumed to work for it**. Candidate questions, each one narrow yes/no:
1. **Lost requirement:** per removed or rewritten entry, "Does the proposed revision omit a fact, requirement or planned action from this entry that no later update has superseded?"
2. **Stale carry-forward:** per kept or rewritten entry, "Does this entry still assert something that a recent update has superseded?" The recent updates would be the released payloads since the last check.

| | |
| --- | --- |
| **Trigger** | Every valid proposed edit that removes or rewrites entries |
| **Information: Claude** | Its context, the proposed diff, and (B) Jev's answers |
| **Information: Jev** | The old entry text, the proposed replacement text (or "removed"), and the recent released updates. Never future rounds, truth or deleted history beyond the entry being removed |
| **Who edits** | Claude: apply, revise or withdraw. Jev never approves or rejects |
| **Overhead** | One extra Claude turn per checked edit in **both** arms (pilot runs made 11–15 edits, so this could add about a third more calls), plus Jev calls in B |

## Possible failure modes

- **False alarms** cause churn: Claude revising correct edits.
- **Anchoring:** Claude applies everything Jev does not flag.
- **Compound questions:** "omits something still current" mixes recall with currency. This may need splitting.
- **Request size:** large rewrites may exceed batch limits.
- **Overhead in both arms** may dominate any benefit.

## Diagnostics before any agent run

- **A fresh labelled set**, for example `jev-diag/3`: (old entry, proposed revision, recent updates) triples, with labels for each question, written before any Jev answer.
- **Sources:** realistic edits taken from existing CLM traces, mutated to include both risks and correct edits.
- **Readiness:** the strategy is not ready for an agent pilot unless the component shows useful separation at a pre-fixed threshold.

## Outcomes

- **Primary:**
  - strict success, especially omissions and stale facts;
  - all-attempt cost.
- **Secondary:**
  - edits revised or withdrawn after the check in each arm;
  - calls and time added by the check;
  - Jev latency and cost.

## Limitations

- **The check opportunity itself is an intervention**, and its overhead is measured in both arms.
- **Scope:** the same task family and model as 009.
- **Not comparable across experiments:** results are not comparable with strategies 1 and 2 without a [common-workload comparison](../jev-assistance-roadmap.md#order-and-gating).

---

# Component diagnostic protocol (2026-10-13, session 8, written before any case labels, code or paid call)

_The planned design above is kept as written. This section covers **only** an offline-designed, live Jev **component diagnostic**. No agent integration, edit blocking or end-to-end run is part of it, and no main-model calls are authorised._

## Question

**Can Jev detect important information incorrectly lost or changed in a proposed context rewrite?**

- **Who does what:** Claude would propose the rewrite and Jev would check it. This is a checking intervention. It does not claim that Jev replaces Claude's reasoning, or that it reduces input cost.
- **Why test the component first:** experiments 009 and 010 found no benefit for affected-entry advice on the incident workload, and their failures were omissions and miscitations whose relation to context edits was **not** established.

## What Jev receives (one request per case)

**`state`:**

| Field | Content |
| --- | --- |
| `task` | The relevant task instructions the agent already has (a fixed per-family text) |
| `current_context` | The working-context entries before the rewrite (`id`, `role`, `body`), in order |
| `update` | An already released update needed to justify a change, or `""` if none |
| `proposed_context` | Claude's proposed replacement entries, in order |

**Never included:** labels, justifications, categories, family names, provenance, hidden answers, future requirements or evaluator data.
- **Neutral ids:** case ids are neutral (`c01`…, in a shuffled order) and are not sent; entry ids are ordinary (`n1`…).
- **No obligation list:** no extracted list of "critical obligations" is supplied. Jev must judge from the contexts alone.

## Judgments (`jev-edit-check/1`): three separate `noul` questions per case

1. **`lost`:** Does the proposed context drop, or mark as finished, an obligation, requirement, exception, open question or unresolved item that the current context still treats as active, when neither the current context nor the update says it is finished, superseded or no longer needed?
2. **`changed`:** Does the proposed context state a value, number, limit, condition, status or relationship differently from the current context, without the update or the current context supporting the change?
3. **`evidence`:** Does the proposed context remove the evidence reference supporting a claim it keeps, or attach a kept claim to a different reference than the current context did?

**Each question has fixed `true` and `false` criteria** (recorded verbatim in the code and in the freeze below). The criteria state explicitly:
- shortening, paraphrasing, merging and removing superseded, duplicated or completed items are **not** harmful;
- verbatim preservation is not required.

**Case verdict (predeclared):** *flagged* if **any** of the three probabilities is ≥ **0.5**, a reporting convention that is not tuned on frozen results.
- **Per-question results** are reported too. The three questions about one case are **not** independent examples.
- **Missing answers:**
  - a case where all three answers are missing, or the call failed after its retry, is **unanswered**;
  - partial answers use the available maximum and are reported as partial;
  - **for the gate, an unanswered harmful case counts as missed, and an unanswered acceptable case as falsely flagged.**

## Cases

**Labels:** **harmful**, a rewrite that loses or changes still-important information without support; **acceptable**, a correct rewrite; **ambiguous**, where continued importance depends on information absent from the checker's input, or reasonable readers would disagree. Ambiguous cases are reported separately.

**Development set:** **8 cases** from 2 families (customer support ticket; feature-flag rollout), 4 harmful and 4 acceptable. They are used only to check the API shape and the question wording; any wording change and every development call is recorded.

**Frozen set:** **32 labelled cases**, 16 harmful and 16 acceptable, from 8 further families (2 harmful + 2 acceptable each), **plus 4 ambiguous**.
- **The families:**
  - incident notes from real 010 v3 runs;
  - a CSV → JSON export change (the planned W2 workload's example);
  - invoice rules;
  - an API rate-limit migration;
  - data retention;
  - an on-call handoff;
  - a deploy checklist;
  - research notes with citations.
- **Harmful categories (16):**
  - an active requirement omitted (4);
  - an exception lost (2);
  - a value or condition changed (3);
  - a status changed without support (1);
  - an unresolved item presented as completed (3);
  - an evidence reference lost or wrong (3).
- **Acceptable categories (16):**
  - paraphrase or consolidation;
  - removal of superseded information (justified by the update);
  - removal of duplicated or completed work;
  - historical information kept as historical;
  - real edits.
- **Provenance, recorded per case:**
  - **`real-unmodified`:** a real 010 v3 edit, notes only;
  - **`real-altered`:** a real edit with a **deliberately injected** mistake, never described as an observed failure;
  - **`constructed`.**
- **Families are split** between the development and frozen sets.

**Labels and justifications are written before any Jev answer exists.**
- **Harmful cases** name the exact unsupported loss or change.
- **Acceptable cases** say why the rewrite is safe.
- **Programmatic validation:** the builder checks quoted values and references against the case text.
- **The labels are author-created**, not independently validated ground truth.

## Reference results

- **Always flag:** recall 16/16 with 16/16 false flags. This is the trivial reference.
- **Deterministic checks** (no semantics):
  - **D-ref:** any reference token (`file:line`, `§N`, ticket or change ids like `ABC-123`, `[Author Year]`) present in the current context but absent from the proposed one;
  - **D-num:** any number in the proposed context that appears in neither the current context nor the update;
  - **D-any:** D-ref or D-num.

  **What they catch:** dropped citations and invented numbers. **What they cannot judge:** whether a dropped item was still needed, or whether a change was justified.

Jev is useful here only if it adds judgment beyond these checks.

## Readiness gate (predeclared; engineering pilot-readiness only)

**On the 32 frozen labelled cases, Jev's case verdict must have:**
- **at least 14 of 16 harmful cases detected;**
- **at most 2 of 16 acceptable cases flagged;**
- **no material payload leakage or implementation defect.**

**Ambiguous cases do not count toward the gate.**

**Passing only supports considering an agent pilot.** It does not establish better task performance, lower cost or improved context management.

**If the gate fails:** the result is kept and the failure pattern explained, with **no automatic tuning cycle**. The frozen set is run **once**.

## Budget

- **Authorised:** up to **USD 3 of additional TypeSafe spend** for this diagnostic, including development calls and retries.
- **The ceiling** is set to the settled spend at the start + 3, replacing unused allowances.
- **Not authorised:** no main-model calls and no agent runs.

## Development run and question freeze (2026-10-13, before the frozen run)

**Development run:** `runs/jev-diagnostic/20261013T030359-edit-dev` (exported as a diagnostic).
- **Calls:** 8 requests and 8 attempts, with 0 errors, all answered by `jev-1.13.0`. The API accepted the object-valued state and the three noul questions with criteria.
- **Results:** 4/4 harmful detected and 0/4 acceptable flagged.
- **Latency and cost:** 0.25 s mean, 10,071 input tokens, USD 0.000421.
- **Changes after the development run:** **no wording change.** The question set below is the one used for development.

**Frozen settings:**
- **Question version:** `jev-edit-check/1` (SHA-256 of the question and criteria set, as sorted JSON: `c52a24b497f1226699109a3cd0d92e05a1572d88d0ff876d96e8cbfe6185461f`).
- **The scope instruction given with each question:** "Compare state.current_context (the working context before the rewrite) with state.proposed_context (the replacement). state.task is the task the context serves and state.update is already released information that may justify changes (empty if none)."
- **The questions and criteria** (verbatim):
- **`lost`:** Does the proposed context drop, or mark as finished, an obligation, requirement, exception, open question or unresolved item that the current context still treats as active, when neither the current context nor the update says it is finished, superseded or no longer needed?
  - **true:** Yes if an item that is still active in the current context is missing from the proposed context, or is now described as done, closed, answered or no longer applicable, and neither the current context nor the update supports that. This includes losing an exception or condition attached to a requirement that is kept.
  - **false:** No if every active item is still present, possibly paraphrased, shortened or merged; if removed items were superseded, completed, duplicated or closed according to the current context or the update; or if historical information is kept as history. A shorter context is not by itself a loss.
- **`changed`:** Does the proposed context state a value, number, limit, condition, status or relationship differently from the current context, without the update or the current context supporting the change?
  - **true:** Yes if a value, threshold, amount, date, percentage, status, scope or which-applies-to-what relationship differs from the current context and the update does not justify the new version.
  - **false:** No if values, conditions and statuses mean the same (wording may differ), or if every difference is justified by the update or by the current context itself.
- **`evidence`:** Does the proposed context remove the evidence reference supporting a claim it keeps, or attach a kept claim to a different reference than the current context did?
  - **true:** Yes if a claim that remains in the proposed context had a source reference (file:line, document section, ticket, dashboard, link or citation) in the current context and that reference is now missing, or the claim now cites a different reference without the update supporting it.
  - **false:** No if kept claims keep their references (possibly reformatted or merged), if a claim and its reference were removed together, or if a reference changed in a way the update supports.
- **Model and API:** `jev-1.13.0` (pinned) at `https://api.typesafe.ai/v1/systemone`; a 15 s timeout and 1 runtime retry for 429/529/5xx/timeouts, with no hidden retries. Each attempt is reserved and settled in the ledger as kind `jev-diagnostic`.
- **Cases:** `diagnostic-cases-v1.json`, SHA-256 `1d54373555eb339b374016671afdb27f8014942dbbe7014a06ec61e596ebfe78`. The frozen split has 16 harmful, 16 acceptable and 4 ambiguous cases.
- **Scoring:**
  - **Threshold:** 0.5; flagged if **any** question reaches it.
  - **Missing answers:** a case with all answers missing (or a failed call) is unanswered and counts as missed if harmful, or flagged if acceptable. A partial case uses the available maximum.
- **Reported:**
  - detections, misses and false flags with raw counts, precision and recall;
  - per question and per category;
  - the ambiguous cases separately;
  - the always-flag and deterministic references;
  - latency, tokens, cost and errors.
- **Gate:** at least 14/16 harmful detected, at most 2/16 acceptable flagged, and no leakage or defect. The frozen set is run **once**.

## Frozen run result record (2026-10-13)

- **The run:** `runs/jev-diagnostic/20261013T030432-edit-frozen`, executed **once** with the frozen question and cases. 36 requests and attempts, 0 errors, 0 unanswered, all answered by `jev-1.13.0`, at 0.24 s mean and USD 0.002213.
- **Gate:** harmful detected **16/16** (passes ≥ 14); acceptable flagged **3/16** (**fails** ≤ 2); no leakage or defect. **The gate FAILED.**
- **False flags:** `c02` (a completed follow-up removed; `changed` 0.70), `c29` (a real edit adding log findings; `changed` 0.60) and `c27` (a real edit replacing older log ranges with newer ones; `evidence` 0.58).
- **Ambiguous cases:** 0.64, 0.62, 0.63 and 0.45.
- **Deterministic reference D-any:** 7/16 recall with 3/16 false flags, on the same three cases.
- **As this protocol requires:** the result is kept; the threshold, question and labels are unchanged; the frozen set is not rerun; and no tuning cycle or agent pilot was started.
- **Spend:** USD 0.002634 in total (development and frozen runs), TypeSafe only. The ledger is at USD 82.005891 of USD 85.003257.
