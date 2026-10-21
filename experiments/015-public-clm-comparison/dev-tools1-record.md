# 015 – `dev-tools1`: one live development session of `paper-clm-tools/1`

_Pre-run record written 2026-10-21, before dispatch. The result is added below after the run._

## Scope and authorisation

**What runs:** one session of `paper_clm_tools` (`paper-clm-tools/1`, [paper-clm-tools.md](paper-clm-tools.md)) on docthread-dev-1, all eight turns (`docthread-task/2`, `p015-turn-endings/1`, `p015-truncation/1`).
- **The plan:** clm-lib `configs/p015/proposed-tools-dev1.json`, committed at `d7f362e` and planned unmodified (copied here as [dev-tools1-spec.json](dev-tools1-spec.json)). Its note and `settings_status` still say "not authorised"; the authorisation below supersedes them.
- **The settings:** the shared model settings as for dev-v3a (`claude-sonnet-5`, adaptive thinking, effort high, `max_tokens` 8,192, 5-minute cache, `p015-retry/1` with 2 provider retries). The arm's documented settings: limit 29,952 (32,000 − 2,048), 60 steps and 144 calls per turn, rollback to a 2,048-token margin with 6 retries per session and then a final turn, readouts on, finalize at 3 steps left.
- **Unchanged before and during the run:** the instructions, the implementation, the estimator, the task, the scorer and the settings. guarded-clm and every shell-arm version are untouched.

**Not an interface-only ablation:** `paper_clm_tools` differs from `paper_clm_shell` in its rollback (to a margin, retries per session, a final-turn note), its notices (kept in the history, with size readouts on every tool result) and its free-step rule (only accepted `context_apply` steps are free), as well as in its interface. A difference between this session and dev-v3a cannot be attributed to the interface alone.

**Authorisation:** given by the maintainer on 2026-10-21. It covers exactly one development session, including its configured automatic provider retries, up to US$4 in total, allocated from the remaining overall allowance. The ledger and programme ceilings are not raised. No second session, replacement run or comparison block is authorised.
- **The launch:** a new launch ID, `dev-tools1`, with its own block authorisation. The dev-v3a authorisation is not reused.
- **The effective block limit is US$4.00.** Programme room and ledger room are both US$28.878563.
- **What counts towards the block:** confirmed charges, charges assumed at the reservation for uncertain outcomes, and open reservations.

**Starting state, verified:** cumulative ledger spend US$102.778513, programme 015 US$14.678767, no pending reservations, ledger ceiling US$131.657076. These are the expected figures.

**The freeze:** [dev-tools1-freeze-record.json](dev-tools1-freeze-record.json).

| Item | Value |
| --- | --- |
| contract sha256 | `706a01b3…` |
| clm-lib | `d7f362e` |
| clm-lib source sha256 | `bbf8a943…` |
| instance | docthread-dev-1 (seed 7301, `lease`) |
| prices.toml | unchanged |
| dependencies | pydantic-ai-slim 2.27.1, anthropic 0.125.0, Python 3.13.15 |

## Predeclared interpretation

This session checks live compatibility and observes editing behaviour. Four things are recorded separately:
1. whether provider requests are accepted, including requests after edits;
2. whether the model attempts substantive context reductions;
3. whether those edits are accepted and reach later requests;
4. pressure, rollback, recovery, later-turn continuation and the final task outcome.

**How outcomes are read:**
- **No edit:** the session is inconclusive about live editing.
- **Invalid edits or wrong answers** are reported as outcomes, without changing the arm.
- **Not a compatibility gate:** a perfect score or a completed task is not required.
- **A concrete provider or harness defect** stops further dispatch, and the evidence is preserved. Nothing is patched and retried within this authorisation.

## Result (added after the run)

**The run:** launched detached at 2026-10-20T11:57:52Z (UTC; 2026-10-21 local) and finished at 11:59:25Z. Wall time was 87 s, of which 83.9 s was provider time. The session ended in turn 4 as **`provider_failure`**: the provider returned HTTP 400, `invalid_request_error`, for the request that carried the second accepted edit. The launcher does not retry a 400 and does not dispatch anything after a session ends, so dispatch stopped there. Nothing was patched or rerun.

**The evidence:** [dev-tools1-export/](dev-tools1-export/), which verifies (manifest problems none, checksums pass, no home paths or credentials), and the exposure report [dev-tools1-exposure.md](dev-tools1-exposure.md) (and `.json`).

### 1. Provider compatibility

**19 of 20 requests were accepted,** including the request carrying the first committed edit (attempt 17).

**The request carrying the second committed edit (attempt 19) was rejected:**

