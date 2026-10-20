# 015 – Confirmation `confirm1`: record (COMPLETE; 18 sessions, each run once)

_Run 2026-10-19, 11:21:03 to 12:00:30 UTC. Six fresh docthread instances × three arms, one session each, under the decisions recorded before any instance was generated ([confirm1-prerun-decisions.md](confirm1-prerun-decisions.md)). The evidence: [confirm1-export/](confirm1-export/), [confirm1-freeze-record.json](confirm1-freeze-record.json), [confirm1-instance-manifest.json](confirm1-instance-manifest.json) and the exposure report ([confirm1-exposure.md](confirm1-exposure.md), [.json](confirm1-exposure.json))._

**This is one session per arm per instance on one model.** The six instances, not the 18 sessions, are the independent units, and no significance claim is made.

## The freeze

**What was frozen:**
- **the contract:** sha256 `ab14c53d…`, 18 sessions in the balanced order;
- **the configuration:** clm-lib `configs/p015/proposed-confirmation.json` at `13e30c2`;
- **the instances:** from the manifest (sha256 `86799fab…`; the `plan` size reading, 95,923 to 123,358 characters);
- **the revisions,** all clean: clm-lib `13e30c2`, clm-lib-test-results `a0d03812`, guarded-clm `cce58c1` (0.2.0.dev1, source `51e6dbe8…`);
- **the dependencies:** pydantic-ai-slim 2.27.1, anthropic 0.125.0, Python 3.13.15;
- **the sandbox:** Docker 20.10.13, `python:3.12-slim`;
- **the price:** `claude-sonnet-5` at $2 / $2.50 / $4 / $0.20 / $10 per million tokens. `prices.toml` is unchanged, and the price was not rechecked online.

**The arms and rules:**
- guarded-clm; `paper-clm-shell/2` (profile `paper`); `token-tail-p015/1`;
- `docthread-task/2`, `p015-turn-endings/1` and `p015-truncation/1`;
- the shared smoke-dev2 model, cache, retry and limit settings.

**The authorisation:** US$40 additional.
- **The bounds:** block stop 40.0, programme 015 ceiling 43.557330, and the ledger ceiling raised from 103.099746 to 131.657076 at a recorded spend of 91.657076.
- **At launch:** all three gate bounds allowed $40.00, with nothing pending.

**The credential:** the documented API key, loaded with tracing off only in the launching command.

| k | instance | mechanism | seed |
| --- | --- | --- | --- |
| 1 | `docthread-confirm-1` | lease | 7407 (7401 skipped: shared a development identifier) |
| 2 | `docthread-confirm-2` | memory | 7402 |
| 3 | `docthread-confirm-3` | pages | 7403 |
| 4 | `docthread-confirm-4` | lease | 7404 |
| 5 | `docthread-confirm-5` | memory | 7405 |
| 6 | `docthread-confirm-6` | pages | 7496 (15 seeds skipped: identifier or size checks) |

## Completion and spend

**The block completed:** all 18 sessions ran once. The launcher exited normally, and no session was stopped, uncertain, interrupted or rerun.

**No attempt went wrong:** all 473 provider attempts succeeded on their first try, with no failure, retry, refusal or output truncation, in the 115 user turns attempted (109 completed) of the 144 planned. No step limit or call cap occurred.

**Charges:**
- **confirmed:** $10.873678, all at provider-reported usage (473 ledger entries);
- **at reservation (uncertain):** $0;
- **pending:** none;
- **the block:** $10.873678 of $40, leaving $29.126322 unused;
- **programme 015:** $14.431008 (including the earlier $3.557330);
- **the ledger:** 102.530754 spent under the 131.657076 ceiling.

The remainder is not permission for anything further.

**Against the estimate:** expected $10 to $25, high scenario $36. The outcome was near the low end, chiefly because every paper session stopped early.

## Results (exact-format points out of 10, the preregistered primary outcome)

