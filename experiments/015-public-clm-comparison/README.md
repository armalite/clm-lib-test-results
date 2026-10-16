# 015 – Public CLM comparison (programme overview)

**Status (2026-10-16): in preparation.**
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
- **`paper_clm_tools`,** if run, is a separately labelled adaptation, not the reference implementation.
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
| 2+ | The development smoke, the freeze, the confirmation launch and paired analysis | not started; each needs a separate authorisation |

**Library-first sequencing (2026-10-15):** the lite arms' context-management runtime is being built as the separate guarded-clm library, which clm-lib will import at a pinned version. The library comes first; its roadmap is in its own `docs/implementation-plan.md`. This supersedes the earlier plan to build the incident-thread generator right after chunk 1.

**Update (2026-10-15):** the library is the `ClmContext` Pydantic AI capability; its README and SPEC describe it. An earlier library chunk with a different design was retired. No experiment result comes with it, and nothing in 015 has run.

## Documents

- [`protocol-draft.md`](protocol-draft.md): the **draft** protocol for the first milestone. It is not frozen and has not been approved.
- [`decisions.md`](decisions.md): a checklist of the decisions still open. **No full Phase 0 review has been done or approved.**
- [`docthread-workload.md`](docthread-workload.md): the workload, its offline sessions and the proposed confirmation-instance rule.
- [`paper-clm-shell-fidelity.md`](paper-clm-shell-fidelity.md), [`arm-settings.md`](arm-settings.md) and [`arms-offline.md`](arms-offline.md): the paper and summary arms.
- [`confirmation-design.md`](confirmation-design.md) and [`launcher.md`](launcher.md): the proposed confirmation design and how to run the launcher.

## Model and sources

- **Intended main model:** `claude-sonnet-5`. Its price and settings are **not configured yet**: they will come from the official pricing page and model documentation, with a retrieval date. Nothing has been guessed or probed.
- **Interface requirements** come only from public sources: the CLM paper (arXiv 2609.37725v1) and the reference harness README at the commit pinned in clm-lib's `docs/architecture.md`. No reference implementation source code was read or copied.
