# 015 – Open decisions (checklist)

_Started 2026-10-15. **No full Phase 0 review has been done or approved.** This file lists only the decisions that chunk 1's foundations depend on or have exposed. An item is checked only when the maintainer has approved it._

## Fidelity

- [ ] **A source-by-source fidelity mapping for `paper_clm_shell`.** For every element, it gives the source (paper section or reference README line), our implementation, and any difference. Known so far from the public README:
  - one `bash` tool, with one command per turn;
  - the context mirrored to a file, with one block per message;
  - a protected prefix (system prompt and task);
  - an edit gate (`fit` by default) and receipts;
  - edit-only turns free for `max_steps`, but counted by `lm_call_cap`;
  - nudges at fixed ratios, plus a persistent nudge;
  - rollback when over the limit.

  The README states nothing about tool-output truncation, about a response with zero or several tool calls, or about how stderr is returned.
- [ ] **The explicit differences between `paper_clm_shell` and `paper_clm_tools`.** `context_read` and `context_apply` are our adaptation; neither the paper nor the README describes them.
- [ ] **Batch policy per arm:** whether several tool calls in one response may run, and in what order. The paper arm's one command per turn has to be mapped onto native calls without silently executing only the first.

## Arm semantics

- [ ] **The exact v2 recovery-reset semantics,** relative to the current code.
- [ ] **The output guard's ordering and fit rules for v3_1.** They are separate from `tool-output-cap/1`; the guard is not implemented.
- [ ] **Output limits for context tools** (for example the size of a `context_read` result).
- [ ] **The free-editing-step policy per arm.** The counters record task and editing steps but apply no rule.

## Counting and limits

- [ ] **What the 144-call session cap counts.** The candidates are `main_calls`, `main_attempts`, `main_and_summary_calls` and `all_attempts`.
  - The existing clm-lib `max_calls` counts every provider attempt, summaries and retries included (with summaries excluded under `summary_calls_in_max_calls = false`).
  - Choosing one of these changes how much work each arm can do. In particular, it decides whether the summary baseline's summary calls consume the same allowance.
- [ ] **Whether a separate cap on total billable attempts is added** for financial bounding, and its value. Setting one is not a financial authorisation.
- [ ] **The 60-task-steps-per-user-turn limit:** confirm it, and how it interacts with free editing steps.

## Added 2026-10-15 (library-first sequencing)

- [ ] **How `clm_lite_v2` and `clm_lite_v3_1` map onto the guarded-clm library's configuration** (clm-lib integration work, clm-lib SPEC §28; tracked here, not in the library's plan).
  - The library is one capability, `clm_context()`, whose trace variant is `clm_lite_v3_3`.
  - Whether the 015 lite arms are this design, configurations of it, or need separate definitions is open.
  - clm-lib's runner isn't Pydantic AI based, so how it hosts the capability is also open.
- [ ] **The scope of the 144-call cap:** **per session or per user turn.** The draft protocol here says a per-session cap, while the guarded-clm design brief says 144 calls per turn. They conflict, and the conflict is recorded, not resolved.
- [ ] **The free-step rule:** under the guarded-clm design, a response whose **first** tool call is `edit_context` is a free task step, even when later calls do task work. Confirm whether the lite arms use this rule and how the paper arms' free editing turns compare.
  - **Note:** in the library, the step and call counts are per run (one user turn). The model-facing status count can drift from the enforced count (library SPEC 13.9).

## Integration (2026-10-15)

- [x] **The integration boundary** (clm-lib architecture G1 to G8):
  - guarded-clm owns the capability;
  - Pydantic AI owns the model and tool lifecycle;
  - clm-lib owns scheduling, tools, accounting, records and export, on a dedicated `clm_lib.p015` path in a separate environment.

  Implemented and verified offline.
- [ ] **A public pin of guarded-clm for recorded runs.** Development uses the sibling checkout. Run records hold the version, git revision, dirty state and source fingerprint.
- [ ] **Provider compatibility for live use.** Pydantic AI 2.27.1's Anthropic model needs an Anthropic SDK that still accepts sampling parameters. The p015 environment pins 0.125.0, verified offline only. It needs confirmation in an authorised smoke, or a decision on another model integration.
- [ ] **Mapping the 015 lite arms onto `clm_context()` settings** (still open).

## Workload (2026-10-16)

