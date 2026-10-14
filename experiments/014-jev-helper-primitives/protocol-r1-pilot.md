# 014 – R1 matched development pilot protocol (FROZEN 2026-10-14, before the first paid call)

**The question:** does the configured R1 delegation approach offer any practical advantage over ordinary CLM, on requirements-register maintenance through CLM context edits?

**What it is:** a small **development pilot** of 2 instances × A/B, run once per cell. **No larger evaluation is authorised or implied.**

**Separate from, and leaving unchanged:**
- the prompted demonstration;
- the first W3 pilot ([protocol-comparison.md](protocol-comparison.md));
- the R1 smoke ([protocol-r1.md](protocol-r1.md)). Its verdict stays "not demonstrated under its frozen criteria", and its last-request analysis stays exploratory.

## Conditions

| | A: ordinary CLM | B: configured R1 Jev-assisted CLM |
| --- | --- | --- |
| Mode | `clm_helpers` (reusable helpers allowed) | `clm_helpers` with `--jev-primitive on` |
| Task, requirements, source access, visible tests | identical (W3 task prompt with the register objective; earlier stage files rereadable) | identical |
| Register objective and assessment timing | identical (`register-checks/1`: at each stage release and at the final answer) | identical |
| Model, effort, caching, layout, budgets, limits, validation | identical (`configs/exp014p2.toml`) | identical |
| Extra instruction | none | [`r1-instruction-b.txt`](r1-instruction-b.txt), **byte-identical to the R1 smoke** (SHA-256 prefix `69440997d89fdcab`) |
| System prompt | the ordinary CLM prompt (`2026-10-13.8`) | the same plus `JEV_PRIMITIVE_CLAUSE` |

**A** chooses its own context-management method. Nothing forces it to rewrite everything, avoid helpers, or add review steps.

**B** writes its own helper in each run. It is not seeded with the R1 smoke's helper, and no mappings are supplied.

**No changes to B:** the R1 instruction is not reworded, and no better helper is prescribed.

**The budget:** a shared **12,000-token** request budget. This pilot tests **register maintenance through CLM context edits under that budget, not the benefits of compaction under tight context pressure.** Pressure, spill and recovery events are kept and reported. The budget is not raised to avoid them.

## Instances (registered before any run of this pilot)

The W3 generator (`export-gen/2`) has no free schedule generator. The two fresh instances are **new seeds of the two existing development schedules**, assigned in sequence and not chosen for any expected outcome. Values, records, visible tests and hidden checks are new; the item structure matches `w3-dev-1` and `w3-dev-2`.

| Instance | Seed | Schedule | Values (p2, region, cap) | Fixture SHA-256 prefix | Hidden checks / snapshot checks |
| --- | --- | --- | --- | --- | --- |
| `w3-dev-3` | 8503 | as `w3-dev-1` | legal, eu, 30 | `9329f86faf1ed3ed` | 64 / 112 |
| `w3-dev-4` | 8504 | as `w3-dev-2` | regulator, eu, 20 | `61855298ed1e66cb` | 64 / 112 |

**Mechanical checks** (offline; the same tests as the earlier instances, now including these two):
- the reference matches an independent implementation;
- the visible tests pass on it;
- each faulty solution fails its category;
- the independent solution is strictly successful in the sandbox;
- correct register representations score no error at every stage;
- the information boundary holds.

## Order, budget and stopping

**The order, each cell once:**
1. `w3-dev-3` A;
2. `w3-dev-3` B;
3. `w3-dev-4` B;
4. `w3-dev-4` A.

**Budget:**
- **At the start:** spent USD 86.457271.
- **The authorisation:** USD 3 new, both providers, all attempts included; earlier allowances are not stacked. The ceiling becomes **89.457271**.
- **Before each run:** the remaining allowance must be at least USD 0.60, otherwise stop.

**Rules:**
- **Every attempt is kept, and nothing is replaced.** Poor task performance, non-delegation, bad helper choices and non-compliance with the instruction are results.
- **A genuine harness defect** (a runtime, scorer or recording fault): keep the attempt, **stop**, and report it. It is not repaired and replaced.
- **Stop** after the four runs and their analysis.

## Delegation measurement (frozen before the runs)

**The tool:** `clm-lib replay-jev` (`jev-replay/2`). It runs offline in the sandbox, makes no paid calls, and leaves the originals untouched. Applied to each B execution that called Jev:

- **Recorded responses** must reproduce the accepted revision. Otherwise the step is `not_reproduced`, investigated, and never counted.
- **The primary intervention is the last actual Jev response of the execution** (`inverted_last`, `permuted_last`; reported under `last_request`):
  - every earlier request receives its recorded answers;
  - the last request receives valid substituted probabilities: 1 − p, or the request's recorded answers rotated by one position (a one-item request keeps its answer under rotation);
  - the response schema and item keys are preserved, and every served value is logged.
  - **If the intervention makes the code issue a request** for which no recorded item answer exists, the replay is `unsupported_counterfactual`. No answer is ever attached to a different request.
