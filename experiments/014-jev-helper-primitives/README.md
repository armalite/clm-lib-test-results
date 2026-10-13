# 014 – Model-authored context-management helpers with Jev semantic primitives

**Status: PLANNED.** The core capability (`jev-primitive/1`) is implemented in clm-lib and verified **offline only**, with a scripted fake Jev. **No live run or paid call has been made.**

## Why a new experiment

**What 008–012 tested:** *advisory* and *filtering* integrations. Jev's answers reached Claude as messages it had to read and act on in another turn (008–011), or a host filter changed what Claude saw (012). See the [programme review](../jev-programme-review.md).

**The idea those experiments left untested:** in the original Jev + CLM idea, Claude's **own context-management code** calls Jev as a semantic primitive and uses the answers in the same execution. For example, a saved helper asks which notes an update affects, then rewrites only those notes. **No extra Claude turn is spent requesting or interpreting the answer, and the editing policy is the model's code, not a host rule.**

**What earlier findings say about it:** they neither establish nor rule out its value.

**Implementing the capability first:** it can be built before choosing a final evaluation workload, and it has been.

## The capability (clm-lib SPEC §25; offline-verified)

- **The interface for model code:** `import clm_jev`; `clm_jev.judge(question, {key: text}, background="", criteria=None)` returns `{"status", "answers": {key: probability}, "model", "error"}`.
- **What happens during the call:** the call waits while the host answers through a mailbox in the workspace, then the same execution continues.
- **Who decides what:** the code chooses the entries, the question, how to read the probabilities, and what to write. The runtime validates the resulting `context.json` as for any CLM edit.
- **Safeguards:** opt-in; up to 20 items per call, 4 calls per execution and 30 per run; size limits; every request and response recorded; ledgered attempts; no sandbox network or credentials; no host file reading on the code's behalf.

**What it does not remove:**
- Jev's latency and cost;
- the tokens Claude spends writing or revising the helper code;
- errors from badly chosen questions or thresholds;
- the input Claude has already processed before it runs the helper.

**Offline mechanism tests** (`tests/test_jev_primitive.py`, real sandbox, **scripted fake Jev**):
- a saved helper asks about three requirements against an update and revises only the affected one, keeping the unrelated requirements and the historical observation; the edit is accepted and appears in the next request;
- the helper is reused in a later step, and a different answer takes a different branch;
- service errors are reported to the code (which leaves the context unchanged);
- call limits, invalid requests, a timeout while waiting, and an unanswered request at exit;
- **the same number of model calls as scripted actions:** the Jev exchange happens between the execution's start and result events.

**These tests show the mechanism works. They are not evidence that a real model writes a useful helper, or that Jev improves outcomes.**

## Next stage (planned; not authorised, not run)

### A. Prompted capability demonstration (one labelled run)

- **What runs:** one live run with `--jev-primitive on` on the existing **W2 changing-requirements workload** (`w2-dev-1`), whose staged updates change some rules and leave others in force.
- **An added instruction, declared as such:** "In this run, write and save a context-management helper that uses `clm_jev` to decide which of your notes a new stage changes, and use it at least once." This makes it a **configured** demonstration, not spontaneous adoption.
- **What it must show:**
  - a real model writes and saves a helper;
  - the helper calls real Jev mid-execution and uses the answers;
  - the resulting edit is accepted and appears in the next request;
  - the ledger and records are complete.
- **What it cannot show:** any benefit.
- **Estimated cost:** about USD 0.2–0.4 (Anthropic) plus under USD 0.01 (TypeSafe). An authorisation of USD 1 would cover one retry.

### B. Benefit comparison (only after A works; needs its own protocol)

- **A:** ordinary CLM with the same coding and helper abilities (`clm_helpers`).
- **B:** the same plus `clm_jev`, either available (optional) or under a **declared** policy instruction ("use a Jev-assisted helper when a new stage arrives"). The two are reported separately.

**Guards:**
- **The control is not made to spend extra calls.** It keeps its ordinary one-step editing; no confirmation or review step is added to either condition.
- **Optional adoption is measured separately:** whether B uses the primitive at all, which 008 and 010 v1 show can be zero, is kept apart from its effect when used. A configured-use condition is labelled as configured.
- **No privileged evidence:** Jev sees only text B's own code sends, which A's code could also read.
- **Code is not proof of benefit:** writing a helper is not evidence of a performance benefit. Outcomes are correctness, cost, time, calls and tokens, against the control.

**What could be displaced:** the reasoning tokens and deliberation Claude spends deciding which notes an update affects, possibly a separate inspection step, and possibly over-editing (rewriting unaffected notes).

**What remains:**
- every model turn Claude takes anyway;
- writing and maintaining the helper;
- Jev's calls;
- the fact that Claude still reads the update and its context in each request.

**Can existing workloads exercise it?** **W2 can** (staged partial changes and a deferred obligation), and incident rounds could (round updates against many notes). But **in 008–012, Claude already handled these updates well**, so there is little error to remove. A benefit comparison on these workloads is therefore expected to measure overhead more than benefit. **Run A before deciding whether B is worth a protocol.** No new generator is proposed.

**No saving is promised.**
