# 014 – Model-authored context-management helpers with Jev semantic primitives

**Status: prompted live capability demonstration DONE (2026-10-13), one run.** The capability (`jev-primitive/1`) works end to end with a real Claude model and real Jev. **The use was instructed (configured use), not spontaneous adoption, and nothing here measures a benefit.** The benefit comparison (B below) is proposed only; it has no protocol and has not been run.

## Result: prompted live capability demonstration

- **Protocol:** [protocol.md](protocol.md), frozen before the run. **Instruction:** [demonstration-instruction.txt](demonstration-instruction.txt), appended to the task text and recorded verbatim in `run.json → extra_instruction` (SHA-256 prefix `fcc1da240f1408f8`, matching the frozen file).
- **Run:** `20261013T102922-clm_helpers-cacheon-jprim-w2-dev-1-7d51`, run once, on `w2-dev-1` (W2 changing-requirements coding workload, 5 stages, 35 hidden checks). Evidence: [`artifacts/runs/demo/guided/…`](artifacts/runs/demo/guided/20261013T102922-clm_helpers-cacheon-jprim-w2-dev-1-7d51/) (own `SHA256SUMS`).

### What Claude wrote, and what it asked Jev

At step 2, Claude wrote and saved `ctxhelper.py` ([final version](artifacts/runs/demo/guided/20261013T102922-clm_helpers-cacheon-jprim-w2-dev-1-7d51/workspace/ctxhelper.py); first version in `scripts/step-002.py`). Its `update(new_req, new_notes)` function:

1. sends **every current note** to `clm_jev.judge` with the question *"Do the new requirements change or replace the rule described in this note?"*, with the new stage's REQUIREMENTS.md as background;
2. for each note, **if the answer is above 0.5**, and the note is not labelled historical and not already marked, **prefixes the note** with `[REVIEW: possibly affected by newer stage, see CHANGED rules]`; otherwise the note is kept unchanged;
3. drops the step transcript entries (ids starting with `s`), whatever Jev answered;
4. appends the new stage's note, whose text Claude wrote itself in the calling script.

```python
p = probs.get(e['id'])
if 'historical' not in e['body'].lower() and '[REVIEW' not in e['body'] and p is not None and p > 0.5:
    e['body'] = '[REVIEW: possibly affected by newer stage, see CHANGED rules] ' + e['body']
```

### The four Jev calls (all inside a running execution)

| Step (stage) | Notes asked about → Jev answer | What the helper's logic did with the answer |
| --- | --- | --- |
| 4 (stage 2) | n.s1 0.21 | nothing marked; added n.s2 |
| 7 (stage 3: CSV → JSON, `exported_by` obligation triggered) | n.s1 **0.87**, n.s2 **0.67** | **marked n.s1 and n.s2**; added n.s3 |
| 10 (stage 4: owners see their own records) | n.s1 **0.92**, n.s2 0.17, n.s3 0.24 | the calling script first removed all markers; the helper then **re-marked only n.s1**; added n.s4 |
| 13 (stage 5: `max_records`, `truncated`) | n.s1 0.31, n.s2 0.17, n.s3 **0.63**, n.s4 0.18 | nothing new marked: n.s1 was already marked, and n.s3 contains "historical", so it was exempt; added n.s5 |

Each call followed the order execution start → Jev request and answer → execution result → accepted `context.json` edit, within the same step. Jev's own latency was 0.21–0.26 s per call, and the host handled each request in 0.39–0.44 s.

### Criteria (from code and traces)

