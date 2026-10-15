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

- [ ] **How `clm_lite_v2` and `clm_lite_v3_1` map onto the guarded-clm library's configuration** (now library plan step 3).
  - The ported library is one capability, `clm_context()`, whose trace variant is `clm_lite_v3_3`.
  - Whether the 015 lite arms are this design, configurations of it, or need separate definitions is open.
  - clm-lib's runner isn't Pydantic AI based, so how it hosts the capability is also open.
- [ ] **The scope of the 144-call cap:** **per session or per user turn.** The draft protocol here says a per-session cap, while the guarded-clm design brief says 144 calls per turn. They conflict, and the conflict is recorded, not resolved.
- [ ] **The free-step rule:** under the guarded-clm design, a response whose **first** tool call is `edit_context` is a free task step, even when later calls do task work. Confirm whether the lite arms use this rule and how the paper arms' free editing turns compare.
  - **Note (port):** in the ported library, the step and call counts are per run (one user turn). The model-facing status count can drift from the enforced count (library SPEC 13.9).

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
