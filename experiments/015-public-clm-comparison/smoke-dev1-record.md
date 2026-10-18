# 015 – Live development smoke `smoke-dev1`: record (PARTIAL, stopped for a harness defect; closed, not resumed)

_Run 2026-10-18 (UTC). **A compatibility smoke, not a performance comparison.** One session per arm was planned.
One session completed, one was stopped by the operator after 3 calls, and one was not run. Plan: [smoke-plan.md](smoke-plan.md)._

## Status (updated 2026-10-19, after the offline fix)

| Session | Status |
| --- | --- |
| s01 guarded-clm | **Completed, but affected by the harness defect.** 7 of its 23 attempts failed and were retried. Its requests and answers are valid compatibility evidence; its attempt counts, latency and cost are not representative of a clean session. It is not relabelled as clean. |
| s02 `paper_clm_shell` | **Stopped by the operator; incomplete.** It is kept as recorded. Resolving it as `abandoned` is recommended, but needs the maintainer's decision. |
| s03 `token_tail_p015` | **Never ran.** |

**The launch is closed:**
- **The fix changed the clm-lib source,** so the launcher refuses this contract ("fingerprint clm_lib_source_sha256 differs from the launch contract"). The matrix must not resume against changed source.
- **The protections are kept:** the STOP file (`now`) stays in place, and the contract, fingerprints, attempts, exports and ledger entries are unchanged.
- **Charges are not reconciled downward.** The 7 failed attempts stay charged at their reservation ($1.371392) unless authoritative provider billing shows otherwise.

