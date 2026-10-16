# 015 – Running sessions with the resumable launcher

_Written 2026-10-16. **No live run is authorised.** These instructions are for offline (scripted) launches now,
and for a live launch only after a separate written authorisation._

The launcher is `python -m clm_lib.p015.launcher`, in clm-lib's p015 environment (`.venv-p015`), started from the
clm-lib checkout. It runs on its own, independent of any chat session. Everything it knows is on disk in the
launch directory. It is specified in clm-lib SPEC §31.

## Commands

```bash
.venv-p015/bin/python -m clm_lib.p015.launcher plan SPEC.json LAUNCH_DIR
```
```bash
.venv-p015/bin/python -m clm_lib.p015.launcher run LAUNCH_DIR
```
```bash
.venv-p015/bin/python -m clm_lib.p015.launcher status LAUNCH_DIR
```
```bash
.venv-p015/bin/python -m clm_lib.p015.launcher stop LAUNCH_DIR
```
```bash
.venv-p015/bin/python -m clm_lib.p015.launcher export LAUNCH_DIR DEST_DIR
```

- **`plan`** writes the immutable launch contract (`contract.json` and `contract.sha256`). It holds the sessions in their run order (arms rotated per instance), each session's cache tag, the arm and model settings, the ledger and authorisation paths, and the fingerprints of the configuration and the loaded source.
- **`run`** dispatches the planned sessions in order.
  - **It refuses** (exit code 4) if the contract, its digest or any fingerprint differs; if another launcher holds the lock (exit 3); or while a stop is pending (exit 6).
  - **It stops** with exit code 5 when the spending allowance is reached.
- **`stop`** stops after the current session. `stop --now` stops before the next provider attempt or turn, as does SIGTERM or SIGINT. `stop --clear` removes a pending stop.
- **`resolve SESSION --as abandoned|rerun --reason TEXT`** decides an `uncertain`, `interrupted` or `stopped` session: abandoned (a missing cell) or rerun (a new run directory; the old one is kept). A finished run whose outcome is `complete` or `arm_failure` is a result and cannot be rerun.
- **Paths:** give the ledger and authorisation paths in the spec relative to the clm-lib checkout. `export` reports a problem, and exits 1, if the contract or the event log holds a home-directory path.
- **`export`** exports every run: complete runs in full, incomplete ones as partial exports that declare what is missing. Each export is checked, and a launch manifest ties them together.

## Session states and outcomes

| state | meaning | next |
| --- | --- | --- |
| `planned` | not yet dispatched | `run` dispatches it |
| `running` | a launcher is running it; found at start, it means the launcher died | `run` marks it `uncertain` or `interrupted` |
| `finished` | the session ran to an ending, recorded with its outcome | none; kept |
| `uncertain` | the launcher died with a provider attempt in flight; its outcome is unknown and charged at the full reservation | `resolve` |
| `interrupted` | the launcher died between attempts | `resolve` |
| `stopped` | a stop was honoured during the session | `resolve` |
| `abandoned` | resolved as a missing cell | none; kept |

**Outcomes of finished runs:**
- **`complete`:** every question ended normally.
- **`arm_failure`:** `context_limit`, `step_limit`, `call_cap`, `summary_call_cap` or `model_behaviour`. These are results of the arm.
- **`provider_failure`:** the provider failed after the bounded retries.
- **`spend_stopped`:** a spending refusal.
- **`harness_defect`:** the harness failed: an accounting-bound violation, an unavailable sandbox, a task-tool failure, or an error it cannot attribute. This is never counted against an arm.

## Spending controls

**The authorisation file** is written by the maintainer, never by the launcher. It names the experiment and this launch:

```json
{"experiment": "015", "launch_id": "<launch>", "programme_ceiling_usd": 0, "block_stop_usd": 0,
 "live": false, "granted_by": "...", "granted_at": "...", "reason": "..."}
```

**When the launcher rereads it:** before every user turn and every provider attempt, summariser attempts and retries included. A restarted launcher rereads it the same way.

**The check before each attempt:** the attempt's full reservation must fit within both of these:
- **the programme ceiling,** less the spend of every `p015:*` ledger entry and any open reservation;
- **the block stop,** less this launch's spend and any open reservation.

**What the check counts:** open reservations include those another process has left pending in the ledger file. A refused attempt is recorded and never reaches the model.

**Reporting:** confirmed cost (provider usage at the dated price) is reported apart from charges assumed at the reservation (unknown outcomes) and from open reservations.

**Carry-over:** an authorisation names one launch, so unspent authorisation never carries over. The launcher never creates or raises an authorisation or a ledger ceiling.

**The ledger** is the one in the contract. The launcher opens an existing ledger at its stored ceiling, so it never lowers or raises it. A live launch must use the persistent clm-lib ledger, with a ceiling the maintainer has set for this experiment (`clm-lib budget --set-ceiling X --reason "..."`). No such ceiling has been set.

## Before any live launch (not done)

- **A written authorisation** for a specific block, with a programme ceiling and a block stop.
- **The development smoke,** separately authorised (protocol-draft.md, readiness).
- **`mode: "live"` in the spec,** a dated price for the model in `configs/prices.toml` (present for `claude-sonnet-5`), and a credential source. The launcher checks only that a source exists, never its value.
