# 015 – `paper_clm_tools` (`paper-clm-tools/1`): specification, differences and offline verification

_Written 2026-10-20. **Offline only: no model has run this arm, and it has not been evaluated.** The implementation is clm-lib SPEC §39 (`src/clm_lib/p015/papertools.py`). confirm1 and dev-v3a are unchanged: they remain `paper-clm-shell/2` and `/3` results respectively, and dev-v3a remains a failed development validation._

## What it is

**`paper_clm_tools` is the second paper-style arm** planned for programme 015 (clm-lib SPEC §27). Like the paper's CLM, the model manages its own context. It does so through two structured tools instead of a shell and a context file:
- `context_read`, to view its context as numbered blocks;
- `context_apply`, to change it.

**It is a structured-tools adaptation, not a reproduction of the paper's shell interface.** The paper and its harness README describe only the shell design ([paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md)). The arm's mechanics follow an existing structured-tools implementation of the same design, used as an engineering reference. That implementation is not public; this document describes its behaviour only as far as the arm reproduces it. Its wording, prompts, results and configuration are not used.

`paper_clm_shell` is unchanged (versions 1, 2 and 3), and the two designs are kept apart: the tools arm does not take the shell arm's rules where they differ (see below).

## The specification

**The context:**
- **Blocks:** one numbered block per message part, after the pinned parts. Each block is user text, a note, the model's reply text, a tool call (its arguments as JSON) or a tool result. The runtime keeps each block's kind, tool name and call id; the model changes text only.
- **Pinned parts:** the system prompt, the first user message and every rollback note. They are not shown as blocks and cannot be changed.
- **`context_read(from_block, to_block, page)`:** blocks rendered as `=== block n | role ===` and their text, paged to the 8,000-character tool-output cap.
- **`context_apply(ops)`:** one operation set per step. It is checked at once, against the context including the calling reply, and a second `context_apply` in the same step is refused. An accepted set is staged and applied, all or nothing, when the next request is built.

**The operations:**

| Operation | Effect |
| --- | --- |
| `replace_text` {block, old, new} | Replaces text that occurs exactly once in the block |
| `replace_block` {block, text} | Replaces the block's whole text. A tool result stays the native result of its call; a tool call's text must stay a JSON object |
| `delete` {blocks} | Removes blocks; a tool call and its result go together. The current step's calls cannot be deleted |
| `substitute` {pattern, replacement, blocks?} | A regular-expression substitution over the listed blocks or, without a list, over every text block that exists at staging |
| `insert` {after, role, text} | Adds `[role]\ntext` as user text in the request that holds or follows block `after` (0: the start), after that request's tool results |

**The rebuild and its checks:**
- emptied messages are dropped, and same-kind neighbours are merged;
- the request being built stays the framework's own object;
- the result must start with a request and may not leave a call without its result;
- a block may not be both changed and removed, and no block may be left empty.

**Feedback:**
- **A refused set** gets `REJECTED: <reason> Your context is unchanged.`
- **An accepted set** gets `Accepted: N operation(s) on block(s) …; your context will be about X of L tokens. They take effect on your next call.`
- **The `fit` gate** applies at staging and again at the commit. A set that no longer applies at the commit is reported in a note, and nothing changes.

**The limit and recovery:**
- **The limit:** the budget minus the 2,048-token reserve (32,000 → 29,952), checked on each request as sent, with the readouts and notes included.
- **Over the limit:**
  - the newest replies and their tool results are undone until 2,048 tokens are free;
  - a pinned note names the calls whose output did not fit and asks the model to make room (`retry k of 6`).
- **Retries:** up to 6 **per session**, across turns. User messages are never removed.
- **After the retries:** the note says this is the model's last turn and asks for its final answer. Any later over-limit request in the session ends the turn as `context_limit`.
- **With `max_retries=0`,** the first over-limit request ends the turn.

**Notices,** kept in the history as user text. Rollback notes are pinned; the others can be edited like any block.
- **Readouts:** each tool result in the request ends with `[context: about N of L tokens]`.
- **The reminder:** given once when the context is within 2,048 tokens of the limit, and re-armed when it falls below.
- **The finalize notice:** given when at most 3 steps or calls are left.

**Steps:**
- 60 task steps and 144 model calls per user turn.
- A response whose only calls are `context_apply`, every one accepted, is a free step.
- `context_read` and a rejected edit are task steps.

**The settings and their status:**

