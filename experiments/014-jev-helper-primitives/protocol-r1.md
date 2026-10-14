# 014 – Development revision R1 protocol: one configured delegation smoke (FROZEN 2026-10-14, before the run)

**What this is:** a **configured capability demonstration**. It tests whether Claude can write a reusable procedure in which **Jev's judgments, consumed by the helper's own code during the same execution, select substantive register changes**.

**What it is not:** a test of spontaneous adoption, or of practical benefit.

**How it relates to earlier work:**
- It follows [revision-delegation.md](revision-delegation.md), the design.
- It is separate from the completed W3 pilot ([protocol-comparison.md](protocol-comparison.md)) and from the earlier demonstration. Both are unchanged.

**No comparison follows** from this smoke, whatever its result.

## Settings

- **Task:** `w3-smoke-1` (`export-gen/2`, 5 stages; change notices at stages 3–5; code scorer `export-checks/2`, register scorer `register-checks/1`).
  - **The same instance as the pilot's B smoke:** a development instance, never part of an outcome comparison.
- **Condition:** `clm_helpers` with `--jev-primitive on` and the R1 instruction [`r1-instruction-b.txt`](r1-instruction-b.txt), appended to the task text and recorded in `run.json → extra_instruction`.
  - **Prompts otherwise unchanged:** prompt version `2026-10-13.8`, including `JEV_PRIMITIVE_CLAUSE`.
- **Config:** `configs/exp014r1.toml`, identical to `exp014c.toml` except the ceiling.
  - **Model:** `claude-opus-5-5`, effort low.
  - **Caching:** on, with `blocks/1` and `run-tag/1`.
  - **Primitive:** 8 calls per execution, 40 per run, 20 items.
  - **Jev:** `jev-1.13.0`.
- **Context budget: 12,000 tokens,** recorded explicitly.
  - **Why:** this generous budget isolates the delegation mechanism.
  - **What it does not claim:** that the budget makes any later comparison fair. Extra context consumption can be a real consequence of an assisted approach. A future benefit comparison must justify its own shared budget and count the pressure, spill and recovery costs that result.
- **The contract** (the instruction, verbatim, is in `r1-instruction-b.txt`; it applies to the caller **and** the helper):
  - the helper reads the register from `context.json`;
  - the caller passes the newly released stage and general parameters, plus optional text about new items keyed by the new ids. It passes no affected-item lists, no edits to existing items, and does not name existing items;
  - Jev's answers govern keep, amend and retire;
  - the helper holds no hard-coded decisions about particular existing items;
  - fallbacks print `FALLBACK:`, and overrides go through a helper function that prints `OVERRIDE:`.

  No reference helper, mappings or truth are given to the model.

## Budget and attempts

- **The allowance:** USD 1 new, both providers. The settled spend at the start is USD 86.182345, so the ceiling is set to **87.182345**, which replaces the unused remainder of the comparison phase's allowance.
- **One attempt.** At most one replacement, and only after a **demonstrated harness defect**: a runtime, scorer or recording fault that invalidates the evidence. It must fit within the same cap, both attempts are kept, and a new freeze record is appended first.
- **Not reasons to replace a run:** poor helper behaviour, non-delegation, incorrect edits, model errors, and failure to follow the instruction. These are results.
- **No changes after the run:** the instruction is not revised after the run, and no pilot or evaluation follows.

## Analysis rules (frozen)

**Evidence per Jev-using execution** (`clm-lib replay-jev`, `jev-replay/2`; offline, sandboxed, no paid calls, originals untouched):

1. **`recorded`** must reproduce the accepted revision. Otherwise the step is `not_reproduced`, its nondeterminism is investigated and explained, and it is never counted as dependence.
2. **`withheld`** tests the fallback path only. A clean no-edit fallback is **not** evidence that Jev selected the original edits.
3. **`inverted` and `permuted`** are **valid substituted probabilities**:
   - the same response shape, item keys and per-item matching;
   - 1 − p, or each recorded request's answers rotated by one position;
   - every served value logged.