| instance | guarded-clm | `paper_clm_shell` | `token_tail_p015` |
| --- | --- | --- | --- |
| 1 (lease) | **10**, recall 3/3; 8 of 8 turns; $0.926, 159 s | **4**, 0/3; **`context_limit` in turn 4** (3 of 8 completed); $0.261, 128 s | **10**, 3/3; 8 of 8; $0.606, 148 s |
| 2 (memory) | **10**, 3/3; 8 of 8; $1.444, 183 s | **0**, 0/3; **`context_limit` in turn 1** (0 of 8 completed); $0.223, 85 s | **10**, 3/3; 8 of 8; $0.564, 139 s |
| 3 (pages) | **10**, 3/3; 8 of 8; $1.045, 141 s | **4**, 0/3; **`context_limit` in turn 4** (3 of 8); $0.239, 100 s | **10**, 3/3; 8 of 8; $0.323, 86 s |
| 4 (lease) | **9**, 3/3; 8 of 8; $1.133, 220 s | **4**, 0/3; **`context_limit` in turn 4** (3 of 8); $0.246, 96 s | **9**, 3/3; 8 of 8; $0.711, 174 s |
| 5 (memory) | **10**, 3/3; 8 of 8; $1.044, 122 s | **4**, 0/3; **`context_limit` in turn 4** (3 of 8); $0.279, 127 s | **10**, 3/3; 8 of 8; $0.541, 130 s |
| 6 (pages) | **9**, 3/3; 8 of 8; $0.810, 124 s | **4**, 0/3; **`context_limit` in turn 4** (3 of 8); $0.261, 139 s | **10**, 3/3; 8 of 8; $0.216, 65 s |
| **totals** | 58/60; $6.404; 949 s | 20/60; $1.509; 675 s | 59/60; $2.960; 742 s |

The times are wall-clock time per session.

**Every paper-arm session ended early,** at the arm's context limit, under the common stop-on-first-incomplete-turn policy. Its unattempted turns are unanswered under the fixed denominator. Nothing is inferred about how they would have scored.

**Paired differences, per instance (points; cost):**

| pair | instance 1 | 2 | 3 | 4 | 5 | 6 | across the six |
| --- | --- | --- | --- | --- | --- | --- | --- |
| guarded − paper | +6; +$0.67 | +10; +$1.22 | +6; +$0.81 | +5; +$0.89 | +6; +$0.77 | +5; +$0.55 | median +6 (range +5 to +10), positive in 6 of 6 |
| guarded − summary | 0; +$0.32 | 0; +$0.88 | 0; +$0.72 | 0; +$0.42 | 0; +$0.50 | −1; +$0.59 | median 0 (range −1 to 0); 5 ties, 1 negative |
| paper − summary | −6; −$0.34 | −10; −$0.34 | −6; −$0.08 | −5; −$0.46 | −6; −$0.26 | −6; +$0.04 | median −6 (range −10 to −5), negative in 6 of 6 |

**Reading costs with completion:**
- **The paper arm** costs least because it stopped early (3 or 0 of 8 turns). It is not equally effective and cheaper.
- **guarded-clm and the summary arm** both completed every turn and scored within one point of each other on every instance. guarded-clm cost more on every instance, $0.32 to $0.88 more: $6.40 against $2.96 in total. Arithmetically, the difference is in cache-write charges, which is consistent with the caching layout seen in the smokes (qualified 2026-10-20; see below): guarded-clm rebuilds each request, so most of its input is a cache write (2.22M written, 0.39M read), while the summary arm's is mostly reads (1.38M read, 0.82M written).

## The values that were not correct

**Official scores are unchanged.** This explanation comes from the evidence.

**Format misses (the fact was retrieved):**
- **guarded-clm, instance 4, the quote:** the cause line, with a `seq ` prefix added and the column padding collapsed (`not_a_journal_line`).
- **guarded-clm, instance 6, the quote:** the cause line, with the column padding collapsed.

**A summarisation error:**
- **summary arm, instance 4, the quote:** the cause line with the `seq ` prefix and collapsed padding, **and a wrong tenant id** (`tn-4735` for `tn-4951`).
- **Its source:** the arm's fifth summary had rewritten that line with the wrong id, which occurs elsewhere in the evidence. The page holding the true line had been retrieved. So this is a fact corrupted by summarisation, not only a format change.

**Unanswered:** the paper arm's fields in the turn where it stopped and in every later turn: 6 values on instances 1 and 3 to 6, and all 10 on instance 2.

There were no other misses: every other value of the two completing arms was correct, including all 36 recall values (18 per arm: 3 per session over six instances; denominator clarified 2026-10-20).

## Context management (from the exposure report)

**guarded-clm:**
- **Pressure:** the peak reported input was 25,548 to 28,122 tokens (80 to 88% of the 32,000 budget). PRESSURE notices came in 3 to 7 requests per session.
- **Edits:** 3 to 6 accepted per session, with 1 rejected in three sessions. Twice the model tried to edit a protected entry, and the library refused.
- **Holds:** 1 to 7 hold records per session, 20 in all (corrected 2026-10-20; see the qualifications below).
- **Estimates:** within about 1.5% of reported input (median ratio 1.006 to 1.015).

