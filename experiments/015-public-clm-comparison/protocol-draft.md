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

## Readiness checklist (added 2026-10-15; the draft above is kept as written)

- [x] The guarded-clm library is complete and verified offline.
- [x] The harness integration (`clm_lib.p015`) is verified offline:
  - transcripts identical to direct library runs;
  - accounting per attempt;
  - refusals before dispatch;
  - export with checksums.
- [ ] Pin guarded-clm to a public revision for recorded runs.
- [ ] The incident-thread generator and scorer.
- [ ] The paper arms and the summary arm in the harness.
- [ ] The lite-arm mapping onto `clm_context()` settings.
- [ ] The `claude-sonnet-5` price and settings, from official sources.
- [ ] Provider compatibility, confirmed in an authorised smoke.
- [ ] A spending authorisation. **None exists.**
- [ ] A frozen protocol.

**There are no paid results.** The integration evidence is scripted and offline only, and is not an experiment result.

## Note added 2026-10-16 (the draft above is kept as written)

- **Arms:** the README's arm scope now applies. The comparison is guarded-clm, `paper_clm_shell` and the `token-tail/1` summary baseline; `paper_clm_tools` is only a labelled adaptation.
- **Task tools:** the "search and page-read tools" above are now the four docthread tools, `read_journal`, `list_changes`, `queue_stats` and `read_playbook` ([docthread-workload.md](docthread-workload.md)).
- **Correctness:** it comes from `docthread-score/1`, which reports recall diagnostics separately.

**Readiness:**
- [x] The incident-thread generator and scorer are verified offline, with scripted sessions only.
- [ ] Confirmation instances.
- The rest of the checklist above still applies.

## Note added 2026-10-16, later (the draft above is kept as written)

- **Arms:** `paper_clm_shell` (`paper-clm-shell/1`) and the summary baseline (`token-tail-p015/1`, the p015 adaptation of `token-tail/1`) are implemented. They are verified offline on docthread with scripted models, and the real sandbox for the shell arm. See [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md), [arm-settings.md](arm-settings.md) and [arms-offline.md](arms-offline.md).
- **Limits as implemented offline:** 60 task steps and 144 main-model calls per user turn in all three arms; summariser calls have their own per-turn cap (24, provisional) and do not count towards the 144. The per-session reading of the cap above is still open, not resolved.
- **Confirmation instances:** a proposed deterministic rule is in [docthread-workload.md](docthread-workload.md). No instance has been generated.

**Readiness:**
- [x] The paper and summary arms in the harness, verified offline (scripted only).
- [ ] The cap scope and whether summariser calls count (decisions.md).
- [ ] The confirmation instances, drawn at freeze by the agreed rule.
- [ ] The live SDK and model compatibility checks, in an authorised smoke: the Anthropic SDK pin (0.125.0) with Pydantic AI 2.27.1; the intended model's acceptance of each arm's request shape (sampling, `max_tokens`, thinking, tool definitions); and the reservation bound's one-token-per-byte assumption.
- [ ] The intended model's price and settings, from official sources.
- [ ] A spending authorisation. **None exists.**
- [ ] A frozen protocol.

**There are still no paid results.**
