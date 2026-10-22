# 015 – Prompt-caching review: guarded-clm, the summary baseline and `paper-clm-tools/2`

_Written 2026-10-22. **Offline review**, with no provider or token-counting calls and no spend. It covers confirm1's guarded-clm and `token_tail_p015` sessions ([confirm1-record.md](confirm1-record.md)) and supp-tools1's `paper-clm-tools/2` sessions ([supp-tools1-record.md](supp-tools1-record.md)). No protocol, export, score or record was changed._

## Verdict

**Full-conversation caching was enabled and configured as documented for every arm.**
- The five-minute lifetime fitted the observed request intervals.
- **No harness behaviour materially obstructed reuse.**
- **The arms reused the cache very differently, and the differences come from their own request layouts:**
  - the summary baseline and `paper-clm-tools/2` keep a native, append-only conversation, so they reused the whole previous request on every ordinary call;
  - guarded-clm's request builder sends its context as one rebuilt block, so only the tools and system prompt could be reused.
- **One small avoidable cost:** the summary baseline's separate summariser calls had caching enabled but could never be read. That made the baseline slightly more expensive, by US$0.20 (6.8%).

**The existing cost results stand** as measurements of the recorded cached setup. **No rerun for caching is recommended.**

## The documented setup (sources read 2026-10-22)

**Anthropic, [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching):**
- **Automatic caching:** a top-level `cache_control` "automatically applies the cache breakpoint to the last cacheable block and moves it forward as conversations grow". Each request caches up to its last block and reads earlier content from the cache.
- **Combining breakpoints:** explicit breakpoints (here, the last tool definition and the system prompt) can be combined with automatic caching, which uses one of the four slots.
- **The prefix order:** `tools`, then `system`, then `messages`.
  - A change at any level invalidates that level and everything after it.
  - A hit needs a 100% identical prefix up to the cached block.
  - Entries are written at breakpoints, and each breakpoint looks back at most **20 positions** for an existing entry.
- **Lifetime:** five minutes by default, refreshed at no cost on each hit, measured from the start of each request. The one-hour option is for prompts reused less often than every five minutes.
- **Minimum length:** 1,024 tokens for Claude Sonnet 5. Shorter prefixes are silently not cached.
- **Thinking:** blocks in earlier assistant turns are cached with the conversation. Sonnet 4.6 and later keep them, so the cache stays valid across tool-result turns.

**The pinned adapter** (pydantic-ai-slim 2.27.1 with anthropic 0.125.0, the versions recorded in both contracts; `pydantic_ai/models/anthropic.py`):
- `anthropic_cache` becomes the top-level `cache_control` on the first-party client;
- `anthropic_cache_tool_definitions` marks the last tool;
- `anthropic_cache_instructions` marks the system prompt block;
- all three carry the given TTL, and message breakpoints are trimmed to stay within four.

**The recorded configuration,** identical in both contracts and for every arm, the summariser included (clm-lib `src/clm_lib/p015/live.py`):
- `cache_ttl` `5m`, with breakpoints `automatic`, `tool_definitions` and `instructions`;
- every recorded attempt's settings carry `anthropic_cache`, `anthropic_cache_tool_definitions` and `anthropic_cache_instructions`, all `5m`.

## What the runs sent

**The method:** raw HTTP bodies were not recorded. Every attempt's recorded request (the messages after the arm's own processing, the tool parameters and the settings) was replayed through the pinned adapter over an in-memory transport, with a placeholder key and no network: [caching-review-reconstruct.py](caching-review-reconstruct.py).
- **What it shows:** the body the pinned adapter emits for each recorded request, compared block by block with the previous request, beside the **recorded** cache reads and writes.
- **What it is:** reconstructed evidence. It does not prove a historical cache hit. The recorded usage is the measurement.

| | guarded-clm (confirm1) | summary agent (confirm1) | summariser (confirm1) | `paper-clm-tools/2` (supp-tools1) |
| --- | --- | --- | --- | --- |
| requests | 176 | 152 | 20 | 193 |
| automatic caching (top-level) | yes, every request | yes, every request | yes | yes, every request |
| explicit breakpoints | last tool (`edit_context`), system prompt | last tool, system prompt | system prompt (839 characters, below the 1,024-token minimum) | last tool (`context_apply`), system prompt |
| TTL | 5 min | 5 min | 5 min | 5 min |
| tools and system within a session | identical | identical | no tools; identical | identical |
| changing framing | `<runtime_status>` at the end of the single user block, every request: step, calls, size estimate, context revision | a finish notice in the last steps; the question restated after a summary, dropped at the next turn | each call's transcript | readouts on tool results and notes, kept and appended, never removed |
| conversation layout | **one rebuilt user text block** (`<task>`, `<working_context>`, `<runtime_status>`) | native messages, append-only between summaries | one user block per call | native messages, append-only except edits and rollbacks |
| input read / written (recorded) | 14.9% / 85.1% (0.39M / 2.22M) | 76.6% / 23.4% (1.38M / 0.42M) | 0% / 100% (0 / 401,497) | 77.5% / 22.5% (3.46M / 1.00M) |

**The session tag** (the `run-ref` line opening the system prompt) is fixed for a session, so it does not change between requests. It makes the system and conversation entries session-specific. The tool-definition prefix precedes it and is shared across sessions.

**The intervals:** the longest gap between consecutive agent requests in any session was 53 s (guarded-clm), 27 s (summary) and 26 s (`paper-clm-tools/2`), with medians of 2–4 s. Five minutes was enough.

## How reuse behaved, transition by transition

