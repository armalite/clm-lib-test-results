# 015 – Confirmation `confirm1`: pre-run decisions (recorded before any confirmation instance was generated)

_Recorded 2026-10-19T08:39:30Z, before instance generation, planning or any provider call. These are the maintainer's written decisions for the confirmation block. They are frozen with the launch (see the freeze record)._

## The design

- **Instances:** six fresh docthread instances: `docthread-confirm-1` to `6`, seeds 7401 to 7406, mechanisms lease, memory, pages, lease, memory, pages. They follow the predeclared rule and its deterministic skip rule ([docthread-workload.md](docthread-workload.md), "Confirmation instances").
- **Sessions:** one per arm per instance, 18 in all, in the launcher's balanced order.
- **Arms:**
  - guarded-clm 0.2.0.dev1, at the accepted source fingerprint `51e6dbe8…` (checkout `cce58c1`);
  - `paper-clm-shell/2` with the documented paper profile;
  - the summary baseline `token-tail-p015/1`, unchanged.
- **Task and endings:** `docthread-task/2`, `p015-turn-endings/1` (stop on the first incomplete turn) and `p015-truncation/1`, for every arm.
- **Shared settings:** as smoke-dev2. The configuration is clm-lib `configs/p015/proposed-confirmation.json` at commit `0bc84b1`.

## The evidence-size reading: `plan`

**The chosen bounds:** 95,923 to 123,358 characters. They are `agent.plan`'s outputs on the two development instances (106,581 and 112,144 characters), widened by the declared 10%.

**This corrects the earlier, inconsistent numerical range** ("about 100,000 to 139,000"), which had been derived from scripted sessions' total reads. It was decided before generating any confirmation instance. The readings `plan_with_recall` and `stated` are not used.

## The paper arm

**`paper-clm-shell/2` and its documented paper-profile choices are approved:**
- the reminder 2,048 tokens before the usable limit (27,904), once per crossing;
- the README's literal free-step rule;
- last-step rollback, up to 6 per turn, then one final over-limit request, then the context limit;
- one `bash` command per response;
- reasoning parts not mirrored;
- sampling not sent.

See [confirmation-design.md](confirmation-design.md), "Paper-arm choices for confirmation".

**The rejection feedback in version 2:**
- it counts against context;
- any further rollback needed to fit it uses the existing six-rollback allowance;
- no retries or headroom are added.

It is a documented adaptation, not a reproduction of unspecified behaviour of the original implementation. The reminder, free-step rule, rollback margin, allowance and terminal behaviour are unchanged.

## The analysis

**Primary outcome:** exact-format points out of 10 (`docthread-score/1`).

**Reported:**
- each instance, with paired differences between arms;
- every failure and unanswered field, kept;
- cost alongside completion and score.

**The unit:** instances, not the 18 sessions, are the independent units for any uncertainty across instances.

**The optional substantive-correctness diagnostic is not implemented and not enabled.** Individual format failures may be explained from the evidence, without changing official scores or adding another aggregate score.

## Spending

**The authorisation:** at most US$40 additional, for the planned 18 sessions and their existing bounded automatic retries. It does not cover extra sessions, replacement runs after model or harness failures, further smokes, tuning, or another block. The unused smoke allowance does not carry over.

**The starting state, verified before any change:**
- ledger spend 91.657076, 0 pending;
- programme 015 charged 3.557330;
- ledger ceiling 103.099746.

**To be set:**
- the block stop: 40.0;
- the programme 015 ceiling: 43.557330;
- the ledger ceiling: 131.657076.

## Instance generation (2026-10-19T08:41:10Z): done; the block is paused before planning

**How it was run:** the prepared checker, once, with `--size-reading plan --confirm-freeze`. It applied only the declared checks and skip rule.

**The manifest:** [confirm1-instance-manifest.json](confirm1-instance-manifest.json), sha256 `86799fab…`. It holds check names, seeds, sizes and output fingerprints, and no answers.

**Result:** all six instances valid.

| k | mechanism | chosen seed | skipped seeds (failed check) |
| --- | --- | --- | --- |
| 1 | lease | **7407** | 7401 (`no_dev_identifiers`) |
| 2 | memory | 7402 | none |
| 3 | pages | 7403 | none |
| 4 | lease | 7404 | none |
| 5 | memory | 7405 | none |
| 6 | pages | **7496** | 15 seeds, 7406 to 7490: 10 failed `no_dev_identifiers` (two of them also `evidence_size`), 5 only `evidence_size` |

**Observed, not acted on:**
- **Six of the skipped seeds** for instance 6 (a `pages` instance) **were above the `plan` upper bound** (123,358; they measured 125,191 to 125,828), and two were below the lower bound (87,402 and 93,751). The bounds come from the two development instances, which are `lease` and `memory`. So the size check can exclude more `pages` instances, and the selected `docthread-confirm-6` (105,961 characters) comes from the smaller part of that template's range.
- **`no_dev_identifiers`** failed for 11 of the 17 skipped seeds.

These are mechanical consequences of the predeclared checks and the chosen reading. No answer, location or outcome was inspected.

**Why the block is paused:** the committed launch configuration (`configs/p015/proposed-confirmation.json` at `0bc84b1`) states the predeclared seeds 7401 and 7406. By the rule, instances 1 and 6 take 7407 and 7496. That is a configuration change that must be reviewed and committed before planning. Following the maintainer's instruction, no plan, ceiling change, authorisation or provider call was made. The change is prepared in the clm-lib working tree for review.

## Correction (dated 2026-10-19, after the run; the text above is kept as written)

**The count of seeds above the upper bound was wrong.** The addendum above says that "six of the skipped seeds for instance 6 were above the `plan` upper bound". It was **five**: 7406, 7418, 7430, 7454 and 7472, measuring 125,191 to 125,828 characters. Two were below the lower bound (7478 and 7484).

**The rest stands:** the table, the manifest and the chosen seeds are unchanged and correct.