- [x] **The incident-thread workload** is `docthread` ([docthread-workload.md](docthread-workload.md)). It is an independently written public scenario (a document-processing pipeline). It has eight questions, ten values, three recall values (questions 5, 7 and 8, from 2, 1 and 3) and one read-only collection with four tools. Generator, task and scorer are versioned. It supersedes an earlier, abandoned plan for this workload.
- [x] **The answer contract:** a fenced `json` block, the same in every arm and stated in each user turn.
- [x] **The development instances:** `docthread-dev-1` (seed 7301, lease mechanism) and `docthread-dev-2` (seed 7302, memory mechanism). They were fixed before any agent ran.
- [ ] **Confirmation instances:** how many, which mechanisms, and how the seeds are drawn at freeze time. They are never used in development. A deterministic rule is proposed in [docthread-workload.md](docthread-workload.md) (2026-10-16): six instances, two per mechanism, seeds 7401 to 7406, mechanical checks only. It needs approval.
- [ ] **Whether the scripted 10/10 transfers to real models** (unknown), and whether the task needs tuning after a development smoke. Any such tuning must be recorded and must precede freezing.
- [ ] **The arm list** (README, 2026-10-16): guarded-clm, `paper_clm_shell`, `token-tail/1`; `paper_clm_tools` only as a labelled adaptation. To be confirmed in the frozen protocol.

## Arms (2026-10-16)

- [ ] **The `paper_clm_shell` fidelity mapping** is written ([paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md)), with every adaptation listed. It needs approval. It replaces the bullet list under "Fidelity" above.
- [ ] **The batch policy:** in `paper_clm_shell` only the first `bash` call of a response runs, and any other gets an explicit not-run result; task-tool calls run in every arm. Approve or change.
- [ ] **The free-step rule for `paper_clm_shell`:** the README's rule, applied literally (an edit-only command that changed the file is free even when its edit was rejected).
- [ ] **The summary arm's version:** `token-tail-p015/1` keeps `token-tail/1`'s trigger, tail split, length rule, acceptance and summariser layout; the unit of history, the summary's placement and the summariser's system text changed ([arm-settings.md](arm-settings.md)). Approve or change.
- [ ] **The summariser cap** (24 per turn, provisional), and whether summariser calls count towards the 144-call cap (they do not, offline).
- [ ] **Sampling for `paper_clm_shell`:** the README's temperature 0.7 and top_p 0.95 conflict with the intended model, which rejects non-default sampling. This is a material conflict, recorded and not resolved: either the model's defaults (a recorded departure) or another model.
- [ ] **How reasoning parts are treated** in the mirror (not mirrored offline) and in summaries.

## Settings and launcher (2026-10-16, later)

- [x] **The cap scope:** 144 logical main-model calls per user turn, in every arm (the integrated guarded-clm configuration). Summariser calls are outside it, with their own allowance, and are counted in every total. This settles the per-session versus per-turn item above for the offline contract. It is confirmed at the freeze.
- [ ] **The summariser allowance:** 24 per turn, provisional ([arm-settings.md](arm-settings.md), "The summariser allowance").
- [ ] **Thinking:** adaptive (recommended) or disabled; the conflicts are listed in [arm-settings.md](arm-settings.md).
- [ ] **`max_tokens`:** 8,192 (recommended), 4,096 or 16,384.
- [ ] **The cache policy:** ordinary 5-minute automatic caching with tool and instruction breakpoints, isolated per session (recommended); or a 1-hour TTL.
- [ ] **The paper-fidelity questions** ([paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md), "Open questions").
- [ ] **The confirmation design:** 18 sessions ([confirmation-design.md](confirmation-design.md)).
- [x] **The bounded retry policy** `p015-retry/1`, with SDK retries off; and the launcher's spending controls `p015-spend/1`. Both are built and verified offline. No authorisation is implied.

## guarded-clm strict ratio learning (2026-10-16; superseded the same day, kept as a record; not current decisions)

