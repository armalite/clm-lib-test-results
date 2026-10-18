# 015 – First live development smoke: plan for review

_Written 2026-10-18. **NOT AUTHORISED.** This is a plan for review. No live call, token count or spend has been
made, and no authorisation or ledger change exists. A smoke result is not a performance comparison._

## Scope

**What runs:** one development instance, `docthread-dev-1` (seed 7301, the lease mechanism), with one session per arm and the existing eight-turn docthread task.

**The order,** fixed before any live result (the launcher's balanced order for one instance):
1. guarded-clm;
2. `paper_clm_shell`;
3. `token_tail_p015`.

**Why `docthread-dev-1`:** it is the first development instance, and the one with the most offline records. It is chosen here, before any live result, and is not changed afterwards.

**What does not run:** no confirmation instance is generated or used.

**The configuration:** clm-lib `configs/p015/smoke-dev1.json`, a complete live launch spec. The launcher refuses it until the authorisation below exists.

## Settings

**Provider facts re-checked 2026-10-18:**
- **Model status:** `claude-sonnet-5` is "Active", with retirement not sooner than June 30, 2027 ([model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)). The [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) lists it among "Legacy models (still available)".
- **Prices:** $2 input, $2.50 for 5-minute cache writes, $4 for 1-hour writes, $0.20 cache reads and $10 output per million tokens. The $2/$10 price is now the standard price ([pricing](https://platform.claude.com/docs/en/about-claude/pricing)), unchanged from clm-lib's `configs/prices.toml`.
- **Thinking and sampling:** adaptive thinking is the model's default, the `high` effort level is supported, and non-default sampling is rejected ([thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)).
- **Caching:** the minimum cacheable prefix is 1,024 tokens; there are at most 4 breakpoints; TTLs must match ([prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)).

**No blocker was found.**

| Setting | Value | Shared or arm-specific |
| --- | --- | --- |
| model | `claude-sonnet-5` | shared |
| thinking | adaptive (the `thinking` field is not sent) | shared |
| effort | `high` | shared |
| sampling | not sent | shared |
| output limit | `max_tokens` 8,192, covering thinking and the answer | shared |
| prompt caching | 5-minute TTL; breakpoints after the tool definitions, after the instructions, and automatic (see below) | shared policy; the cache behaviour differs by request layout |
| retries | at most 2 per logical call (`p015-retry/1`: 429, 500, 502, 503, 504, 529, connection failures); SDK retries off | shared |
| main-model calls | 144 logical calls per user turn | shared |
| task steps | 60 per user turn | shared limit; **what counts as a step is arm-specific:** guarded-clm, a response whose first call is `edit_context` is free; `paper_clm_shell`, an edit-only `bash` step is free; summary, every response counts |
| context budget | 32,000 tokens | shared |
| reserve | 2,048 tokens, giving a limit of 29,952 (guarded-clm, paper arm) | **arm-specific:** the summary arm keeps token-tail's own 1,000-token recovery reserve (hard limit 31,000), unchanged |
| summariser calls | at most 24 per user turn, counted apart and included in every cost total | summary arm only |
| library | guarded-clm 0.2.0.dev1, `3f184734362c4c9e24d7f5e2a2d6de5fa18153dd`, source sha256 `51e6dbe8…d9e4` | guarded-clm arm |
| context management | the arms' own designs (the working context and guard; the mirrored file and shell; summaries) | **the intended difference** |
| paper profile | `paper` (below) | paper arm |

**These are experiment settings.** guarded-clm is not changed by them.

### Caching, as implemented (unchanged)

**Request order** is tools, then system, then messages. In every agent request:
1. **The tool-definition breakpoint** (on the last tool) comes before the system prompt.
   - **Not session-specific:** its prefix is the same for every session with the same tools. In this smoke the tools differ by arm (`edit_context`, `bash` or neither), so the three sessions do not share it.
   - **Probably not cached at all:** at about 640 to 1,000 tokens, it is probably under the 1,024-token minimum.
2. **The instructions breakpoint** (on the last system block) follows the `run-ref: <32 hex>` line that starts each session's system prompt. It is session-specific.
3. **The automatic breakpoint** (the last cacheable block) is session-specific, for the same reason.

**Summariser requests** have no tools and no `run-ref` line. Their prefix is the summariser's own system text, then question 1, which is the same for every instance, then a session-specific transcript. A shared prefix across sessions is possible in principle, but the identical part is far below the 1,024-token minimum.

**Isolation is therefore not complete, and its practical effect is not known.** Cache reads and writes are reported per request, from the provider's usage.

### The paper arm's rules (the current proposal)

| Rule | Current behaviour | Source |
| --- | --- | --- |
| **When the reminder appears** | One editing reminder when the request estimate reaches the limit minus 2,048: 27,904 tokens | **The paper** (Appendix E: "2,048 tokens before the budget"). Reading "budget" as the usable limit is **a harness reading** of an ambiguous term |
| **Whether it repeats** | Once per crossing; re-armed when the estimate falls below 27,904 again | **Harness choice:** the paper does not say |
| **Rejected edits** | An edit-only step (one `bash` call that changed the mirror, exited 0 and printed nothing) is free, **even if the edit was rejected** | **README rule, read literally:** neither source addresses rejected edits |
| **Rollback** | Over the 29,952 limit, the last step is rolled back and the request retried, up to 6 per turn. Then one final over-limit request is allowed, and if the next is still over, the turn ends as `context_limit`. A request over the 32,000 budget itself ends the turn at once. Rollback never reaches earlier turns | Six, and the last step: **the paper** (BrowseComp-Plus). The final request after exhaustion: **the README** (the paper is silent). Keeping rollback within the turn, and the immediate end over the budget: **harness adaptations** |

**The README alternative** (not run) has nudges at 25, 50 and 75% of the budget, an adaptive persistent nudge, and rollback to a 2,048-token margin, up to 50.

**The summary policy** (`token-tail-p015/1`) is unchanged.

## What the smoke checks

**Purpose:** live compatibility and measurement. Task scores are recorded descriptively; three sessions are not a performance comparison.

| Check | Where it is recorded |
| --- | --- |
| the provider accepts each arm's request format and history handling (rebuilt single messages, replayed and edited histories, thinking blocks, caching fields) | `attempts.jsonl`: outcome and error per attempt. Any 4xx is a compatibility defect |
| edits, guards, summaries and rollbacks operate as recorded | `trace.jsonl`: guarded-clm edits, holds and pressure; paper `paper_edit_*`, `paper_rollback` and reminders; summary `summary_applied` and the summariser calls |
| usage, cache reads and writes, retries and costs are all accounted | `attempts.jsonl` (`reported`, `retry`, `logical_call`, `category`, `charged_usd`, `cost_basis`), the ledger entries, and the export manifest (charges by category and by basis) |
| actual context-management exposure | the peak reported input per arm against the 32,000 budget; counts of pressure notices, holds, edits, reminders, rollbacks and summaries; refetches; evidence read |
| exports and provenance are complete | `launcher export` with `verify_export`. Each `session.json` records the guarded-clm revision, version and fingerprint, the settings and the contract fingerprints |

**How each session's outcome is classified:**
- **Harness or provider compatibility defect:**
  - a 4xx response to a request the harness built;
  - endings `harness_defect`, `sandbox_unavailable`, `tool_failure` or `unclassified_error`;
  - an export or provenance problem.

  A defect stops the smoke for review. Nothing is retried automatically.
- **An arm's legitimate failure or limit ending:** `context_limit`, `step_limit`, `call_cap`, `summary_call_cap` or `model_behaviour`. This is a result: kept, and not rerun.
- **Spend stop:** `spend_refused` (a block stop or programme ceiling). The launcher stops, and nothing is raised automatically.
- **Provider failure:** the call failed after the bounded retries. It is kept and not rerun automatically.
- **Insufficient context-management exposure:**
  - guarded-clm: no pressure, hold or edit;
  - paper arm: no reminder, edit or rollback;
  - summary arm: no summary;
  - in each case, also no reported input reaching 70% of the budget (22,400).

  This is reported as insufficient exposure, not as an arm failure.

**A smoke can succeed without any arm solving the task.**

**Rules:**
- every attempt and partial run is kept;
- no outcome is replaced;
- instructions are not tuned after seeing results;
- the launcher never advances to confirmation;
- an interrupted or uncertain session is never rerun automatically.

## Estimated spend (not a forecast)

**Inputs:** the recorded scripted `docthread-dev-1` sessions, at the verified prices, with the ordinary cache model and the assumptions of [arm-settings.md](arm-settings.md), "Cost scenarios". The token counts are synthetic.

| Session | A (500 output tokens a call) | B (1,500) | C (1,500 and twice the calls) |
| --- | --- | --- | --- |
| guarded-clm (keep) | $1.49 | $1.85 | $3.70 |
| `paper_clm_shell` (keep / tidy) | $0.39 / $0.59 | $0.76 / $1.34 | $1.52 / $2.69 |
| summary, with its summariser calls | $0.54 | $0.94 | $1.87 |
| **all three** | **about $2.4 to $2.6** | **about $3.6 to $4.1** | **about $7.1 to $8.3** |

**Estimated range for the three sessions: about $2.5 to $8.5.**

**Not covered by the estimate:**
- real token counts;
- thinking at effort `high`;
- real call counts;
- retries;
- cache behaviour.

Measuring these is part of the smoke's purpose.

**The theoretical maximum the caps allow** is not an expectation. Every turn would have to reach 144 calls of about $0.14 at most each, plus 24 summariser calls: roughly $166 a session per arm, or about $530 for the three. **The block stop is the real bound.**

**Recommended hard allowance: $15**, both as the block stop and as the programme ceiling for this smoke. That is about 1.8 times the high scenario.

**How reservations affect admission:** before every attempt (summariser attempts and retries included), the attempt's full reservation must fit within the allowance, less confirmed spend, assumed spend and open reservations.
- **The reservation** assumes one token per byte of the request at the cache-write rate, plus 8,192 output tokens.
- **Recorded bounds** give at most about $0.27 (guarded-clm), $0.33 (summary arm agent calls), $0.23 (summariser calls) and $0.43 (paper arm, whose serialised history is largest) per attempt. Live requests with thinking signatures may be somewhat larger.
- **So the last $0.30 to $0.50 of the allowance cannot admit another call.**
- **Each reservation is settled down** to the provider-usage cost after the call. An unknown outcome is charged at the full reservation and reported apart.

## The authorisation and ledger change this needs (not made)

**The active ledger** (`runs/ledger.json`, read 2026-10-18 without modification):
- stored absolute ceiling: $89.457271;
- spent: $88.099746, with no pending reservations.

**The remaining $1.36 came from experiment 014's authorisation.** It does not carry over to 015.

**If you approve the $15 allowance, two steps follow, both by you:**

1. **Raise the stored ceiling** to spent plus the new allowance, so that no earlier allowance is reused:
   ```bash
   uv run clm-lib budget --set-ceiling 103.099746 --reason "Programme 015 development smoke smoke-dev1 (docthread-dev-1, three sessions): user-authorised USD 15 new spend; earlier allowances do not carry over"
   ```
   `clm-lib budget` prints its summary using its default configuration's $10 ceiling. That is in memory only, and the launcher reads the stored ceiling.
2. **Write the authorisation file** `runs/p015-smoke-dev1-authorisation.json` (clm-lib, gitignored):
   ```json
   {"experiment": "015", "launch_id": "smoke-dev1", "programme_ceiling_usd": 15.0, "block_stop_usd": 15.0,
    "live": true, "granted_by": "<you>", "granted_at": "<date>",
    "reason": "015 development smoke, docthread-dev-1, three sessions"}
   ```

## Launch procedure — NOT AUTHORISED

These commands are for after the two steps above, and only with your separate go-ahead. They run from the clm-lib checkout. Nothing here has been run.

1. **Pre-flight:**
   - clm-lib is clean or committed;
   - guarded-clm is at `3f18473` and clean (`plan` refuses otherwise);
   - Docker is running (`docker info`);
   - a credential source exists (the launcher checks presence only and never prints it).
2. **Plan:**
   ```bash
   .venv-p015/bin/python -m clm_lib.p015.launcher plan configs/p015/smoke-dev1.json runs/p015/smoke-dev1
   ```
3. **Run detached, with a durable log:**
   ```bash
   nohup .venv-p015/bin/python -m clm_lib.p015.launcher run runs/p015/smoke-dev1 > runs/p015/smoke-dev1.log 2>&1 &
   ```
4. **Watch:**
   ```bash
   .venv-p015/bin/python -m clm_lib.p015.launcher status runs/p015/smoke-dev1
   ```
5. **Stop if needed.** `stop` stops after the current session; `stop --now` stops before the next attempt.
   ```bash
   .venv-p015/bin/python -m clm_lib.p015.launcher stop runs/p015/smoke-dev1 --now
   ```
6. **Export when it ends:**
   ```bash
   .venv-p015/bin/python -m clm_lib.p015.launcher export runs/p015/smoke-dev1 ../clm-lib-test-results/experiments/015-public-clm-comparison/smoke-dev1-export
   ```

**Logs and state:**
- `runs/p015/smoke-dev1.log`;
- `runs/p015/smoke-dev1/events.jsonl`, `status/` and `runs/<session>/r1/` (recorder files);
- the contract and its digest;
- the ledger entries.

**The expected export:** a launch manifest, the contract, the event log, `SHA256SUMS`, and one verified session export per run (partial for an uncertain or stopped run).

**Recovery:**
- A run killed with an attempt in flight becomes `uncertain`, and its reservation is charged in full. Without one, it becomes `interrupted`.
- Neither is redispatched. `resolve --as abandoned` or `--as rerun` needs your decision and a reason, and a rerun keeps the old run.
- A spend stop ends the launch; nothing raises the allowance.
- A changed source or configuration makes `run` refuse the contract.

## Decision before execution

**The paper arm's three rules** (above) need your confirmation: the reminder point, its repetition, and the rejected-edit free step.
- **Recommendation:** confirm them as provisional for this compatibility smoke. They are recorded in the contract (`paper_rules`).
- **Consequence:** the smoke measures these behaviours as implemented. Changing any of them later needs a reviewed arm change and new offline verification, and smoke observations about reminders might not carry over.

**Separately:** the $15 allowance and the two steps above, then a go-ahead to launch.
