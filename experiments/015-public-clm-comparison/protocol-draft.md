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

## Note added 2026-10-16, settings and launcher (the draft above is kept as written)

**Settled offline, not frozen:** the comparison contract in [arm-settings.md](arm-settings.md).
- **Calls:** 144 logical main-model calls per user turn in every arm, which resolves the scope question in favour of per turn, as in the integrated guarded-clm configuration. Summariser calls have their own provisional allowance of 24 per turn and are counted in every total.
- **Retries:** one bounded policy, `p015-retry/1`, with the SDK's own retries off.
- **The model configuration** `p015-model/1`: `claude-sonnet-5`; sampling not sent; adaptive thinking at effort `high`; `max_tokens` 8,192; ordinary 5-minute prompt caching, isolated per session.
- **Prices:** dated, in clm-lib's `configs/prices.toml`.

**Paper fidelity** was reviewed against the agreed source priority ([paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md)). The default is now the paper's settings: one editing reminder, and last-step rollback up to six times. The README's rules are kept as the alternative profile. Four questions remain open.

**The launcher** (`p015-launch/1`, with spending controls `p015-spend/1`) is built and proven offline ([launcher.md](launcher.md)). **The confirmation design** is proposed as 6 instances × 3 arms = 18 sessions ([confirmation-design.md](confirmation-design.md)).

**Readiness for the docthread comparison:**
- [x] The three arms, verified offline (scripted).
- [x] The comparison contract: counters, retries, model, cache and summariser settings, settled offline.
- [x] The resumable launcher with spending controls, verified offline.
- [x] Dated prices for `claude-sonnet-5`.
- [ ] Your decisions:
  - the paper-fidelity questions;
  - thinking adaptive or disabled;
  - `max_tokens`;
  - the summariser allowance;
  - the cache TTL;
  - the confirmation design.
- [ ] A public pin of guarded-clm for recorded runs.
- [ ] A ceiling for this experiment on the active clm-lib ledger, which is currently over its stored ceiling, so every live attempt is refused.
- [ ] **The development smoke,** separately authorised: SDK and framework compatibility on the real API; the model's acceptance of each arm's request shape (thinking replay, edited histories, caching); real token counts and cache behaviour against the estimators; the reservation bound; truncation at `max_tokens`; summariser behaviour.
- [ ] Any task change after the smoke, recorded before the freeze.
- [ ] The freeze: protocol, instances (drawn by the confirmation rule), prompts, settings and source state.
- [ ] A spending authorisation for the confirmation block. **None exists.**

**Remaining for the docthread comparison:** the decisions above; the smoke and its write-up; the freeze and instance generation; the authorised confirmation launch; paired per-instance analysis and the write-up, including every failed or missing run.

**Remaining for the wider public programme** (not started, and not implied by docthread readiness):
- `paper_clm_tools`, as a labelled adaptation;
- keep-all and the other planned baselines;
- the poisoned thread and the other scenarios;
- the further tasks and ablations in the public plan;
- separate live comparisons of v1 and v3, if still wanted;
- each needs its own design, offline proof and authorisation.

**There are still no paid results.**

## Note added 2026-10-16, strict ratio learning and corrections (the draft above is kept as written)

- **guarded-clm configuration:** the 015 comparison configuration sets `strict_ratio_learning=True` explicitly. It was verified offline against guarded-clm `db619a8` (0.2.0.dev0) in [strict-ratio-verification.md](strict-ratio-verification.md).
  - **Kept apart:** the earlier offline verification used guarded-clm 0.1.0, without the option. There are still no live results.
  - **Still pending:** the library's default (False now) and the final live revision pin.
- **Correction to the readiness item above,** "A ceiling for this experiment on the active clm-lib ledger, which is currently over its stored ceiling, so every live attempt is refused":
  - **The ledger:** the stored ceiling is $89.457271, with $88.099746 spent; the $10.00 figure was a default configuration applied in memory by `clm-lib budget` ([arm-settings.md](arm-settings.md), open item 8).
  - **What refuses live attempts now:** the absence of any 015 authorisation.
  - **No carry-over:** room left from earlier experiments does not authorise 015.
- **Explicit live settings:** a live launch plan is now refused unless every experimental choice is stated (arm-settings.md, "Corrections and additions"). The proposed values are in clm-lib's `configs/p015/proposed-comparison.json`. They are proposals, and stating them is not a spending authorisation.

**Readiness (updated):**
- [x] guarded-clm's strict ratio learning integrated, explicitly enabled in the proposed configuration, and verified offline (scripted and provider-like usage only).
- [x] Live plans refuse unstated experimental choices.
- [x] The documentation corrections from the read-only review.
- [ ] guarded-clm's library-default decision, then a final live revision pin.
- [ ] The decisions still listed in arm-settings.md and decisions.md: thinking, effort, `max_tokens`, the cache TTL and breakpoints, the retry count, the summariser allowance, the paper profile and its three rules, the 60-step limit and the confirmation design.
- [ ] A 015 authorisation and, if the active ledger is used, an explicit ceiling change for 015. **None exists.**
- [ ] The separately authorised development smoke. It also checks the live SDK and model compatibility items listed in the earlier readiness notes.
- [ ] The freeze.

