# 015 – Proposed confirmation design (lean initial design)

_Written 2026-10-16. **Proposed, not approved, and not a paid-run authorisation.** It stays proposed until the
maintainer has reviewed the final readiness and cost report. No confirmation instance has been generated,
inspected or run._

## Revised proposal (2026-10-19), for review

_Supersedes the arm and settings lines of the 2026-10-16 text below, which is kept as written. **Not approved, not
frozen and not authorised.** No confirmation instance has been generated, inspected or run._

**The configuration:** clm-lib `configs/p015/proposed-confirmation.json`. It plans offline into a temporary directory without generating an instance (`tests/p015/test_confirmation_plan.py`).

| | Proposed |
| --- | --- |
| arms | guarded-clm 0.2.0.dev1 (source `51e6dbe8…`; checkout pin `cce58c1`, rechecked at the freeze); `paper_clm_shell` **`paper-clm-shell/2`** (profile `paper`); the summary baseline `token-tail-p015/1`, unchanged |
| task | `docthread-task/2`, the same for every arm |
| endings | `p015-turn-endings/1` (stop on the first incomplete turn) and `p015-truncation/1`, for every arm |
| shared settings | unchanged from smoke-dev2: `claude-sonnet-5`, adaptive thinking, effort high, `max_tokens` 8,192, 5-minute caching with three breakpoints, at most 2 retries per logical call, a 32,000 budget, 60 steps, 144 calls and 24 summariser calls per turn |
| instances | the six below, by the predeclared rule (unchanged) |
| sessions | 18, in the launcher's balanced order (below) |

**Discrepancy with the earlier proposal:** none in the design itself (six instances, two per template, one session per arm). The earlier configuration file, `configs/p015/proposed-comparison-0.2.0.dev1.json`, is kept unchanged. It is not a runnable confirmation: it has no instance list, pins `3f18473`, and states no task, turn-ending or paper version. The new file replaces it for review.

### Prepared steps (none executed)

1. **Decisions, by the maintainer:**
   - approve `paper-clm-shell/2` and settle the paper arm's open questions ([paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md); its three rules are provisional);
   - approve this design, the analysis plan below and the allowance.
2. **Two offline tools:** **built and verified offline (2026-10-19; clm-lib SPEC §37).**
   - the instance checker, `clm_lib.p015.docthread.confirm`;
   - the exposure report, `clm_lib.p015.exposure`;
   - both are described under "Freeze and launch checklist" below. No confirmation instance has been generated.
3. **The freeze:**
   - commit and clean all trees;
   - recheck the guarded-clm pin and source fingerprint;
   - run the instance check, and update the configuration's seeds only by the skip rule;
   - plan into `runs/p015/confirm1`;
   - write a freeze record with the instance-check results, the contract digest, the revisions, the ledger state and the price.
4. **Authorisation, by the maintainer:** the allowance and any ledger ceiling change. The programme's remaining $11.44 of the original $15 is not enough on its own.
5. **Execution:** a detached background launch, under the documented credential procedure, with the resume and stop commands used for the smokes. Each session runs once, and nothing is rerun automatically.

### Estimated spend (not a forecast)

**From smoke-dev2's measured sessions:**
- guarded-clm $1.02 (8 turns);
- the summary arm $0.44 (8 turns, 3 summaries);
- the paper arm $0.22, but for 4 turns only: it stopped at its context limit. Near the limit, a request cost about $0.012, mostly cache reads. An accepted edit rewrites history, so the next request is written to the cache again, at about $0.07.

The confirmation instances' natural evidence may be up to about 30% larger than `docthread-dev-1`'s.

| per instance | low | central | high |
| --- | --- | --- | --- |
| guarded-clm | $0.80 | $1.10 | $2.00 |
| summary baseline | $0.35 | $0.55 | $1.20 |
| `paper_clm_shell` | $0.20 (it stops early, as in smoke-dev2) | $1.00 (it completes, with some edits) | $2.80 (it completes, with many edits and rewrites) |
| **per instance** | **$1.35** | **$2.65** | **$6.00** |
| **18 sessions** | **about $8** | **about $16** | **about $36** |

**The paper arm's cost is the most uncertain:** version 2 may help it recover and complete more turns, which costs more than smoke-dev2's stopped session.

**Recommended:**
- **an expected range of about $10 to $25;**
- **a hard allowance (block stop) of $40,** about 1.1 times the high scenario, covering conservatively charged uncertain attempts. It needs a programme allowance and a ledger ceiling change, both by the maintainer.

**Reservations:** a paper-arm attempt reserved up to about $0.40 in smoke-dev2, so the last $0.40 to $0.50 of any allowance cannot admit another attempt.

### Analysis plan (final for review)

**The primary outcome is preregistered and unchanged:** the scorer's exact-form points out of 10 (`docthread-score/1`), per instance and arm, with recall out of 3 and every value's status. No other score replaces or supplements it as a headline.

