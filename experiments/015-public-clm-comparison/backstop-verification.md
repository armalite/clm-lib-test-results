# 015 – guarded-clm 0.2.0.dev1 (always-on implausible-ratio backstop): offline integration verification

_Written 2026-10-16. **Offline and scripted only. There are no live results.** This is the integration verification
for the accepted library implementation. It is kept apart from:
- the strict-learning verification of the superseded `db619a8` ([strict-ratio-verification.md](strict-ratio-verification.md));
- the earlier verification against guarded-clm 0.1.0 ([docthread-workload.md](docthread-workload.md), [arms-offline.md](arms-offline.md))._

## The accepted implementation

| Item | Value |
| --- | --- |
| guarded-clm revision | `3f184734362c4c9e24d7f5e2a2d6de5fa18153dd`, "Make the implausible-ratio backstop always on, remove strict_ratio_learning (0.2.0.dev1)" |
| version | `0.2.0.dev1`, in both the distribution and the module |
| source fingerprint (`library_provenance()`) | `51e6dbe8df7669ff8265d725976260f61891b6624d9c2201c7edc83dfcf2d9e4` |
| checkout | clean; read-only throughout this work |
| how clm-lib uses it | imported from the sibling checkout (editable) in clm-lib's p015 environment. `uv.lock` records 0.2.0.dev1, a one-line change since the last commit. The revision and fingerprint are stated in the successor configuration, and `plan` checks them against the loaded library |
| trace variant label | unchanged (`clm_lite_v3_3`); the implementation is identified by its version, revision and fingerprint |

## The change, from the source

- **`strict_ratio_learning` is gone** from `clm_context()` and `ClmContext`.
- **The shared estimator now always ignores** a new-text observation below 0.5 characters per token. That observation no longer lowers the new-text ratio.
- **An observation of exactly 0.5 still counts** (the condition is `observed >= 0.5`).
- **The other learning rules are as before:**
  - only requests no smaller than the last are learnt from;
  - an addition of fewer than 200 tokens is ignored;
  - the ratio only moves down;
  - the overall ratio and the anchor are updated as before.
- **The guard is unchanged:** its own ratio, which learns only from requests that extend the last answered one, and its conservative fit formula. Against guarded-clm 0.1.0 (`775a163`), `capability.py` is identical; only `estimate.py` (the backstop) and the version changed.

**Not neutral in general:** a request that would have taught a ratio below 0.5 is now estimated differently, and the limit and guard decisions that depend on that estimate can change. It does not make token counting accurate.

## The integration change in clm-lib

- **Removed:** the `strict_ratio_learning` field of the guarded arm's settings, and the argument passed to `clm_context()`.
- **Refused with a migration error:** any spec or contract that names `strict_ratio_learning`, whatever its value, at `plan` and in the contract check. Nothing is ignored or translated.
- **The superseded configuration** is kept byte-identical (sha256 `e76f7cb9…`) as `configs/p015/superseded/proposed-comparison-strict-db619a8.json`, with a README. The launcher refuses it.
- **Its exact inputs** (that configuration, the strict-learning test file, the live-spec test file and the integration diff) are preserved with that verification's local evidence, with checksums and provenance.
- **The successor configuration:** `configs/p015/proposed-comparison-0.2.0.dev1.json`. It has no removed option, and it pins the library (version, revision, source fingerprint).
- **Live plans that include guarded-clm** must state that pin. Any plan that states one is refused if the loaded library differs, or if it has uncommitted changes.
- **Kept from earlier chunks:** explicit live settings, the separate spending authorisation, immutable contracts, fingerprint checks and restart protections.
- **Old contracts** made against `db619a8` are refused, because the fingerprints differ (tested). Nothing old was rewritten or resumed.
- **Unchanged:** the paper and summary arms, the workload, the scorer and the model settings.

## Checks (network blocked; provider-like reported usage where calibration matters)

