# 015 – `paper-clm-shell/3`: fidelity mapping and offline verification

_Written 2026-10-20. **Offline only: no model has run with version 3, and it has not been evaluated.** confirm1 remains a `paper-clm-shell/2` result. The sources are the same as for [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md): the paper (§4.1, Appendices D and E) and the harness README at `18dc111`. No reference source code was read. The implementation is clm-lib SPEC §38 (`src/clm_lib/p015/paper/parts.py`)._

## Why a version 3

**What happened in confirm1:** every paper-arm edit was rejected, and most were prose summaries replacing whole tool exchanges ([confirm1-findings.md](confirm1-findings.md), section 2).

**Why version 1's mirror refused them:**
- it encoded each whole message as one block, with tool calls and results inside as text sections;
- it rebuilt the native call and result pairing from those sections, so a summary that dropped them could not be turned back into a valid provider request.

**What version 3 changes:** the representation, so that legitimate reductions of that kind can be accepted. The model still decides what to keep, delete or summarise, and the runtime only checks structure and rebuilds.

## The mapping

| Element | What the sources say | `paper-clm-shell/3` | Classification |
| --- | --- | --- | --- |
| The file and its path | README: `/tmp/.live_ctx/LIVE_CTX_MAIN.txt`, written before each command; one `[[CTX_TURN i role=…]]` block per message after the pinned system prompt and task | The same path, written before each command. **One block per message part,** headed `[[CTX_BLOCK n kind=…]]`, after the pinned prefix and before the reply holding the running command | **Adaptation:** a finer block unit and a different header, so that a tool result's text can be edited while the runtime keeps its native pairing |
| Free editing | Paper §4.1: the model edits the context file with Bash, "freely" | Any block's text may be rewritten (a tool call's must stay JSON), any block deleted, notes added; kept blocks keep their order | **Source-supported in substance.** The order rule is ours |
| Summarising a tool result | Not addressed | A tool result's text may be replaced by any text and stays the native result of its call | **Our representation choice,** in line with free editing |
| Calls and results | README: the file is parsed back into a valid message list | Deleting either half of a pair deletes both; the runtime rebuilds valid messages (empty messages dropped, neighbours merged, results first) | **Adaptation:** the provider's pairing rule, enforced structurally rather than by the model's text |
| Notes | Not specified | `[[CTX_BLOCK note]]` (or leading text) becomes user text in the next user or tool message; a note before all kept blocks opens the context, sent within the request that holds the pinned question | **Ours** |
| The running reply | Not specified | Not in the file, and unchanged while its command runs | **Adaptation** (version 1 showed it and refused any change to it) |
| Reasoning parts | Not specified | Not shown. Kept with an unchanged reply; dropped from a reply that changed | **Adaptation** (a replayed signature must belong to the reply as written) |
| Validity and feedback | README: a rejected edit is not applied, and the model is told why | The same, with a reason for each refusal; kept through rollback as in version 2 | **Source-supported;** the carry through rollback is our adaptation |
| The edit gate | README: `fit` (accept if the result fits the limit) | `fit`, measured with the running reply included | **Source-supported** |

## Rollback: what the sources support, and what is ours

Unchanged from version 2.

| Rule | Status |
| --- | --- |
| Over the limit, roll back the last turn (one model step and its results) and retry, up to six times | **Source-supported:** the paper's BrowseComp-Plus setting. "Turn" is read as one model step, consistent with its free "editing turns" |
| The count of six is per user turn | **Ours:** the paper does not say what the six are counted over |
| Rollback stays within the current user turn | **Ours** |
| After the six, one final over-limit request; then the turn ends at its context limit | **The README's rule,** used where the paper is silent |
| A request over the 32,000 budget itself ends the turn at once | **Ours** |
| No headroom margin after a rollback (the request returns to its state before the last step) | **The paper's rule followed literally.** The README instead rolls back until 2,048 tokens are free; that is not used |
| A rejected edit's reason is repeated once beside the rollback notice when its step is rolled back | **Ours** (versions 2 and 3), for the README's "the model is told why" |

## Offline verification

**Where:** clm-lib `tests/p015/test_paper_parts.py`, with synthetic data and scripted responses. No network or model call, a placeholder key and temporary ledgers. **19 tests pass.**

**Through the real `ArmSession`, Docker sandbox and Anthropic adapter,** with request bodies captured by an in-memory transport:
- **A summary is accepted:** a command rewrites two journal results as one-line summaries. The edit is accepted, and every later request carries the summaries as the native `tool_result` of their calls; the page text is gone.
- **A second turn edits too:** it deletes a call and its result and adds a note, and the next request reflects both.
- **Every request is well formed:** each body sent alternates user and assistant roles, and pairs every `tool_use` with its `tool_result`.
- **A rejected edit changes nothing:** an edit naming a block that does not exist is rejected. The earlier context is sent unchanged, and the command's result says why.

**The parser's rules on synthetic messages:**
- an unchanged file keeps every message object;
- a tool result replaced by prose stays paired;
- deleting either half of a pair deletes both;
- notes and an opening note are placed as stated;
- a whole file rewritten as one note is accepted;
- reasoning is kept with an unchanged reply and dropped from a changed one;
- unknown, duplicate, reordered, non-JSON-call, emptied, half-pair-changed and reply-ending edits are refused with reasons;
- the instructions state the format with a generic example.

**Rollback and the launcher:**
- a rejected edit whose step is rolled back still reports its reason;
- messages rebuilt by an accepted edit stay rollable within the turn;
- an eight-turn launch with version 3 completes 10/10 with the scripted investigator.

**Versions 1 and 2 are unchanged:** their existing tests pass (clm-lib `test_paper_shell.py`, `test_paper_feedback.py`).

## What is not established

- **Whether a real model's edits are accepted,** or whether the arm then completes more turns.
- **What a live check would need** to answer that: a small development run with version 3, which is not authorised.
- **The headroom question is unchanged:** after a rollback the request is still close to the limit.
- **Exact fidelity is not claimed:** this is a paper-inspired shell-editing arm with our representation, and the sources do not specify the reference's message encoding.
