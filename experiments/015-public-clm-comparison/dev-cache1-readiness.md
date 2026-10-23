# 015 – `dev-cache1` readiness (offline)

_2026-10-23. Offline only: no provider or token-counting calls, no spend, no authorisation, no ledger change. Protocol: [dev-cache1-protocol.md](dev-cache1-protocol.md)._

## Status

**Ready to authorise, once the maintainer has committed the clm-lib integration.** The launch contract fingerprints the clm-lib source, so planning should happen after that commit, from a clean checkout.

## The library pin

| | |
| --- | --- |
| package | guarded-clm 0.2.0.dev2 (editable, sibling checkout) |
| revision | `d1d6d1dd6040b526c50b491979771b75abe3d19e`, clean |
| source fingerprint | `5da9751503c8fab143ba5400e9e416422404fce868554c68f7f3c8a531823f07` |
| what it adds | the opt-in `segmented` and `segmented_task_last` layouts, a context cache point, and message origin by `ModelRequest.metadata` (its decisions P8 to P12); default unchanged (`single`) |
| installed metadata | 0.2.0.dev2 after re-syncing `.venv-p015` (it still said 0.2.0.dev1, a stale editable install). Only that package changed |

## The harness integration (clm-lib SPEC §41, uncommitted at the time of writing)

- `request_layout` and `cache_point` are passed from the guarded arm's settings to `clm_context()`.
- Invalid combinations are refused at planning and before dispatch.
- Live plans must state both options.
- The resolved options are recorded in the contract (`guarded_request`), the session record and the export manifest.
- **Historical configurations are unchanged**, pinned to 0.2.0.dev1 at cce58c1, and refused against the loaded library.

## The configurations

| | file sha256 |
| --- | --- |
| A, `configs/p015/proposed-cache-dev1-a.json` | `39237859dd23c3bf201f1d43d793032039906a9643b381c17ea8eb50e60169ec` |
| B, `configs/p015/proposed-cache-dev1-b.json` | `c112d05c5760e7a31532fd841869e30b2860a694cc90e0348707088b5bcecdf6` |

Both pass the live-plan completeness, pin, version and option checks against the loaded library.

## Offline verification

clm-lib `tests/p015/test_request_layout.py`, 16 tests. Both configurations are planned and run by the real launcher in live mode, through the pinned Anthropic adapter (pydantic-ai-slim 2.27.1, anthropic 0.125.0) over an in-memory transport, with the network blocked:
- **Configurations:**
  - A and B differ only in the layout, the cache point and the automatic breakpoint;
  - A's arguments and model settings equal confirm1's guarded sessions'.
- **Refusals:** invalid combinations are refused before anything is written, and an edited contract before dispatch.
- **On the wire:**
  - A sends one block with automatic caching;
  - B sends the entries first, then the cache marker on the last entry and the task and status in an unmarked tail, with three breakpoints;
  - no origin metadata reaches the provider.
- **Eligibility** (documented prefix rules, not hits): A's only eligible prefix is tools and system. B's previous marker is eligible on ordinary calls and new-turn starts; after an accepted early edit, only the first request's head.
- **Records:**
  - turn records appear once and protected;
  - the accepted edit removes its entry, and the refused edit of a protected record changes nothing;
  - the rebuilt-request metadata is kept in every turn's recorded history in B;
  - prefixed user turns stay user turns;
  - finalize notes stay notes;
  - a step-limit continuation keeps the metadata.
- **Provenance:** contracts, session records, attempts and export manifests distinguish A from B, and both exports verify.
- **A check of the tests:** dropping the options before `clm_context()` fails five tests.
- **The analysis script** ran on exports of the scripted run and produced the per-call tables. Its figures came from the test double's emulated usage, so they are not evidence.
- **The whole suite:** the p015 suite and clm-lib's main gates pass; the counts are in clm-lib docs/results.md and the handoff.

## Remaining live uncertainties

- whether the provider reads B's context marker on ordinary calls and at new-turn starts (the lookback, the minimum cacheable length and the 5-minute lifetime all apply);
- how the provider tokenizes the separate blocks, and so the real sizes;
- whether the model behaves comparably with the task after its working context;
- whether edits occur at all, and how far reuse falls back after them;
- the cost difference, which with one session each also reflects what the model chose to do.

## To launch (not done; for the maintainer)

1. Commit the clm-lib integration; check that guarded-clm is still clean at d1d6d1d.
2. Write `runs/p015-dev-cache1-a-authorisation.json`, naming launch `dev-cache1-a` with `live: true`, the programme ceiling and a US$2.50 block stop. Do the same for B.
3. Plan A from the committed configuration into `runs/p015/dev-cache1-a`, freeze (with this protocol's sha256), and run.
4. Once A's last attempt is at least 6 minutes old, plan, freeze and run B the same way.
5. Export both and run `dev-cache1-analysis.py` on the two exports. Write `dev-cache1-record.md`.