**The fix:** `p015-session-loop/1` (clm-lib SPEC §34), verified offline only. See [The fix](#the-fix-2026-10-19-offline) below.

## Authorisation and freeze

**The allowance:** USD 15 total for the block, approved by the maintainer.
- **Ledger ceiling:** 89.457271 → 103.099746, set from settled spend 88.099746, so earlier allowances were not reused.
- **Authorisation file:** clm-lib `runs/p015-smoke-dev1-authorisation.json` (local), with programme ceiling and block stop both 15.0.

**Frozen before the first call** ([smoke-dev1-freeze-record.json](smoke-dev1-freeze-record.json)):
- **contract:** sha256 `63bb1e86…b3ef32`;
- **clean source revisions:** clm-lib `1a9c838`, clm-lib-test-results `10969930`, guarded-clm `3f18473` (0.2.0.dev1, source `51e6dbe8…d9e4`);
- **dependencies:** pydantic-ai-slim 2.27.1, anthropic 0.125.0, Python 3.13.15;
- **the price:** `claude-sonnet-5` at $2 / $2.50 / $4 / $0.20 / $10 per million tokens;
- **the instance:** `docthread-dev-1`, seed 7301, the lease mechanism;
- **the order:** guarded-clm, `paper_clm_shell`, `token_tail_p015`.

**The credential:** the documented local API key, loaded only in the launching command. The SDK reported that this key took precedence over any discovered profile.

**The export:** [smoke-dev1-export/](smoke-dev1-export/), made with the existing launcher export. Both runs verify (`verify_export`): the s01 run is complete, and the s02 run is a partial export. The scans found no credential or local path.

## What happened

| Session | Ending | Wall time | Logical calls | Attempts (failed / retried) | Score | Confirmed cost | Charged at reservation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s01 guarded-clm | 8 turns completed | 74 s | 16 | 23 (7 / 7) | 6/10; recall 2/3 | $0.455897 | $1.371392 |
| s02 `paper_clm_shell` | `stopped` by the operator in turn 1 (the 4th attempt was refused before dispatch) | 21 s | 3 | 4 (0 / 0; 1 refused) | not scored (unfinished) | $0.038159 | $0 |
| s03 `token_tail_p015` | not started | – | – | – | – | – | – |
| **block total** | | | | | | **$0.494056** | **$1.371392** |

**Charged to the block:** $1.865448, with no reservations pending. The block has $13.134552 left of its $15.

## The harness defect

**What happened:** from turn 2 on, the first provider attempt of every user turn failed with a connection error after about 5 ms (7 of the 23 s01 attempts). Each time, the bounded retry (`p015-retry/1`) then succeeded.

**Cause (reproduced offline, without a provider):**
- the p015 runners start each user turn in a new `asyncio.run` event loop;
- the session's `AsyncAnthropic` client is built once per session;
- its kept-alive connection belongs to the previous turn's closed loop, so the next turn's first request fails with "Event loop is closed".

In the offline reproduction, the local server **received** that request before the client failed. The live failed attempts may therefore have reached the provider and been billed. Each is charged conservatively at its full reservation, recorded as an unknown outcome.

**Why the offline tests missed it:** they used scripted models or an in-memory transport, never a real connection pool.

**What was done:**
- the defect was found during s01;
- a stop after the current session was requested, then a stop before the next attempt, which ended s02 after 3 calls;
- every attempt and partial run is kept;
- **no fix was made during the smoke, and no session was rerun.**

## Compatibility and measurement (what the evidence supports)

**Provider acceptance:** for guarded-clm, every rebuilt request was accepted, with adaptive thinking (1,981 thinking tokens reported), effort `high`, and no sampling fields. The paper arm's first three requests were accepted, including several task-tool calls in one response (8 calls over 3 responses). No 4xx occurred.

**Context management (guarded-clm):**
- the peak reported input was 22,544 tokens, just past 70% of the 32,000 budget;
- one request carried the PRESSURE notice;
- one edit was accepted;
- 20 guard checks ran, with no held-back output, no over-limit request and no refetch.

**The exposure was small.** The live agent read 33,482 characters of evidence in 20 tool calls (the scripted plan for this instance: 106,581; the workload's range is about 112,000 to 126,000), with several parallel calls. So management was only lightly exercised. The paper and summary arms were not exercised.

**Estimates against reported usage (guarded-clm):** the status-line estimate was within about 5% of the reported input for most requests, and up to 10% low on a large append. It was about 20% high on the first request after the edit (8,632 estimated against 7,183 reported).

**Caching:**
- **guarded-clm:** of 263,782 input tokens, 109,078 were cache reads, 154,688 cache writes and only 16 uncached. As predicted for a layout that rebuilds every request, most of its input was written at the 1.25× rate.
- **Across sessions:** s02's first request read nothing from the cache, so no cross-session reuse was observed.

**s01's values, descriptively:**
- correct: the rejecting component and first rejection time, the rejected count, the symptom code, the first rejected job and the peak wait;
- the faulty change and the adjacent change: scored `other_evidence`. The answers held the right ids (CHG-24924, CHG-61023), but as the whole change-log entry rather than the id (corrected 2026-10-19; see below);
- the quote: a real journal line, but not the cause line (`wrong_line`);
- the procedure step: `P-3.3 (restore)` against `P-3.3`, scored `not_in_evidence`.

**This says nothing about how the arms compare.**

## Limitations

- **The block is incomplete:** only one arm finished, so the paper and summary arms' live behaviour (edits, rollbacks, summaries, the 1,000-token reserve of the summary baseline against 2,048 in the others) is not established.
- **The guarded-clm session's context pressure was light.**
- **The charges at reservation** overstate the likely real cost of the 7 failed attempts. That is the conservative rule; the real billing is unknown.

## Exposure and answer analysis (2026-10-19, from the export; the task is not changed)

**Why the guarded session read 33,482 characters against the scripted 106,581:**

| Turn | Scripted plan | Live s01 | Reading |
| --- | --- | --- | --- |
| 1 | 4 intake pages and moss-ocr pages 1–9: 82,332 | 6 queue statistics, then moss-ocr pages 1, 7, 8, 9: 29,951 | **Efficient retrieval.** It found the rejecting queue from the statistics and jumped to the first rejection (page 9). Both values were correct. |
| 2 | 7 change logs: 1,942 | the same 7: 1,942 | the same evidence |
| 3 | queue statistics: 756 | no read (answered from turn 1) | **Efficient reuse;** correct |
| 4 | moss-ocr pages 10–12, up to the cause line: 19,962 | no read | **Missed evidence:** it quoted a retry line from page 8. The only line with the cause (`worker.lease_seconds=45`, seq 255185 at 11:44:55) is on page 12, which was never read. |
| 6 | 3 playbook sections: 1,589 | the same 3: 1,589 | the same evidence |
| 5, 7, 8 | memory questions, no reads | no reads | |

- **About 52,000 of the difference is efficient retrieval:** the model navigates the journal instead of paging through it.
- **About 20,000 is missed evidence,** in turn 4.
- **The offline sizing is not representative of a searching model.** The scripted investigator reads sequentially. So the planned pressure on a 32,000-token budget was not reached: the peak input was 22,544 tokens, and the PRESSURE notice first appeared in turn 8. This is one session on one development instance, so it does not justify resizing the task. It is a fact to recheck in the corrected smoke.

**Where the wrong answers lie relative to the edit:** the single accepted edit came in turn 8 (logical call 14, the request carrying the PRESSURE notice; the next request fell from 45,006 to 14,227 characters). All four wrong values came earlier, in turns 2, 4, 5 and 6. So context management did not cause them.
- **Three are answer-form misses:** the right id was given with surrounding text (turns 2 and 5), or with an annotation (turn 6). The scorer's exact-value rule marks them wrong as designed. This is recorded, not changed.
- **One is missed evidence** (turn 4, above).
- **Recall:** 2/3. The turn-5 recall value is the turn-5 answer-form miss; the other two recall values were correct.

## The fix (2026-10-19, offline)

**Root cause:** the p015 runners ran each user turn with `asyncio.run`, which creates and closes an event loop per turn. The session's single `AsyncAnthropic` client, shared with the summary arm's summariser, kept its pooled connection bound to the previous turn's closed loop.

**The fix (`p015-session-loop/1`, clm-lib SPEC §34):**
- a session runs all its turns on one `asyncio.Runner`;
- `close()` closes the session's model clients on that loop, then the loop, and the launcher calls it however the session ends;
- a closed session refuses turns;
- pooling, retries, requests, accounting and every arm's behaviour are unchanged.

**Offline evidence:** a loopback HTTP/1.1 keep-alive server with synthetic responses; no provider and temporary ledgers only.
- **The old pattern** fails on turn 2 with "Event loop is closed", after the server received the request. This is the live symptom.
- **With the fix,** all three arms run several turns over one connection, with no failed or retried attempt; server requests equal recorded attempts.
- **Also checked:**
  - successive sessions each use their own loop and client;
  - summariser requests run on the session loop;
  - an error ending and a stop ending close cleanly;
  - request bodies equal the in-memory transport's;
  - a three-arm launch completes and its export verifies.

**Live spend for the fix:** $0.00. The ledger is unchanged.

## Next checkpoint (recommended; not launched, not authorised)

**A fresh three-arm smoke under the corrected harness,** separately identified (for example launch id `smoke-dev1b`):
- the same settings as `configs/p015/smoke-dev1.json`, with only the launch id changed, as a new configuration file;
- one eight-turn session each on `docthread-dev-1` for guarded-clm, `paper_clm_shell` and `token_tail_p015`;
- a new freeze record.

It is a replacement of the whole smoke, not a resumption of `smoke-dev1`.

**Does it fit the remaining block?**
- **The estimate:** about $2.5 to $8.5 for the three sessions ([smoke-plan.md](smoke-plan.md)). s01 cost $0.456 confirmed under light exposure.
- **The remainder:** $13.134552 of the original $15. The ledger has the same room (ceiling 103.099746 − spent 89.965194), so **no ceiling change is needed.**
- **An authorisation file for the new launch id** would state `programme_ceiling_usd` 15.0, which already counts the $1.865448 charged, and `block_stop_usd` 13.134552.
- **The remainder is not permission:** running it needs the maintainer's new, explicit approval, because the original approval excluded replacement sessions.

**Before the freeze:**
1. The maintainer reviews and commits the fix in clm-lib, and the record updates in this repository, so that both trees are clean at the freeze.
2. Run the offline checks against the committed source: `ruff`, `mypy` (both environments) and `pytest` (main and p015, including `tests/p015/test_session_loop.py`).
3. Check that guarded-clm is clean at `3f18473` (0.2.0.dev1) and that the stated pin matches.
4. `plan` the new launch into a new directory. That records the contract and fingerprints of the committed source, and the freeze record is written then.
5. Make no source edit while the launch runs.

**Decisions needed:**
1. Whether to resolve `smoke-dev1` s02 as `abandoned` (recommended).
2. Whether to approve the fresh smoke within the remaining $13.13, and its launch id.
