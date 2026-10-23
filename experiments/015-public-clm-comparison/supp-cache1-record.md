# 015 – `supp-cache1` record: guarded-clm's recommended caching configuration on confirm1's instances

_Run 2026-10-23T03:24Z to 04:16Z under [supp-cache1-protocol.md](supp-cache1-protocol.md) (sha256 `445f144dca51109a7c99c19337fef1b02daccbeaa25b2d6e96f361eb84fc9a25`, in the [freeze record](supp-cache1-freeze-record.json)). A supplemental evaluation on previously used instances, compared descriptively with confirm1's frozen, non-contemporaneous guarded-clm and summary results._

## In short

- **All six sessions completed all eight turns and scored 10/10:** 60/60, against confirm1's guarded-clm 58 and summary 59. Recall was 3/3 in every session of all three.
- **The expected cache reuse held in every session.**
  - All 122 ordinary calls and all 42 new-turn starts read the previous request's cached working context.
  - The prospective boundary check matched the predicted prefix exactly on 199 of 200 attempts. The remaining one was a consistent fallback to the tools and system prompt; there were no mismatches.
  - No session read anything at its first request, so there was no shared-prefix reuse across sessions.
- **The block cost US$3.251979, all confirmed:** about half of confirm1's guarded sessions (US$6.40432) and 10% more than its summary sessions (US$2.959886).
  - The new sessions did more work: 17% more attempts and 25% more input than confirm1's guarded sessions.
  - Billed the way the original configuration bills, the same input would have cost an estimated US$7.12 instead of US$2.30.
- **No provider error, retry, harness defect or rejected edit.** The new sessions made 36 accepted edits, against 24 in confirm1's guarded sessions.
- **The reading:** the evidence fits a default change, within the limits below. The decision is the maintainer's.

## What this is

- **Not contemporaneous:** a later supplemental evaluation, on confirm1's six instances (already used), with guarded-clm 0.2.0.dev2 in dev-cache1 B's configuration. confirm1's sessions ran on 2026-10-19/20.
- **Several changes at once:** against confirm1's guarded sessions, the configuration changes the library revision, the request layout (segmented, with the task after the working context), the context cache marker and the host caching together.
- **Not attributed to caching alone:** differences in work, scores or cost may come from any of these, from provider-side variation between dates, or from chance. Six sessions support a description, not a significance claim.

## What ran

| | |
| --- | --- |
| launch | `supp-cache1`, contract `4b27f3f567c17031…`, frozen 03:24:33Z |
| configuration | dev-cache1 B unchanged: `segmented_task_last`, `cache_point` 5m, tool and instruction breakpoints (5m), no automatic caching; budget 32,000, 60 steps, 144 calls; claude-sonnet-5, adaptive thinking, effort high, `max_tokens` 8,192; `docthread-task/2`, `p015-turn-endings/1`, `p015-truncation/1` |
| library | guarded-clm 0.2.0.dev2, d1d6d1d, source `5da97515…`, installed metadata 0.2.0.dev2, clean |
| checkouts at freeze | clm-lib 2200f8b clean; clm-lib-test-results 40a58763 with only this block's three pre-run files; guarded-clm clean |
| instances | confirm1's frozen manifest; all six fixtures reproduce its `outputs_sha256` |
| spec | [supp-cache1-spec.json](supp-cache1-spec.json): dev-cache1 B with only the launch id, authorisation, instances, note and settings status changed |
| order and isolation | confirm-1 to confirm-6, one `run --max-sessions 1` each, every session 395–396 s after the previous session's last attempt |
| spending | block stop US$10.00 (effective US$10.00); programme ceiling US$43.55733 and ledger ceiling US$131.657076, both unchanged |

- **The procedure:** a resumable script, detached from the chat session, loaded the key through the documented `api.env` procedure with tracing off. After every session it checked for defects, compatibility errors and open reservations, and no check stopped the block. Nothing was rerun or replaced, and no source changed during the block.
- **The lifetime assumption:** the longest gap between consecutive attempts within a session was 48 s, inside the 5-minute cache lifetime.

## Per instance

From the predeclared [supp-cache1-analysis.py](supp-cache1-analysis.py) (output: [supp-cache1-analysis.md](supp-cache1-analysis.md), [.json](supp-cache1-analysis.json)). "New" is this block; G and S are confirm1's guarded-clm and summary sessions.

