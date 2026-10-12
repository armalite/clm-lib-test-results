# 009 – Protocol: update-triggered Jev context review (strategy 1)

_Written on 2026-10-13, before any paid experiment-009 call. Later notes are appended below; earlier sections are not rewritten afterwards. Roadmap: [`../jev-assistance-roadmap.md`](../jev-assistance-roadmap.md)._

## Question

**When meaningful new evidence arrives, does Jev's affected-entry advice help Claude review its existing working context?**

**The flow in the assisted arm:**
1. New evidence is released.
2. Jev assesses the current context entries against it.
3. Claude receives the evidence and the advice together.
4. Claude decides whether and how to edit.

**Comparison:**
- **A (control): CLM alone.** At each update point Claude sees the same update and the same instruction to consider whether it affects its existing context.
- **B (assisted):** the same, plus Jev's advice and a short explanation of it.

**Equal in both arms:** Claude decides every edit. It may:
- leave the context unchanged;
- edit part of an entry;
- keep facts as history;
- consolidate or remove entries;
- write ordinary reusable helpers.

No edit is required, and nothing rewards agreeing with Jev.

**Relation to 008:**
- **008:** an independently optional Jev action, which the agent never used.
- **009:** the review point is created by the runtime in both arms, so review is never left to chance. Only the advice differs.

## Task and update boundary

**Task:** experiment 007's multi-round incident (`incident-rounds-gen/1`, scorer `rounds-score/1`), unchanged.
- **How evidence arrives:** the agent requests the next round with `advance`.
- **Each round:** `board.md` (incident-board updates, listing only what changed), sometimes `changes.md` (change records), and five service logs of about 23–41k characters per round.

**Why the historical release notice is not enough:** it is only *"Round k of n released. New files are under /task/fixtures/round-kk/."* plus a file listing. It carries no substantive evidence for Jev to assess.

**The chosen payload (`round-files/1`, `src/clm_lib/update_review.py`):**
- **Content:** that round's `board.md` lines, then its `changes.md` lines, verbatim and in file order, each prefixed with its `round-kk/<file>:<line>` reference.
- **Mechanical processing only:**
  - blank lines and Markdown heading lines are dropped;
  - a payload over 4,000 characters is cut at a line boundary with a marker (never needed on the dev instances: at most about 500 characters).
- **Never added:** no summary, interpretation or selection.
- **Logs are excluded,** because they are too large for an 8,000-token request budget. The model still reads them from the files as before.
- **Identical in both arms:** the payload is the same text in both arms. In B it is also Jev's `update`.
- **Empty rounds:** a round whose board has no update lines and has no change log gives an empty payload. Both arms are then told no board or change-log lines were released, and Jev is not called.

**Trigger:** every release of rounds 2…n through `advance`. Round 1 is present at the start, when the context is empty.

**Presentation change (versioned, this experiment only):**
- **Both arms:** the release observation keeps its historical text and gains an `UPDATE (round-files/1; context revision R was current at this release)` block with the payload, plus "Consider whether this update affects your working context."
- **B only:** the advice block is appended after it.
- **Unchanged:** historical runs and configurations never show these blocks.

## What Jev receives (B)

- **The update:** the payload above, as `state.update`.
- **The candidates:** every entry of the context revision current at the release, in context order. This is exactly the working context the model saw in that step's request; the advance step's own entries are appended afterwards.
- **Fixed scope:** nothing is filtered by score, label or role, so model notes, step actions, observations and runtime receipts are all scored.
- **Cap:** at most 60 candidates. Any beyond are listed in the observation as "not assessed", never silently omitted. A cap above the context's realistic size (an 8,000-token budget) means it should not bind.
- **Only the active context:** the experiment-008 revision-boundary fix is preserved. Deleted entries, future rounds, logs not yet in context, evaluator truth and hidden labels are never sent, and tests check this.
- **Batching:** one `noul` question per entry with the fixed **`jev-review/1`** question and criteria, unchanged from 008. Batches hold up to 20 questions and 60,000 entry characters.
- **Model:** `jev-1.13.0`, pinned. The returned `model` field is recorded.