| Setting | Value | Status |
| --- | --- | --- |
| `budget_tokens` / `reserve_tokens` | 32,000 / 2,048 (limit 29,952) | Shared with every 015 arm |
| `max_steps` / call cap | 60 / 144 per turn | Shared with every 015 arm |
| `max_output_chars` (`context_read` pages) | 8,000 | The task tools' output cap |
| `max_retries` | 6 per session | The reference's investigation setting |
| rollback margin, reminder point | 2,048 tokens | The reference's setting (the reserve) |
| `readouts` | on | The reference's setting |
| `finalize_steps` | 3 | The reference's setting |
| a reported input over the budget ends the session | off | The reference's default; programme 015 has no such rule for any arm |

## Differences from the structured-tools reference (all intentional)

1. **Code and wording:** the code is written for clm-lib. The model-facing instructions, tool descriptions, notices, receipts and refusal reasons are clm-lib's own wording. They carry the same information, the same prefixes (`Accepted:`, `REJECTED:`, `[context manager]`) and the same readout format.
2. **The size estimate:** clm-lib's `p015-ratio-estimate/1`, the same estimator as the shell and summary arms, replaces the reference's own estimate and calibration. A different estimate can move the points at which reminders, rollbacks and refusals happen.
3. **The workload and prompts:** programme 015's docthread task, system prompt, task tools, output cap and scorer are used, with the shared model settings. None of the reference's own tasks, prompts, conditions or configuration is used.
4. **One capability:** the step limit and the context run in one capability, in the reference's order: the step check first, then the commit, the limit and the notices. The 144-call cap is also the runner's request limit, as for the other arms.
5. **Trace records:** the arm's own record types (`tools_edit`, `tools_commit`, `tools_rollback`, `tools_reminder`, `tools_request`). A commit record keeps sizes and the block count, not a rendering of the whole context.
6. **Not reproduced:** a block kind that the reference uses only for its other context modes. No message here can produce it.

## Differences from `paper_clm_shell` (its `paper` profile, versions 2 and 3)

Recorded as they stand. Neither arm has been changed towards the other.

| Rule | `paper_clm_shell` | `paper_clm_tools` |
| --- | --- | --- |
| **Interface** | One `bash` tool. The context is mirrored to a file in a sandbox and edited with shell commands | `context_read` and `context_apply`; no sandbox |
| **Representation** | v2: one block per message; v3: one block per part, under `[[CTX_BLOCK n …]]` headers the model must keep | One block per part. Numbers are given by the runtime and never written by the model |
| **When an edit applies** | Checked after the command and applied to the next request | Staged and checked at once, applied when the next request is built, with the fit gate checked again |
| **Free step** | An edit-only command: the file changed, exit 0, no output. A rejected edit is also free | Only `context_apply` calls, every one accepted. A rejected edit is a task step |
| **Rollback unit** | The last step per retry | The newest replies, until 2,048 tokens are free |
| **Rollback scope** | The current user turn only | The session: earlier turns' replies can be undone. User messages are never removed |
| **Retry count** | 6 per user turn | 6 per session |
| **After the retries** | One final over-limit request, then `context_limit` | A note stating the last turn, then `context_limit` at the next over-limit request |
| **A request over the 32,000 budget** | Ends the turn at once | Not sent, by the estimate: any request over the 29,952 limit is rolled back or ends the turn |
| **Size readouts** | None | On every tool result |
| **Reminder** | Once per crossing of the limit minus 2,048 tokens, transient | Once per crossing of the same point, kept in the history |
| **Notices** | Transient (`[context]`), never kept | Kept as user text (`[context manager]`); rollback notes pinned |
| **Rejection feedback** | In the command's result; v2 and v3 repeat it once beside the rollback notice if its step is undone | In the receipt; a commit-time failure is a kept note |
| **Shared** | budget, reserve, steps, call cap, output cap, `fit` gate, task, scorer, model settings | the same |

## Fidelity limitations

- **The interface is not the paper's.** The paper's CLM edits a mirrored file with shell commands; this arm uses structured operations. It answers a different question: whether model-managed context works through purpose-built tools. It does not answer whether it works through a shell.
- **The recovery rules come from the reference, not the paper.** The retry count (6) matches the paper's BrowseComp-Plus setting. The margin rollback, the final turn and the per-session count follow the reference, which is consistent with the paper harness README's description. The paper does not say what its six retries are counted over.
- **The size estimate is clm-lib's.** It is calibrated from the provider's reported input. Before the first observation it uses a fixed ratio, so the first requests' sizes are approximate.
- **Thinking blocks:** a reply whose text is changed keeps its other parts, its thinking included. Whether the provider accepts such a replayed reply has not been checked live. The shell arm's version 3 drops reasoning from a changed reply; that rule was not adopted here.

## Offline verification

**Where:** clm-lib `tests/p015/test_paper_tools.py`, 33 tests. They use synthetic messages and fixtures, scripted responses, a placeholder key and temporary ledgers, with network blocked. No provider or token-counting call was made.