| instance | points new / G / S | cost new / G / S (US$) | attempts new / G / S | task calls new / G | input tokens new / G | output tokens new / G | new: wall time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| confirm-1 | 10 / 10 / 10 | 0.564 / 0.926 / 0.606 | 36 / 28 / 33 | 45 / 37 | 535,543 / 376,422 | 16,425 / 12,816 | 195 s |
| confirm-2 | 10 / 10 / 10 | 0.591 / 1.444 / 0.564 | 36 / 37 / 32 | 41 / 48 | 613,201 / 589,930 | 17,290 / 15,913 | 204 s |
| confirm-3 | 10 / 10 / 10 | 0.512 / 1.045 / 0.323 | 34 / 26 / 21 | 38 / 35 | 426,321 / 425,459 | 12,112 / 11,331 | 151 s |
| confirm-4 | 10 / 9 / 9 | 0.414 / 1.133 / 0.711 | 28 / 31 / 39 | 38 / 41 | 422,773 / 444,116 | 12,084 / 18,156 | 142 s |
| confirm-5 | 10 / 10 / 10 | 0.382 / 1.044 / 0.541 | 26 / 26 / 29 | 34 / 31 | 460,335 / 431,036 | 11,117 / 9,888 | 133 s |
| confirm-6 | 10 / 9 / 10 | 0.790 / 0.810 / 0.216 | 46 / 28 / 18 | 48 / 39 | 811,185 / 343,723 | 25,900 / 9,360 | 324 s |
| **total** | **60 / 58 / 59** | **3.252 / 6.404 / 2.960** | **206 / 176 / 172** | **244 / 231** | **3,269,358 / 2,610,686** | **94,928 / 77,464** | 1,149 s |

- **Completion:** every session of all three completed all eight turns (`complete`). There were no limit endings, truncations or spending endings.
- **Summed model latency:** new 1,121 s, G 925 s, S 721 s.

**Cache use** (provider-reported tokens):

| | read | written | uncached | read share |
| --- | --- | --- | --- | --- |
| new (6) | 2,532,380 | 644,532 | 92,446 | 77.5% |
| confirm1 guarded (6) | 389,981 | 2,220,529 | 176 | 14.9% |
| confirm1 summary (6) | 1,384,829 | 824,724 | 344 | 62.7% |

**Edits, holds and refetches (guarded sessions):**

| instance | accepted new / G | rejected new / G | held back new / G | refetches new / G |
| --- | --- | --- | --- | --- |
| confirm-1 | 7 / 3 | 0 / 1 | 2 / 2 | 2 / 1 |
| confirm-2 | 9 / 6 | 0 / 1 | 3 / 7 | 3 / 6 |
| confirm-3 | 6 / 3 | 0 / 1 | 1 / 3 | 1 / 3 |
| confirm-4 | 3 / 4 | 0 / 0 | 4 / 4 | 2 / 3 |
| confirm-5 | 3 / 4 | 0 / 0 | 3 / 1 | 0 / 0 |
| confirm-6 | 8 / 4 | 0 / 0 | 2 / 3 | 2 / 2 |
| **total** | **36 / 24** | **0 / 3** | **15 / 20** | **10 / 15** |

## Cache reuse in the new sessions

| instance | first-request read | ordinary calls reading the previous marker (share) | new-turn starts reading the previous marker (share) | after an edit: attempts (share) | boundary check: exact / fallback / mismatches |
| --- | --- | --- | --- | --- | --- |
| confirm-1 | 0 | 21 / 21 (0.750) | 7 / 7 (0.933) | 7 (0.633) | 35 / 0 / 0 |
| confirm-2 | 0 | 19 / 19 (0.764) | 7 / 7 (0.949) | 9 (0.719) | 34 / 1 / 0 |
| confirm-3 | 0 | 20 / 20 (0.721) | 7 / 7 (0.919) | 6 (0.354) | 33 / 0 / 0 |
| confirm-4 | 0 | 17 / 17 (0.760) | 7 / 7 (0.945) | 3 (0.325) | 27 / 0 / 0 |
| confirm-5 | 0 | 15 / 15 (0.775) | 7 / 7 (0.960) | 3 (0.744) | 25 / 0 / 0 |
| confirm-6 | 0 | 30 / 30 (0.812) | 7 / 7 (0.951) | 8 (0.595) | 45 / 0 / 0 |