## Note added 2026-10-16, pause (the draft above is kept as written)

**Paused (2026-10-16): programme 015 is waiting for a revised guarded-clm release.**
- **Superseded:** the proposed configuration with `strict_ratio_learning=True` (clm-lib `configs/p015/proposed-comparison.json`). It must not be used for live runs. The library's design is being revised; the option is expected to be replaced by a narrower backstop, which is not yet available.
- **Still valid, but only for what they recorded:** the strict-learning checks in [strict-ratio-verification.md](strict-ratio-verification.md) hold for guarded-clm `db619a8` (0.2.0.dev0) with the settings recorded there.
- **Still in place:** the launcher's explicit-live-settings validation and the documentation corrections.
- **Next step:** inspect the new library revision, update the integration and the proposed configuration, and verify them offline.
- **No 015 live calls or spending are authorised.**

## Note added 2026-10-16, accepted library (the draft and the pause note above are kept as written)

**Status:** accepted library integrated and verified offline; live readiness decisions and spending authorisation remain outstanding.

- **The pause above has ended.** guarded-clm 0.2.0.dev1 (`3f18473`, the always-on implausible-ratio backstop) is integrated without the removed option and verified offline ([backstop-verification.md](backstop-verification.md)).
- **The strict-learning configuration** is superseded and refused by the launcher.
- **The current proposed configuration** is clm-lib `configs/p015/proposed-comparison-0.2.0.dev1.json`.

**Readiness (updated):**
- [x] The accepted guarded-clm implementation integrated, pinned (version, revision, fingerprint) and verified offline.
- [x] Live plans state every choice. Obsolete and superseded configurations are refused.
- [ ] The decisions still open: thinking, effort, `max_tokens`, the cache TTL and breakpoints, the retry count, the summariser allowance, the paper profile and its three rules, the 60-step limit and the confirmation design.
- [ ] A 015 authorisation and, if the active ledger is used, an explicit ceiling change for 015. **None exists.**
- [ ] The separately authorised development smoke.
- [ ] The freeze.

## Note added 2026-10-18, smoke plan (the draft and the notes above are kept as written)

**The first live development smoke is planned for review and NOT AUTHORISED:**
- one development instance (`docthread-dev-1`), one session per arm, the eight-turn task;
- no confirmation instances and no performance claim;
- the plan: [smoke-plan.md](smoke-plan.md); the configuration: clm-lib `configs/p015/smoke-dev1.json`.

**Readiness for the smoke:**
- [x] A complete live spec, pinned to guarded-clm 0.2.0.dev1, with explicit settings re-checked against the official documentation on 2026-10-18. It plans offline and is refused without an authorisation.
- [x] An estimated spend of about $2.5 to $8.5 for the three sessions, a recommended $15 hard allowance, and the exact ledger and authorisation steps.
- [ ] Your confirmation of the paper arm's three rules (or a change, made and verified first).
- [ ] The ceiling change and the authorisation file. **Neither exists.**
- [ ] The go-ahead to launch.

## Note added 2026-10-18, smoke run (the draft and the notes above are kept as written)

**The development smoke ran, and is partial:**
- guarded-clm completed 8 turns (6/10; a compatibility result, not a comparison);
- `paper_clm_shell` was stopped after 3 calls;
- `token_tail_p015` was not run.

**The harness defect:** the session client is reused across each turn's new event loop, so the first attempt of each turn after the first fails and is retried. Each failed attempt is charged at its reservation.

**Spend:** $1.865448 charged ($0.494056 confirmed, $1.371392 at reservation), none pending.

**Details:** [smoke-dev1-record.md](smoke-dev1-record.md).

**Readiness:**
- [ ] The harness fix, verified offline against a real (local) connection pool.
- [ ] The maintainer's decision on s02, and on running the remaining sessions within the block.
- [ ] Then the rest of the smoke. The freeze and the confirmation design stay pending.

## Note added 2026-10-19, harness fix (the notes above are kept as written)

**The fix:** one event loop per session (`p015-session-loop/1`), verified offline against a local keep-alive server. No live call was made.

**smoke-dev1 is closed, not resumed:**
- guarded-clm completed, but under the defect;
- `paper_clm_shell` is incomplete;
- `token_tail_p015` never ran.

