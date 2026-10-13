# 011 – Can Jev check a proposed context rewrite? (component diagnostic)

**Status: component diagnostic complete; readiness gate FAILED.**
- **The result:** Jev detected **16 of 16** harmful rewrites, but falsely flagged **3 of 16** acceptable ones. The predeclared maximum was 2.
- **Not done:** no agent integration, edit blocking or end-to-end run was built or run, and no main-model calls were made.
- **Context:** part of the [Jev-assistance roadmap](../jev-assistance-roadmap.md). Protocol: [`protocol.md`](protocol.md), with the component-diagnostic section and the freeze written before the frozen run.

## The question

**Can Jev detect important information incorrectly lost or changed in a proposed context rewrite?**

This tests a different judgment from 009 and 010, where Jev scored whether an update affected each entry. Here, Claude would propose a rewrite of its working context and Jev would check it. It is a checking intervention, not a substitute for Claude's reasoning or a way to reduce input cost.

**What Jev received (one request per case).** The state held:
- **`task`:** the task instructions;
- **`current_context`:** the entries before the rewrite;
- **`update`:** any already released update needed to justify a change, or empty;
- **`proposed_context`:** the replacement entries.

**What it never received:** labels, justifications, categories, case or family names, provenance, hidden answers, future requirements, or a pre-extracted list of "critical obligations".

**Three separate yes/no probabilities (`jev-edit-check/1`, verbatim in the protocol):**
1. **`lost`:** does the rewrite drop, or mark as finished, an obligation, requirement, exception, open question or unresolved item still active in the current context, without support?
2. **`changed`:** does it state a value, number, limit, condition, status or relationship differently, without support?
3. **`evidence`:** does it remove the reference supporting a claim it keeps, or attach a kept claim to a different reference?

**Settings:**
- **The criteria** state that shortening, paraphrase, merging and removing superseded, duplicated or completed items are not harmful.
- **Verdict:** a case is *flagged* if any probability reaches **0.5**, a reporting convention fixed in advance.
- **Model:** `jev-1.13.0`, with a 15 s timeout and 1 retry.

## The cases (`diagnostic-cases-v1.json`, `jev-edit-diag/1`)

**Built by:** [`diagnostic-cases-v1.build.py`](diagnostic-cases-v1.build.py), which validates the quoted strings and references mechanically. SHA-256 `1d543735…fe78`.

| Set | Harmful | Acceptable | Ambiguous | Families |
| --- | --- | --- | --- | --- |
| Development | 4 | 4 | — | customer support ticket; feature-flag rollout |
| Frozen | 16 | 16 | 4 | incident notes; CSV → JSON export (the planned W2 example); invoice rules; API rate-limit migration; data retention; on-call handoff; deploy checklist; research notes |

**Frozen-set composition:**
- **Structure:** each frozen family has 2 harmful and 2 acceptable cases.
- **Harmful categories:**
  - an active requirement or item omitted (4);
  - an exception lost (2);
  - a value or condition changed (3);
  - a status changed without support (1);
  - an unresolved item presented as completed (3);
  - an evidence reference lost or wrong (3).
- **Acceptable categories:** paraphrase and consolidation; removal of superseded information (justified by an update); removal of duplicated or completed work; historical information kept as history; and real edits.

**Provenance:**
- **constructed:** 38 cases.
- **real-unmodified:** 3 cases, real context edits from 010 v3 runs (notes only). One is labelled acceptable and two ambiguous.
- **real-altered:** 3 cases. One restores a dropped reference, making it acceptable; two carry a **deliberately injected** mistake, labelled harmful. **These are not failures observed in agent runs.**

**About the labels:**
- **Author-created:** they were written before any Jev answer, and are not independently validated ground truth.
- **Harmful cases** name the exact loss or change; **acceptable cases** say why the rewrite is safe.
- **No leakage:** a test checks that no label, id, family name or wording such as "injected" reaches any payload.

## Results