**Ordinary calls without an edit:**
- **The summary agent and `paper-clm-tools/2`:** every append-only request read the whole previous request (122 of 122 and 141 of 141). The largest append was 15 blocks, inside the 20-position lookback.
- **guarded-clm:** no request was append-only. Every request rebuilt its single user block, whose `<runtime_status>` section differs each time. Each request therefore read exactly the tools and system prefix (2,300 tokens in confirm-1, on every call) and wrote the rest.
  - **Why the unchanged text wasn't reused:** the text before the status was usually an unchanged prefix of the previous block's text (5,860 of 6,126 characters at one step). But a cache entry ends at a block boundary, so text inside a changed block cannot be reused.

**The start of a new user turn:**
- **The summary agent and `paper-clm-tools/2`:** append-only, with full reuse (for example, `paper-clm-tools/2` confirm-5 attempt 5 appended 15 blocks and read 12,306 tokens).
- **The summary arm, after a summary:** the first message's restated question ("The question you are working on now: …") is removed at the next turn. The prefix changes inside the first message, and reuse falls back to tools and system (for example, confirm1 s03 attempt 27).
- **guarded-clm:** the working context is restructured, as on every request.

**Summary creation and the request after it:**
- **The 20 summariser calls** read nothing and wrote their whole request: their system prompt is below the cacheable minimum, and each transcript is new.
- **The first agent request after each summary** starts from the new summary and reads only the tools and system prefix. Across all 24 such transitions, including the turn starts above, every one fell back to tools and system.

**Accepted context edits (`paper-clm-tools/2`):** 24 of 25 commits fell back to the tools and system prefix (2,412 tokens).
- **Why:** the edits changed early blocks, earlier-turn material, which invalidates everything after them.
- **Where some prefix survived:** a cache entry would have had to exist at a boundary within the lookback, and the only entries were at earlier requests' ends, which are too far forward.

**Rollback and rejected edits (`paper-clm-tools/2`):**
- **Rejected edits** leave the context unchanged, so they are append-only with full reuse.
- **Of 21 rollback transitions,** 15 reused an earlier entry: the undone steps' requests had written entries at the boundary the rollback returned to. Six fell back to tools and system, once with 99% of the request's characters unchanged, because no entry existed at a boundary within reach.

## Findings, by kind

**A. Expected effects of each arm's context-management design:**
1. **guarded-clm reuses only its tools and system prompt.** This is a property of guarded-clm's own request builder (library-owned), not of the harness: it sends the whole context as one rebuilt text block that ends with a status section changing every request. Consequently 85% of its input was billed at the cache-write rate. This confirms the mechanism confirm1's record described as consistent with the cost gap ([confirm1-record.md](confirm1-record.md), [confirm1-findings.md](confirm1-findings.md)). The request-level evidence now shows it directly, and the earlier wording needs no correction.
2. **The summary baseline:** full reuse within a summary; summaries reset reuse to the tools and system prefix; and the turn after a summary rewrites once, because the restated question is dropped.
3. **`paper-clm-tools/2`:** full reuse between edits. Accepted early edits reset reuse, and most rollbacks keep it.

**B. Avoidable behaviour in the shared harness or integration:**
- **The summariser calls were sent with the shared caching settings.** Each call wrote its whole request (401,497 tokens over 20 calls), and nothing could ever read it. The premium paid for writing rather than sending as ordinary input was **US$0.200748**, 6.8% of the summary arm's US$2.960. That is an arithmetic decomposition of the recorded charges at the frozen price (writes at US$2.50 per million, input at US$2.00).
  - **It did not obstruct any reuse,** and it made the baseline slightly costlier, not cheaper.
  - **The smallest correction:** send summariser calls without `anthropic_cache` and the instruction breakpoint. That is a configuration-only change, with no model-visible effect, and it would affect only the summary arm's cost.
- **Nothing else found:**
  - tools and system were stable in every session;
  - no per-request text sits in the harness-owned prefix;
  - the TTL fitted;
  - no append-only request exceeded the lookback.

**C. Possible design changes that would alter the tested implementation (none applied):**
- **guarded-clm (library-owned):** sending the stable leading part (task and working-context entries) as separate blocks, with a breakpoint before the status, would allow reuse within a turn. That is a library change, left untouched here.
- **The summary baseline:** keeping the restated-question block in place and appending the new question would avoid the turn-boundary rewrite. It changes what the model sees, so it is a baseline revision.
- **The summariser:** it cannot reuse the agent's prefix, because it has a different system prompt, no tools and a one-block transcript. Sharing the agent's prefix would mean a new summariser layout, which is a baseline revision, not a correction.

**D. What the evidence cannot resolve:**
- **After early edits and some rollbacks in `paper-clm-tools/2`,** large unchanged prefixes were not read.
  - **The open question:** would an extra explicit breakpoint (the unused fourth slot) at a stable earlier boundary have found a live entry? That depends on entry positions and lifetimes that were not recorded. Only a live test could show it, and it would change cache configuration only.
- **Character shares versus tokens:** the unchanged-prefix shares above are in characters, from the reconstruction. Without token counting they are approximate.

## Should more be run?

**For the existing comparison, no:**
- every arm had automatic full-conversation caching with the documented explicit breakpoints and a fitting TTL;
- the large differences in reuse follow from the arms' own layouts, which are legitimate outcomes;
- the one avoidable harness cost is small and works against the summary baseline.

**An optional caching experiment** would answer one specific question: would a fourth, explicit message-level breakpoint at a stable earlier boundary restore reuse after `paper-clm-tools/2`'s early edits and rollbacks? It is configuration-only, needs no rerun of the other arms, and is not needed for any conclusion recorded so far.
