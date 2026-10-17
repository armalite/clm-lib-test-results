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

## Open live items as first written (kept as written; resolved or restated below, 2026-10-16)

1. **The scope of the 144-call cap** (per session or per user turn), and **whether summariser calls count** towards it, are open in [decisions.md](decisions.md). All arms use per user turn offline, and summariser calls do not count.
2. **The summariser cap** (24 per turn) is provisional.
3. **Sampling:** the paper's README uses temperature 0.7 and top_p 0.95. The intended model rejects non-default sampling, so either the arms use the model's defaults, which is a recorded departure from the paper's settings, or another model is chosen.
4. **Model settings:** `max_tokens`, effort and thinking; how reasoning parts are mirrored (`paper_clm_shell`) or summarised; whether they are replayed.
5. **Caching:** breakpoint placement and TTL per arm. Nothing is cached offline.
6. **Estimators against the real tokenizer:** each arm's estimate is calibrated only on provider-reported usage, which offline sessions do not have.
7. **Provider compatibility:** the p015 environment's Anthropic SDK pin (0.125.0) and Pydantic AI 2.27.1 need confirming in an authorised smoke. The intended model's price, and the reservation bound's one-token-per-byte assumption, need checking.
8. **A public pin of guarded-clm** for recorded runs.

## The comparison contract (settled offline, 2026-10-16; not frozen)

### Counting

