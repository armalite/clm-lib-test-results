# 015 – Live development smoke `smoke-dev2`: record (COMPLETE: three sessions, each run once)

_Run 2026-10-19 (UTC). **A compatibility smoke, not a performance comparison.** One eight-turn session per arm on
`docthread-dev-1`. It replaces the closed [`smoke-dev1`](smoke-dev1-record.md) under the corrected harness. The plan
is in [protocol-draft.md](protocol-draft.md) (the successor-smoke note)._

## Authorisation and freeze

**Approved by the maintainer:**
- `docthread-task/2`;
- `p015-turn-endings/1` for all three arms (stop on the first incomplete turn);
- the `p015-truncation/1` rule;
- one session per arm, from clm-lib `configs/p015/smoke-dev2.json`;
- resolving smoke-dev1's operator-stopped paper session as abandoned.

**The allowance:** at most USD 13.134552 additional. That is the remainder of the original USD 15 programme allowance, which already includes the USD 1.865448 charged to smoke-dev1.
- **No ceiling change** was made, and none was authorised.
- **The authorisation** (clm-lib `runs/p015-smoke-dev2-authorisation.json`, local) sets a programme ceiling of 15.0 and a block stop of 13.134552. At launch, the programme gate, the block stop and the ledger all allowed exactly $13.134552.

**Not authorised:** continuation (`p015-turn-endings/2`), arm repairs, guarded-clm changes, confirmation runs, additional instances and further replacement sessions.

**Frozen before the first call** ([smoke-dev2-freeze-record.json](smoke-dev2-freeze-record.json)):
- **the contract:** sha256 `b419c3af…`;
- **clean revisions:** clm-lib `414789a`, clm-lib-test-results `faf06e3a`, guarded-clm `cce58c1`;
  - guarded-clm `cce58c1` is `3f18473` plus a README link: `git diff 3f18473 cce58c1 -- src` is empty;
  - its source sha256 is `51e6dbe8…`, the accepted 0.2.0.dev1;
- **the dependencies:** pydantic-ai-slim 2.27.1, anthropic 0.125.0, Python 3.13.15;
- **the price:** `claude-sonnet-5` at $2 / $2.50 / $4 / $0.20 / $10 per million tokens. `prices.toml` is unchanged since smoke-dev1, and the price was not rechecked online;
- **the sandbox:** Docker 20.10.13, image `python:3.12-slim` (local);
- **the order:** guarded-clm, `paper_clm_shell`, `token_tail_p015`.

**The credential:** the documented local API key, loaded with tracing disabled only in the launching command. The SDK reported that it took precedence over any discovered profile.

**smoke-dev1, before launch:** s02 was resolved `abandoned`, on the maintainer's approval. That changed its status file only: its contract, STOP state, export and charges are unchanged.

## What happened

**Launch:** 05:51:10 to 05:56:36 UTC, exit 0.

| Session | Ending | Wall time | Main-model calls | Attempts (failed / retried) | Score | Recall | Confirmed cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s01 guarded-clm | 8 turns completed (`complete`) | 118 s | 27 | 27 (0 / 0) | 10/10 | 3/3 | $1.024310 |
| s02 `paper_clm_shell` | `context_limit` in turn 4 (`arm_failure`) | 100 s | 20 | 20 (0 / 0) | 4/10 | 0/3 | $0.222977 |
| s03 `token_tail_p015` | 8 turns completed (`complete`) | 108 s | 23 (plus 3 summariser calls) | 26 (0 / 0) | 9/10 | 3/3 | $0.444595 |
| **block total** | | | | **73 (0 / 0)** | | | **$1.691882** |

**Charges:**
- **all confirmed:** $1.691882 at provider-reported usage;
- **charged at reservation:** $0;
- **pending reservations:** none;
- **uncertain attempts:** none.