**The guarded session's exposure** (33,482 characters read, against 106,581 scripted) mostly reflects efficient navigation, plus the unread pages that held the only cause-signature line. Correction, 2026-10-19: the submitted quote was a real, retrieved line that failed the unstated cause-signature requirement; see the record. The offline sizing assumes sequential reading. This is to recheck, not to act on yet; see [smoke-dev1-record.md](smoke-dev1-record.md).

**Readiness:**
- [x] The harness fix, verified offline against a real (local) connection pool.
- [ ] The maintainer's review and commit of the fix.
- [ ] The decision on s02.
- [ ] Approval of a fresh three-arm smoke within the block's remaining $13.13.

## Note added 2026-10-19, development revision (the notes above are kept as written)

**Changes, all offline** (clm-lib SPEC §35):
- **The task wording** (`docthread-task/2`): the reply format states each field's form, and question 4 asks for the line that states the causing setting with its value. The scorer, evidence, tools and budgets are unchanged, and version 1 is kept.
- **Turn endings:**
  - `p015-turn-endings/1`: the first incomplete turn ends the session;
  - `p015-turn-endings/2`: a turn ending at a main-model step or call limit ends only that turn, and the next turn runs. This is supported by guarded-clm only. The paper and summary arms cannot follow it safely through their existing bookkeeping, so launches with them are refused.
- **Truncation:** a response stopped at `max_tokens` ends the session as `output_truncated` (`p015-truncation/1`). Its cost is recorded, nothing is retried, earlier turns keep their scores, and the rest are unanswered. This is a public protocol decision for development runs.

**The successor smoke** (`smoke-dev2`, clm-lib `configs/p015/smoke-dev2.json`):
- the same instance (`docthread-dev-1`), arm order and settings as smoke-dev1;
- `docthread-task/2` and `p015-turn-endings/1`;
- guarded-clm 0.2.0.dev1, with the same library source as `3f18473`, pinned to the current checkout `cce58c1` (`3f18473` plus a README link);
- a new launch id and authorisation path;
- not authorised.

**Readiness for the successor smoke:**
- [x] The harness fix, the clarified task, the explicit ending policy and truncation handling, verified offline.
- [ ] The maintainer's review and commit of these changes, so that the freeze records clean trees.
- [ ] A decision: keep `p015-turn-endings/1` for this smoke, or first approve a reviewed change that lets the paper and summary arms continue after a limit-ended turn.
- [ ] At the freeze, recheck the guarded-clm checkout revision and source fingerprint against the pin.
- [ ] The authorisation. The block's remaining $13.134552 is not permission.
- [ ] The decision on smoke-dev1 s02 (resolve as abandoned, recommended).

## Note added 2026-10-19, successor smoke run (the notes above are kept as written)

**smoke-dev2 ran once per arm** ([smoke-dev2-record.md](smoke-dev2-record.md)):
- guarded-clm completed 8 turns, 10/10;
- `paper_clm_shell` ended at its context limit in turn 4, 4/10;
- `token_tail_p015` completed 8 turns, 9/10 (the quote copied with collapsed column spacing).

**No connection failure, retry, step or call limit, or truncation occurred.** All 73 attempts were confirmed, totalling $1.691882. The programme stands at $3.557330 of $15.

**A compatibility smoke, not a comparison.**