- [x] **The 015 configuration sets `strict_ratio_learning=True` explicitly** (the maintainer's decision, 2026-10-16). It does not depend on the library's default, which is False. Offline verification: [strict-ratio-verification.md](strict-ratio-verification.md), against guarded-clm `db619a8`, 0.2.0.dev0.
- (superseded, no longer open) **guarded-clm's own default** for the option: the option was removed in 0.2.0.dev1.
- (superseded, no longer open) **The final live revision pin after that decision:** replaced by the accepted-library item below.
- [x] **clm-lib's harness default** for specs that omit the field is False: the earlier integration behaviour. It is always passed explicitly.

- **Superseded (2026-10-16, later):** the strict-learning configuration above must not be used for live runs. guarded-clm is being revised, and the option is expected to be replaced by a narrower backstop. The integration and the proposed configuration will be updated, and verified offline, against the new revision. The checks against `db619a8` remain valid for that revision and its recorded settings only.

## The accepted guarded-clm implementation (2026-10-16)

- [x] **guarded-clm 0.2.0.dev1 at `3f184734362c4c9e24d7f5e2a2d6de5fa18153dd`** (source sha256 `51e6dbe8…d9e4`), with its always-on implausible-ratio backstop, is the library implementation for 015. Integrated and verified offline: [backstop-verification.md](backstop-verification.md).
- [x] **The pin:** the successor configuration (clm-lib `configs/p015/proposed-comparison-0.2.0.dev1.json`) states the version, revision and source fingerprint. `plan` refuses a live plan without them, or one whose pin differs from the loaded library.
- [x] **The removed option is refused:** any configuration naming `strict_ratio_learning` is refused with a migration error, whatever its value.
- **What this does not do:** freeze the live protocol or authorise a smoke.

## The first live development smoke (2026-10-18; proposed, not authorised)

- [x] **The smoke settings, chosen by the maintainer for this smoke:**
  - `claude-sonnet-5`, adaptive thinking, effort `high`, `max_tokens` 8,192;
  - 5-minute caching with the existing breakpoints;
  - at most 2 retries per logical call;
  - 144 calls, 24 summariser calls and 60 steps per turn;
  - a 32,000-token budget with the 2,048-token reserve (the summary arm keeps its own).

  Verified against the official documentation on 2026-10-18; see [smoke-plan.md](smoke-plan.md). These choices are for the smoke and do not freeze the protocol.
- [x] **The instance and order, fixed before any result:** `docthread-dev-1`; guarded-clm, `paper_clm_shell`, `token_tail_p015`.
- [x] **The paper arm's three rules,** confirmed by the maintainer as provisional for this smoke (2026-10-18).
- [x] **The $15 allowance:** the ceiling was set to 103.099746, and the authorisation file was written (2026-10-18).
- [x] **The launch** (2026-10-18). It is **partial and stopped for a harness defect** ([smoke-dev1-record.md](smoke-dev1-record.md)).
- [x] **The harness fix** (2026-10-19): one event loop per session (`p015-session-loop/1`), verified offline against a local keep-alive server. It awaits the maintainer's review and commit.
- [x] **`smoke-dev1` is not resumed:** the fix changed the source fingerprint, and the launcher refuses its contract. s01 stands as completed under the defect; nothing is reconciled downward without provider billing.
- [ ] **s02:** resolve it as abandoned (recommended).
- [ ] **A fresh three-arm smoke** under the corrected harness (for example `smoke-dev1b`), within the block's remaining $13.13: **a new approval is needed**, since replacements were outside the original scope.

## Explicit live settings (2026-10-16)

- [x] **A live launch plan must state every experimental choice.** It is refused otherwise, before anything is written. Proposed values are in clm-lib's `configs/p015/proposed-comparison.json`, with `settings_status` separating approved from proposed. **A stated value is not an approval and not a spending authorisation.**
- [ ] **The proposed values themselves:** thinking adaptive, effort `high`, `max_tokens` 8,192, a 5-minute cache with three breakpoints, 2 retries, a summariser allowance of 24, the paper profile with its three rules, and the inherited 60 steps and 32,000 budget. **None of these is approved.**

## Caching

- [ ] **Breakpoint placement and TTL per arm.** The tool definitions and system text form the first part of the prefix. History-replaying arms and request-rebuilding arms cache differently, so this is a comparison variable that needs a stated rule.

## Model, pricing and budget

- [ ] **The `claude-sonnet-5` price,** with source and retrieval date, added to clm-lib's `configs/prices.toml`. It is absent now, and live dispatch refuses to run without it.
- [ ] **Model settings:** effort, thinking configuration and `max_tokens`. Per the public docs, Sonnet 5 runs adaptive thinking by default, and `max_tokens` covers thinking and output.
- [ ] **A check of the reservation bound's assumption** (at most one token per UTF-8 byte) for this model's tokenizer.
- [ ] **A spending ceiling and authorisation** for any live work. **None has been agreed.** Earlier estimates and unused allowances are not authorisation.

## Still to build (each item reviewed before live authorisation)

- [ ] the incident-thread generator and scorer;
- [ ] the four CLM arms;
- [ ] resumable background launching with spending guards;
- [ ] exports and paired analysis;
- [ ] offline proof through the real runner.

## Out of scope for the first milestone

The poisoned thread and the other scenarios, the wider programme's workloads and baselines, and separate live runs of v1 and v3. None of these is to be invented during the first milestone.
