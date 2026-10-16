# 015 – `paper_clm_shell`: fidelity to the public sources

_Written 2026-10-16. **Nothing has run against a model.** This maps each element of the paper's shell-based context
editing onto clm-lib's implementation, `paper-clm-shell/1` (clm-lib SPEC §30)._

## Sources

Only these public sources were used. No reference source code was read.

- **The harness README**, at a fixed revision:
  https://github.com/facebookresearch/context-language-models/blob/18dc11115f50f261233c5bba7937834491e307e8/clm/clm_harness/README.md
- **The paper**, version 1, HTML: https://arxiv.org/html/2609.37725v1. Section 4.1 and Appendices D and E are used.

The implementation was written independently from these descriptions. It is **not byte-identical** to the
reference harness, and is not claimed to be: its prompts, notices, file encoding inside a block, estimator and
sandbox are clm-lib's own. Where a source is silent, the choice made is listed as an adaptation.

## Element by element

| Element | What the sources say | `paper-clm-shell/1` | Difference or adaptation |
| --- | --- | --- | --- |
| **Context access** | README: one `bash` tool. Paper §4.1: the mirror's path is given in the system prompt, and edits sync automatically. | One `bash` tool, one command per call. The mirror path and format are stated in the arm's instructions, which Pydantic AI sends as system text. | The docthread evidence is reached only through the four shared task tools, which are native tools in every arm. The shell holds no evidence. |
| **The sandbox** | Not specified in the sources used. | A fresh Docker container per command (`python:3.12-slim`). No network, non-root, all capabilities dropped, `no-new-privileges`, 512 MB, 1 CPU, 128 processes, read-only root, private `/tmp`, `HOME=/tmp`, 30 s timeout. Mounted: only the mirror directory (`/tmp/.live_ctx`) and a per-session scratch `/work`, which persists between commands. | Ours. No fixture, scorer data, host path, credential or Docker socket is mounted, and there is no host fallback. |
| **The mirrored context** | README: `/tmp/.live_ctx/LIVE_CTX_MAIN.txt`, written before each command. It holds every turn after the system prompt and the task, one `[[CTX_TURN i role=…]]` block per message. | The same path and header (`ctx-turn-mirror/1`), written before each command. Roles are `user`, `assistant` and `tool`. | The encoding inside a block is ours: reply text, then `<<call id=… tool=…>>` sections with JSON arguments; results in `<<result …>>` (or `<<retry …>>`) sections. Reasoning parts are not mirrored (a live item). |
| **The pinned prefix** | README: the system prompt and the task are pinned. | The first request is pinned: the system prompt and question 1, with its reply format. | **Mapping:** the docthread "task" is the first question. Questions 2 to 8 arrive as later user turns, so they are editable blocks, as "every turn after" implies. |
| **When edits take effect** | README: if the file changed, it is parsed back into a valid message list. | After the command ends, a changed file is parsed. If accepted, it becomes the conversation from the next request on. | **Adaptation:** the last block (the reply holding the running command) must stay unchanged, so that its call is still answered. The README does not say how that block is treated. |
| **The edit gate** | README: `fit` by default (accepts if the result fits the limit), or `shrink`. | `fit` only. The result must parse, be a valid conversation and fit the limit. | `shrink` is not implemented; asking for it is an error. |
| **Invalid edits** | README: a rejected edit is not applied, and the model is told why; there is a one-line receipt. | A rejected edit changes nothing, and a one-line receipt with the reason is appended to the command's result. An accepted edit's receipt gives the block counts and the new size. | The receipt wording is ours. |
| **Size reporting and reminders** (revised 2026-10-16) | Paper App. E: "CLM receives its editing reminder 2,048 tokens before the budget"; repetition and wording not stated; "every tool result reports your current size" is steering-experiment text only. README: nudges at 25, 50 and 75% **of the budget**, each once and re-armed after the context shrinks, plus an adaptive persistent nudge relative to the limit, repeated every turn near it. | **`paper` profile (default):** one reminder when the request is within 2,048 tokens of the limit; once per crossing, re-armed below. **`readme` profile:** the README's nudges, now with the budget as the denominator. No per-result size report in either. | The paper's "budget" is read as the usable limit (budget minus reserve), so the reminder fires at 27,904 tokens: an ambiguity, see the review below. Repetition and wording are ours. The first implementation used the README nudges, with the limit as the denominator. Both were corrected. |
| **Free editing steps and task steps** | README: `max_steps` 64; an edit-only turn (mirror changed, no output, exit 0) is free. Paper App. E (BrowseComp): editing turns don't count toward the turn limit. | 60 task steps per user turn (the 015 standard). A response whose only call is `bash`, and whose command changed the mirror, exited 0 and printed nothing, is free. | The README's rule is applied literally, so an edit that changed the file but was rejected is also free. The model is not told about free steps. |
| **Call limits and their scope** | README: `lm_call_cap` = 2 × `max_steps` + 24, per task, counting free turns. | 144 = 2 × 60 + 24, per user turn, counting every main-model response, free ones included. | **Unresolved:** whether the cap is per session or per user turn is open in decisions.md. All three arms use per user turn offline. |
| **Over-limit handling** (revised 2026-10-16) | Paper App. E (BrowseComp-Plus): when a request would exceed the budget, "CLM rolls back the last turn and retries, up to six times"; what follows is not stated. EdgeBench-10: up to 50. README: the newest turns are rolled back until 2,048 tokens are free; 50 retries; then one final turn, and the run stops if still over. | **`paper` profile:** the last step is rolled back, and the request is retried while still over the limit, up to 6 per turn; then the README's one final over-limit request; then the turn ends (`context_limit`). **`readme` profile:** the README's rule, up to 50. A notice tells the model what was rolled back. | **Adaptations:** rollback is limited to the current user turn (never earlier turns or the turn's question); after the six retries, the README's final request is used, since the paper is silent there. The notice is ours. A request over the budget itself ends the turn at once. |
| **Context limit** | README: `context_budget_tokens` required (CLI default 32,000); `context_budget_reserve_tokens` 2,048. Paper App. D (ContextBench): 32,768 with 2,048 reserved. App. E (TerminalBench): 32,000. | Budget 32,000, reserve 2,048, limit 29,952 (the same budget as guarded-clm's). | None. |
| **Size estimation** | Not described in the sources used. | Characters over a ratio (`p015-ratio-estimate/1`): fixed 4 for scripted models; otherwise starting at 3 and moving halfway towards each call's observed ratio. No token-counting call. | Ours, and different from guarded-clm's estimator. |
| **Several tool calls in one response** | README: one command per turn. | Only the first `bash` call of a response runs. Any other `bash` call gets an explicit result saying it was not run, so nothing is skipped silently. Task-tool calls in the same response run, as in every arm; a `bash` call runs alone (Pydantic AI's `sequential` barrier): calls listed before it finish first, and calls after it start once it ends. | Ours. |
| **Multi-turn handling** | Paper App. D: each operation arrives as a new user message in one continuous conversation. | Each docthread question is a new user turn in one conversation. The editable conversation, the estimator and the nudge state persist. Step, call and rollback counts are per turn. | None beyond the per-turn scope above. |
| **Finishing** | README: `finish_policy` `submit` (an echo of `COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT`) or `open_ended`; `finalize_nudge_turns` 3. | A reply without tool calls ends the turn: the shared fenced-`json` answer contract. A notice when at most 3 steps or calls are left. | **Mapping:** the shared answer contract replaces `submit`, so that every arm ends a turn the same way. |
| **Command output** | Not stated in the README (truncation, stderr). | The shared `tool-output-cap/1` (8,000 code points, with a stderr reserve), and an exit-code and duration header. | Ours: the same cap as the task tools. |
| **Sampling** (revised 2026-10-16) | Paper App. E (BrowseComp-Plus): temperature 0.7, top-p 0.95, up to 4,096 generated tokens per call. README: 0.7, 0.95, `max_tokens` 16,384. | Not sent. `max_tokens` 8,192 (shared by all arms). | **Necessary adaptation:** Claude Sonnet 5 rejects non-default sampling (provider docs, retrieved 2026-10-16), so the paper's sampling cannot be reproduced. The output limit is a shared setting; see arm-settings.md. |

## Source-priority review (2026-10-16)

**The agreed rule:** the paper's experimental settings for the relevant task type come first. The README's defaults are recorded as the alternative.

**The relevant task type:** docthread is closest to **BrowseComp-Plus** in Appendix E. It is question answering by tool-driven retrieval over a fixed corpus, with large documents read through a reader tool. Its arrival of operations as new user messages in one conversation follows **ContextBench** (Appendix D). The 015 standards (a 32,000 budget, 60 steps and 144 calls) take precedence where they were fixed.

**Sources:**
- the paper, https://arxiv.org/html/2609.37725v1 (Section 4.1 and Appendices D and E), read 2026-10-16;
- the README at revision `18dc11115f50f261233c5bba7937834491e307e8`, read 2026-10-16.

No reference source code was read.

| Rule | Supported by the paper | README alternative | Necessary adaptation | Implementation choice (not established by a source) |
| --- | --- | --- | --- | --- |
| **Reminder timing** | One editing reminder, 2,048 tokens before the budget | 25/50/75% nudges and the adaptive persistent nudge | none | Whether it repeats: here once per crossing, re-armed. Its wording |
| **Reminder denominator** | "the budget" | the budget (escalating nudges); the limit (persistent nudge) | none | Reading the paper's budget as the usable limit (27,904 tokens), see the open question |
| **Fit versus shrink** | not stated | `fit` by default; `shrink` optional | none | Only `fit` is implemented |
| **Free editing steps** | "editing turns do not count toward the turn limit" | an edit-only turn: mirror changed, no output, exit 0 | none | A rejected edit that changed the file and printed nothing is also free (README read literally; neither source addresses it) |
| **Several calls in one response** | not stated | one command per turn | Task tools are native calls shared by every arm, so they run alongside | Only the first `bash` call runs; others get an explicit not-run result |
| **Rollback scope and exhaustion** | the last turn, up to 6 (BrowseComp-Plus); 50 (EdgeBench-10); exhaustion not stated | newest turns to a 2,048 margin, 50, then one final turn | Rollback stays within the current user turn | After 6, the README's one final over-limit request |
| **The running-command block** | not stated | not stated | The model's call must remain answered in the next request, and its reasoning signature must survive (provider rule) | The block must stay unchanged, or the edit is rejected |
| **Multi-turn task** | operations arrive as new user messages in one conversation (Appendix D) | not stated | Questions 2 to 8 are editable user blocks; step, call and rollback counts are per turn | The first question is the pinned task |

**Corrected (2026-10-16):**
- **The default profile** is now the paper's (`profile="paper"`): the single reminder and the last-step rollback up to six.
- **The README rules remain** as `profile="readme"`.
- **The README nudge denominator** is now the budget, as the README states. The first implementation used the limit, and the earlier version of this file wrongly called the README ambiguous there.

Both corrections are covered by tests in clm-lib (`tests/p015/test_paper_shell.py`).

**Open questions for the maintainer.** The arm is not approved or frozen until these are decided.
1. **Where the reminder fires.** The options:
   - **(a) 2,048 tokens before the usable limit:** 27,904 tokens. This is implemented and recommended, because the paper's "budget" is the request limit in its TerminalBench and ContextBench descriptions.
   - **(b) 2,048 tokens before 32,000:** 29,952 tokens. This equals the limit, so the reminder would coincide with rollback and could never be acted on first.
2. **Whether the reminder repeats.** The options:
   - **(a) once per crossing, re-armed below:** implemented;
   - **(b) on every request above the point.**

   The paper is silent. I recommend (a), as the closest reading of "its editing reminder".
3. **Rejected edits and the free-step rule.** The options:
   - **(a) free, by the README's literal rule:** implemented;
   - **(b) a rejected edit counts as a task step.**

   I recommend (b) only if you read "editing turn" as a turn that edited the context. Neither source decides.
4. **Profile:** confirm `paper` as the comparison default, with `readme` recorded as the alternative and not run.

## What is deliberately not added

None of guarded-clm's features is added to this arm: there is no structured working context, edit tool, output guard, runtime status block or protected entries. The two arms share only what every arm shares (see [arm-settings.md](arm-settings.md)).

## Verification

See [arms-offline.md](arms-offline.md). The scripted sessions use the real Docker sandbox.