**Timing:** the advice is obtained **on the host, before the next main-model call**, inside the advance step. It costs no extra Claude turn.

**The B observation's advice block** has the same format as 008: every scored entry with its probability, or "no answer", plus coverage and any service problem.
- **Failures:** a failed call becomes "no answer" and a notice, and the run continues.
- **Advisory only:** the advice never edits context and never approves or rejects an edit.

## Prompts (version `2026-10-13.1`; earlier texts byte-identical)

**Both arms**, appended to the `clm_helpers` system prompt (`UPDATE_REVIEW_CLAUSE`):

```
UPDATE REVIEW (this run):
- When a new round is released, the observation also shows that round's incident-board and
  change-log lines verbatim, with their file:line references (logs are not included; read them
  from the files as usual), and the context revision that was current at the release.
- At each such update, consider whether it affects your existing working context. You may leave
  the context unchanged, edit part of an entry, keep facts as history, consolidate or remove
  entries, or use your own helpers. No edit is required.
```

**B only** (`UPDATE_REVIEW_JEV_CLAUSE`):

```
- With each update the runtime also asks a fast classifier (Jev), for every entry of that context
  revision, for the probability that the update requires reconsidering a current assertion or
  planned action in the entry. The advice is probabilistic and can be wrong, and it never edits
  your context. A low probability is not a reason to delete an entry, and a high one does not mean
  the entry is wrong. You decide whether and how to edit.
```

## Shared controls

**Config:** `configs/exp009.toml`. It matches `configs/exp008.toml` apart from three settings:
- `[update_review]`, which is switched on per run;
- the experiment-008 review action, which stays off;
- the ceiling.

**The same for both arms:**
- `claude-opus-5-5`, effort low;
- an 8,000-token request budget, 4,096 output tokens and 60 main-model task calls;
- mode `clm_helpers`;
- the `blocks/1` layout, 5-minute prompt caching, and a cold `run-tag/1` cache per run;
- the spill and pressure-notice fixes, and the revision status line;
- the scorer.

**Conditions:** `clm_helpers+upd:on` (A) and `clm_helpers+upd-jev:on` (B). Run ids carry `-upd` or `-updjev`.

## Sequence (each step recorded; nothing rerun because of a result)

1. **Offline checks** (`tests/test_update_review.py`, with the full suite):
   - historical behaviour unchanged;
   - opt-in;
   - identical update text in both arms at the same step;
   - Jev sees only current entries and released board and change-log lines;
   - advice never mutates context;
   - failures are accounted and the run continues;
   - accepted edits still determine the next request;
   - export.
2. **Live integration smoke check:** one B run on `rounds-diag-2`, role `smoke`, excluded from every comparison. It verifies the in-loop live path, which 008 never exercised: the Jev call inside the run, ledger kind `jev`, the advice observation, usage and the returned model.
3. **Fresh component diagnostic:** `diagnostic-cases-v1.json` in this folder (`jev-diag/2`).
   - **Fingerprint:** SHA-256 `6874c0693b0ac736cbcf1949ef8a77655e4766aa9cb139586db16ba8f69fae5d`.
   - **Content:** 24 cases (13 affected, 9 unaffected, 2 ambiguous) on 8 real `round-files/1` payloads from `rounds-diag-1` and `rounds-diag-2`. Those instances are reserved for diagnostics and the smoke run, and never used in the pilot or evaluation.
   - **Labels:** written on 2026-10-13, before any Jev answer.
   - **Why fresh cases:** the request construction changed materially from 008. The update is now a multi-line, multi-thread payload, and candidates include step actions and receipts as well as notes.
   - **Reporting:** at the fixed 0.5 reporting threshold, with ambiguous and unanswered cases separate. The threshold is not an editing policy.