| | Criterion | Result |
| --- | --- | --- |
| **A** | helper written and saved | **Yes.** `ctxhelper.py`, created at step 2 and revised at step 10. |
| **B** | real Jev called mid-execution | **Yes.** 4 requests, 4 calls (`jev-1.13.0`), all `ok`, at steps 4, 7, 10 and 13; recorded in `jev_primitive/0001–0004.json` and `jev/0001–0004.json`. |
| **C** | the answer governed the edit | **Yes, narrowly.** A threshold (`p > 0.5`) on the answers decided which notes received the marker: at steps 7 and 10 the marked set followed the answers. **But the edit Jev controlled was only a fixed prefix.** Jev never decided note content, removal, or the replacement text; Claude wrote the new notes in its calling scripts, and the transcript entries were dropped unconditionally. |
| **D** | accepted edit reaches the next request | **Yes**, for all 5 edits. Each next request's working context equals the accepted revision followed by the runtime's normal step entries (`sN.act`, `sN.obs`, `sN.rcpt`), and nothing else. |
| **E** | reuse | **Yes.** The saved helper ran at steps 4, 7, 10 and 13. At step 10 Claude improved it: the historical check became case-insensitive (the first version looked for `HISTORICAL`, but Claude's own note says `historical`), and already-marked notes are no longer marked twice. The improved check is what exempted n.s3 at step 13. |
| **F** | task outcome and edit quality | **35/35 hidden checks, no stale or regressed modules.** No visibly harmful edit. Two weaknesses: (1) the markers say *possibly affected* but not *which part*, and n.s1's CSV description stayed in the note after the CSV format was replaced (n.s3 records the replacement); (2) the word "historical" anywhere in a note exempts the whole note, so n.s3, which is current and partly affected by stage 5 (Jev 0.63), was left unmarked. n.s5 recorded the change, so nothing was lost here. The n.s2 marker at steps 7–9 was arguable (stage 3 triggered its obligation rather than replacing it). |

### Calls, cost and time

- **Main model:** 14 calls (14 actions, 0 repairs, 0 summaries, 0 retries). The primitive itself caused **no extra model calls**. Output tokens: 4,586.
- **Jev:** 4 calls, 10 items, 4,930 input tokens, USD 0.000208, 0.93 s total service latency.
- **Total:** USD 0.183869 (Anthropic 0.183661, TypeSafe 0.000208), 105.2 s. The ledger moved from USD 84.351732 to 84.535602 settled, within the USD 1 authorisation (ceiling 85.351732).
- **For orientation only, not a comparison:** the ordinary `clm_helpers` run on the same instance in 011 (a different prompt version, no instruction) also scored 35/35, with 15 calls, USD 0.150, 88 s and 3,383 output tokens. One run each cannot attribute any difference to the primitive.

### A worked example: task requirement versus library mechanism

- **The fictional task requirement (W2, stage 3):** the export format changes from CSV to JSON. This triggers a stage-2 obligation: once the format is no longer CSV, add `exported_by`.
- **The library mechanism:** at step 7 Claude's script implemented that change, then called its own `ctxhelper.update`. The helper asked Jev, about each note, whether the stage-3 text changes or replaces it. Jev answered 0.87 for n.s1 (which describes the CSV header) and 0.67 for n.s2 (which holds the obligation). The helper's `p > 0.5` rule marked both notes, and added Claude's new n.s3 note. The runtime validated the new `context.json`, accepted it as revision 9, and the step-8 request showed both marked notes. No extra Claude turn was spent on the decision.

### Limits of this result

- **One instructed run.** It shows the capability works with real models, not that Claude would choose it, nor that it helps.
- **Jev's influence was small:** a review marker on one or two notes. The substantive context content was written by Claude either way.
- **Same instance as the 011 pilot**, which ordinary CLM already solved: there was no error here for the helper to remove.

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

## Plan as written before the demonstration

### A. Prompted capability demonstration (one labelled run; done, see the result above)

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

**After the demonstration (proposal only; not authorised, not run):**
- **The observed overhead:**
  - **Tokens:** this run produced 1,203 more output tokens than the 011 ordinary run on the same instance. The helper code is part of that difference, but one run each cannot separate it from ordinary variation.
  - **Latency:** each Jev call added about 0.4 s.
  - **Notes:** Claude still wrote every note itself.
- **The displaced work:** in this run it was close to none, because Jev only decided a review marker.
- **Prerequisite:** a B comparison is worth a protocol only on instances where ordinary CLM visibly mis-edits notes, keeping stale rules or dropping rules still in force. The current W2 instances show no such errors (35/35 in both 011 and here).
- **Reporting:** configured use (an instruction as here) and voluntary use (the primitive available, with no instruction) must be separate conditions, each against the same `clm_helpers` control.
