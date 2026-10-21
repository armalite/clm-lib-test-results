# 015 – Public CLM comparison (programme overview)

**Status (2026-10-16): in preparation.**

**Accepted library integrated and verified offline; live readiness decisions and spending authorisation remain outstanding** (2026-10-16).
- **The library:** guarded-clm 0.2.0.dev1 at `3f18473` (the always-on implausible-ratio backstop), integrated and verified offline ([backstop-verification.md](backstop-verification.md)).
- **Current proposed configuration:** clm-lib `configs/p015/proposed-comparison-0.2.0.dev1.json`. Its other settings are still proposals.
- **Ended:** the earlier pause, which was waiting for the revised library (recorded in [protocol-draft.md](protocol-draft.md)).
- **Superseded and refused by the launcher:** the strict-learning configuration. Its checks ([strict-ratio-verification.md](strict-ratio-verification.md)) remain valid only for `db619a8` and the settings recorded there.
- **The first live development smoke ran on 2026-10-18 and is PARTIAL, stopped for a harness defect** ([smoke-dev1-record.md](smoke-dev1-record.md)).
  - **Progress:** guarded-clm completed 8 turns; `paper_clm_shell` was stopped after 3 calls; `token_tail_p015` was not run.
  - **The defect:** the first attempt of each turn fails when the client is reused across turns' event loops. **Fixed and verified offline on 2026-10-19** (clm-lib SPEC §34, `p015-session-loop/1`).
  - **Status:** the launch is closed and is not resumed against the changed source. guarded-clm completed but under the defect; `paper_clm_shell` is incomplete; `token_tail_p015` never ran.
  - **Spend:** $1.865 charged ($0.494 confirmed, $1.371 at reservation) of the $15 block.
- **The confirmation block `confirm1` ran on 2026-10-19 and is COMPLETE** ([confirm1-record.md](confirm1-record.md)): six fresh instances × three arms, each session once.
  - **Exact-format points (totals over the six instances):** guarded-clm 58/60, `token_tail_p015` 59/60, `paper_clm_shell` 20/60. Every paper session stopped at its context limit, and no mirror edit was accepted.
  - **Spend:** $10.873678 confirmed of the $40 block; no retries and no failed attempts.
  - **Interpretation:** one model and one task family; instances are the units. The paper result is a result of this implementation. The editing contract that rejected every paper edit is mostly our representation, so the comparison is not reference-aligned there ([confirm1-findings.md](confirm1-findings.md), 2026-10-20).
- **The successor smoke `smoke-dev2` ran on 2026-10-19 and is COMPLETE** ([smoke-dev2-record.md](smoke-dev2-record.md)). Each session ran once:
  - guarded-clm 10/10;
  - `paper_clm_shell` ended at its context limit in turn 4 (4/10);
  - `token_tail_p015` 9/10.

  73 attempts, none failed or retried. $1.691882 was charged, all confirmed; the programme stands at $3.557330 of $15. This is a compatibility result, not a comparison. No further live work is authorised.

- The guarded-clm library is complete.
- The harness integration and the public incident-thread workload (`docthread`) are done, verified offline with scripted models only.
- The comparison settings are settled offline, and a resumable launcher with spending controls is built. Both are verified with scripted models only ([arm-settings.md](arm-settings.md), [launcher.md](launcher.md)).
- The three core arms run offline on docthread: guarded-clm, `paper_clm_shell` and the summary baseline (`token-tail-p015/1`). This is verified with scripted models, and the real sandbox for the shell arm ([arms-offline.md](arms-offline.md)).
- Nothing has run against a provider, and there are no results. No API calls of any kind have been made for 015, the ledger has not changed, and no experimental spending ceiling has been agreed.

## What this programme is for

The programme compares the published CLM design, adapted as closely as practical, with this project's lighter CLM variants and with a summary baseline, on tasks where context has to be managed across several user turns.

## The first milestone

**A comparison on an eight-turn incident thread, with five arms:**

| Arm | Short description | Status |
| --- | --- | --- |
| `paper_clm_shell` | The paper's design: a mirrored context file that the model edits with a general shell in the Docker sandbox, with a tool-call message history | not implemented |
| `paper_clm_tools` | The same idea through structured `context_read` / `context_apply` tools. This is **our adaptation**: neither the paper nor the reference README describes such tools | not implemented |
| `clm_lite_v2` | This project's lighter CLM, version 2: requests are rebuilt from the working context. Its exact definition, including its recovery-reset semantics relative to the current code, is still to be written | not implemented |
| `clm_lite_v3_1` | This project's lighter CLM, version 3_1, which includes an output guard. The guard's ordering and fit rules are still to be decided | not implemented |
| `token-tail/1` | The existing summary baseline from experiment 003 | exists (unchanged) |