4. **Reference rerun (not new evidence):** 008's frozen diagnostic, rerun once unchanged as a model-stability check. Those cases were already observed, so this is not an unseen evaluation and nothing is tuned against it.
5. **Development pilot (four runs):**
   - **Command:** `compare --tasks rounds-dev-1,rounds-dev-2 --reps 1 --conditions clm_helpers+upd:on,clm_helpers+upd-jev:on`.
   - **Order:** dev-1 A then B; dev-2 B then A.
   - **Instances:** these were used in 007 and 008; the pilot runs are fresh. Perfect scores would limit accuracy claims but not efficiency findings.

**If the diagnostic shows a substantial question-design problem,** it is reported before the pilot rather than tuned around.

**Activation check (reported, not forced):**
- substantive updates occurred while work remained;
- B's Jev calls scored a non-empty current context.

No edit is forced to satisfy it.

## Measured and recorded

- **Correctness:** strict success and every scorer category, including stale facts, omissions and citation errors. Failed runs stay in all totals.
- **Cost and usage:** total cost and usage by provider (Anthropic, TypeSafe); elapsed time and each provider's latency; main-model calls, tokens, and cache reads and writes.
- **Every Jev attempt:** retries, errors, the response, usage, latency, cost and the returned model version.
- **Per update** (`summary.json → update_review.records`, and `update_review` events):
  - step, stage, revision, the exact payload and its SHA-256;
  - candidate ids, entries not assessed, answers, and the advice's size in characters.
- **What followed each update:** the accepted edits before the next update (by revision), candidates changed, and, in B, flagged entries changed or not changed and unflagged entries changed.
  - **Not attribution:** "followed by an edit" is temporal association only.
  - **Comparison:** control-arm candidates changed are reported the same way, for comparison.
- **Request growth:** the characters appended per update in both arms (payload), plus B's advice characters, and the per-request token and cache metrics. Any growth or cache disruption from the advice is reported. No saving is claimed for context the model has already read.

## Larger evaluation: a plan only, not authorised

- **Sample:** 4 fresh instances × 3 repetitions × 2 arms = **24 runs**.
  - **Instances:** new seeds of the same generator (for example `rounds-eval-5..8`), registered uninspected when the plan is frozen. `rounds-eval-1..4` were used by 007.
  - **Order:** alternating by instance and repetition.
- **Primary outcomes:** strict success and mean all-attempt cost per run.
- **Secondary outcomes:**
  - categories;
  - elapsed and provider time;
  - calls and cache usage;
  - updates followed by edits;
  - flagged-then-changed and flagged-not-changed;
  - advice overhead.
- **Budget:** the pilot's mean cost per run per arm × 12 × 1.25. It needs its own authorisation.
- **Limits:**
  - one synthetic task family and one model;
  - the dev instances may already be at the accuracy ceiling;
  - logs are not part of the update, so connections that only logs reveal are outside what Jev sees.

## Budget

- **This experiment:** at most **USD 10 of new spend** across Anthropic and TypeSafe, covering the smoke check, the diagnostics and the four-run pilot.
- **Ledger at the start:** USD 48.408962 spent across 2,861 entries, with nothing pending. The ceiling was then USD 56.993902, and 008's unused allowance does not carry over.
- **New ceiling:** set explicitly to **USD 58.408962** (spend + 10), with `configs/exp009.toml` carrying the same value.
- **Not authorised:** no paid runs for strategies 2 or 3, and no evaluation.

## Live session record (2026-10-12 UTC / 2026-10-13 local)

Run in the order fixed above. No case, label, threshold, payload rule or prompt was changed after seeing any answer.

1. **Offline checks:** ruff, format and mypy are clean, and the full suite passed (171 tests, including 11 in `tests/test_update_review.py`).
   - **A test fix found on the way:** adding `configs/exp009.toml` made 008's historical-config test fail, the same class of failure as the 008 provenance issue. Its historical set is now explicitly the configs before exp008.
   - **Compatibility:** re-exports of 007 and 008 reproduced their metrics and every artifact checksum.