- **Classes:**
  - `substantive` (a register item's label or content changes) is kept apart from `marker_only`, `no_register_dependence`, `crash_under_substitution`, `no_edit_under_substitution` and `substitution_identical`;
  - **not substantive:** changes in logging, markers, crashes, early exits or fallback alone.
- **Withheld responses** measure fallback only. They do not establish substantive selection.
- **Full-execution substitutions** (`inverted`, `permuted`) are reported as supporting evidence. They are often unsupported for sequential helpers.
- **The scope of a conclusion:** a last-response intervention tests the decisions governed by that last request (`last_request_items`). It does **not** establish that every earlier edit in the execution depended on Jev.
- **Code review** of caller and helper code identifies:
  - the actual judgment-dependent branches;
  - hard-coded mappings, unconditional edits, overrides and fallbacks;
  - Jev-independent work (new-item initialisation, transcript cleanup).

  The static audit is supporting evidence only.

**A B run counts as "mechanism used" when:**
- at least one execution that is a change notice (stages 3–7) is reproduced and `substantive` under a last-request intervention;
- and code review finds no caller-supplied selection for that execution.

The number of notice stages meeting this is reported per B run.

## Outcomes, measured and reported separately

1. **Mechanism use:**
   - the delegation evidence above;
   - helper creation, revision and reuse;
   - `FALLBACK:` and `OVERRIDE:` counts;
   - Jev calls, items, latency, errors and cost.
2. **Correctness of the edits:**
   - code: `export-checks/2`, final and at every stage snapshot;
   - register: `register-checks/1` at every assessment point, with harm, history errors and incomplete counts per stage. Transient errors and later corrections are listed, not only the final state;
   - Jev-governed selections against the evaluator truth (after the run; evaluator-only), with the decisions the last-request intervention tested marked;
   - the final registers read by hand.

   **The scorers and their accepted representations are not changed after seeing the results.**
3. **Task performance and efficiency of the whole approach:**
   - **primary:** total cost across both providers per run;
   - elapsed time and main-model calls (actions, repairs, retries);
   - uncached input, output, cache reads and cache writes;
   - executions, accepted edits, pressure, spill and recovery events;
   - requirement rereads;
   - register size per assessment point (items, CURRENT/HISTORY counts, characters) and the growth of HISTORY entries;
   - **setup against maintenance cost, where the traces support it:** the main-model cost of the step whose code first creates a helper module, separately from all other steps. Total cost, including setup, stays the primary measure, and no future amortisation is claimed.

   No input saving is credited to Jev: Claude receives the context and the update before it calls its helper.

**Analysis:**
- **What is reported:** per run, each A/B pair (B − A), and per-condition means of the two runs, labelled descriptive.
- **No inference from n = 2:** no benefit is claimed.
- **Outcome 3 stands on its own:** if B is cheaper or more correct in both pairs, that is reported as a development observation, not as an established effect. If B is worse, that is reported and explained.

## Freeze records

_(Appended below; earlier records are never edited.)_

### Freeze record 1 (2026-10-14, before the first paid call of this pilot)

- **Source:** clm-lib HEAD `8309a27` plus uncommitted changes (`git diff HEAD` prefix `117b141be5e3f949`):
  - instance registration (`w3-dev-3`, `w3-dev-4`, and `SCHEDULE_ALIASES` in `w3.py`);
  - the replay's neutral `last_request` keys;
  - tests;
  - `configs/exp014p2.toml`.

  Runtime, scorers and prompts are unchanged.
- **File prefixes:**
  - `src/clm_lib/w3.py` `b335def0eec93bd8`
  - `src/clm_lib/tasks.py` `4fb599577645591a`
  - `src/clm_lib/replay.py` `78e08e69e6f155d1`
  - `src/clm_lib/runner.py` `a8aecb8ec383c3dd`
  - `src/clm_lib/register_score.py` `e77cbc1ab5d2d375`
  - `src/clm_lib/jev_primitive.py` `3408dee1dd1a9e81`
  - `src/clm_lib/prompts.py` `01375b848c223f50`
  - `configs/exp014p2.toml` `4ea4a1e19938aad2`
  - `tests/test_w3.py` `c4b2e22eb4b736bd`
- **Instruction B:** `r1-instruction-b.txt`, prefix `69440997d89fdcab`, unchanged since the R1 smoke.
- **Verification:** ruff, format and mypy are clean, and pytest **297 passed**. That includes the new instances' mechanical checks and the sandbox runs of the independent solution on `w3-dev-3` and `w3-dev-4`.
- **Ledger before the ceiling change:** spent 86.457271, ceiling 87.182345.

### Result record (after the four runs; nothing above was changed)

- **Runs,** each once in the frozen order. There were no replacements and no harness defects. The step-24 `invalid` Jev requests on dev-3 B were B's own helper sending more than 20 items, which the primitive rejected explicitly as documented.
  - **dev-3 A:** `20261014T041357-clm_helpers-cacheon-w3-dev-3-89e5`;
  - **dev-3 B:** `20261014T041616-clm_helpers-cacheon-jprim-w3-dev-3-a692`;
  - **dev-4 B:** `20261014T041952-clm_helpers-cacheon-jprim-w3-dev-4-7abc`;
  - **dev-4 A:** `20261014T042247-clm_helpers-cacheon-w3-dev-4-32ed`.
- **Spend:** USD 1.642475. The ledger moved from 86.457271 to 88.099746, against the 89.457271 ceiling.
- **Mechanism used:** yes, in both B runs. The recorded replays reproduced every Jev-using execution. The last-request intervention was `substantive` at notice stages 3 and 6 (dev-3 B) and 4–7 (dev-4 B). Code review found answer-driven branches and no caller-supplied selection.
- **Correctness:** all four runs scored 64/64, with no snapshot failures and register harm 0 at every stage.
- **Efficiency:** B cost +97.7% (dev-3) and +61.3% (dev-4), with means of A USD 0.293 and B USD 0.528.
- **Details:** in the [README](README.md#r1-matched-development-pilot-results).