**`token_tail_p015`:**
- **Pressure:** the peak reported input was 20,160 to 23,165 tokens.
- **Summaries:** 1 to 5 per session (20 in total). All were accepted on the first attempt, and no summariser cap was reached.

**`paper_clm_shell` (version 2):**
- **No mirror edit was ever accepted,** in any of the six sessions. There were 12 rejections, in all six sessions:
  - 8 times, a tool block held text outside result sections;
  - twice, the file did not start with an assistant block;
  - once, results answered calls that had been removed;
  - once, the running command's block was changed.
- **What the model wrote:** in every case it rewrote tool exchanges as prose summaries, dropped or invented the call and result headers, or prefixed a user block. That conflicts with the mirror format stated in its instructions, which the arm needs to keep native tool calls paired.
- **The rejections were correct:** the validator applied the documented rules. There is no harness defect.
- **Version 2's feedback:** its carried rejection feedback reached the model 7 times, in 4 of the 6 sessions. No later edit was accepted.
- **The ending, in all six sessions:** one reminder, six rollbacks, one over-limit request, then `context_limit`. The peak reported input was 29,697 to 32,126 tokens; one request's reported input (32,126) exceeded the 32,000 budget, while the arm's estimate (31,621) had been within it.
- **The turn of the stop:** turn 4 (the quote question, which reads further into the journal) on five instances. On instance 2 it came in turn 1, the first investigation.

## Deviations, surprises and limitations

**Deviations:** none from the frozen protocol. The two replaced seeds follow the declared rule and were committed before planning.

**Surprises:**
- **The paper arm** failed the same way in all six instances, as in smoke-dev2.
- **The summary arm's one miss** came from its summariser altering an identifier.

**The paper arm's result is a result of this implementation:** `paper-clm-shell/2`, its mirror encoding and its validation, under the paper's rollback rule, with Claude Sonnet 5.
- The model never produced an edit in the required format, so the arm never reduced its context.
- This shows that the arm, as implemented here, did not work with this model.
- **It does not show that the paper's method is ineffective.** The mirror's result-section format, the "starts with an assistant block" rule, and the near-limit rollback are documented adaptations or choices; [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md) gives the sources. A different encoding, or a model trained on the reference format, could behave differently.

**The `pages` instances were filtered more:**
- the size bounds came from the two development instances (lease and memory);
- at k = 6, the size check excluded five seeds above the upper bound and two below the lower (seven in all; two of them also failed the identifier check), before 7496 passed;
- so the two `pages` instances come from the narrower, smaller part of that template's range. Results on them speak to that range.

**Small numbers:** one session per arm per instance, on one model and one task family, with six instances. Ties dominate the guarded-clm and summary comparison (5 of 6), so no difference between those two arms in points is established.

**The price** was not rechecked online during this session. All charges use the recorded price.

## Exports and verification

**The export:** made with the launcher's export, 18 runs. Each verifies (`verify_export`), the top-level `SHA256SUMS` checks, and the scans found no credential or local path.

**The exposure report** was run on the export without modifying it. Its per-turn figures add up to each session's totals.

**The earlier evidence** (both smokes' exports, records and freeze records) is unchanged.

## Qualifications (dated 2026-10-20, after the findings review; the scores and evidence are unchanged)

See [confirm1-findings.md](confirm1-findings.md).

**Holds:**
- **The corrected counts:** 20 hold records over 16 distinct tool outputs, and 15 re-reads of held outputs. 11 of the 16 outputs were eventually admitted; the other 5 were not read again.
- **What was wrong:** the earlier line, "15 of the 20 were later read again and admitted", mixed re-read records with admitted outputs.

**Cost:**
- **The arithmetic:** the guarded-clm − summary cost difference ($3.444) is entirely cache-write charges (+$3.490), offset by cache reads (−$0.199) and raised by output (+$0.154).
- **Why it is not a cause:** the request layout is the documented mechanism, but the design did not vary layout or caching, so the cause is not isolated. "Follows the caching layout" should be read as consistent with it, not as a causal claim.

**The paper arm:**
- **The rejections were valid, and the representation is ours:** its 12 rejected edits were correct under the documented rules. But most of those rules are our representation (the result-section encoding, assistant-first alternation, the unchanged running block), not requirements the paper or README state.
- **What the replays show:** most rejected edits were large prose rewrites (7 of the 11 replayed cut 91–97% of the mirror).
- **So the comparison is not reference-aligned for the editing contract.**