2. **Smoke:** `20261012T115543-clm_helpers-cacheon-updjev-rounds-diag-2-f112`. It completed (strict) with 8 advised updates and no Jev errors, reporting `jev-1.13.0`.
3. **Fresh diagnostic:** `20261012T115847-frozen`. At 0.5: 12/13 affected flagged, 1/9 unaffected flagged; ambiguous 0.90 and 0.53. It revealed no substantial design problem, so the pilot went ahead.
4. **Reference rerun:** `20261012T115851-frozen`. The same classifications as 2026-10-12; probabilities within 0.05.
5. **Pilot:** comparison `20261012T115926`, 4/4 strict successes. B's Jev scored a non-empty context at all 16 updates with a payload, and nothing was forced.

**Spend:** USD 1.801066 of the USD 10 (Anthropic 1.798257, TypeSafe 0.002809). The ledger is at USD 50.210028 of USD 58.408962. No evaluation was run, and nothing for strategies 2 or 3.

## Provenance note: experiment 008's "155 tests passed" (2026-10-13)

Experiment 008's build session reported "155 tests passed". Its next session then found the committed historical-config test failing. Both statements were true, for different source states:
- **The 155-test run:** at 2026-10-12T10:02:54Z, on the working tree **before** `configs/exp008.toml` existed. It collected 155 tests and printed no failures. Its summary line was suppressed because the repository's `addopts = "-q"` combined with `-q` gives `-qq`.
- **The change after it:** at 10:07:08Z, `configs/exp008.toml` was written with `status_shows_revision = true`, which the historical-config test rejects. No full test run followed before commit `0884608`.
- **The committed state:** `0884608` (and `a1f3dd5`, which changed only `CLAUDE.md`) therefore had **1 failing test of 155**. In an extract of `0884608`, `test_jev.py` gives 1 failed and 16 passed.
- **The fix:** that test was corrected in `3733c9c`. Adding `configs/exp009.toml` broke it again in the same way, so its historical set is now explicitly the configs written before 008.
- **Impact:** the failure is in a test's choice of configs, not in runtime behaviour. No 008 or earlier evidence is affected, and none is rewritten.

## Evaluation freeze (2026-10-13, before any evaluation call)

**Authorised by the maintainer:** the planned 24-run evaluation, with at most **USD 20 of additional total spend** across both providers, including retries and any live verification. This replaces the unused pilot allowance.
- **Ledger at the start:** settled spend USD 50.210028 across 3,046 entries, with 0 pending.
- **Ceiling set explicitly** from USD 58.408962 to **USD 70.210028** (`ceiling_history` entry 8).

**Instances:** `rounds-eval-5`, `-6`, `-7` and `-8`.
- **Generation:** seeds 7205–7208 of `incident-rounds-gen/1`, scorer `rounds-score/1`. They were registered in `tasks.py` this session, with the eval split extended from 4 to 8; seeds 7201–7204 are unchanged.
- **Never used before:** they appear in no earlier run, run selection or export, and were not used in development, calibration, the pilot or 007's evaluation.
- **Mechanical validation only:**
  - 12, 10, 11 and 12 rounds;
  - every round has a board and five logs;
  - non-empty payloads at 10/11, 9/9, 10/10 and 10/11 releases;
  - three incidents in each truth record;
  - a scripted offline run completes and scores in both arms.

  No answer, truth value or scenario detail was read to tune anything.
- **Fixture SHA-256 prefixes** (JSON of all files): `a5d30f776d93394f`, `dc12b9c9d3694a4a`, `62497650c0ae8aa7`, `dc2c479d613c0c40`.

**Sample:** 4 instances × 3 repetitions × 2 conditions = **24 runs**, sequential. The runs on one instance are repeated measurements of four task instances, not twelve independent task designs.