| Check | Result |
| --- | --- |
| the accepted revision is loaded (version, revision, clean); the option is absent from `clm_context()`, `ClmContext` and `GuardedSettings`; the capability builds without it | pass |
| **the library's backstop boundary** (its own `Calibration`): an observation of 500 characters at 1,000 tokens (0.5) lowers the new-text ratio to 0.5; at 1,001 tokens (just below 0.5) it does not; the overall ratio updates either way | pass |
| **the edit-and-read regression** (the guarded-clm regression shape: a read, then one response that deletes it and reads about as much while reported input rises, then a large read) | direct library and `GuardedSession` transcripts are identical; the run completes with the edit accepted and no over-limit or context-limit record; the new-text ratio stays above 2.0 (the later plausible append is learnt from) |
| **ordinary append-only learning** | identical transcripts; the ratio learns from provider-like usage (between 0.5 and 2.5) |
| **an edit-containing request with a plausible observation** (a delete, while the same response reads 6,000 characters) | identical transcripts; the edit is accepted; the ratio learns (between 0.5 and 2.5) |
| **the existing direct-versus-session cases** (11, including guard bursts, pressure and recovery re-arming, retained protected answers, the step and call limits, and tool and provider failures) | identical transcripts |
| **guarded-clm's 32 stored scenarios through clm-lib's accounting wrapper,** against this revision's stored transcripts | all match |
| an obsolete `strict_ratio_learning` (True or False) | refused, with the migration message; nothing written |
| the superseded configuration | refused, pointing to the successor |
| a pin with a different revision or version | refused; nothing written |
| version, revision and fingerprint | recorded in the contract (pin and fingerprints), `session.json` provenance and the export manifest; `verify_export` clean |
| a contract as made against `db619a8`, with the removed option | refused (`guarded_clm_source_sha256` fingerprint, and the obsolete setting); nothing dispatched |
| live settings and spending gates | an incomplete live plan is refused before anything is written; the live authorisation gate is unchanged (`test_live_spec.py`) |

### The re-recorded `over_budget_ignored` transcript

**The library re-recorded one stored transcript.** Comparing its `db619a8` and `3f18473` versions field by field:

| Part | Changed? |
| --- | --- |
| requests to the model (every call, with its messages, instructions, tools and usage) | **no** |
| record types and order (guard checks, the held-back output, the context limit) | **no**: the same guard decisions |
| ending | **no**: still `ContextLimitError`, "over the budget itself" |
| estimate figures | **yes**: |

**The estimate figures that changed:**
- the guard checks' shared base, 42,668 → 42,468;
- their projections, 42,818 / 42,778 → 42,618 / 42,578;
- the held-back record's shared estimate, 109,268 → 42,602, and its conservative estimate, 42,818 → 42,618;
- the context limit's estimate, 95,668 → 42,574, also shown in the error text.

**What the hosted check shows:** clm-lib's hosted scenario check matches the new stored transcript. No historical experiment export was modified.

## docthread compatibility (scripted)

**What was run:** guarded-clm on both development instances, with the scripted `tidy` and `keep` policies, synthetic and fixed usage: 8 sessions, all exported and verified. The raw records are in clm-lib, in the ignored `runs/backstop-2026-10-16/`.

**Results:**
- **Every session matches the corresponding earlier `db619a8` record with strict learning off**, after removing timestamps and run ids: the same requests, traces, tool results and turns.
- **The headline figures are therefore unchanged:** 10/10, peak estimates of 6,220, 4,544, 27,236 and 25,034 (dev-1) and 6,172, 4,508, 27,253 and 26,598 (dev-2), and the same pressure and hold counts.

**What this shows:** the scripted usage never produces an observation below 0.5, so the backstop never acts here. That shows compatibility, not neutrality under real usage.

## Limitations

- **Usage is synthetic or provider-like only.** How often real usage produces implausible observations is unknown until a separately authorised development smoke.
- **guarded-clm's own test suite** was not run here. The library records its own results, and this verification relies on its stored transcripts through clm-lib.
- **This selects the library implementation only.** It does not freeze the live protocol or authorise a smoke.