- **Observed (provider-reported usage):**
  - **within turns:** all 122 ordinary calls read exactly the previous request's prefix;
  - **at new-turn starts:** all 42 did;
  - **after an accepted edit:** reuse fell back to an earlier marker: 4 of 36 times to the first request's head, once to the tools and system prompt, otherwise to a later marker;
  - **across sessions:** no first request read anything.
- **The boundary check** combines two kinds of evidence. Reconstructed request evidence (the working-context entries of each recorded request) predicts which earlier prefix is eligible; provider-reported usage is checked against it.
  - **199 of 200 matched exactly.**
  - **The one fallback:** confirm-2 attempt 30, after an edit, with more than 19 entries beyond the head. It read 2,284 tokens, below the head's 2,362. That is consistent with the tools and system prompt, whose size this layout doesn't show.
  - **Assumptions:** the documented exact-prefix rule, the 20-block lookback and the lifetime, which held (48 s at most between attempts).

## Cost and work

- **Against confirm1's guarded sessions:** −US$3.152 in all (−49%). Every instance was cheaper, from −US$0.02 (confirm-6) to −US$0.85 (confirm-2).
  - **Input:** billed at US$2.30. Billed the way the original configuration bills (the tools and system prompt read, everything else written), the same input would have cost an estimated US$7.12. That estimate takes the tools-and-system prefix as each session's first cached head minus 80 tokens, as in dev-cache1.
  - **Output:** the new sessions produced 23% more (US$0.95 against US$0.77).
  - **Work:** 30 more attempts, 13 more task calls, 25% more input and 12 more accepted edits.
  - **Inferred, not established:** the saving on input is far larger than the extra work, so the configuration's billing is very likely the main cause of the difference. How much the extra work itself comes from the new layout cannot be told apart from chance here.
- **Against confirm1's summary sessions:** +US$0.292 in all (+10%). The new sessions were cheaper on three instances (confirm-1, -4, -5) and dearer on three (confirm-2, -3, -6).
  - The summary arm did less work: 172 attempts and 2.21M input, against 206 and 3.27M.
  - confirm-6 is the clearest case: the new session made 46 attempts and read 811k tokens, against the summary session's 18 attempts and 236k.
- **Not established:** a typical saving. One pair per instance on reused instances.

## Task completion and new failure patterns

- **Completion:** all 48 turns completed in the new sessions, as in both baselines.
- **No new failure pattern:** no context, step or call limit, no truncation, no rejected edit, no provider error.
- **Scores:** 60/60, against 58 and 59; the paired differences are +1 on confirm-4 and confirm-6 against guarded-clm, and +1 on confirm-4 against the summary.
- **A difference in behaviour:**
  - the new sessions edited more (36 against 24 accepted edits) and refetched less (10 against 15), with fewer holds (15 against 20);
  - confirm-6 used markedly more steps than either baseline (46 attempts against 28 and 18);
  - whether this comes from the task being after the working context, the segmentation or chance is not determined by six sessions.

## Does it support making this configuration the default?

- **What the protocol's criteria give:** they are met.
  - the reuse held in all six sessions, with no mismatch;
  - completion and scores were not worse than confirm1's guarded sessions (all complete; 60 against 58);
  - there was no failure pattern that confirm1's guarded sessions lacked.
- **Together with dev-cache1:** the evidence supports proceeding with the library's planned default change (guarded-clm plan step 6), on these terms.
- **The limits of that support:**
  - one model and one workload family, on reused instances;
  - non-contemporaneous baselines;
  - the configuration's parts were not separated;
  - the new sessions' tendency to more steps on some instances (confirm-6) is a cost risk worth keeping in view.
- **The decision and any release are the maintainer's.** Nothing was switched or published here.

## Not exercised

Retries, rejected edits, over-limit allowances, output truncation, limit endings and the `p015-turn-endings/2` continuation. No further run is scheduled.

## Spend

- **The block:** 206 attempts, US$3.251979 confirmed from provider usage; none assumed, no reservation open. US$6.748021 of the block was left unused.
- **The ledger:** US$112.813033 spent of the unchanged US$131.657076 ceiling (US$18.844043 left).
- **Programme 015:** US$24.713287 of US$43.55733 (US$18.844043 left).
