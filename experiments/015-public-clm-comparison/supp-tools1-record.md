# 015 – `supp-tools1`: supplemental evaluation of `paper-clm-tools/2` (record)

_Pre-run stub written 2026-10-22, before dispatch. The protocol is [supp-tools1-protocol.md](supp-tools1-protocol.md), the specification [supp-tools1-spec.json](supp-tools1-spec.json) and the freeze record [supp-tools1-freeze-record.json](supp-tools1-freeze-record.json). The results are added below after the run._

## Result (added after the run)

**The run:** launched detached at 2026-10-21T22:44:24Z (UTC; 2026-10-22 local); the launcher ended with code 0 at 22:57:52Z. **All six scheduled sessions ran,** once each.
- **No compatibility incident:** no provider error (193 of 193 attempts accepted, no retries) and no `request_incompatible`.
- **The pre-registered stop** was never triggered. Nothing was patched, rerun or replaced.

**The evidence:** [supp-tools1-export/](supp-tools1-export/), which verifies (6 runs, manifest problems none, every checksum passes, no home paths or credentials), and the exposure report [supp-tools1-exposure.md](supp-tools1-exposure.md) (and `.json`).

**These are supplemental results,** distinct from confirm1 and from the development runs. The confirm1 figures below are its frozen results ([confirm1-record.md](confirm1-record.md), [confirm1-exposure.md](confirm1-exposure.md)), unchanged.

### Primary: score and completion per instance

| Instance | `paper-clm-tools/2` points (recall) | Ending | Turns completed | guarded-clm | summary | `paper_clm_shell` v2 |
| --- | --- | --- | --- | --- | --- | --- |
| docthread-confirm-1 | **5** (1/3) | context limit in turn 6 | 5 of 8 | 10 | 10 | 4 |
| docthread-confirm-2 | **4** (0/3) | context limit in turn 5 | 4 | 10 | 10 | 0 |
| docthread-confirm-3 | **4** (0/3) | output truncated in turn 4 | 3 | 10 | 10 | 4 |
| docthread-confirm-4 | **9** (3/3) | complete | 8 | 9 | 9 | 4 |
| docthread-confirm-5 | **4** (0/3) | context limit in turn 5 | 4 | 10 | 10 | 4 |
| docthread-confirm-6 | **10** (3/3) | complete | 8 | 9 | 10 | 4 |
| **total** | **36/60** (7/18) | 2 of 6 complete | 32 of 48 | 58/60 | 59/60 | 20/60 |

**Paired differences in points** (`paper-clm-tools/2` minus the confirm1 arm, per instance 1 to 6):
- **against guarded-clm:** −5, −6, −6, 0, −6, +1; total **−22**;
- **against the summary arm:** −5, −6, −6, 0, −6, 0; total **−23**;
- **against `paper_clm_shell` v2:** +1, +4, 0, +5, 0, +6; total **+16**.

**The scoring:** of the 24 points lost, **20 were missing answers** from turns that never ran (the session ended early), and **4 were wrong answers**: three evidence lines that were not the requested event, and one value that was not a journal line. The recall fields fall in turns 5, 7 and 8.

### Primary: cost, time and calls

| Instance | Cost (USD) | Wall (s) | Main calls | Against guarded-clm (USD) | Against summary (USD) | Against shell v2 (USD) |
| --- | --- | --- | --- | --- | --- | --- |
| confirm-1 | 0.547946 | 119 | 30 | −0.378 | −0.058 | +0.287 |
| confirm-2 | 0.646012 | 132 | 32 | −0.798 | +0.082 | +0.423 |
| confirm-3 | 0.881623 | 217 | 36 | −0.163 | +0.559 | +0.642 |
| confirm-4 | 0.438507 | 107 | 35 | −0.695 | −0.272 | +0.192 |
| confirm-5 | 0.963934 | 171 | 34 | −0.081 | +0.423 | +0.685 |
| confirm-6 | 0.343230 | 62 | 26 | −0.467 | +0.127 | +0.082 |
| **total** | **3.821252** | 808 (784 provider) | 193 | guarded-clm 6.404 | summary 2.960 | shell 1.509 |

**No provider retries** occurred. **The cost figures cover unequal work:** four of the six sessions stopped early, so they are not costs of the same work as guarded-clm's and the summary arm's eight-turn sessions.

### Mechanism