**The operations, on synthetic messages:**
- the block view and pinning;
- a summary replacing a tool result stays the native result of its call;
- deleting either half of a pair deletes both, and neighbours merge;
- `replace_text`, `substitute` and `insert` (placement after the results; the role becomes the label);
- a whole history replaced by one note;
- the final request changes in place only when asked;
- twelve kinds of invalid set are refused with their reasons and change nothing: no operations, an unknown block, text not found exactly once, an emptied block, no change, an unknown operation, non-JSON call text, a changed half of a deleted pair, a deleted block also changed, a bad role, an invalid pattern, and no request left to send;
- the current step's calls cannot be deleted;
- paging, and rollback (including nothing left to undo);
- the instructions state the mechanism and settings only;
- a staged set that no longer applies at the commit is reported and changes nothing.

**Sessions through the real `ArmSession` and Pydantic AI's Anthropic adapter,** over an in-memory HTTP transport, so that the request bodies are checked:
- **Turn 1:** a journal result is replaced by a one-line summary and another read's call is deleted. The next request carries the summary as the native `tool_result` of its call; the deleted call and result are gone.
- **The receipt** starts `Accepted:` and carries the readout. The edit step was free: 3 task steps and 1 free step.
- **Turn 2** starts from the edited context. Its deletion of the summarised pair, and its inserted note, reach the next request.
- **Every request body** alternates roles and pairs each `tool_use` with its `tool_result`.
- **The commit records** show the context shrinking.
- **A rejected edit** (text not found) leaves every earlier message identical in the next body. It counts as a task step.
- **A second `context_apply` in one step** is refused, the first applies, and the step is not free.
- **`context_read`** pages the current view.

**Pressure and recovery across turns,** through `ArmSession` with a scripted model, a small budget (8,048) and one retry:
- **Turn 1:** over the limit, the arm rolls back to the 2,048-token margin, and the rollback note asks for room. The model's deletion of every earlier call is applied: the next request lacks those calls and still holds the pinned note. The turn completes.
- **Turn 2:** over the limit again, the model is told it has no retries left, and it answers.
- **Turn 3:** the over-limit request ends the turn (`context_limit`).
- **Every request sent** stayed within the limit.
- **With no retries,** the first over-limit request ends the turn. Continuation is refused.
- **The step limit** gives the finalize notice.

**The launcher, accounting and export:**
- eight-turn launches on docthread-dev-1 with the scripted investigator's `tools_keep` and `tools_tidy` policies (budget 12,000) both complete 10/10, with edits committed;
- every finished attempt is in the main category and counted;
- the launch export verifies with no problems;
- the exposure report counts the commits from the trace;
- a live plan must state the arm's version, budget, retries and readouts;
- `p015-turn-endings/2` is refused for the arm;
- the default arm set is unchanged;
- the proposed live spec (below) passes the live-plan checks, and a scripted copy of it plans, runs and completes.

**The other arms are unchanged:** the full p015 suite (284 tests) and the historical suite (349) pass, and ruff, format and mypy are clean in both environments.

## What is not established

- **How a real model uses the tools:** whether it edits at all, whether its edits are accepted, and whether it completes more turns than the shell arm did.
- **Whether the provider accepts every rebuilt request,** in particular replies with thinking blocks whose text was changed.
- **How the per-session retries and the margin rollback behave** on a real eight-turn thread, and what the persistent notices cost in context.
- **The cost:** an edit rewrites earlier messages, which can turn cache reads into cache writes.

## A proposed live validation (not authorised, not run)

**What it would be:** one session of `paper_clm_tools` on docthread-dev-1, eight turns. It would use dev-v3a's shared model, cache and retry settings (`claude-sonnet-5`, adaptive thinking, effort high, `max_tokens` 8,192, 5-minute cache), `docthread-task/2` and `p015-turn-endings/1`. The arm settings would be those in the table above. A development check of the interface, not a comparison.

**The draft spec:** clm-lib `configs/p015/proposed-tools-dev1.json`. It passes the launcher's live-plan and version checks; it has not been planned.

**Criteria to fix before running:**
- whether at least one `context_apply` set is accepted and committed;
- whether every request is accepted by the provider;
- the ending, the turns completed and the score;
- the edits' kinds and sizes, from the trace.

**The estimated cost:** about US$0.5–1.5. The basis is confirm1's complete eight-turn sessions (mean US$0.49 for the summary arm and US$1.07 for guarded-clm, whose rebuilt requests are mostly cache writes, as this arm's edited ones may be) and dev-v3a (US$0.25 for four turns). The proposal is a block of at most US$4, including retries and reservations. It fits under the current ledger ceiling without raising it, but it needs the maintainer's explicit authorisation.