**Per instance, paired:**
- **For each of the six instances:** the three arms' points, recall, endings, completed, attempted and planned turns, and cost, side by side.
- **For each pair of arms within an instance:** the difference in points and the difference in cost.

The six instances' differences are listed as they are.

**Not pooled:** the 18 sessions are not independent task instances, because each instance contributes three paired sessions. There is no pooled mean as a claim, no significance test, and no "wins" tally across instances.

**Early endings stay visible:** a session that stops keeps its ending, and its unanswered and unattempted fields are shown as such, under the fixed denominator of 10. They are never imputed or inferred.

**Cost is read with completion and correctness, never alone.** An arm that stops early and so spends less is reported as stopping early. It is not called equally effective but cheaper. Any cost comparison is stated with each arm's completed turns and points beside it.

**The exposure report** (clm-lib `p015-exposure/1`) is published for every session, per session and per turn. Its documented limits on attribution are reported with it.

**An optional diagnostic: substantive correctness. Not approved; it needs the maintainer's decision before the freeze.** If approved, it is reported beside the primary score for every arm, never as a headline, and it is never applied to the smokes. Its exact rule, per scored value whose primary status is not `correct`:

| Field type | Counts as substantively correct when |
| --- | --- |
| id, code or name (`faulty_change`, `adjacent_change`, `procedure_step`, `symptom_code`, `first_rejected_job`, `rejecting_component`) | the given text contains **exactly one** token of the field's form, and it equals the true value, ignoring case as the scorer does. The forms are: change id `CHG-` + 5 digits; step id `P-` + digits `.` digits; symptom code `SYM-` + capitals and hyphens; job id `J-` + 8 capitals or digits; component name, one of the instance's component names. |
| time, count, seconds | never: these keep the scorer's judgement |
| quote (`evidence_event`) | the scorer's three conditions hold after every run of whitespace is collapsed to one space, in both the given text and the journal lines: at least 24 characters, a substring of one failing-component incident-hour line, and the cause signature present |
| missing or malformed | never |

**Its scope:** it is motivated by format misses in both smokes, in different arms. It would apply only to values given with surrounding text or spacing changes. It would not apply to unanswered fields, wrong identifiers, lists of candidates, or quotes from lines without the cause. It is defined before any confirmation result exists, and it is not chosen because any arm looked better.

### Paper-arm choices for confirmation (each stated; approval pending)

The fidelity document's "open questions" are these concrete choices. Each value below is what `paper-clm-shell/2` implements and the proposed configuration states.