| Instance | Edits committed (earlier-turn / current-turn) | Thinking blocks omitted | Refusals (current-turn thinking / over limit / other rules) | Refusal receipts lost to rollback | Rollback events (steps undone) | Retries exhausted, final turn given | Reminders | Peak reported input |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| confirm-1 | 3 (3 / 0) | 4 | 2 / 0 / 0 | 0 | 7 (12) | yes | 6 | 29,966 |
| confirm-2 | 5 (5 / 0) | 6 | 0 / 1 / 0 | 1 | 7 (11) | yes | 6 | 30,274 |
| confirm-3 | 6 (3 / 3) | 3 | 1 / 0 / 3 | 1 | 7 (13) | yes | 9 | 29,978 |
| confirm-4 | 2 (2 / 0) | 3 | 2 / 0 / 1 | 0 | 7 (10) | yes | 4 | 29,444 |
| confirm-5 | 7 (5 / 2) | 2 | 1 / 0 / 1 | 1 | 7 (14) | yes | 7 | 29,772 |
| confirm-6 | 2 (2 / 0) | 2 | 0 / 0 / 0 | 0 | 3 (4) | no | 3 | 28,256 |
| **total** | **25 (20 / 5)** | 20 | **6 / 1 / 5** | 3 of 12 | 38 (64) | 5 of 6 | 35 | |

**The edits:**
- **Delivery:** every deletion of an accepted edit is absent from the request that carried it and from every later request. No deleted call reappears.
- **The 20 earlier-turn edits** removed or rewrote material from completed turns, and 20 thinking blocks were omitted from merged or altered replies. Every request after them was accepted.
- **The 5 current-turn edits** were all `replace_block` rewrites: four on this turn's tool results (`read_journal` and `list_changes`, one of them with eight rewrites in one set) and one on a note. **This path, untested in dev-tools2, was exercised live,** and every later request was accepted.

**The restriction and the other refusals:**
- **Six refused sets would have changed a current-turn reply carrying thinking.**
- **Five broke ordinary operation rules:**
  - a tool call's text must remain JSON, twice;
  - a thinking block has no editable text, twice;
  - the operations would change nothing, once.
- **One would have gone over the limit.**
- **Three of the twelve refusal reasons never reached the model,** because the step was undone by an overflow rollback. That is the existing behaviour.

**Endings and pressure:**
- **In five sessions** the six per-session retries were all used and the final turn given. Three of those then ended at the next over-limit request (confirm-1, -2 and -5).
- **confirm-3** ended when a response reached the 8,192-token output limit (`p015-truncation/1`).
- **confirm-4** completed after using its retries in an earlier turn.
- **confirm-6** never exhausted them.
- **Reported input versus the limit:** in confirm-2 the peak reported input (30,274) exceeded the 29,952 limit while the estimate stayed under it. It remained under the 32,000 budget, and the request was accepted.

### Reading, as pre-registered

- **The scores and completion:** `paper-clm-tools/2` scored 36/60 against confirm1's 58 (guarded-clm) and 59 (summary). The deficits come from four sessions that stopped early. It scored 16 points more than confirm1's `paper_clm_shell` v2, whose sessions all stopped at turn 4 or earlier.
- **What this is not:** a supplemental evaluation of a later-developed adaptation, on instances already used. It is not a contemporaneous comparison, not the paper's method, and not an interface-only ablation. **No difference is attributed to the editing interface alone:** the arm also differs in rollback, notices, the free-step rule and the version 2 restriction.
- **The mechanism:** compatibility held on every path exercised. Earlier-turn rebuilds with thinking omitted, current-turn result rewrites and current-turn refusals were all exercised. Commit-time refusal and an incompatible rollback still never occurred.
- **The binding constraint:** the session-wide budget of six rollback retries. It was exhausted in five of six sessions, mostly by the model's own `context_read` views and journal reads in the heaviest turn.
- **The sample:** one model, one task family, six instances. Instances are the units, and no significance claim is made.

### Charges

| | USD |
| --- | --- |
| confirmed (provider usage, 193 entries) | **3.821252** |
| assumed at the reservation | 0 |
| pending | 0 |

**The block:** US$3.821252 of the US$10 block.

**The ledger after the run:**
- spent 107.817646 (from 103.996394);
- programme 015 at 19.7179 (from 15.896648);
- the programme ceiling (43.55733) and ledger ceiling (131.657076) unchanged;
- nothing pending.