**Conditions and settings:** unchanged from the pilot.
- **Conditions:** A `clm_helpers+upd:on`, B `clm_helpers+upd-jev:on`.
- **Config:** `configs/exp009.toml` (SHA-256 `44f86c4c…26a4`). It differs from the pilot's committed config only in the non-behavioural ceiling value and its comment.
- **Main model:** `claude-opus-5-5`, effort low; an 8,000-token request budget, 4,096 output tokens and 60 task calls.
- **Request:** the `blocks/1` layout, 5-minute caching on in both arms, and `run-tag/1` cold isolation per run.
- **Runtime fixes:** spill and pressure-notice fixes on, plus the revision status line.
- **Prompts:** version `2026-10-13.1`. Clause hash prefixes are `fab94d7c8aaa5029` (both arms) and `c5439547714382ef` (B).
- **Jev:**
  - model `jev-1.13.0`;
  - question `jev-review/1` (text hash `f98789b3280d4a6d`, criteria `809831976af7ac21`);
  - payload `round-files/1`;
  - candidates: every entry of the current revision, capped at 60 with any beyond listed;
  - batches of 20 questions and 60,000 characters;
  - a 15 s timeout, 1 retry for 429/529/5xx/timeouts, and failures shown as "no answer" plus a notice.
- **Prices:** `configs/prices.toml` (SHA-256 `fb4521b7…85e4`).

**Run order** (from `condition_schedule`: alternating by instance index + repetition; A first in 6 of 12 blocks):

| Rep | eval-5 | eval-6 | eval-7 | eval-8 |
| --- | --- | --- | --- | --- |
| 1 | A, B | B, A | A, B | B, A |
| 2 | B, A | A, B | B, A | A, B |
| 3 | A, B | B, A | A, B | B, A |

**Code provenance:**
- **Commit:** `0247b1c`, plus uncommitted `tasks.py` (instance registration) and `exp009.toml` (ceiling), saved as a patch (SHA-256 `5bafc10e…39a3`).
- **Patch check:** `compare` saves its own patch at the start, and it is checked against this one.
- **Pre-run checks:** ruff, format and mypy clean; 171 tests passed (including Docker-backed tests).

**Failure rules (unchanged, predeclared):**
- every run is kept, including failures, exhaustion and invalid runs;
- `compare` halts on the existing halt statuses, such as an accounting-bound violation;
- no run is replaced or repeated, and no setting changes after results;
- a material implementation defect stops the evaluation and is documented, and results from before and after a fix are never pooled.

**Analysis (as planned):**
- **Primary:** strict success and mean all-attempt cost per run.
- **Secondary:** categories, medians, elapsed, provider and Jev time, calls, edits, tokens and cache use, and advice-to-edit records.
- **Matching:** paired by (instance, repetition) block, and aggregated by instance as well as across runs.

## Evaluation execution notes (2026-10-13)

- **Comparison `20261012T124415`:** run sequentially in one `compare` invocation with `configs/exp009.toml` and `--max-usd 19`.
- **Completion:** all **24 of 24** cells completed, in the frozen order. There was no halt, no missing cell, and no invalid, repeated or replaced run.
- **Provenance:** the patch saved by `compare` is byte-identical to the frozen patch (SHA-256 `5bafc10e…39a3`).
- **No deviations** from the freeze. Nothing was tuned, and no setting was changed during or after the evaluation.
- **No implementation defect was found.**
  - **Jev:** all 117 calls succeeded, with `jev-1.13.0`, no retries and no errors.
  - **Payload updates:** every update with a payload in the assisted arm was scored against a non-empty current context.
  - **Main model:** there were no repairs, API retries, recoveries or rejected edits.
- **Scoring:** 6 runs were not strict successes (4 A, 2 B). All are kept and reported; the README has the details.
- **Answers:** these were read only after all 24 runs had finished, to classify failures and select trace examples.
- **Spend:** USD 9.477545 (Anthropic 9.467744, TypeSafe 0.009801). The ledger stands at USD 59.687573 of the USD 70.210028 ceiling, with nothing pending.
- **Result:**
  - **Cost and time:** the pilot's cost and time advantage for the assisted arm did not repeat. Its mean cost was USD 0.415 vs 0.375 for the control, and its mean elapsed time 158 s vs 149 s. It was cheaper in 4 of 12 blocks.
  - **Strict success:** 10/12 vs 8/12, which is not conclusive.
