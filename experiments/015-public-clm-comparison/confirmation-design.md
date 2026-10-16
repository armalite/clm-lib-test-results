# 015 – Proposed confirmation design (lean initial design)

_Written 2026-10-16. **Proposed, not approved, and not a paid-run authorisation.** It stays proposed until the
maintainer has reviewed the final readiness and cost report. No confirmation instance has been generated,
inspected or run._

## The design

- **Instances:** six fresh docthread instances, two per public failure template (`lease`, `memory`, `pages`).
- **Runs:** one run per arm on each instance, for the three core arms: guarded-clm, `paper_clm_shell` (the `paper` profile) and `token-tail-p015/1`.
- **Size:** **18 sessions.**

## Instances

**Seeds and validation:** these follow the rule in [docthread-workload.md](docthread-workload.md), "Confirmation instances".

| k | name | seed | mechanism |
| --- | --- | --- | --- |
| 1 | `docthread-confirm-1` | 7401 | lease |
| 2 | `docthread-confirm-2` | 7402 | memory |
| 3 | `docthread-confirm-3` | 7403 | pages |
| 4 | `docthread-confirm-4` | 7404 | lease |
| 5 | `docthread-confirm-5` | 7405 | memory |
| 6 | `docthread-confirm-6` | 7406 | pages |

**Mechanical checks, which read no answers:**
- uniqueness of support over all calls;
- every output at most 7,800 characters;
- the failing journal's page layout;
- the natural-investigation evidence size within 100,000 to 139,000 characters;
- no identifier shared with a development instance.

**An invalid seed** is skipped and recorded, and the instance takes seed 7400 + *k* + 6*j* (the next *j*), keeping its mechanism.

**Generation** happens only at the approved freeze. Until then, no fixture is generated for development, and no answer is inspected. The workload is not tuned on any model outcome, public or private.

## Run order

**Instance-major,** in the order of k. Instance k runs the arms rotated by (k − 1) mod 3, which is the launcher's `balanced_order`, a cyclic Latin square:

| instance | 1st | 2nd | 3rd |
| --- | --- | --- | --- |
| 1, 4 | guarded-clm | `paper_clm_shell` | summary |
| 2, 5 | `paper_clm_shell` | summary | guarded-clm |
| 3, 6 | summary | guarded-clm | `paper_clm_shell` |

Over the six instances, each arm runs first, second and third exactly twice. The order is fixed in the launch contract before the first call.

## Reporting (per instance, paired)

**For each instance and arm:**
- points out of 10 and recall points out of 3, with each value's status;
- the endings and the outcome;
- user turns, main-model calls, provider attempts and retries, summariser calls and attempts, task steps, free editing steps, and accepted and rejected edits;
- uncached input, cache reads, cache writes and output tokens, by category (main and summary);
- latency;
- confirmed cost, and cost assumed at the reservation.

**Comparison:** each arm against each other, **within each instance**, as differences in points and in cost. The six paired differences are reported as they are. With n = 6 there is no significance claim and no pooled performance claim.

## Keeping every run

- **Every run is kept and reported,** including failures, exhausted allowances and missing cells.
- **An arm's failure is a result:** its unfinished values score as missing.
- **A harness defect is never counted against an arm.** Its run is kept and listed apart.
- **A rerun happens only through `resolve --as rerun` with a reason,** and only for runs that are uncertain, interrupted, stopped, harness defects, provider failures or spend stops. A rerun gets a new run directory; the old one is kept and reported. A `complete` or `arm_failure` run is never rerun.
- **A missing cell** (abandoned, or never run because the allowance ended) is reported as missing, not imputed.

## Not yet decided

- the cost bound for the 18 sessions, in the readiness and cost report ([arm-settings.md](arm-settings.md), "Cost scenarios");
- whether six instances are enough, which may be revisited after the development smoke, but never after looking at confirmation outcomes;
- the open settings in [arm-settings.md](arm-settings.md) and [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md).