4. **Classes:**
   - **Under substitution:** `substantive` (a register item's label or content changes) is kept apart from `marker_only`, `no_register_dependence`, `crash_under_substitution`, `no_edit_under_substitution`, `substitution_identical` and `unsupported_counterfactual`. The last applies when the substituted answers make the code ask something the original run never asked; no recorded answer is ever paired with an incompatible request.
   - **Under withholding:** `crash_without_answers` and `no_edit_without_answers` are reported likewise.
   - **No one-to-one requirement:** an answer need not change exactly one item. The analysis traces how the changed judgments produce the changed selection, including legitimate effects on related items.
5. **Code review** of the caller and helper source of every Jev-using execution, and of every other execution that writes `context.json`:
   - it identifies predetermined mappings, unconditional writes, direct register writes, overrides and fallbacks, and **the branches that consume Jev's answers**;
   - the static audit (register-item literals, ids of existing items in code) is supporting evidence only;
   - initialising items for new requirements and transcript cleanup may be independent of Jev. They are reported separately, and are neither delegation nor automatically a violation.

**Success: R1 demonstrated** requires all three of the following.

| | Criterion |
| --- | --- |
| **Contract** | at each counted stage, the Jev-using execution's caller supplies no affected-item list, no edits to existing items and no names of existing items, and the helper holds no hard-coded decisions about particular existing items (code review) |
| **Reproducible** | `recorded` reproduces that execution |
| **Judgment-dependent selection** | at **at least 2 of the 3 change notices (stages 3, 4, 5)**, a counted execution is `substantive` under **at least one valid substitution** (inverted or permuted), and code review confirms the difference comes from a branch of the helper's selection logic that consumes the answers |

**Reported separately** (none of these changes the verdict):
- contract compliance per execution, including violations at any stage;
- replay reproducibility;
- which stages show judgment-dependent selection;
- helper creation, revision and reuse;
- `FALLBACK:` and `OVERRIDE:` counts, and Jev error statuses;
- register correctness (`register-checks/1`), and the correctness of each Jev-governed edit against the evaluator truth (after the run, evaluator-only);
- code correctness (`export-checks/2`);
- real Jev calls within executions;
- model calls, tokens, caching, cost and elapsed time.

**Successful delegation may still make incorrect edits.** A demonstrated mechanism is not described as useful or safe.

**One concrete trace** will be reported: new requirement → helper question → real Jev answer → executed decision branch → actual context change → next model request. It is followed by the corresponding valid-answer counterfactual. Observed results are kept apart from illustrative examples.

## Freeze records

_(Appended below; earlier records are never edited.)_

### Freeze record 1 (2026-10-14, before the R1 smoke; no paid call of R1 made yet)

- **Source:** clm-lib HEAD `602128d` plus uncommitted changes (`git diff HEAD` prefix `dcf217e1d3a8940d`).
  - **Changes:** `replay.py` (`jev-replay/2`) and its tests; `configs/exp014r1.toml`.
  - **Runtime, workload and scorers:** unchanged since the comparison phase.
  - **File prefixes:**
  - `src/clm_lib/replay.py` `e5627e291fed6bea`
  - `src/clm_lib/runner.py` `a8aecb8ec383c3dd`
  - `src/clm_lib/w3.py` `67cf4b38ddc50afd`
  - `src/clm_lib/register_score.py` `e77cbc1ab5d2d375`
  - `src/clm_lib/jev_primitive.py` `3408dee1dd1a9e81`
  - `src/clm_lib/prompts.py` `01375b848c223f50`
  - `configs/exp014r1.toml` `937024b1da0898cb`
  - `tests/test_w3.py` `7e333764ad237ff4`
- **Instruction:** `r1-instruction-b.txt`, prefix `69440997d89fdcab`.
- **Fixture:** `w3-smoke-1` `021c631ee4b3e70c`.
- **Verification:** ruff and format are clean, mypy reports no issues, and pytest **294 passed**. That includes the new replay tests: item-level matching, valid substitutions with logs, unsupported counterfactuals, substitution classes and the code audit.
- **Offline check of the pilot under `jev-replay/2`:** dev-1 B (output not exported; the exported `/1` replays are unchanged). Every Jev-using execution was `no_register_dependence` under both valid substitutions, and the audit flagged register literals and existing item ids in every caller. This agrees with the pilot's conclusion.
- **Ledger before the ceiling change:** spent 86.182345, ceiling 87.535602.

### Record 2 (after the smoke; nothing above was changed)

- **Run:** `20261014T020047-clm_helpers-cacheon-jprim-w3-smoke-1-5bae`, run once. No replacement: no harness defect was found.
- **Cost and ledger:** USD 0.274928; the ledger now stands at USD 86.457271 spent against the 87.182345 ceiling.
- **Replay:** `jev-replay/2` as frozen. The recorded answers reproduced all 5 Jev-using executions.
- **Verdict under the frozen criteria: NOT demonstrated.**
  - **Stages 3–5:** both valid substitutions are `unsupported_counterfactual`. The helper judges new items one after another, and each later request contains the register text as already changed by the earlier answers. So substituted answers produce requests the original run never made, and no valid answer exists for them.
  - **Stage 2:** the only step with valid-substitution evidence was `substantive` under the permutation, but stage 2 holds initial requirements, not a change notice.
- **Post-hoc analysis addition** (made after seeing the result, and **not used for the verdict above**): `replay.py` gained `inverted_last` and `permuted_last`, which substitute only each execution's final Jev request. The code is fingerprinted in the README. Under these, every Jev-using execution was `substantive`, including stages 3, 4 and 5. This is reported as exploratory evidence only.
