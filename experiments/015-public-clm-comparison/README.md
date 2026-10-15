# 015 – Public CLM comparison (programme overview)

**Status (2026-10-15): in preparation. Nothing has run and there are no results.** No API calls of any kind have been made for 015, the ledger has not changed, and no experimental spending ceiling has been agreed.

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

## Deferred (not started; nothing will be invented for these during the first milestone)

- the wider programme's additional workloads and baselines;
- the poisoned thread and the other scenarios;
- separate live comparisons of v1 and v3.

## Progress

| Chunk | Content | State |
| --- | --- | --- |
| 1 | Shared foundations in clm-lib (SPEC §27): the native-tool transport `native-tools/1`, tool interfaces, counters `session-counters/1`, the task-tool output cap `tool-output-cap/1`, and accounted native dispatch. All opt-in; not yet wired into the runner | **done offline**: scripted-provider tests and one real-sandbox test; no live calls |
| lib-1 | [guarded-clm](https://github.com/armalite/guarded-clm) library, its chunk 1: configuration, context store, transactional edits and protected turns (its own repository and SPEC) | **done offline** (2026-10-15) |
| 2+ | Incident-thread generator and scorer, the arms, the launcher, exports, offline proof through the real runner | not started; **now after the library chunks** (see below) |

**Library-first sequencing (2026-10-15):** the lite arms' context-management runtime is being built as the separate guarded-clm library, which clm-lib will import at a pinned version. The library comes first; its roadmap is in its own `docs/implementation-plan.md`. This supersedes the earlier plan to build the incident-thread generator right after chunk 1. The generator and scorer are still required. How `clm_lite_v2` and `clm_lite_v3_1` map onto the library is an open decision.

## Documents

- [`protocol-draft.md`](protocol-draft.md): the **draft** protocol for the first milestone. It is not frozen and has not been approved.
- [`decisions.md`](decisions.md): a checklist of the decisions still open. **No full Phase 0 review has been done or approved.**

## Model and sources

- **Intended main model:** `claude-sonnet-5`. Its price and settings are **not configured yet**: they will come from the official pricing page and model documentation, with a retrieval date. Nothing has been guessed or probed.
- **Interface requirements** come only from public sources: the CLM paper (arXiv 2609.37725v1) and the reference harness README at the commit pinned in clm-lib's `docs/architecture.md`. No reference implementation source code was read or copied.
