# 015 – `dev-cache1`: guarded-clm's original and recommended caching configurations (protocol)

_Prepared 2026-10-23, offline. **Proposed, not authorised, not run.** Results go in a separate `dev-cache1-record.md` after the run; this protocol is not edited after launch, and its sha256 goes in the freeze record. Readiness: [dev-cache1-readiness.md](dev-cache1-readiness.md)._

## What this is, and what it is not

- **A development check** of two complete guarded-clm configurations on one development instance, one session each. It asks whether the recommended configuration's cached prefixes are actually read by the provider within and across user turns, at what cost, and whether the session behaves comparably.
- **It compares complete configurations.** B changes the request layout (one block versus one block per entry), the order (the task after the working context), the context cache marker and the message-level breakpoint together. No difference is attributed to any one of them.
- **One session per configuration** on docthread-dev-1. That supports a mechanism check (does reuse happen where the documented rules say it can?), not a performance claim. Score, completion and cost differences of one session each are reported, not generalised.
- **Not part of confirm1** or any comparison of arms, and not an evaluation of guarded-clm against other implementations.
- **Offline eligibility is not evidence of a hit.** The offline checks (clm-lib SPEC §41) show which prefixes the configurations make eligible; only the provider's reported usage shows what was read.

## The configurations

Both use guarded-clm **0.2.0.dev2, revision `d1d6d1dd6040b526c50b491979771b75abe3d19e`, source fingerprint `5da9751503c8fab143ba5400e9e416422404fce868554c68f7f3c8a531823f07`**, and confirm1's shared settings: claude-sonnet-5, adaptive thinking, effort high, `max_tokens` 8,192, at most 2 retries per logical call (`p015-retry/1`), budget 32,000 with 60 task steps and 144 calls per turn, `docthread-task/2`, `p015-turn-endings/1` (the first incomplete turn ends the session), `p015-truncation/1`, eight questions, a session-specific `run-ref` line.

| | A (original) | B (recommended) |
| --- | --- | --- |
| clm-lib file | `configs/p015/proposed-cache-dev1-a.json` | `configs/p015/proposed-cache-dev1-b.json` |
| launch id | `dev-cache1-a` | `dev-cache1-b` |
| `request_layout` | `single` | `segmented_task_last` |
| `cache_point` | none | `5m` |
| message-level caching | automatic (`anthropic_cache`, 5m) | none |
| tool-definition breakpoint | 5m | 5m |
| instruction breakpoint | 5m | 5m |
| breakpoints per request | 3 (tools, system, last block) | 3 (tools, system, last entry) |

- **A is confirm1's guarded configuration** with the library defaults stated explicitly. Its `clm_context()` arguments and model settings equal confirm1's guarded sessions'.
- **B is the library's recommendation** (guarded-clm decisions P11): the stable working context ends at the cache marker; the task and runtime status follow it unmarked, so nothing is written at the changing tail.
- **Nothing else differs.** The library defaults are unchanged; both sessions select their layout explicitly.
- **Why two launches:** the cache breakpoints belong to the model configuration, which a contract shares across its sessions. Each launch has one session and its own authorisation and block, so neither can consume the other's allowance.

## Order and separation (predeclared)

1. **A runs first.**
2. **B starts no sooner than 6 minutes after A's last attempt finished.** The tool definitions come before the session's `run-ref` line, so their cache entry is not session-specific. The gap lets A's 5-minute entry expire, so B's first request cannot read it.
3. **No reruns, replacements or reordering.** A failed or exhausted session is reported as it is. Session identifiers: `dev-cache1-a.s01-docthread-dev-1-guarded_clm.r1` and `dev-cache1-b.s01-docthread-dev-1-guarded_clm.r1`.
4. **Stopping:** `stop --now` only for a concrete harness defect, a provider incompatibility (an HTTP 400 on a request the configuration produced), or the spending bounds; never for results. B still runs after an A that ended early, unless the cause is a defect that also affects B.

## Measurements (all kept, whatever they show)

Per session:
- **provider acceptance:** attempts, outcomes, HTTP errors and retries;
- **per call:** the provider-reported cache reads, cache writes, uncached input and output tokens, and the charge;
- **the class of each call**, from its recorded request (the predeclared [dev-cache1-analysis.py](dev-cache1-analysis.py), sha256 `28cde9953e045e9fcdc06e6a7fc1e4c05c66243e0fb35939d9e8374184864210`):
  - `first`: the session's first request;
  - `ordinary`: the same task, the previous entries a prefix of this request's;
  - `turn_start`: the task section changed (a new user turn);
  - `after_change`: the same task, but earlier entries changed or went (an accepted edit took effect);
  - `retry`;
- **reuse by class:** the read share (reads over total input) for ordinary calls and for new-turn starts, and the reads on the call after each accepted edit;
- **the session:** score (points and recall points), completed turns and endings, PRESSURE requests and over-limit records, accepted and rejected edits, calls, summed latency, and total confirmed cost.

**Untested paths are reported as untested.** Whether edits happen is the model's choice; edits are not forced or prompted. If a session makes no accepted edit, invalidation after edits is not exercised in it. Likewise for retries, PRESSURE and over-limit allowances.

## Interpretation (predeclared)

- **Reuse within turns is demonstrated** for B if B's ordinary calls report cache reads clearly beyond the tools-and-system prefix, i.e. beyond what A's ordinary calls read. **Reuse across turns is demonstrated** if B's new-turn starts do the same. Otherwise each is reported as not demonstrated, with the per-call figures.
- **A's expected pattern** (from the 2026-10-22 caching review) is reads of the tools-and-system prefix only. A departure is reported, not explained away.
- **After an accepted edit,** B is expected to fall back to an earlier boundary (often only the first request's head). How far it falls back is reported per edit.
- **Cost:** both sessions' confirmed costs, and B's minus A's, are reported. With one session each, a cost difference is not separated from differences in what the model did (calls, edits, turns completed).
- **Task behaviour:** scores, endings and the number of calls are reported side by side. No score is required, and none is treated as a pass or failure of the configuration. A change in behaviour may come from the task being after the working context, from the segmentation or from chance; this design cannot tell them apart.
- **What would follow:** if reuse is demonstrated in both directions and B's session behaves comparably, the library may proceed toward its planned default change (guarded-clm plan step 6), with any wider confirmation planned separately. If not, the record says which part failed, and the default stays.

## Spending (proposed; not authorised)

- **Expected:** about US$0.8–1.5 for A (the reference guarded session on this instance and task, in smoke-dev2, cost US$1.024; the seven guarded sessions on task version 2 cost US$0.81–1.44). About US$0.35–1.6 for B, depending on what is actually read.
- **Proposed hard allowance:** a block stop of **US$2.50 per launch, US$5.00 in all**, within the existing programme ceiling (US$43.55733; US$19.7179 spent, so US$23.84 left) and the ledger ceiling (US$131.657076; US$107.817646 spent). No ceiling change is needed.
- **Nothing is authorised by this protocol.** Each launch needs the maintainer's authorisation file naming its launch id.