**Readiness:**
- [x] The successor smoke.
- [x] A review of the paper arm's rollback behaviour near the limit: [paper-arm-smoke-dev2-review.md](paper-arm-smoke-dev2-review.md) (2026-10-19). No harness defect, and nothing inconsistent with the sources. One unspecified interaction matters: rollback removes a rejected edit's receipt, defeating the README's stated property that the model is told why.
- [ ] Decide the proposed narrow correction (carry a rolled-back step's edit receipt into the rollback notice; `paper-clm-shell/2`), with the fidelity document's open questions, before the confirmation design is frozen. If approved, verify it offline; no further development smoke is needed for compatibility.
- [ ] Any further step (confirmation design, instances, allowance): the maintainer's decision. Nothing is authorised.

## Note added 2026-10-19, paper arm version 2 and the confirmation proposal (the notes above are kept as written)

**`paper-clm-shell/2`** (clm-lib SPEC §36) keeps a rejected edit's reason through the rollback of its step. That is a documented adaptation, preserving the README's "the model is told why".
- **Unchanged:** every other paper rule.
- **The smokes:** both ran version 1, and their results stay version 1 results.
- **Not measured:** the change is verified offline only. Its effect on a real model is unmeasured, and the arm's context-limit risk remains.

**The confirmation proposal** is in [confirmation-design.md](confirmation-design.md) ("Revised proposal"; clm-lib `configs/p015/proposed-confirmation.json`):
- guarded-clm 0.2.0.dev1, `paper-clm-shell/2` and the summary baseline;
- `docthread-task/2`, `p015-turn-endings/1` and `p015-truncation/1`;
- the smoke-dev2 shared settings;
- six fresh instances: 18 sessions;
- an estimated $10 to $25, with a recommended $40 hard allowance.

**Readiness for confirmation:**
- [x] The paper-arm feedback correction, verified offline.
- [ ] The maintainer's approval of `paper-clm-shell/2`, the paper arm's open questions, the design and the analysis plan (including whether to report the optional substantive diagnostic).
- [x] The instance checker (`p015-instance-check/1`) and the exposure report (`p015-exposure/1`), built and verified offline (2026-10-19). The report's totals match both smokes' records, and no confirmation instance has been generated.
- [ ] The evidence-size reading for the instance rule (`plan` recommended; see [confirmation-design.md](confirmation-design.md)).
- [ ] The freeze: clean trees, the pin recheck, instance generation and checks, the plan and the freeze record.
- [ ] The allowance and a ledger ceiling change (the maintainer).
- [ ] Then a detached launch. No further development smoke is needed: no open item concerns provider compatibility.

## Note added 2026-10-19, confirmation run (the notes above are kept as written)

**`confirm1` ran to completion:** 18 sessions, each once ([confirm1-record.md](confirm1-record.md)).

**Exact-format points out of 10, totals over six instances:**
- guarded-clm 58/60 (every session completed);
- `token_tail_p015` 59/60 (every session completed);
- `paper_clm_shell` 20/60: every session ended at its context limit (turn 4 on five instances, turn 1 on one), and no mirror edit was ever accepted.

**Spend:** $10.873678, all confirmed, of the $40 block. Nothing is pending, and nothing further is authorised.

**Readiness:** the programme 015 confirmation block is complete. Any further block, replacement or change to an arm needs a new decision and authorisation.

## Note added 2026-10-20, paper arm version 3 (the notes above are kept as written)

**The change:** `paper-clm-shell/3` (clm-lib SPEC §38; [paper-clm-shell-v3.md](paper-clm-shell-v3.md)) replaces the paper arm's message-level mirror with a part-level one. Prose summaries of completed tool exchanges can now be accepted, and valid provider messages are rebuilt.

**Status:** verified offline only, and not evaluated. confirm1 is unchanged and remains a version 2 result.

**Readiness:**
- [x] Version 3, verified offline through the real runner, the Docker sandbox and the provider request bodies.
- [ ] A decision on whether to run a small live development check of version 3 (not authorised).

## Note added 2026-10-20, dev-v3a (the notes above are kept as written)

**The result:** one live session of `paper-clm-shell/3` on `docthread-dev-1` ([dev-v3a-record.md](dev-v3a-record.md)). Its only edit, a 91.6% reduction written on the final over-limit request, was rejected because the model renumbered the headers of the blocks it kept. The turn ended at its context limit in turn 4 (4/10).

**The validation's criteria:** **not demonstrated.**

**Spend:** $0.247759, confirmed.

**Readiness:** the comparison waits for a decision on that blocker. Nothing further is authorised.

## Note added 2026-10-21, dev-tools1 (the notes above are kept as written)

**The result:** one live session of `paper-clm-tools/1` on `docthread-dev-1` ([dev-tools1-record.md](dev-tools1-record.md)).
- **The edits:** in turn 4 the model made two substantive deletions of tool exchanges. Both were accepted, and the first reached the provider and was accepted.
- **The failure:** the provider rejected the request carrying the second (HTTP 400) because thinking blocks in a reply the arm had rebuilt (two replies merged) were altered. The session ended there: turns 1–3 correct, 4/10, recall 0/3.

**Not an interface-only ablation:** the tools arm differs from the shell arm in rollback, notices and the free-step rule as well as interface.

**Spend:** $0.270354, confirmed.

**Readiness:** blocked. The arm's rebuild must keep signed thinking blocks unchanged, which needs a reviewed revision. Nothing further is authorised.

## Note added 2026-10-21, `paper-clm-tools/2` (the notes above are kept as written)

**The correction:** the dev-tools1 failure is corrected offline in `paper-clm-tools/2` ([paper-clm-tools-v2.md](paper-clm-tools-v2.md)). Merged or altered replies from earlier turns are sent without their thinking blocks; nothing else changes.

**Not established:** acceptance by the provider. Edits that merge or alter replies inside the turn in progress are not covered.

**Readiness:** a live check of version 2 would need a new authorisation. None is given.

## Note added 2026-10-22, the current-turn restriction (the notes above are kept as written)

**The resolution:** the open in-turn gap is closed offline. Version 2 now refuses, before dispatch, any edit that would change a reply of the turn in progress carrying thinking ([paper-clm-tools-v2.md](paper-clm-tools-v2.md)). That turn's tool results can still be rewritten.

**For any comparison:** the tools arm cannot delete the current turn's tool exchanges while its replies carry thinking. This is a compatibility restriction of the adaptation.

**Readiness:** unchanged. A live check needs a new authorisation.