Some v1 and v3 behaviour will be implemented internally where it is needed to define v2 and v3_1 exactly. They will not get separate live runs in this milestone.

**Arm scope (2026-10-16), which supersedes the arm table above where they differ:**
- **The public comparison:**
  - guarded-clm (the lite arm, hosted by clm-lib);
  - the reference-aligned `paper_clm_shell`;
  - the commonly available baseline from the accepted plan, the `token-tail/1` summary baseline.
- **`paper_clm_tools`,** if run, is a separately labelled adaptation, not the reference implementation. **Implemented and verified offline on 2026-10-20** (`paper-clm-tools/1`, [paper-clm-tools.md](paper-clm-tools.md)). One live development session on 2026-10-21 ([dev-tools1-record.md](dev-tools1-record.md)) ended at a provider rejection of a rebuilt reply's thinking blocks, a blocker for any comparison.
- **No other strategies:** none are ported or approximated. The names `clm_lite_v2` and `clm_lite_v3_1` are superseded by the single guarded-clm arm.
- **Later work:** additional tasks, baselines or ablations follow the public plan and need later authorisation.

## Deferred (not started; nothing will be invented for these during the first milestone)

- the wider programme's additional workloads and baselines;
- the poisoned thread and the other scenarios;
- separate live comparisons of v1 and v3.

## Progress

