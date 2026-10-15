# 015 – Draft protocol for the first milestone (DRAFT, not frozen, not approved)

_Written 2026-10-15, before any 015 run. Nothing here is authorised to run. This file will be revised before it is frozen; the frozen protocol will be a separate file, and this draft will be kept as it was._

## Question

On an eight-turn incident thread, how do the published CLM design (as adapted here), this project's lighter CLM variants and a summary baseline compare on task correctness and on the cost of reaching it?

## Arms

`paper_clm_shell`, `paper_clm_tools`, `clm_lite_v2`, `clm_lite_v3_1`, and the `token-tail/1` summary baseline. See the [overview](README.md). **None of the four CLM arms is defined precisely yet.** The fidelity mapping and the arm definitions are open items in [decisions.md](decisions.md).

## Shared conditions (proposed)

- **Model:** the same main model for every arm, intended to be `claude-sonnet-5`. Its price, effort, thinking and `max_tokens` settings are still to be fixed from official documentation.
- **Task tools:** the same shared tools in every arm: the incident thread's search and page-read tools, which are not built yet. Context tools are given only where the arm's design calls for them.
- **Tool output:** task-tool results are capped by `tool-output-cap/1`, at 8,000 Unicode code points of content per result, with framing and notices recorded separately (clm-lib SPEC §27.4).
- **Transport:** native tool calls (`native-tools/1`, SPEC §27.1). Every emitted call is answered. Whether several calls per response may run is set **per arm** and recorded.
- **Counters:** `session-counters/1` (SPEC §27.3), which separate user turns, main-model calls, summary calls, provider attempts and retries, requested and executed tool calls, task and editing steps, and accepted and rejected edits.

## Proposed limits (recorded, not implemented)

- **60 task steps per user turn.** Which steps count as free editing steps is an arm-specific decision, still open.
- **A 144-call session cap.** Which calls count is **pending**. 144 equals 2 × 60 + 24, the reference README's default `lm_call_cap` formula at 60 steps; that README applies it per task and counts free editing turns.
- **A separate cap on total billable attempts** may be proposed as a financial bound. **No financial authorisation exists.**

## Measurements (proposed)

Correctness per user turn and at the end comes from the incident-thread scorer, which is not built yet. The scorer will be frozen before any comparison.

Cost and work:
- provider-reported uncached input, cache writes, cache reads, output tokens, latency and cost, per attempt and per role;
- logical calls, attempts and retries;
- requested, executed and declined tool calls;
- task and editing steps;
- edit outcomes.

## Procedure (outline; every step needs separate review)

1. Finish the arm definitions, the generator and scorer, and the launcher.
2. Prove the whole path offline through the real runner, with scripted models and the real sandbox.
3. Get a separate authorisation for any live smoke, and a further one for any comparison runs.
4. Freeze the protocol, instances, prompts, configuration and source state before the first paid call of the comparison.
5. Keep every attempt; replace nothing; report missing cells.

## State

**Nothing has run. There are no results.**

## Note added 2026-10-15 (the draft above is kept as written)

The lite arms' runtime will come from the separate guarded-clm library, so the library chunks come first. The 144-call cap is described above as per session; the library's design brief says per user turn. The conflict is open in [decisions.md](decisions.md).