| Choice | Proposed value | Source status | Effect if changed |
| --- | --- | --- | --- |
| profile | `paper` (the README's rules kept as `readme`, not run) | the agreed rule that the paper comes first | `readme` would change the reminders, the rollback margin and the allowance (50) |
| reminder point | 2,048 tokens before the usable limit: **27,904** | the paper's "2,048 tokens before the budget", with budget read as the limit | at 2,048 before 32,000 (29,952) the reminder would coincide with rollback and could not be acted on |
| reminder repetition | once per crossing, re-armed below | not stated in the sources | repeating on every request above 27,904 adds a notice to each request near the limit |
| rejected edit's free step | free when the command changed the file, exited 0 and printed nothing (the README read literally) | not decided by either source | counting it would make a silent rejected edit use a task step (it affects only the 60-step limit) |
| rollback | the last step, retried while over the limit, up to 6 per turn, within the current turn; then one final over-limit request; then `context_limit`; a request over 32,000 itself ends the turn | the paper (6, last turn), plus the README's final request where the paper is silent | the README's to-margin rollback would leave about 2,048 tokens free, but overrides paper-first |
| several commands in one response | only the first `bash` call runs; others get a "not run" result | the README's one command per turn | none in the smokes |
| reasoning parts | not mirrored (they count towards the request, and cannot be edited) | not stated | mirroring would expose signatures to editing |
| sampling | not sent; `max_tokens` 8,192 shared | a necessary adaptation (the model rejects non-default sampling) | none available |
| rejection feedback through rollback (`/2`) | kept once, beside the rollback notice | an adaptation for the README's "the model is told why" | `/1` drops it, as in smoke-dev2 |

**What version 2's feedback does and does not do:**
- **It counts towards context:** the rejection feedback is part of the request the rollback measures, and of the request sent.
- **Fitting it uses the existing allowance:** any further rollback needed to fit the feedback is counted against the existing six per turn.
- **No extra retries or headroom:** none are granted, and the terminal rule is unchanged.
- **Its real-model effect is unmeasured:** it is an adaptation. It does not remove the arm's context-limit risk.

**The one wording in the instance rule that needs a decision:**
- **The rule says:** "the evidence a natural investigation reads (`agent.plan`, measured as output sizes only) lies within the development instances' range, widened by 10%: about 100,000 to 139,000 characters".
- **The conflict:** for `agent.plan` the development instances measure 106,581 and 112,144 characters, so widening by 10% gives **95,923 to 123,358**. The stated "about 100,000 to 139,000" was derived instead from the scripted sessions' total reads, including policy-dependent re-reads (112,638 to 126,418; see [docthread-workload.md](docthread-workload.md)).
- **The choice:** the checker therefore requires the reading to be named:
  - `plan` (the literal measure, 95,923–123,358; **recommended**, because it is the measure the rule names);
  - `plan_with_recall` (102,928–131,799);
  - `stated` (100,000–139,000).
- **Its effect:** which seeds pass the size check, and so possibly which seeds are skipped. Nothing else.

### Freeze and launch checklist (not executed)

**A. Review and commit,** by the maintainer:
- review and commit clm-lib and clm-lib-test-results;
- decide: `paper-clm-shell/2` and the paper choices above, this design and analysis plan, the optional diagnostic, the size reading, and the allowance.

**B. Clean source and the library pin:**

Run from the clm-lib checkout:

```bash
git status --porcelain
```
```bash
git -C ../clm-lib-test-results status --porcelain
```
```bash
git -C ../guarded-clm status --porcelain
```
```bash
git -C ../guarded-clm rev-parse HEAD
```
```bash
.venv-p015/bin/python -c "import json; from clm_lib.p015 import launcher as L; c=json.load(open('configs/p015/proposed-confirmation.json')); print(L.live_spec_problems(c), L.library_pin_problems(c), L.version_problems(c))"
```

Every status must be empty. The guarded-clm revision must equal the configuration's pin (and the source fingerprint `51e6dbe8…`), or the pin is updated by a reviewed commit. All three problem lists must be empty.

**C. Protocol freeze, before any confirmation instance is generated:** commit this design, the analysis plan, the chosen size reading and the configuration. The freeze commit is recorded in the freeze record.

**D. Instance generation and checks,** once, at the freeze:

```bash
.venv-p015/bin/python -m clm_lib.p015.docthread.confirm runs/p015/confirm1-instances.json --size-reading plan --confirm-freeze
```

This prints names, seeds and pass or fail only. If a seed was skipped, the configuration's `instances` are set to the manifest's `config_instances` in a reviewed commit, and nothing else changes. The manifest is published with the freeze.

**E. Plan the immutable contract,** with the balanced order:

```bash
.venv-p015/bin/python -m clm_lib.p015.launcher plan configs/p015/proposed-confirmation.json runs/p015/confirm1
```

Then write the freeze record: the contract digest, revisions, ledger state, price, instance manifest digest and size reading.

**F. A separate spending authorisation, by the maintainer only:**
- set the ledger ceiling (`clm-lib budget --set-ceiling X --reason "..."`);
- write `runs/p015-confirm1-authorisation.json` (schema as for the smokes: `experiment`, `launch_id` `confirm1`, `programme_ceiling_usd`, `block_stop_usd`, `live` true, `granted_by`, `granted_at`, `reason`).

**G. Launch detached,** in one command that loads the key with tracing off:

```bash
set +x; set -a; . "$HOME/.config/clm-lib/api.env"; set +a; nohup setsid .venv-p015/bin/python -m clm_lib.p015.launcher run runs/p015/confirm1 > runs/p015/confirm1.log 2>&1 < /dev/null &
```

**H. Monitor, stop and export:**

```bash
.venv-p015/bin/python -m clm_lib.p015.launcher status runs/p015/confirm1
```
```bash
tail runs/p015/confirm1/events.jsonl
```

To stop before the next attempt:

```bash
.venv-p015/bin/python -m clm_lib.p015.launcher stop runs/p015/confirm1 --now
```

After the launch ends:

```bash
.venv-p015/bin/python -m clm_lib.p015.launcher export runs/p015/confirm1 ../clm-lib-test-results/experiments/015-public-clm-comparison/confirm1-export
```
```bash
.venv-p015/bin/python -m clm_lib.p015.exposure ../clm-lib-test-results/experiments/015-public-clm-comparison/confirm1-export --markdown confirm1-exposure.md
```

Nothing is relaunched or resolved automatically, and uncertain attempts are never resolved without the maintainer.

### Authorisation scope (proposal only)

**The proposed hard allowance is USD 40 of additional spend** for the 18 confirmation sessions, including retries, summaries and conservatively charged uncertain attempts. It is not a top-up of an earlier allowance, and the unused remainder of the smokes' $15 does not carry over.

**Earlier charges stay counted:** programme 015 has been charged USD 3.557330 so far (smoke-dev1 1.865448, smoke-dev2 1.691882). The spend gate counts every programme-015 charge against the programme ceiling.

**If USD 40 is approved,** the figures follow, at today's ledger:

| | Value | Derivation |
| --- | --- | --- |
| block stop (launch `confirm1`) | **40.0** | the approved allowance |
| programme ceiling | **43.557330** | $3.557330 already charged + $40 |
| ledger ceiling | **131.657076** | $91.657076 spent today + $40, set by the maintainer with `--set-ceiling` |

If any other spend reaches the ledger first, the ceiling is recomputed from the spent figure at that time, never raised by more than the approved $40.

**The estimate stays a proposal:** expected about $10 to $25; a high scenario of about $36.

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