**The frozen run (`20261013T030432-edit-frozen`, run once)**, at the fixed 0.5 threshold:

| On the 32 labelled frozen cases | Jev (any question ≥ 0.5) | Always flag | D-ref (a reference disappears) | D-num (a new unexplained number) | D-any (D-ref or D-num) |
| --- | --- | --- | --- | --- | --- |
| **Harmful detected (recall)** | **16 / 16** | 16 / 16 | 5 / 16 | 4 / 16 | 7 / 16 |
| **Acceptable flagged** | **3 / 16** | 16 / 16 | 2 / 16 | 2 / 16 | 3 / 16 |
| Precision | 16 / 19 | 16 / 32 | 5 / 7 | 4 / 6 | 7 / 10 |

**Per question** (one case's three answers are not independent examples):
- **`lost`:** 11/16 recall, 0 false flags.
- **`changed`:** 15/16 recall, 2 false flags.
- **`evidence`:** 6/16 recall, 1 false flag.
- **On their own dimension, every question fired:** **10/10** harmful cases labelled `lost` were flagged by `lost`, **7/7** labelled `changed` by `changed`, and **3/3** labelled `evidence` by `evidence`.

**Ambiguous cases** (reported separately; not in the gate):
- `c23`, does a streamed-export update supersede the large-export rule? Max 0.64.
- `c07`, a real edit dropping a log reference with its claim: 0.62.
- `c18`, a real consolidation dropping older log ranges: 0.63.
- `c06`, an on-call watch item removed: 0.45.

**Calls and cost:**
- **Frozen run:** 36 requests and 36 attempts, with **0 errors** and 0 unanswered or partial cases, all answered by `jev-1.13.0`.
- **Latency:** **0.24 s** mean per case (max 0.46 s).
- **Usage:** 52,747 input and 1,944 output tokens, **USD 0.002213**.
- **Development run** (`20261013T030359-edit-dev`): 4/4 detected, 0/4 false flags, USD 0.000421, and no wording change afterwards.

## Detections, false alarms and misses

**Detections the deterministic checks could not make** (no reference disappeared and no new number appeared):
- **An exception lost while its section stays cited:** "records under legal hold are never deleted" became "deleted after 30 days regardless of age (RP-4 §2, §2.3)" (`lost` 0.85).
- **An exception lost (CSV → JSON):** "admins may also export archived projects" removed under a format-only change notice (0.95).
- **A requirement omitted (CSV → JSON):** the confidential-row exclusion removed (0.96).
- **A condition removed:** "promote to 100% only after the canary error rate stays below 1% for 30 minutes" became "after 30 minutes" (0.96).
- **Citations swapped between two claims,** with both references still present (`evidence` 0.95 and 0.97).
- **Unresolved items presented as finished:** "step 3 NOT done" became "steps 1–3 done" (0.87); an unchecked open question became an answered claim (0.90).
- **The real-altered incident cases:** a change record's suspicion (CHG-113 `cache.ttl_s=-1`) removed (0.83 max), and a "mitigated" thread recorded as "resolved" (0.92).

**Misses:** none at the case level.

**False alarms (3):**
- **`c02`, on-call:** a follow-up the context already marked "done 02:30" was removed, and `changed` scored 0.70. This is an over-flag by the question itself.
- **`c29`, a real incident edit, unmodified:** the edit added new log findings to a note, and `changed` scored 0.60.
- **`c27`, a real incident edit, altered only to restore a reference:** older log ranges were replaced by newer ones, and `evidence` scored 0.58.

**What the false alarms have in common (post hoc observation; labels not changed):**
- **The real-edit pair** (`c29`, `c27`) incorporated findings from **logs the agent had read, which are not in the checker's input.** The `update` field held only the round's board and change-log lines, so from Jev's view those additions look unsupported. This is a **payload-scope limitation** of the design, not only a question error: a checker needs the tool observations that justify an edit.
- **The same three cases** are exactly the ones D-any also flags falsely. The deterministic checks fail on those cases too.

**One more observation (not a result):** every harmful case's maximum probability was at least 0.83, and every acceptable case's was at most 0.70. **No threshold change is made or claimed**, because the threshold was frozen at 0.5, and tuning on these answers would make the frozen set no longer an evaluation.

## Readiness gate (predeclared)

| Criterion | Required | Result |
| --- | --- | --- |
| Harmful cases detected | at least 14 / 16 | **16 / 16: passed** |
| Acceptable cases flagged | at most 2 / 16 | **3 / 16: FAILED** |
| No payload leakage or implementation defect | none | none found (leak test passes; 0 errors) |

**The gate fails, so an agent pilot is not justified by this diagnostic.** As the protocol requires, the result is kept, the threshold and question are not changed, and the frozen set is not rerun.

## What this shows and does not show

**It shows:**
- **On these author-labelled cases,** Jev's three narrow questions separate harmful from acceptable rewrites far better than the deterministic checks (16/16 vs 7/16 recall), including semantic losses that leave every reference and number intact.
- **Each question tracks its own dimension.**
- **It is fast and cheap:** about 0.24 s and USD 0.00006 per check.

**It does not show:**
- that Jev would improve an agent's task performance, cost or context management;
- reliability beyond 36 small cases written by one author;
- that the failures in 009 and 010 came from context edits (those analyses did not establish that).

**Why the gate failed:** two of its three false alarms are real edits whose justification lies in tool output the checker never saw. A real checker would need that evidence, or it would over-flag ordinary note-taking.

## Possible next steps (not done; each needs its own decision and authorisation)

**1. A diagnostic v2:** this would be a new version with **fresh** labelled cases, not a re-run of this frozen set. The checker's input would include the **tool observations made since the previous context revision** (bounded, mechanical), and the question wording would be fixed before any answers. This addresses the observed failure pattern. It is a new tuning cycle and is not started automatically.

**2. If a future diagnostic passes, a small agent pilot could look like this:**
- **Workload:** the planned W2 changing-requirements workload (CSV → JSON with persistent permissions and filtering), where rewrites can lose still-valid obligations. The incident workload's failures were citation errors at answer time.
- **The flow:**
  - Claude's `execute` writes a candidate `context.json` (no double execution);
  - the runtime holds it as a proposal and asks Jev with the three questions;
  - the observation reports the scores;
  - Claude then applies, revises or withdraws the proposal in its next step. **Advice may be ignored.**
- **Extra calls:** about one main-model call per checked edit, in both checking conditions.
- **Conditions:**
  - A: ordinary CLM;
  - B: the same hold-and-confirm step **without** Jev;
  - C: the same step **with** Jev's scores.

  This separates the overhead of the confirm step (B vs A) from Jev's contribution (C vs B).
- **Measures:**
  - false alarms: flags on edits a scorer or audit finds harmless;
  - unnecessary repairs: revisions after false flags;
  - real downstream errors: scored omissions or changes traced to an edit in the revision history;
  - cost, calls and time.

## Spend

- **Development run:** USD 0.000421.
- **Frozen run:** USD 0.002213.
- **Total:** **USD 0.002634**, TypeSafe only (44 calls), of the USD 3 authorised. No main-model calls.
- **Ledger:** USD 82.005891 spent of the USD 85.003257 ceiling, with nothing pending.

## Where is the evidence?

- `protocol.md`: the component-diagnostic protocol (before any labels or code), the development run, the question freeze, and the result record.
- `diagnostic-cases-v1.json` and `diagnostic-cases-v1.build.py`: the cases, labels and their builder.
- `artifacts/diagnostics/20261013T030432-edit-frozen/` and `…030359-edit-dev/`:
  - `requests/<case>.json`: the exact request (no labels), the response, latency, usage and cost;
  - `summary.json`: scores, per-question results, categories, references and deterministic detail.
