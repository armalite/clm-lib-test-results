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
| **Size reporting and reminders** | README: nudges at 25, 50 and 75% of the budget. An adaptive persistent nudge fires when the room left is below max(10% of the limit, 2 × the largest of the last 3 tool outputs), never below 50% of the limit (`persistent_nudge_obs_mult` 2). Paper App. E: "every tool result reports your current size" is steering-experiment text only. | The same thresholds and rule. Each threshold fires once when crossed and is re-armed when the size falls below it; several thresholds crossed at once give one notice. No per-result size report. | **Mapping:** the percentages are taken of the limit (budget minus reserve), because the README's use of "budget" there is ambiguous. Notices are transient: appended to the request, not mirrored, not kept. Their wording is ours. |
| **Free editing steps and task steps** | README: `max_steps` 64; an edit-only turn (mirror changed, no output, exit 0) is free. Paper App. E (BrowseComp): editing turns don't count toward the turn limit. | 60 task steps per user turn (the 015 standard). A response whose only call is `bash`, and whose command changed the mirror, exited 0 and printed nothing, is free. | The README's rule is applied literally, so an edit that changed the file but was rejected is also free. The model is not told about free steps. |
| **Call limits and their scope** | README: `lm_call_cap` = 2 × `max_steps` + 24, per task, counting free turns. | 144 = 2 × 60 + 24, per user turn, counting every main-model response, free ones included. | **Unresolved:** whether the cap is per session or per user turn is open in decisions.md. All three arms use per user turn offline. |
| **Over-limit handling** | README: the newest turns are rolled back until `retry_edit_margin_tokens` (2,048) are free; `max_num_retry_on_limit` 50; after the retries, one final turn, then the run stops if still over. Paper App. E: up to 6 rollbacks (BrowseComp) or 50 (EdgeBench). | Before a request over the limit, the newest complete steps of the current user turn are removed until 2,048 tokens are free under the limit. A notice says so. Up to 50 rollback events per turn. Then one final request over the limit is allowed, with a notice; if the next is still over, the turn ends (`context_limit`). A request over the budget itself ends the turn at once. | **Adaptations:** rollback never removes earlier turns or the turn's question; it counts a rollback event, not each removed step, as one retry; and when nothing more can be rolled back, the final request comes early. |
| **Context limit** | README: `context_budget_tokens` required (CLI default 32,000); `context_budget_reserve_tokens` 2,048. Paper App. D (ContextBench): 32,768 with 2,048 reserved. App. E (TerminalBench): 32,000. | Budget 32,000, reserve 2,048, limit 29,952 (the same budget as guarded-clm's). | None. |
| **Size estimation** | Not described in the sources used. | Characters over a ratio (`p015-ratio-estimate/1`): fixed 4 for scripted models; otherwise starting at 3 and moving halfway towards each call's observed ratio. No token-counting call. | Ours, and different from guarded-clm's estimator. |
| **Several tool calls in one response** | README: one command per turn. | Only the first `bash` call of a response runs. Any other `bash` call gets an explicit result saying it was not run, so nothing is skipped silently. Task-tool calls in the same response run, as in every arm; a `bash` call runs alone (Pydantic AI's `sequential` barrier): calls listed before it finish first, and calls after it start once it ends. | Ours. |
| **Multi-turn handling** | Paper App. D: each operation arrives as a new user message in one continuous conversation. | Each docthread question is a new user turn in one conversation. The editable conversation, the estimator and the nudge state persist. Step, call and rollback counts are per turn. | None beyond the per-turn scope above. |
| **Finishing** | README: `finish_policy` `submit` (an echo of `COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT`) or `open_ended`; `finalize_nudge_turns` 3. | A reply without tool calls ends the turn: the shared fenced-`json` answer contract. A notice when at most 3 steps or calls are left. | **Mapping:** the shared answer contract replaces `submit`, so that every arm ends a turn the same way. |
| **Command output** | Not stated in the README (truncation, stderr). | The shared `tool-output-cap/1` (8,000 code points, with a stderr reserve), and an exit-code and duration header. | Ours: the same cap as the task tools. |
| **Sampling** | README: temperature 0.7, top_p 0.95, `max_tokens` 16,384. | Not set offline. | **Unresolved (live):** the intended model rejects non-default sampling, so the README's sampling cannot be applied as given. See the settings note. |

## What is deliberately not added

None of guarded-clm's features is added to this arm: there is no structured working context, edit tool, output guard, runtime status block or protected entries. The two arms share only what every arm shares (see [arm-settings.md](arm-settings.md)).

## Verification

See [arms-offline.md](arms-offline.md). The scripted sessions use the real Docker sandbox.
