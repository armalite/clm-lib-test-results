# 015 – `paper-clm-tools/2`: the dev-tools1 provider failure and its correction

_Written 2026-10-21; the current-turn restriction added 2026-10-22. **Offline only.** No provider or token-counting call was made, and nothing was spent. `paper-clm-tools/1` and the dev-tools1 evidence ([dev-tools1-record.md](dev-tools1-record.md), [dev-tools1-export/](dev-tools1-export/)) are unchanged, and dev-tools1 remains a version 1 result (4/10, `provider_failure`). The implementation is clm-lib SPEC §40._

## The failure, established from the evidence

**The error** (attempt 19 of dev-tools1, HTTP 400, `invalid_request_error`):

> `messages.1.content.3`: `thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.

**The edit before it:** the second accepted edit, staged after attempt 18 and committed into attempt 19. It was a `delete` of blocks 4–8: `read_journal` pages 6 and 8 with their results, and the empty thinking block of page 8's reply.

**What changed in assistant message 1:** the attempt 18 and 19 requests were compared with the provider responses that produced each thinking block.

| Property | Changed? | Evidence |
| --- | --- | --- |
| thinking text | **no** | every block's text is empty both before and after (display `omitted`, the model's default) |
| signatures | **no** | every remaining signature is byte-identical to the one returned |
| which blocks share a message, and their order | **yes** | message 1 held thinking from three provider responses (`…WTwC`, `…1BXw`, `…nLwm`), the last two consecutive at `content.2` and `content.3` |
| surrounding structure | **yes** | the deletion emptied the messages between the replies, and the rebuild merged them into one assistant message: thinking, text, thinking, thinking, tool call |

**The model did not edit thinking.** The rebuild changed how the provider's thinking blocks were grouped.
- **The first edit:** its rebuild also put two responses' thinking into message 1, separated by text, and that request (attempt 17) was accepted.
- **The second edit:** it made two foreign blocks consecutive, a sequence the model never generated, and that request was refused.

**The session's charges:** US$0.270354, all confirmed. Nothing was assumed at the reservation, nothing is pending, and the refused attempt was not billed.

## The documented rules

From the provider's public documentation, read 2026-10-21:

- **Thinking, "Preserving thinking blocks":**
  - "Pass every `thinking` block back to the API complete and unmodified"
  - "**Required:** within a tool-use turn, pass thinking blocks back. **Recommended:** across turns, pass everything back. **Allowed:** outside tool use, omit prior turns' thinking."
  - "Within the latest assistant message, the sequence of consecutive `thinking` blocks must match what the model generated in the original request: you can't rearrange, edit, or partially drop them."
- **Thinking troubleshooting, the "cannot be modified" error:** it "happens when the assistant message you send back differs from the one the API returned, most often because your code … rebuilds the assistant message instead of echoing it". The fix: "Echo the assistant turn back verbatim, thinking blocks included."
- **The Messages API:** "Consecutive `user` or `assistant` turns in your request will be combined into a single turn." Keeping the replies as separate messages would therefore not help.
- **Preserved thinking** (the conversation-bound signature check) applies to Claude Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5. Its 400 reads "bound to a different conversation". dev-tools1 ran `claude-sonnet-5`, and its error is the other one. That check is not the cause here.

**What the installed adapter does** (Pydantic AI 2.27.1): each Anthropic `ThinkingPart` becomes a `thinking` block with its text and signature (or a `redacted_thinking` block), and each response becomes one assistant message. The adapter does not merge messages itself.

## The correction (`paper-clm-tools/2`)

**One reconstruction rule, `ThinkingRule`, applied wherever the arm rebuilds the conversation:** staging, the commit and rollback.
- **The rule:** a reply the rebuild has merged with another or altered (a part removed or edited) is sent without its thinking blocks, provided every one of them came from an earlier user turn.
- **What keeps its thinking as returned:**
  - replies echoed verbatim, the same object;
  - any reply that holds thinking returned in the turn in progress, since thinking must be passed back within a tool-use turn.
- **The scope:** the documented permission, prior turns' thinking outside tool use. The current turn is identified by the signatures of thinking returned in this user turn.
- **A reply left with nothing but thinking** is dropped, and the requests around it merge.
- **Recorded:** the commit and rollback records give `thinking_omitted`.

**Unchanged:**
- the operations, rollback, notices, steps, prompts and instructions;
- budgets, settings and scoring;
- the estimator;
- deleted content stays deleted;
- thinking is still on, and the effort and model are unchanged.

`paper-clm-tools/1` is kept as it was and remains the default. Version 2 must be selected explicitly (`ToolsSettings.version`), and live plans must state the version. No other arm is affected.

## Offline verification

**Where:** clm-lib `tests/p015/test_paper_tools_v2.py`, with synthetic signed thinking: 10 tests for the earlier-turn rule (15 in all; see the next section for the other five).

**On synthetic messages built in the observed shape:**
- version 1 reproduces the refused message (thinking, text, thinking, thinking, tool call, with a foreign block at `content.3`);
- version 2 sends the merged earlier reply as text and tool call only (three blocks omitted). The deletion still takes effect, and the replies echoed verbatim keep their objects and thinking;
- a verbatim earlier reply keeps its thinking;
- an altered earlier reply loses its thinking without a merge;
- a reply holding the current turn's thinking keeps it;
- a deletion between replies merges them and omits both blocks;
- a reply left with only thinking is dropped and its requests merge;
- the version is explicit, and version 1 is the default.

**Through the real `ArmSession` and the installed Anthropic adapter** over an in-memory transport, three turns with signed thinking in the scripted responses, replaying dev-tools1's second edit in turn 2:

| | the request carrying the edit | the next turn's first request |
| --- | --- | --- |
| **version 1** | `[thinking A, text, thinking B, thinking D, tool_use r9]`, `[text]`, `[thinking E, tool_use e1]` (the refused shape) | the same, plus `[thinking F, text]` |
| **version 2** | `[text, tool_use r9]`, `[text]`, `[thinking E, tool_use e1]` | the same, plus `[thinking F, text]` |

**Under version 2:**
- pages 6 and 8 (calls, results and text) are gone from the request;
- every assistant message that carries thinking is exactly one response as returned;
- every `tool_use` is answered by its `tool_result`;
- the next turn rebuilds the same history;
- the commit records `thinking_omitted: 3`.

**The affected checks:** the version 1 tests (`test_paper_tools.py`, 33) and the launcher, live-plan, exposure and turn-ending tests pass; 99 in all. ruff, format and mypy are clean in both environments.

## The turn in progress (added 2026-10-22, the same version)

**The gap the first correction left:** a deletion inside the turn in progress could still merge or alter a reply carrying that turn's signed thinking. An example is deleting one of this turn's earlier reads. Within a tool-use turn, thinking must be passed back complete and unmodified, and no strip is documented there.

**The decision (maintainer, 2026-10-22):** reject such edits; do not defer them.

**The restriction, as implemented:**
- **Provenance:** each reply returned in the current user turn that carries thinking is recorded as its original part objects, in order (`TurnReply`). Grouping is taken from this record, never inferred from thinking text or signatures.
- **The check:** a candidate request is compatible when every recorded reply is one assistant message holding exactly those parts, in that order. Rollback may remove only a trailing run (the newest steps).
- **At staging:** an incompatible operation set is refused as a whole, and the context is unchanged. The reason names the affected blocks and the alternatives: rewrite this turn's tool results, for example with `replace_block`, or make the change in a later turn.
- **At the commit:** the set is rechecked; if incompatible it does not take effect, and a note says why.
- **In rollback:** checked after the undo, before a retry is counted; the undone replies leave the record. A rollback that could not keep the remaining replies intact would end the turn as `request_incompatible`, a harness outcome reported as `harness_defect`. It is not a context limit, and nothing is dispatched.
- **Before every dispatch:** the same check runs as a final guard.
- **Not changed:** current-turn thinking is never stripped, and the rollback rules and allowances are as they were.

**What it prevents in the turn in progress,** for replies of that turn that carry thinking:
- deleting their tool calls, and therefore deleting their tool results, which take the call with them: an earlier read of this turn cannot be deleted while the turn lasts;
- deleting or editing their thinking, text or call arguments; a `substitute` without a block list that would match such text is refused as a whole;
- deletions that empty the messages between two replies, merging a thinking reply, for example deleting the turn's question when the previous turn's last reply would join this turn's first reply.

**What remains possible:**
- every earlier-turn edit (with thinking omitted from merged or altered replies);
- rewriting this turn's tool results, for example as summaries, which is the main in-turn reduction;
- inserting notes;
- editing this turn's user text and notes, or replies without thinking, while every thinking reply stays intact.

Once the turn ends, its exchanges can be deleted like any earlier-turn material.

**How refusals count:** under the existing step rules.
- **A refusal at staging** (`REJECTED:`) makes its step a task step, not a free one.
- **A refusal at the commit** follows an accepted receipt, so its step stayed free, and the note goes into the next request.

**The effect on fidelity and interpretation:** this is a compatibility restriction of the structured-tools adaptation under adaptive thinking, not a claim about the paper's method. The paper's model edits its context freely. Here, within a turn, the model can shrink this turn's tool output only by rewriting it, not by deleting the exchange. A comparison must state this, and must not read the tools arm's in-turn behaviour as the paper's.

**Offline evidence:** clm-lib `tests/p015/test_paper_tools_v2.py`, now 15 tests.
- **The check itself (`turn_problem`):** intact, altered, merged, trailing-removed and gap-removed replies.
- **The commit and rollback:** a staged set is refused again at the commit, with the context unchanged and a note added. A rollback that cannot keep a reply intact stops with `request_incompatible`, classified as `harness_defect` by the launcher.
- **Three turns through the real `ArmSession` and the installed Anthropic adapter,** with synthetic signed thinking:
  - **turn 2's deletion of its own earlier read is refused before dispatch:** the reason names blocks 7, 8, 10 and 11, the next request's earlier messages are identical, and the refusal is a task step (4 task steps, 1 free);
  - **a summary of a turn-2 tool result is accepted** and replaces the page in the next request;
  - **in turn 3 the same deletion is an earlier-turn edit and is applied,** with the two merged replies' thinking omitted;
  - **every request** keeps each thinking reply as returned and pairs every call;
  - no `request_incompatible` record occurs.
- **A rollback inside a turn whose replies carry thinking** removes only the newest steps; the later requests, and the next turn's, stay valid.

**The affected checks:** 107 passed (the arm's two files, and the launcher, live-plan, exposure, turn-ending and arm-fairness tests). Lint, format and types are clean in both environments.

## What is not established

- **Acceptance by the real provider.** Local transports cannot show it.
- **The exact provider check is inferred, not observed.** The error names the "latest assistant message", but it pointed at `messages.1`, which is not the last one. Version 2 follows the documented general rule (thinking in a non-verbatim reply is omitted, outside the current turn) rather than the inferred one about consecutive runs.
- **Rewritten current-turn tool results:** whether the provider accepts them alongside intact thinking replies is not shown. The documented rules concern assistant messages only.
- **The restriction is learned only from refusals:** the instructions do not mention it, so how often the model hits it, and what the refused steps cost, is unmeasured.
- **Models with preserved thinking** (Sonnet 5.5, Opus 5.5 and others) bind thinking to everything before it. Any edit of earlier history invalidates later thinking there, which needs `drop_block` or stripping from the edit point. Version 2 addresses `claude-sonnet-5` as run in 015, not those models.
- **Cost:** the omitted thinking is no longer sent. The effect on the model's reasoning, and the cache writes after an edit, are unmeasured.