> `messages.1.content.3`: `thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.

**Why:** the rebuild.
- The second edit deleted reads 6 and 8 of the moss-ocr journal (each call with its result) and the empty thinking block between them.
- That emptied the messages between the model's first reply of turn 1 and its reply holding read 9. The rebuild merges same-kind neighbours, so those two replies became one assistant message: thinking, text, thinking, thinking, tool call.
- `content.3` is the thinking block of the later reply, moved into the earlier one.

**The first edit's rebuild** had also merged replies: it moved a thinking block to `content.2` of the same message. That request was accepted. **Which rule the provider applied is not isolated.** The second edit differs in moving a further thinking block and in deleting one.

This is the live uncertainty recorded before the run in [paper-clm-tools.md](paper-clm-tools.md): whether the provider accepts rebuilt replies that carry thinking blocks. **It is a concrete defect of `paper-clm-tools/1` under adaptive thinking.**

### 2. Context reductions attempted

The model attempted two substantive reductions, both deletions of whole tool exchanges, in turn 4 after the second rollback. It inserted no notes and rewrote no blocks.

| Edit | Staged after | Operation | What it removed | Request size (chars) |
| --- | --- | --- | --- | --- |
| 1 | attempt 16 | `delete` blocks 2–9, 11–13, 15–16 | turn 1's six `queue_stats` calls and their results, and `read_journal` page 1 with its result | 93,791 → 77,744 |
| 2 | attempt 18 | `delete` blocks 4–8 | `read_journal` pages 6 and 8 with their results, and one empty thinking block | 91,294 → 74,214 (not delivered) |

### 3. Acceptance and delivery

**Both sets were accepted when staged:**
- **Edit 1:** projected size 24,929 tokens.
- **Edit 2:** projected size 23,392 tokens.

**Both were committed when the next request was built.** No edit was rejected at staging or at commit.

**Edit 1 reached the next request.** Attempt 17 was sent without the seven calls and their results: the six queue tables of about 795 characters each, and the 6,103-character journal page 1. The provider accepted it, and the model went on with turn 4. The page-1 text survived in that request only as a copy inside a `context_read` result. The model had read its own context into a tool result, so the reduction was partly offset by its own reads.

**Edit 2 was committed into attempt 19, which the provider rejected.**

### 4. Pressure, recovery and outcome

**Pressure built in turn 4:**
- The context reached 28,135 estimated tokens at attempt 11 and gave the first of three reminders.
- **Rollback 1 (attempt 12, retry 1 of 6):** undid a `read_journal` page and a `context_read` of blocks 1–5, back to 25,179 tokens.
- **Rollback 2 (attempt 15, retry 2 of 6):** undid two large `context_read` views (blocks 1–52, then blocks 14–52 page 2), back to 25,653 tokens.

The overflows in turn 4 were caused largely by the model's own `context_read` views, each a copy of up to 8,000 characters of its context. After the second rollback the model made edit 1, which was a free step, and continued.

**No final turn was given, and no request was sent over the limit:** the peak estimate was 29,397 against 29,952.

**The outcome:** turns 1–3 completed, all correct. Turn 4 ended at the provider failure, and turns 5–8 never ran.
- **Points:** 4/10 (turn 1 2/2, turn 2 1/1, turn 3 1/1).
- **Recall:** 0/3. All three recall fields are in unrun turns, so they score as missing.

**Attempts:** 20 main attempts (11 in turn 4), no retries, 1 failed (the 400), none truncated or refused. The counters were 8 task steps, 2 free steps and 10 calls in turn 4, with 19 task-tool calls in all.

### Charges

| | USD |
| --- | --- |
| confirmed (provider usage) | **0.270354** |
| assumed at the reservation | 0 |
| pending | 0 |
| the 400 attempt | 0 (billing `none`) |

**The block:** US$0.270354 of the US$4 block.

**The ledger after the run:**
- spent 103.048867 (from 102.778513);
- programme 015 at 14.949121 (from 14.678767);
- ceiling unchanged at 131.657076;
- nothing pending.

### Reading against the predeclared interpretation

- **Compatibility:** not established. A request carrying an accepted edit was rejected by the provider, because the rebuilt reply's thinking blocks were changed.
- **Editing:** demonstrated live in part. The model chose substantive reductions without prompting beyond the arm's notices. Both were accepted, and one was delivered and accepted by the provider.
- **Later-turn continuation:** not observed past turn 4.

### Blocker to a comparison

`paper-clm-tools/1` cannot be used with adaptive thinking as it stands. Its rebuild can merge or alter replies that carry signed thinking blocks, which the provider refuses.

**Options for a reviewed revision (none applied):**
- never merge replies, or never change a reply that holds thinking blocks;
- make thinking blocks non-deletable;
- drop thinking from rebuilt replies, as `paper-clm-shell/3` does.

A further observation, not a defect: `context_read` views are added to the context as ordinary tool results. In this session they caused most of the overflow, and they kept copies of deleted text.

**No further session is authorised.** The launch has no rerun, and the session's `provider_failure` is not resolved for a rerun.

## Note added 2026-10-21: diagnosis and correction (the record above is kept as written)

**The diagnosis** ([paper-clm-tools-v2.md](paper-clm-tools-v2.md)): no thinking text or signature was changed. The rebuild merged replies, so the refused message 1 held thinking from three provider responses, two of them consecutive. The provider requires a reply's thinking blocks to come back exactly as returned, and it combines consecutive assistant messages.

**The correction:** `paper-clm-tools/2` (clm-lib SPEC §40), verified offline only. A merged or altered reply from an earlier user turn is sent without its thinking, which the documentation allows outside tool use. Replies echoed verbatim, and the turn in progress, keep their thinking.

**This record is unchanged:** it remains a `paper-clm-tools/1` result, and no new session has run.

