# 015 – `supp-cache1`: supplemental evaluation of guarded-clm's recommended caching configuration on confirm1's instances (protocol)

_Pre-registered 2026-10-23, before any dispatch. Results go in a separate `supp-cache1-record.md` after the run. This protocol is not edited after launch; its sha256 is in the freeze record._

## What this is, and what it is not

- **A later, supplemental evaluation** of guarded-clm 0.2.0.dev2 in the recommended configuration, dev-cache1 B, one session on each of confirm1's six frozen instances. It is not part of confirm1, and its results are reported apart from confirm1 and from every development run.
- **The instances were already used** in confirm1 ([confirm1-record.md](confirm1-record.md)). They are taken unchanged from its frozen manifest ([confirm1-instance-manifest.json](confirm1-instance-manifest.json), sha256 `86799fab…7b82`): docthread-confirm-1 … 6, seeds 7407, 7402, 7403, 7404, 7405, 7496. They are not regenerated as new instances, replaced or selected. The launcher generates each fixture from its seed, and all six reproduce the manifest's recorded `outputs_sha256` (checked before launch).
- **The configuration combines several changes.** Against confirm1's guarded sessions it changes the library revision (0.2.0.dev1 to 0.2.0.dev2), the request layout (segmented, with the task after the working context), the context cache marker and the host caching (no automatic last-block caching). It is not an ablation of any one of them.
- **The baselines are reused and not contemporaneous.** confirm1's guarded-clm and summary sessions ran on 2026-10-19/20 with the then-current harness and library. They are not rerun.
- **What may differ for reasons other than caching:** the model's behaviour on a differently ordered request, provider-side variation between dates, and chance. **No difference is attributed exclusively to caching.**
- **The development history:** the configuration was checked on docthread-dev-1 only ([dev-cache1-record.md](dev-cache1-record.md)), not on these instances.

## The configuration, frozen

**dev-cache1 B exactly**, from `configs/p015/proposed-cache-dev1-b.json` at clm-lib 2200f8b (unchanged since 8fcec77):

| Setting | Value |
| --- | --- |
| guarded-clm | 0.2.0.dev2, revision `d1d6d1dd6040b526c50b491979771b75abe3d19e`, source `5da9751503c8fab143ba5400e9e416422404fce868554c68f7f3c8a531823f07` |
| `request_layout` | `segmented_task_last` |
| `cache_point` | `5m` |
| host caching | tool-definition and instruction breakpoints (5m); no automatic or last-message caching |
| guarded settings | budget 32,000, 60 task steps, 144 calls per turn |
| model | claude-sonnet-5, adaptive thinking, effort high, `max_tokens` 8,192, at most 2 retries per logical call (`p015-retry/1`) |
| task and endings | `docthread-task/2`, eight questions, `p015-turn-endings/1`, `p015-truncation/1` |

**The launch specification** (`runs/p015/supp-cache1-spec.json`, copied to `supp-cache1-spec.json`, sha256 `4d82a40a…2193`) is that configuration with only the launch id (`supp-cache1`), authorisation path, instances, note and settings status changed. The library default is unchanged.

## Order and cache isolation (predeclared)

- **Order:** confirm1's instance order, 1 to 6. Session ids `s01-docthread-confirm-1-guarded_clm` … `s06-docthread-confirm-6-guarded_clm`, run ids `supp-cache1.sNN-…r1`.
- **One session at a time:** each session is dispatched by its own `run --max-sessions 1`, no sooner than 390 s after the previous session's last ledger entry (dev-cache1's procedure).
  - **Why:** the tool definitions precede each session's `run-ref` tag, so their cache entry is shared across sessions; the gap lets the 5-minute entry expire.
  - **Recorded, not assumed:** each session's first-request cache read is recorded. Any non-zero read is reported as shared-prefix reuse.
