# 015 – The three core arms: settings, intentional differences and open live items

_Written 2026-10-16. **Nothing has run against a model.** The settings are the offline defaults in clm-lib. None
is frozen; the protocol freeze decides them._

The arms:
- **guarded-clm:** the `ClmContext` capability, built by `clm_context()` and hosted by `GuardedSession` (clm-lib SPEC §28);
- **`paper_clm_shell`:** `paper-clm-shell/1`, hosted by `ArmSession` ([fidelity](paper-clm-shell-fidelity.md));
- **the summary baseline:** `token-tail-p015/1` (clm-lib's `token-tail/1`, adapted below), hosted by `ArmSession`.

## Shared by all three (checked by `tests/p015/test_arm_fairness.py`)

| Setting | Value |
| --- | --- |
| model | one main model for every arm (offline: scripted models only) |
| system prompt | docthread's `SYSTEM_PROMPT`, identical |
| user turns | `user_message(q)` for questions 1 to 8, identical, one `agent.run` per question in one conversation |
| task tools | `read_journal`, `list_changes`, `queue_stats`, `read_playbook`: identical names, descriptions and argument schemas, through the same bridge |
| argument handling | the same validator; invalid arguments get the same retry text (`invalid arguments: …`) |
| tool results | the same text, capped by `tool-output-cap/1` at 8,000 code points |
| several calls per response | task-tool calls in one response all run, concurrently, in every arm (in `paper_clm_shell`, a `bash` call in the same response runs alone, between them) |
| output contract | plain text; a turn ends with a reply without tool calls; the answer is the fenced `json` block |
| task steps | 60 per user turn |
| model-call cap | 144 = 2 × 60 + 24 per user turn, counting every main-model response |
| budget | 32,000 tokens |
| accounting | the same wrapper, ledger rules, dated price and refusal rules; one attempt numbering per session |
| records and export | the same recorder files and `guarded-session-export/1` |
| endings | the same classification (`completed`, `spend_refused`, `context_limit`, `step_limit`, `call_cap`, `provider_failure`, …) |
| finalize notice | when at most 3 steps or calls are left in the turn (each arm's own wording) |

## Intentional differences (the arms' designs)

| | guarded-clm | `paper_clm_shell` | `token-tail-p015/1` |
| --- | --- | --- | --- |
| context tool | `edit_context` | `bash`, editing the mirror file | none |
| request layout | rebuilt as one user message: task, runtime status, working context | the pinned first request, then the editable conversation | the pinned first request (with the summary), then the kept tail |
| instructions | the library's | the arm's mirror instructions | the automatic-summary instructions |
| enforced limit | 29,952 (budget − 2,048) | 29,952 (budget − 2,048) | hard limit 31,000 (budget − 1,000), as in `token-tail/1` |
| pressure handling | PRESSURE notice from 70% of the budget; the output guard holds back outputs that would not fit | nudges at 25/50/75% of the limit, adaptive persistent nudge | a summary from 70% of the budget |
| over the limit | one over-limit request with a notice, then the turn ends | rollback of the turn's newest steps (up to 50), one final over-limit request, then the turn ends | a forced summary; if it does not fit, the turn ends |
| free task steps | a response whose first call is `edit_context` | a response whose only call is `bash`, which changed the mirror, exited 0 and printed nothing | none |
| size estimator | guarded-clm's own | `p015-ratio-estimate/1` | `p015-ratio-estimate/1` |
| extra model calls | none | none | summariser calls: category `summary`, a cap of 24 per turn (provisional), not task steps, not counted in the 144 |

## `token-tail/1` on the p015 path

| `token-tail/1` (clm-lib) | `token-tail-p015/1` |
| --- | --- |
| trigger: summarise when the estimate reaches 70% of the budget; force a summary over the hard limit (budget − 1,000) | kept |
| tail: `SummaryPolicy.split`, tail 15% and newest 25% of the budget | kept: the same code, over units (one reply and the request after it) instead of entries, so a call is never split from its result |
| summary length: `SummaryPolicy.char_limit` (600 to 3,000 characters, sized to a 50% target); one retry at half the length | kept |
| acceptance: the first attempt must relieve pressure; the retry need only fit the hard limit | kept. A summary longer than requested is accepted if the request fits, as in `token-tail/1` |
| summariser user message: `<task>`, `<transcript_to_summarise>` (one escaped JSON line per entry), the length instruction | kept, unchanged; the task is the first question, and an earlier summary is the first entry |
| summariser system text: `SUMMARY_SYSTEM_TOKEN_TAIL` | a docthread-neutral version: no local files, `file:line` references or stages; it also asks for the questions and answers so far |
| replacement: the summary replaces the older entries | kept: the summary goes into the pinned first request; the current turn's question is restated if it was summarised |
| agent instructions | the automatic-summary paragraph, without the workspace sentence |
| spill of an oversized latest output to a file (runner feature) | not adapted: shared outputs are already capped at 8,000 code points |
| summary calls in the historical call budget (`summary_calls_in_max_calls`) | a separate per-turn summariser cap; see the open items |

Summariser calls go through their own accounting wrapper, so their tokens, cache figures, latency and cost are recorded apart (`category: summary`, ledger kind `p015:summary`). They obey the same authorisation and spending rules, and they receive only what the agent could see.

## Open live items (not resolved here)

1. **The scope of the 144-call cap** (per session or per user turn), and **whether summariser calls count** towards it, are open in [decisions.md](decisions.md). All arms use per user turn offline, and summariser calls do not count.
2. **The summariser cap** (24 per turn) is provisional.
3. **Sampling:** the paper's README uses temperature 0.7 and top_p 0.95. The intended model rejects non-default sampling, so either the arms use the model's defaults, which is a recorded departure from the paper's settings, or another model is chosen.
4. **Model settings:** `max_tokens`, effort and thinking; how reasoning parts are mirrored (`paper_clm_shell`) or summarised; whether they are replayed.
5. **Caching:** breakpoint placement and TTL per arm. Nothing is cached offline.
6. **Estimators against the real tokenizer:** each arm's estimate is calibrated only on provider-reported usage, which offline sessions do not have.
7. **Provider compatibility:** the p015 environment's Anthropic SDK pin (0.125.0) and Pydantic AI 2.27.1 need confirming in an authorised smoke. The intended model's price, and the reservation bound's one-token-per-byte assumption, need checking.
8. **A public pin of guarded-clm** for recorded runs.