**The programme now stands at $3.557330 of $15:** smoke-dev1 $1.865448, smoke-dev2 $1.691882. The ledger is at 91.657076 spent under the 103.099746 ceiling, leaving $11.44267, which is not permission for further work.

**No step limit, call cap, summariser cap or output-limit truncation occurred.** Every stop reason was `tool_use` or `end_turn`.

**The paper arm's session stopped at its context limit** in turn 4, under the common stop-on-first-incomplete-turn policy. That policy differs from a design that would continue to the next turn. Turns 5–8 never ran, and nothing is inferred about how they would have scored.

## The cross-turn connection failure did not recur

smoke-dev1 failed the first attempt of every turn after the first. This time, all 73 attempts succeeded on their first try: no connection error and no retry, across the 20 user turns attempted (19 completed, of 24 planned) in three sessions (corrected 2026-10-19; see the clarifications below), each on one event loop (`p015-session-loop/1`).

## Answers (descriptive)

**guarded-clm, 10/10:** every value correct, in the clarified form.
- **The ids** were bare: `CHG-24924`, `CHG-61023`, `P-3.3`.
- **The quote** was the cause line, copied exactly (seq 255185).
- **Recall:** the turn-5 change id was already in the turn-2 reply, and the change log was also read again; the turn-8 wait was found by reading the queue statistics again; the turn-7 job id was already in the turn-1 reply.

**`token_tail_p015`, 9/10:** every value correct except the quote, which scored `not_a_journal_line`.
- **What it quoted:** the right cause line (seq 255185, with the setting and its value), but with the journal's column padding collapsed (`diagnostic | processing…` for `diagnostic     | processing…`), so it is not a substring of the real line.
- **The padded line was in its request,** including in the third summary, which preserved it. The model normalised the spacing when copying.
- **So this is an exact-format miss:** the fact was found, and the clarified instruction ("copied exactly") did not prevent it. The scorer is unchanged.

**`paper_clm_shell`, 4/10:** turns 1–3 were correct (four values). Turn 4 ended at the context limit, so its quote and the six values of turns 5–8 are unanswered under the fixed denominator.

## Context management and exposure

| | guarded-clm | `paper_clm_shell` | `token_tail_p015` |
| --- | --- | --- | --- |
| evidence read (characters delivered) | 122,436 in 36 tool calls | 56,866 in 21 | 111,341 in 34 |
| journal pages read | 18 (13 distinct; 5 again) | 8 | 16 (12 distinct) |
| repeated tool calls | 7 | 0 | 6 |
| peak reported main-model input | 24,422 (76% of 32,000) | 29,806 (93%) | 20,685 (65%) |
| notices | PRESSURE in 2 requests | context notices in 8 requests | pressure in 3 requests |
| management | 4 edits, all accepted; 1 output held back, then refetched | 1 edit rejected, none applied; 6 rollbacks; 1 over-limit request; `context_limit` | 3 summaries applied (3 summariser calls) |

**The clarified quote question changed exposure.** In turn 4, guarded-clm made 15 reads and the summary arm 13, reading on to the cause line on page 12. smoke-dev1's guarded session read 33,482 characters in total; this one read 122,436, more than the scripted plan's 106,581. So the light exposure seen in smoke-dev1 came largely from the ambiguous question. This is one session per arm, on one development instance.

**guarded-clm:**
- **One held-back output:** page 6 needed about 4,529 tokens with 3,951 free.
- **Edits:** the model then deleted earlier steps and read the page again, and later edits removed further steps.
- **The library worked as specified,** with no over-limit request.