- **No reruns, replacements or repeats.**
- **Stopping:**
  - before the next session, a check stops the block for review on a harness defect, a session left uncertain or interrupted, an open reservation, or a provider compatibility error (an HTTP 4xx other than 429);
  - task endings (context, step or call limits, output truncation) and spending endings are recorded outcomes, and the block continues while the allowance permits;
  - `stop --now` is used only for those defects or the spending bounds.

## Measurements (all kept, whatever they show)

Produced by the predeclared [supp-cache1-analysis.py](supp-cache1-analysis.py) (sha256 `4101840709d44cbca65ef61ee41dec555179db7e0b459f4f6bc171fba56b448c`). It reuses the committed `dev-cache1-analysis.py` (sha256 `28cde995…4210`) for request parsing and attempt classes.

**Per instance, for the new session and for confirm1's guarded-clm and summary sessions:**
- score, recall, completed turns, outcome and endings;
- confirmed and assumed cost;
- summed model latency (wall-clock time for the new sessions from the launcher's events);
- attempts (main and summariser) and task tool calls;
- input and output tokens;
- cache reads, writes and uncached input;
- for guarded sessions: accepted and rejected edits, held-back outputs and refetches.

**For the new sessions, the cache evidence:**
- **reuse within turns and at new-turn starts:** the number of ordinary and turn-start attempts whose reported read equals the previous attempt's read plus written tokens, and the read share of each class;
- **after accepted edits:** the attempts after each edit took effect, and their read share;
- **shared-prefix reuse across sessions:** each session's first-request read;
- **the boundary check, specified prospectively** (dev-cache1's post-hoc method; full rule in the script's docstring):
  - *the evidence:* reconstructed request evidence (the working-context entry lines of the request each attempt recorded, as built by the harness and passed to the adapter, not the HTTP body) checked against provider-reported usage (the only token figures);
  - *the assumptions:* the documented exact-prefix rule, the 20-block lookback (at most 19 more entries than the earlier marker), and the 5-minute lifetime within a session, checked against ledger timestamps;
  - *the fallback:* where no marker is in reach, the prediction is the tools-and-system prefix. Its size is not observable in this layout, so such attempts are checked for consistency (a positive read below the first request's cached head), not for equality;
  - *reported:* exact matches, consistent fallbacks and mismatches, per session.

**Untested paths are reported as untested.** Edits, holds, retries, PRESSURE and limits are the model's and the provider's doing; none is forced.

## Interpretation (predeclared)

- **The cache reuse expected from dev-cache1 holds** if, in every completed session, ordinary and turn-start attempts read the previous marker, and the boundary check shows no mismatch. Any mismatch is reported with its figures, and the expectation is then not met for that session.
- **Task results:** scores, recall, completed turns and endings are reported per instance beside confirm1's guarded and summary results, with paired differences. No score is required and no threshold applies. Six sessions on reused instances support a description, not a significance claim.
- **Cost:** per-instance and total confirmed costs, with the work performed (attempts, tool calls, input and output tokens). A cost difference is not attributed to caching alone, because the work differs between sessions.
- **The library default:**
  - **Supports a default change:** the reuse holds in all six, and completion and scores are not materially worse than confirm1's guarded sessions. "Not materially worse" is judged descriptively: no new failure pattern, and a total within a few points.
  - **Doesn't:** a failure pattern that confirm1's guarded sessions lacked, or reuse that does not hold.
  - **Either way,** the decision and any release are the maintainer's, outside this block.

## Spending (authorised 2026-10-23)

- **Authorised:** exactly six sessions, a US$10.00 block stop, within the existing programme (US$43.55733) and ledger (US$131.657076) ceilings; no ceiling increase.
- **What the block counts:** confirmed provider-usage charges, charges assumed at the reservation for uncertain outcomes, and open reservations (`p015-spend/1`). Retries are reserved and charged like any attempt.
- **Expected:** about US$2.5–6 in all. dev-cache1 B cost US$0.61 on docthread-dev-1, and confirm1's guarded sessions on these instances cost US$0.81–1.44 each under the original configuration.
