# 003 – Protocol

_The sections up to "Calibration" were written before the comparison and are kept as written. "Frozen" and "After the comparison" were added afterwards._

## Proposed procedure

1. **Implement the baseline policy** `token-tail/1` in clm-lib, keeping `fixed-tail/1` (the experiments 001/002 policy) available and selectable. Record the policy id in run provenance. Proposed rule:
   - **Trigger:** unchanged. Compaction starts when the estimated request reaches 70% of the request budget.
   - **Recent tail:** keep the longest run of most-recent entries whose estimated size fits a tail budget (proposed: 15% of the request budget). Recent entries that don't fit, including a single oversized observation, are summarised with the older history.
   - **Summary size:** ask for a summary sized so that the post-compaction request lands near a target (proposed: 50% of the request budget). It is clamped to between 600 and 3,000 characters.
   - **Acceptance and retries:** on the first attempt, accept if the request falls below the pressure point. Otherwise retry once with half the length. After the retry, accept if it fits the hard limit; otherwise end the run with an explicit context overflow.
   - **Summariser instructions:** the same summariser model, with an explicit requirement to preserve current versus superseded values, exact values and references, and unresolved work.
   - **Accounting:** every summary attempt is accounted for, exactly as before.
2. **Offline tests:**
   - large recent observations are compacted;
   - the request after summarisation is constructed correctly;
   - summary attempts are accounted;
   - `fixed-tail/1` remains the default and keeps its behaviour.
3. **Calibration:** matched runs of both arms on a fresh development instance.
   - Check that both arms meet meaningful continuing work.
   - Check that the new baseline summarises less often, leaves room afterwards, and handles large recent entries.
   - Adjust the policy's tail or target only if it does not function as intended. Record every attempt.
4. **Freeze:** the protocol, fresh evaluation instances, model and settings, prompts, policy version, scorer, and the exact source state (captured as a patch by `compare`).
5. **Evaluation:** 3 fresh evaluation instances × 2 arms × 2 repetitions, sequential, alternating arm order across matched pairs. All assigned runs are reported; none are rerun to replace unfavourable outcomes. The scorer rules stay unchanged.

## Proposed settings (pending calibration)

- **Same as experiment 002:** `claude-opus-5-5`, effort `low`, 8,000-token request budget, 70% pressure point, 1,000-token recovery reserve, 2,048 output tokens per call, 20 calls per run, 30 s per execution.
- **Instances:** development `staged-dev-4`, `staged-dev-5`; evaluation `staged-eval-4`, `staged-eval-5`, `staged-eval-6`. All are new seeds of the experiment-002 generator `staged-incident-gen/1`.
- **Scorer:** score/2, unchanged.

## Budget

- The run ledger is cumulative, with a USD 10 ceiling. USD 4.75 remained before this experiment.
- An estimate is made before paid work. If calibration plus evaluation does not fit, the shortfall is reported rather than the experiment being silently shrunk.

## Implementation notes, before calibration

- **One rule added during offline testing, before any paid run:** the single **newest** entry is kept verbatim even above the tail allowance, if it fits a newest-entry cap (25% of the request budget).
  - Without it, a moderately large newest observation would be summarised before the agent had seen it verbatim.
  - A newest entry larger than the cap is still compacted.
  - Because the entry stops being newest on the next step, it cannot block later compaction, which was the `fixed-tail/1` failure mode.
- **Final proposed settings, in `configs/exp003.toml`:** policy `token-tail/1`; tail allowance 15%, newest-entry cap 25% and post-compaction target 50% of the request budget; summary length clamped to 600–3,000 characters; one retry. Everything else is identical to `configs/default.toml`.
- **Offline tests:** `tests/test_summary_policy.py`.
  - A scripted case with a large recent observation overflows under `fixed-tail/1` and completes under `token-tail/1`.
  - The request after a summary is the summary plus the token-bounded tail.
  - Both summary attempts are accounted.
  - `fixed-tail/1` remains the default, with byte-identical prompts.

## Calibration (development instance `staged-dev-4`, matched pair)

| # | Run | Arm | Result | Management observed |
| --- | --- | --- | --- | --- |
| 1 | `20261004T093826-summary-staged-dev-4-9f86` | token-tail/1 baseline | strictly correct, 11 calls, USD 0.257 | pressure from step 5 (stage 2); summaries at steps 5 and 6, each bringing the request to about 50% of the budget; no summaries afterwards; 5 action steps after the first summary |
| 2 | `20261004T093955-clm-staged-dev-4-7411` | CLM | strictly correct, 9 calls, USD 0.206 | 3 unprompted accepted edits (first in stage 1); no pressure reached; 7 action steps after the first edit |

- **Decision:** both arms meet meaningful continuing work, and the baseline compacts with room left as intended. **No settings were changed.**
- The large-recent-entry case did not arise naturally in calibration; the offline tests cover it.
- `staged-dev-5` was not used.
- **Cost:** calibration USD 0.463; ledger remaining USD 4.286.
- **Evaluation estimate:** about USD 2.9 at calibration costs; about USD 4.5 at experiment 002's highest per-run costs. If spend runs high, `compare` marks the final cells missing rather than exceeding the ceiling.

## Changes after calibration and before freezing (provenance only)

The comparison's frozen block now also records the scorer version, the summary policy and each task's **actual** generator version.
- The previous field recorded the single-stage generator constant (`incident-gen/1`) even for staged tasks. Experiment 002's frozen block is affected; its runs' `run.json` files are correct.
- These changes do not affect agent behaviour, prompts, limits or scoring.

## Frozen

Comparison `20261004T094550`, launched on 2026-10-04 with `configs/exp003.toml`. The frozen block records:
- `claude-opus-5-5`, effort `low`, prompt version `2026-10-04.1`;
- generator `staged-incident-gen/1`, scorer `score/2`, summary policy `token-tail/1`;
- the full config;
- git HEAD `d91b587`, the SHA-256 of the uncommitted source (`20261004T094550.patch`), and the untracked `configs/exp003.toml`.

Evaluation instances `staged-eval-4..6` had not been run before.

## After the comparison

- All 12 cells completed; none were missing, invalid or halted. No runs were repeated.
- No scorer, prompt, setting or code changes were made after the evaluation.
- **Cost:** evaluation USD 3.203; calibration plus evaluation USD 3.666. Ledger remaining after the experiment: USD 1.083 of the USD 10 ceiling.
