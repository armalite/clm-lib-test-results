# 015 – Development validation `dev-v3a`: `paper-clm-shell/3` (record: NOT demonstrated; the only edit was rejected)

_Recorded 2026-10-20T09:10:39Z, before planning or any provider call._

**The scope:** a development validation of the repaired editing interface, not an accuracy comparison.
- one session: the paper arm `paper-clm-shell/3` (part-level context file `ctx-part-mirror/1`, profile `paper`), on `docthread-dev-1`, all eight turns;
- `docthread-task/2`, `p015-turn-endings/1` and `p015-truncation/1`;
- the shared smoke-dev2 model, cache, retry, budget and limit settings, unchanged;
- the specification is [dev-v3a-spec.json](dev-v3a-spec.json).

guarded-clm and the summary arm are not run.

**Authorisation:** at most US$4 for this one session, including its bounded retries and any charges at reservation.
- It is allocated from the unused US$29.126322 of the confirmation allowance, so the overall ceilings stay unchanged.
- No replacement, second instance or confirmation run is authorised.

**The starting state, verified:** ledger spend 102.530754, programme 015 spend 14.431008, no pending reservations.

## The interpretation, declared before the run

**The behaviour is demonstrated if a real model:**
1. writes a substantive context reduction through the shell;
2. has that edit accepted;
3. receives a later provider response built from the reduced context, with no request-structure failure.

**Also recorded:** whether the edit came under context pressure, and whether the session continued across later turns.

**Not a gate:** a perfect score. An ordinary later task failure does not invalidate an earlier successful edit.

**Other outcomes:**
- if no substantive edit is attempted, the result is **inconclusive** for this purpose;
- if edits are rejected, their exact reasons are reported.

**No adjustment after the run:** nothing is revised, repaired or rerun.

## Result (run 2026-10-20, 09:11:10 to 09:13:08 UTC)

**The run:** the launcher exited normally, and the session ran once. 19 provider attempts, none failed, retried, refused or truncated.

**The evidence:** [dev-v3a-export/](dev-v3a-export/) (it verifies, and the checksums pass), [dev-v3a-freeze-record.json](dev-v3a-freeze-record.json) and the exposure report ([dev-v3a-exposure.md](dev-v3a-exposure.md)).

| | |
| --- | --- |
| ending | `context_limit` in turn 4 (outcome `arm_failure`); turns 3 completed, 4 attempted, 8 planned |
| score | 4/10, recall 0/3: turns 1–3 correct; turn 4 and the unattempted turns 5–8 unanswered |
| pressure | one reminder, six rollbacks, one over-limit request; peak reported input 31,727 tokens (the arm's estimates within about 0.1% of reported input) |
| edits | 1 attempted and rejected; 0 accepted |
| cost | $0.247759 confirmed of the $4 block; $0 at reservation; nothing pending |
| time | 118 s |

## Against the predeclared criteria

1. **A substantive reduction was written:** **yes.**
   - **When:** on the final over-limit request, under pressure, at attempt 18.
   - **What:** the model rewrote the whole file as a summary note, followed by copies of the later questions and answers.
   - **Size:** the file went from 55,350 to 4,638 characters (91.6% smaller), measured by replaying the command offline in the sandbox on the rebuilt file, which reproduced the recorded reason.
2. **The edit was accepted:** **no.**
   - **The exact reason:** `there is no block 48; the file had blocks 1 to 47`.
   - **What the model did:** it gave the blocks it kept new headers numbered 46 to 50 in sequence, as positions in its new file, instead of keeping their original header lines. The blocks it copied are 23, 39, 40 and 41, and one copy matched no block.
   - **What the rules say:** the instructions tell the model to keep a block by keeping its header line. The parser applied that rule correctly. **This is not a harness defect.**
3. **A response built from reduced context:** **not reached.** The next request was over the limit, and the turn ended.

**So the behaviour was not demonstrated.** The editing interface is not shown to work with this model.

**Before the edit:** the six rollbacks each removed a file-inspection step (listings of about 3.6 KB). The one listing the model saw came on the final allowance, so it had a single attempt at an edit.

## What this means for the next step

**The comparison should not be run yet.**

**The exact observed blocker:** on rewriting the file, the model renumbered the kept blocks' headers, so the edit referred to blocks that do not exist. That happened on its only attempt, after the near-limit rollbacks had removed every earlier inspection.

**Nothing has been revised:** no instruction, arm or rule was changed after this run, and nothing was rerun.

**Any next step is a new decision.** One option is to make a kept block's identity robust to renumbering; another is to give room after a rollback. Either is a behaviour change to the arm, and it must be decided and verified offline before any further live check.

