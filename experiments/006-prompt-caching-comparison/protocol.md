# 006 – Protocol (draft; not frozen; not implemented)

## Facts to account for (from clm-lib, as of 2026-10-05)

- **Current request layout:** a stable system prompt (mode- and task-kind-specific; about 2.6K characters in coding CLM runs), then **one** user message containing `<task>` (about 1.4K characters), `<runtime_status>` (about 0.2K characters, changing every call), then `<working_context>`.
  - Because the per-call status sits **before** the working context, at most the system prompt plus task could be cached as things stand.
  - Caching the accumulated working context needs a layout change: for example, moving the status after the context, or into a separate trailing block.
- **Minimum cacheable prefix:** the bundled API reference gives 512 tokens for `claude-opus-5-5`, flagged there as worth re-checking against current docs. The system prompt alone is above that.
- **Prices** (`configs/prices.toml`, retrieved 2026-10-04) for `claude-opus-5-5`: input USD 4, 5-minute cache write USD 5, cache read USD 0.20, output USD 20 per MTok. Accounting already prices cache reads and writes; reservations assume the highest input-side rate.
- **Invalidation:** a CLM edit or a baseline summary rewrites earlier entries, invalidating the cache from the change onward. The baseline's summary calls use a different system prompt and transcript.
- **Cross-run reuse:** runs of the same mode and task share the system prompt and task text. Within the cache TTL, a later run could read cache written by an earlier one, which would bias sequential matched pairs.

## Proposed procedure

1. **Inspect** request layouts and actual cache eligibility offline (token counts against the minimum), and decide where breakpoints go.
2. **Layout changes:** if the layout must change for caching to be meaningful, apply the same change to **all four conditions**, including caching-off controls, so that layout and caching are not confounded. Record it as a new prompt/layout version; earlier experiments keep their versions.
3. **Cross-run reuse:** decide how to handle it, for example by spacing runs beyond the TTL, adding a per-run unique prefix element, or measuring and reporting it.
4. **Calibrate** on development instances; check that cache writes and reads actually occur.
5. **Freeze,** then run matched comparisons with alternating order. All runs are reported.

## Unresolved decisions

- The task family and instances.
- Breakpoint placement and layout version; whether to use top-level automatic caching or explicit breakpoints.
- TTL (5 minutes vs 1 hour) and the policy on cross-run reuse.
- Whether summary calls also use caching (they would in a realistic deployment).
- Sample size.
- **Budget:** not agreed. Experiment 004's unused authorisation does not carry over.
