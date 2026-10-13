# 014 – Protocol: prompted live capability demonstration (frozen 2026-10-13, before the run)

**What this is:** a **configured capability demonstration**. One run checks that a real Claude model writes a reusable context-management helper that calls real Jev during its own sandbox execution, uses the answer in its own editing logic, and produces an accepted context revision that the next model request uses.

**What it is not:** an adoption experiment or a benefit comparison. **The use of the primitive is instructed, not spontaneous.**

## Settings

- **Task:** `w2-dev-1` (W2 changing-requirements coding workload, generator `export-gen/1`, scorer `export-checks/1`; 5 stages, 35 hidden checks), mode `clm_helpers`.
- **Models:** main model `claude-opus-5-5`, effort low, structured output. Jev `jev-1.13.0` (host client, 15 s timeout, 1 runtime retry, every attempt ledgered; USD 0.042 per million input tokens).
- **Request settings:** `blocks/1` layout, prompt caching on (5 min), `run-tag/1` isolation, 90 calls, an 8,000-token context budget, a 6,000-character output cap, a 30 s execution timeout.
- **Primitive:** `jev-primitive/1` on (`run --jev-primitive on`). Limits: 4 calls per execution, 30 per run, 20 items per call. The `clm_jev.judge` client has a 25 s default wait.
  - **Prompt:** `JEV_PRIMITIVE_CLAUSE` (prompt version `2026-10-13.8`) in the system prompt.
  - **Timeout interplay:** a host call (15 s, plus one retry after 1 s) can outlast the 30 s sandbox limit. The call is then still recorded and charged once, and the execution times out. Requests still pending when an execution ends get no Jev call.
- **The configured instruction:** appended to the task text with `run --extra-instruction-file demonstration-instruction.txt` and recorded verbatim in `run.json → extra_instruction`. Its SHA-256 prefix is `fcc1da240f1408f8`. It names no entries, gives no helper code, question, thresholds or answers, and uses no evaluator truth:

  ```
  CONFIGURED CAPABILITY DEMONSTRATION (this run only):
  - Manage your working context through a reusable Python helper module that you write and save in
    /task/workspace. Use your helper whenever you edit context.json after a new stage is released.
  - Inside the helper, use clm_jev.judge to ask whether newly released requirements affect each of
    your current notes, and use the returned values in the helper's own logic to decide which
    notes to revise, keep or remove, and what text to write. You choose the question wording, how
    to interpret the values, and the replacement text.
  - Keep notes about requirements that a new stage does not affect, and keep any information you
    have labelled as historical.
  - Reuse the saved helper (you may improve it) when a later stage is released.
  ```
- **Source:** clm-lib HEAD `024fc76` plus an uncommitted patch (git diff SHA-256 prefix `8c8c80de61181e8f`):
  - the `extra_instruction` run option (`runner.py`, `cli.py`) and its test;
  - `configs/exp014.toml` (`fe86d34d489a177e`; identical to `exp011pilot.toml` except the ceiling and `[jev_primitive]`).

  File prefixes: `runner.py` `b311d115`, `jev_primitive.py` `3408dee1`, `executor.py` `34d8416b`.
- **Budget:** **USD 1 in total** (both providers, retries included). The ceiling is set from the settled spend of USD 84.351732 to **85.351732**, replacing the unused 012 v2 allowance. **One run only:** no rerun for a poor or unsuccessful result. A partial run is kept if the budget is reached.

## What is checked afterwards (from code and traces)

| | Criterion | Evidence |
| --- | --- | --- |
| **A** | A context-management function was written and saved | workspace files and the step scripts |
| **B** | It called real Jev while the same execution was still running | `jev_primitive/NNNN.json`, `jev/NNNN.json`, events (execution start → `jev_primitive` → execution result) |
| **C** | The answer governed the edit | the helper source: a condition, selection or transformation that uses `answers` and decides the edit. Printing values is not enough |
| **D** | The edit was accepted, and the next request held exactly the accepted entries plus normal runtime additions | the `context_edit` event, the revisions, and the next request's working context |
| **E** | The saved helper ran again on a later update | step scripts and primitive records, reported whether or not it happened |
| **F** | Task outcome and edit quality | hidden checks, and the before/after context, for visibly harmful or unnecessary edits |

**Also reported:**
- main-model calls, including any extra calls the configured workflow caused;
- Jev calls, latency and cost;
- total cost and elapsed time.

**No performance benefit is claimed from one configured run.**

## Result record (added after the run; the sections above are unchanged)

- **Run:** `20261013T102922-clm_helpers-cacheon-jprim-w2-dev-1-7d51`, run once on 2026-10-13. **Not rerun.** The source tree and the instruction matched the frozen prefixes above. `run.json → extra_instruction` hashes to `fcc1da240f1408f8`.
- **Outcome:** completed; 35/35 hidden checks.
- **Calls:**
  - main model: 14 calls, 0 repairs, 0 summaries, 0 retries;
  - Jev: 4 primitive requests and 4 calls, all `ok`, none unanswered at exit, no limit reached.
- **Cost:** USD 0.183869 (Anthropic 0.183661, TypeSafe 0.000208); 105.2 s. The ledger stands at USD 84.535602 settled, against the 85.351732 ceiling.
- **Criteria:**
  - **A:** yes.
  - **B:** yes.
  - **C:** yes, narrowly. A threshold on the answers selected which notes received a fixed review marker; Jev did not decide note content or removal.
  - **D:** yes, for all 5 accepted edits.
  - **E:** yes. The helper ran at 4 updates and was revised once.
  - **F:** 35/35, with no visibly harmful edit. The weaknesses are listed in the README.
- **Details:** in [README.md](README.md#result-prompted-live-capability-demonstration).