**`paper_clm_shell`, the turn-4 failure, step by step (arm result, documented rules; not a harness defect):**
1. Turns 1–3 made no edits.
2. In turn 4, the conversation history reached about 28,000 tokens.
3. The model's first edit command (a Python script carrying its own summaries of the earlier tool results) rewrote those results as plain text, without the mirror's result-section format. The arm's validator rejected it: "a tool block must hold only result sections".
4. That step itself took the request over the 29,952-token limit, so the last-step rollback removed it, including the result that explained the rejection. The model saw only "your last 1 step(s) were rolled back".
5. Its next commands only inspected the mirror. Four outputs pushed the request over the limit and were rolled back; the fifth came after the six rollbacks were used, so it became the one permitted over-limit request; a sixth inspection then ended the turn (corrected 2026-10-19; see the clarifications below).
6. The six rollbacks were: the turn's two-page read, the rejected edit's step, and four inspections.

All of this is the arm's implemented and approved provisional behaviour. It is a fidelity finding to review before any comparison: near the limit, last-step rollback can remove both an edit's rejection reason and any inspection output, leaving the model nothing to act on. No edit was ever applied in this session.

**`token_tail_p015`:**
- **Summaries:** three, at the pressure threshold, each accepted on its first attempt. No summariser retry or cap was reached.
- **What summaries kept:** the third preserved the cause line verbatim. Recall stayed at 3/3, with two values found by reading again.

## Usage, caching and time

| | input (total) | cache reads | cache writes | uncached | output | of which thinking |
| --- | --- | --- | --- | --- | --- | --- |
| guarded-clm | 426,180 | 59,722 | 366,431 | 27 | 9,624 | 4,810 |
| `paper_clm_shell` | 410,704 | 379,137 | 31,527 | 40 | 6,825 | 2,678 |
| `token_tail_p015` (main and summariser) | 288,828 | 162,638 | 126,138 | 52 | 9,662 | 2,324 |

**Caching:**
- **guarded-clm** rebuilds each request, so most of its input was written to the cache, at the 1.25× rate.
- **The paper arm's** append-only history was mostly read from it.
- **The summary arm** is in between: each summary rewrites the request's prefix.

**Latency:** at most about 13 s per call (21 s for one summary-arm call). The provider-call time was 114 s, 80 s and 105 s respectively.

## Exports

[smoke-dev2-export/](smoke-dev2-export/), made with the launcher's export.
- **Verification:** all three runs verify (`verify_export`), and the top-level `SHA256SUMS` checks.
- **The scans** found no credential or local path.

## Clarifications (dated 2026-10-19, after the paper-arm fidelity review)

**The scores are unchanged.** The review is [paper-arm-smoke-dev2-review.md](paper-arm-smoke-dev2-review.md).

**Turn counts:** 24 turns were planned, 20 attempted (8, 4 and 8) and 19 completed (8, 3 and 8). The 73 attempts were made in the 20 attempted turns; the earlier text here said "across 24 user turns".

**The paper arm's turn 4, after the rejected edit:** the model ran six inspection commands, not five rolled back.
- **Four were rolled back** (rollbacks 3 to 6).
- **The fifth** came after the allowance was used, and became the one permitted over-limit request.
- **The sixth** ran on that request; the next request (32,272 tokens) ended the turn.

**What the model saw:** the rejected edit's receipt (`edit rejected, nothing changed: a tool block must hold only result sections`) was in the command's result, which rollback 2 removed, so the model was never shown the reason.

**Exact form, separately from correctness:** guarded-clm 10 of 10 values correct and 10 in the exact form; the summary arm 10 correct and 9 in the exact form (the quote's spacing); the paper arm 4 answered, 4 correct, 4 exact, and 6 unanswered.

## Limitations

- **One session per arm on one development instance.** These are compatibility results, not evidence that any arm is better.
- **The paper arm's score reflects** its turn-4 stop under the common stop policy; its later turns did not run.
- **The summary arm's quote miss** depends on the scorer's exact-substring rule for whitespace, which is unchanged by design.
- **The price was not rechecked** online in this session.

## Recommended next step (not authorised)

Review the paper arm's turn-4 behaviour (rollback removing an edit's rejection reason near the limit) as a fidelity question, before any confirmation design is frozen. Nothing further runs without a new decision and authorisation.