| Chunk | Content | State |
| --- | --- | --- |
| 1 | Shared foundations in clm-lib (SPEC §27): the native-tool transport `native-tools/1`, tool interfaces, counters `session-counters/1`, the task-tool output cap `tool-output-cap/1`, and accounted native dispatch. All opt-in; not yet wired into the runner | **done offline**: scripted-provider tests and one real-sandbox test; no live calls |
| lib-1 | [guarded-clm](https://github.com/armalite/guarded-clm) library, its chunk 1: configuration, context store, transactional edits and protected turns | done offline, then **superseded** the same day (see below) |
| lib | The guarded-clm library: the `ClmContext` Pydantic AI capability (`clm_context()`), with offline verification and packaging | **done offline** (2026-10-15) |
| lib-integration | clm-lib hosting the library at recorded provenance (opt-in `clm_lib.p015` path, separate environment) | **done offline** (2026-10-15): scripted and mocked-provider verification only |
| workload | The public incident-thread workload, `docthread` (generator, tools, task, scorer, scripted investigator): see [docthread-workload.md](docthread-workload.md) | **done offline** (2026-10-16): scripted verification only, no model results |
| arms | `paper_clm_shell` (`paper-clm-shell/1`) and the summary baseline (`token-tail-p015/1`) on the p015 path, with the fidelity mapping, the settings table and the offline sessions: [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md), [arm-settings.md](arm-settings.md), [arms-offline.md](arms-offline.md) | **done offline** (2026-10-16): scripted verification only, no model results; `paper_clm_tools` and every other arm deferred |
| settings + launcher | The comparison contract (counters, retries, model, cache and summariser settings), the paper-fidelity review, the proposed 18-session confirmation design, and the resumable launcher with spending controls: [arm-settings.md](arm-settings.md), [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md), [confirmation-design.md](confirmation-design.md), [launcher.md](launcher.md) | **done offline** (2026-10-16): decisions listed for the maintainer; no live call |
| strict ratio | guarded-clm's `strict_ratio_learning`, explicitly enabled in the proposed 015 configuration and verified offline against `db619a8` ([strict-ratio-verification.md](strict-ratio-verification.md)); review corrections; live plans must state every experimental choice | done offline (2026-10-16); **superseded** the same day by the accepted library row below |
| accepted library | guarded-clm 0.2.0.dev1 (`3f18473`) integrated without the removed option; obsolete and superseded configurations refused; the library pinned in the successor configuration ([backstop-verification.md](backstop-verification.md)) | **done offline** (2026-10-16); succeeds the strict-ratio row above |
| 2+ | The development smoke, the freeze, the confirmation launch and paired analysis | not started; each needs a separate authorisation |

**Library-first sequencing (2026-10-15):** the lite arms' context-management runtime is being built as the separate guarded-clm library, which clm-lib will import at a pinned version. The library comes first; its roadmap is in its own `docs/implementation-plan.md`. This supersedes the earlier plan to build the incident-thread generator right after chunk 1.

**Update (2026-10-15):** the library is the `ClmContext` Pydantic AI capability; its README and SPEC describe it. An earlier library chunk with a different design was retired. No experiment result comes with it, and nothing in 015 has run.

## Documents

- [`protocol-draft.md`](protocol-draft.md): the **draft** protocol for the first milestone. It is not frozen and has not been approved.
- [`decisions.md`](decisions.md): a checklist of the decisions still open. **No full Phase 0 review has been done or approved.**
- [`docthread-workload.md`](docthread-workload.md): the workload, its offline sessions and the proposed confirmation-instance rule.
- [`paper-clm-shell-fidelity.md`](paper-clm-shell-fidelity.md), [`arm-settings.md`](arm-settings.md) and [`arms-offline.md`](arms-offline.md): the paper and summary arms.
- [`confirmation-design.md`](confirmation-design.md) and [`launcher.md`](launcher.md): the proposed confirmation design and how to run the launcher.
- [`strict-ratio-verification.md`](strict-ratio-verification.md): guarded-clm with strict ratio learning, verified offline (superseded; valid only for `db619a8`).
- [`backstop-verification.md`](backstop-verification.md): the accepted guarded-clm 0.2.0.dev1, integrated and verified offline.
- [`smoke-plan.md`](smoke-plan.md): the plan for the first live development smoke.
- [`smoke-dev1-record.md`](smoke-dev1-record.md), [`smoke-dev1-export/`](smoke-dev1-export/) and [`smoke-dev1-freeze-record.json`](smoke-dev1-freeze-record.json): its partial record and evidence.
- [`smoke-dev2-record.md`](smoke-dev2-record.md), [`smoke-dev2-export/`](smoke-dev2-export/) and [`smoke-dev2-freeze-record.json`](smoke-dev2-freeze-record.json): the successor smoke's record and evidence.
- [`dev-v3a-record.md`](dev-v3a-record.md), [`dev-v3a-export/`](dev-v3a-export/): the one live validation of `paper-clm-shell/3` (not demonstrated: its only edit was rejected for renumbered block headers).
- [`paper-clm-shell-v3.md`](paper-clm-shell-v3.md): the paper arm's version 3 (a part-level context file), its fidelity mapping and offline verification; not evaluated live.
- [`dev-tools1-record.md`](dev-tools1-record.md), [`dev-tools1-export/`](dev-tools1-export/): the one live validation of `paper-clm-tools/1` (2026-10-21). Two deletions were accepted and the first reached the provider, but the request carrying the second was rejected (HTTP 400) for altered thinking blocks in a rebuilt reply; turn 4, 4/10, US$0.270354.
- [`paper-clm-tools-v2.md`](paper-clm-tools-v2.md): the dev-tools1 failure established (a rebuilt reply combining several responses' thinking blocks) and its correction, `paper-clm-tools/2`, verified offline only.
- [`paper-clm-tools.md`](paper-clm-tools.md): the structured-tools arm `paper_clm_tools` (`paper-clm-tools/1`). It covers the specification, its differences from the structured-tools reference and from the shell arm, the fidelity limitations, the offline verification and a proposed (unauthorised) live validation. Not evaluated live.
- [`confirm1-findings.md`](confirm1-findings.md): the findings and interpretation review of the confirmation (cost components, the paper editing contract, the blog evidence outline).
- [`confirm1-record.md`](confirm1-record.md), [`confirm1-export/`](confirm1-export/), [`confirm1-freeze-record.json`](confirm1-freeze-record.json), [`confirm1-instance-manifest.json`](confirm1-instance-manifest.json), [`confirm1-prerun-decisions.md`](confirm1-prerun-decisions.md) and the exposure report [`confirm1-exposure.md`](confirm1-exposure.md): the confirmation block (18 sessions, complete).
- [`paper-arm-smoke-dev2-review.md`](paper-arm-smoke-dev2-review.md): the fidelity review of the paper arm's turn-4 failure in smoke-dev2. Its correction, `paper-clm-shell/2`, is verified offline; the revised confirmation proposal is in [`confirmation-design.md`](confirmation-design.md).

## Model and sources

- **Intended main model:** `claude-sonnet-5`. Its price and settings are **not configured yet**: they will come from the official pricing page and model documentation, with a retrieval date. Nothing has been guessed or probed.
- **Interface requirements** come only from public sources: the CLM paper (arXiv 2609.37725v1) and the reference harness README at the commit pinned in clm-lib's `docs/architecture.md`. No reference implementation source code was read or copied.