| Quantity | What it counts | Limit | Where it is recorded |
| --- | --- | --- | --- |
| user turns | the eight questions; one `agent.run` each | 8 per session | `turns.jsonl` |
| logical main-model calls | each model request Pydantic AI makes for the agent | **144 per user turn**, every arm (`UsageLimits(request_limit=144)`; guarded-clm's `ClmStepLimit` enforces the same cap) | `attempts.jsonl` `logical_call`; per-turn counters |
| provider attempts | each dispatched request, including retries of one logical call | at most 1 + 2 retries per logical call (`p015-retry/1`) | `attempts.jsonl` (`attempt`, `retry`), ledger entries |
| task steps | each arm's own rule (below) | 60 per user turn | per-turn counters, trace |
| free editing steps | guarded-clm: a response whose first call is `edit_context`. `paper_clm_shell`: a response whose only call is `bash`, which changed the mirror, exited 0 and printed nothing. Summary arm: none | not counted as task steps; counted as logical calls | trace, per-turn counters |
| summariser calls | each summary request, and its attempts | **24 per user turn (provisional)**; not task steps; not in the 144 | `attempts.jsonl` `category: summary`, ledger kind `p015:summary` |

**guarded-clm's own counters are unchanged:** `ClmStepLimit.steps` and `ClmStepLimit.calls` count per run (one user turn). They map onto the comparison's reporting as follows:
- the library's `calls` is the number of logical main-model calls in the turn;
- the library's `steps` is its task steps;
- provider attempts and retries come from the accounting wrapper, below the library, so the library never sees a retry.

**The model-visible status** may differ from the enforced count (library SPEC 13.9). Both are recorded. No behaviour was changed to make the arms look equivalent: the free-step rules are the arms' own designs.

**Summariser usage counts in every total.** Its calls, attempts, retries, tokens, cache figures, latency and cost are reported in the totals and by category. Its separate allowance only keeps it from consuming the agent's 144 calls. It is not free.

### Retries

**`p015-retry/1`,** the same in every arm and for the summariser:
- **What is retried:** a logical call, up to 2 times, after HTTP 429, 500, 502, 503, 504 or 529, or after a connection failure or timeout. Anything else is not retried.
- **Delays:** 2 s, then 8 s, or the server's `retry-after` if longer, up to 60 s.
- **Accounting:** every retry is a separately reserved, gate-checked and recorded attempt.
- **The SDK's own retries are off** (`max_retries=0`; verified over an in-memory transport). The Anthropic SDK otherwise retries twice by default, unseen.
- **Never retried:** a failed session. After the bounded retries, the session ends as `provider_failure`.

### The model configuration (`p015-model/1`, recommended for all three arms)

**Sources,** retrieved 2026-10-16:
- the pricing page, https://platform.claude.com/docs/en/about-claude/pricing;
- the thinking page, https://platform.claude.com/docs/en/build-with-claude/thinking;
- the extended-thinking page, https://platform.claude.com/docs/en/build-with-claude/extended-thinking;
- Anthropic's model reference, cached 2026-10-06.

| Setting | Value | Basis |
| --- | --- | --- |
| model | `claude-sonnet-5` | the requested model; its exact ID in the provider's model list. Not substituted |
| sampling | not sent | Claude Sonnet 5 rejects non-default `temperature`, `top_p` and `top_k`. **A recorded adaptation:** the paper's 0.7 / 0.95 cannot be reproduced |
| thinking | adaptive (the model's default; `thinking` not sent) | thinking is on by default on Sonnet 5; `disabled` is the alternative (below) |
| effort | `high` (explicit; the model's default) | |
| `max_tokens` | 8,192, shared (thinking and response together) | the paper uses 4,096 per call for BrowseComp-Plus and 8,192 for EdgeBench-10; the README 16,384. 8,192 leaves room for adaptive thinking at `high`; the truncation rate is a smoke item |
| output limit of the model | 128K; context window 1M | the comparison's 32,000 budget is the arms' own limit, not the model's |
| prices (per million tokens) | input $2.00; 5-minute cache write $2.50; 1-hour write $4.00; cache read $0.20; output $10.00 | the pricing page: the $2/$10 price, announced as introductory, "is now the standard price". In `configs/prices.toml` with source and date |
| caching | ordinary automatic prompt caching, 5-minute TTL, plus explicit breakpoints after the tool definitions and after the instructions | the same in every arm (Pydantic AI `anthropic_cache`, `anthropic_cache_tool_definitions`, `anthropic_cache_instructions`) |
| session isolation (corrected 2026-10-16) | each session's system prompt starts with `run-ref: <32 hexadecimal characters>`, fixed in the launch contract | the instruction and automatic breakpoints follow it, so those prefixes are session-specific, and a session reuses its own. **Not complete:** the tool definitions precede the system prompt, so the tool-definition breakpoint's prefix is not session-specific; summariser requests carry no `run-ref` line. The practical effect is not known without live evidence. Not Suffix Cache Reuse |
| retries | SDK off; `p015-retry/1` | above |

**Framework and model compatibility, kept apart:**
- **Pydantic AI 2.27.1 with Anthropic SDK 0.125.0** sends the configuration as specified. Verified offline over an in-memory transport: no sampling fields, no `thinking` field, `output_config.effort`, top-level `cache_control`, breakpoints on the last tool and the system text, and the `run-ref` line first. This shows the request shape only.
- **The model's acceptance** of these requests, real usage and cache behaviour have not been checked, because no live call was made. They are smoke items.

**Reasoning (thinking) and request reconstruction:**
- **No reasoning is editable task evidence.** Thinking parts are not mirrored in `paper_clm_shell`, not summarised, and not shown in guarded-clm's working context.
- **Signatures are preserved:**
  - an unchanged mirror block reuses the original message, with its thinking blocks and signatures;
  - the block holding the running command must stay unchanged, so the last assistant turn of a tool loop keeps its thinking, as the provider requires;
  - the summary arm's kept tail is passed back unchanged;
  - guarded-clm sends a single rebuilt user message, so no assistant turn or thinking block is replayed.
- **The preserved-thinking history check** (the conversation binding of thinking blocks) starts with Claude Fable 5.1, per the thinking page. Claude Sonnet 5 is not in it, so editing, rolling back or summarising earlier turns does not invalidate later thinking blocks there.
- **Conflict to settle before freezing:**
  - **Retained thinking (corrected 2026-10-16):** Sonnet 5 keeps prior turns' thinking blocks in context and bills them as input. Where an arm replays original assistant turns (`paper_clm_shell`, the summary arm's tail), the replayed thinking adds to the real context and cost. guarded-clm never replays it. This is a genuine arm difference under adaptive thinking.
    - **What the estimates see:** the paper and summary arms' overall request estimates **do account for it**. The request's serialised form includes each replayed block's signature, and the ratio calibrates on reported input, which includes the billed thinking. The earlier wording said that their estimators cannot see it, which was wrong.
    - **What remains:** the model-visible mirror and the summariser transcript do not show thinking. Whether signature size tracks thinking tokens per request is a live item.
    - **A limitation to observe later:** the summary arm's tail split sizes its units from visible text only, so a kept tail can hold more real tokens than token-tail's allowance intends. Its algorithm is unchanged.
  - **Edited assistant blocks:** blocks rebuilt from an edit carry no thinking. That an earlier assistant turn without its thinking block is accepted is expected, but it is a smoke item.
  - **The alternative:** `thinking: {type: "disabled"}`, which Sonnet 5 accepts. It removes both issues. Per the provider's migration guidance, the model is then less tool-eager, and Opus-class models have shown tool calls written as text.
  - **Recommendation:** adaptive thinking, with the per-arm reported input and thinking tokens measured in the development smoke. This needs your decision.

### The summariser allowance (24 per user turn, provisional)

**What it is for:** a runaway guard. A broken summariser, or one whose summaries never fit, cannot spend without bound, and summariser calls do not consume the agent's 144.

**Natural need, from the offline sessions:**
- 1 to 3 summariser calls per session; at most 2 in one turn.
- A summary brings the request to about 50% of the budget (the target). Pressure returns at 70%, so a turn needs about 6,400 new estimated tokens per summary episode, and an episode takes at most 2 calls.
- Question 1's natural investigation reads about 100,000 characters: roughly 25,000 to 38,000 tokens at 4 to 2.6 characters per token. That is about 4 to 6 episodes, so 8 to 12 calls in the worst case.
- **24 is about twice the natural worst turn.** It can bind only in a turn that reads far more than the natural investigation, with retries.

**Worst-case exposure with the allowance:**
- **Per turn:** 24 calls, each with at most about 33,000 input tokens and 8,192 output tokens: about $0.15 at confirmed prices, so about $3.6.
- **Per session:** about $29.
- **Reservations** per call are higher (the bound assumes one token per byte at the cache-write rate: about $0.37 a call). They are settled down after each call, and the block stop counts them while open.

**There is no stronger basis:** the figure stays provisional until the development smoke shows real summariser behaviour.

## Cost scenarios (2026-10-16; not a forecast)

**Inputs:** confirmed `claude-sonnet-5` prices (above) applied to the recorded scripted sessions. Their input-token counts are **synthetic**: 2.6 characters of message content per token, declared and not measured.

**Assumptions:**
- **Output** per main or summariser call: 500 tokens (scenario A) or 1,500 tokens including thinking (B and C).
- **Calls:** C doubles the calls, for an agent that searches instead of knowing where facts are.
- **Caching:** ordinary 5-minute prefix caching with perfect reuse within a session. Each request's leading unchanged content is read at $0.20, and everything after it is written at $2.50 (automatic caching writes the whole new suffix). Tool definitions and instructions are left out of the shared prefix, so cache reads are slightly understated.
- **Coverage:** the recorded sessions only, under the scripted policies. guarded-clm `keep` and `paper_clm_shell` `keep` stand for an agent that tidies only under pressure; `tidy` is the low end.

**Per session, in USD** (development instances 1 and 2; with the cache model, and without caching in brackets):

| arm (scripted policy) | calls | input tokens | reused prefix | A | B | C |
| --- | --- | --- | --- | --- | --- | --- |
| guarded-clm, tidy | 38, 39 | 147k, 150k | 6% | 0.54, 0.55 (0.48, 0.50) | 0.92, 0.94 | 1.83, 1.88 |
| guarded-clm, keep | 36, 37 | 530k, 590k | 1% | 1.49, 1.65 (1.24, 1.36) | 1.85, 2.02 | 3.70, 4.03 |
| `paper_clm_shell`, tidy | 75, 77 | 175k, 179k | 54% | 0.59, 0.61 (0.73, 0.74) | 1.34, 1.38 | 2.69, 2.76 |
| `paper_clm_shell`, keep | 37, 38 | 453k, 507k | 90% | 0.39, 0.41 (1.09, 1.20) | 0.76, 0.79 | 1.52, 1.58 |
| summary (incl. 1 to 2 summariser calls) | 39, 40 | 505k, 543k | 81% | 0.53, 0.54 (1.21, 1.28) | 0.92, 0.94 | 1.83, 1.87 |

**Reading it:**
- **Layout drives the cache effect.** guarded-clm rebuilds the whole request on every call, so automatic caching writes nearly all its input at 1.25× and reuses only the system part. With caching on, it costs 10 to 20% more than without. The arms that append history reuse 54 to 90% of their input. This is a genuine layout difference, and it is kept as one common policy, not tuned per arm.
- **18 confirmation sessions** (6 instances × 3 arms), from the `keep` and summary rows:
  - about **$15** in scenario A;
  - about **$22** in B;
  - about **$43** in C.
- **A first development smoke** (one development instance, three arms, all eight questions): about **$2.5 to $7**.

**Conservative bounds** (what the controls allow, not an expectation):
- **Per attempt:** the reservation assumes at most one token per byte of the request, at the cache-write rate, plus `max_tokens` of output. That is up to about $0.28 for a request near the 32,000-token budget, and about $0.37 for a large summariser request. It is settled down to the confirmed cost after the call.
- **Per session, at the caps:**
  - main calls: 8 turns × 144 calls × about $0.14 at most each (about 31,000 input and 8,192 output tokens) gives about **$166**;
  - summariser calls: 8 × 24 × about $0.15 gives about **$29**.

  These caps are not a practical budget. **The block stop is the real bound,** checked before every attempt.

**What only a separately authorised development smoke can settle:**
- real token counts against the synthetic 2.6 characters per token;
- output and thinking tokens per call;
- hidden thinking replayed as input in `paper_clm_shell` and the summary arm;
- real cache reads and writes, and TTL expiry between calls;
- real call counts (search, mistakes, retries);
- real summaries;
- truncation at `max_tokens`;
- 429 and 529 retries.

**Scripted costs are not a live forecast.**

## Open items (2026-10-16)

1. **The fidelity questions** in [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md): the reminder point and its repetition, the rejected-edit free-step rule, and the profile.
2. **Thinking:** adaptive (recommended) or disabled.
3. **`max_tokens`:** 8,192 (recommended), 4,096 (the paper's BrowseComp-Plus value) or 16,384 (README).
4. **The summariser allowance** (24, provisional).
5. **Cache TTL:** 5 minutes (recommended; sessions run continuously) or 1 hour.
6. **Smoke items:**
   - SDK and framework compatibility on the real API;
   - the model's acceptance of each arm's request shape (thinking replay, edited histories, caching);
   - real token counts against the arms' estimators;
   - the reservation bound's assumption;
   - truncation at `max_tokens`;
   - cache reads and writes per arm.
7. **A public pin of guarded-clm** for recorded runs.
8. **The active clm-lib ledger** (corrected 2026-10-16; read without modification):
   - **The figures:** stored ceiling $89.457271 (an absolute cumulative ceiling, last set for experiment 014); spent $88.099746; $1.357525 below the ceiling.
   - **The earlier "$10.00" was wrong.** It came from `clm-lib budget` run without `--config`. That loads `configs/default.toml` (`ceiling_usd = 10.0`) and reports the lower of the stored and configured ceilings, in memory. It is not a persisted change to the stored ceiling.
   - **What refuses live spending now:** the absence of any 015 authorisation, not the ledger.
   - **No carry-over:** remaining room from earlier experiments' authorisations does not authorise programme 015. A 015 launch needs its own authorisation, and an explicit ceiling change if it uses this ledger. Nothing here changes either.

## Corrections and additions (2026-10-16, after the read-only review)

**The review's conclusion:** no accidental biasing defect was found in the checks performed (the request construction of each arm, the cache breakpoints, the counters and the ledger). That is not proof that no bias is possible.

**Three statements were corrected in place above:**
- the cache isolation row;
- the retained-thinking bullet;
- open item 8 (the ledger).

**Their earlier wording:**
- "independent sessions never share a cached prefix";
- "The arm's estimator and mirror cannot see it";
- "spent $88.10 against a stored $10.00 ceiling".

**What remains unchanged:** thinking-history handling, cache placement, the arms' estimators, the model settings and the paper-fidelity rules. The review evidence is a local, ignored clm-lib file, and the corrections are restated here.

**guarded-clm `strict_ratio_learning`** (superseded 2026-10-16, later: removed in guarded-clm 0.2.0.dev1; the next paragraph is kept as the record of what was proposed, and is not a current instruction):
- the proposed 015 configuration sets it to **True**, explicitly, whatever the library default becomes;
- the library revision used offline is `db619a8`;
- see [strict-ratio-verification.md](strict-ratio-verification.md).

The library default is False, and clm-lib's own harness default for older specs is False.

**Explicit live settings:**
- **A live plan is refused** unless it states:
  - thinking;
  - effort, or null for not sent;
  - `max_tokens`;
  - the cache TTL and breakpoints;
  - `max_retries` with `retry_policy: "p015-retry/1"`;
  - and, for the arms selected: guarded-clm's library pin (version, revision, source fingerprint; replacing `strict_ratio_learning`, 2026-10-16); the paper arm's profile, `reminder_before_tokens` and the three implemented `paper_rules`; and the summariser allowance.
- **The proposed values** are in clm-lib's `configs/p015/proposed-comparison-0.2.0.dev1.json` (the earlier `proposed-comparison.json` is superseded), whose `settings_status` separates the approved choices from the proposed ones. **A value there is not an approval and not a spending authorisation.**

## The accepted library (2026-10-16, later)

**guarded-clm 0.2.0.dev1** (`3f18473`) replaces the strict-learning configuration ([backstop-verification.md](backstop-verification.md)).
- **No settings:** the guarded arm takes no strict-learning setting, and a configuration naming one is refused.
- **Its estimates differ from 0.1.0** only where a request would have taught a ratio below 0.5 characters per token.
- **Open item 7 above** ("A public pin of guarded-clm for recorded runs") is met offline. The successor configuration states the version, revision and fingerprint, and `plan` checks them against the loaded library.
- **The other open items are unchanged and unapproved.**
