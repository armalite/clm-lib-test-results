# 012 – Jev screening of incoming tool results: protocol draft

**Status: PLANNED, offline phase only.** No paid call or agent run has been made for 012. Nothing in this file is implemented in clm-lib unless it says so.

**Question:** can Jev screening of incoming tool results improve a CLM agent by reducing unnecessary input before the main model processes it?

**The screening is a filtering layer beside CLM.** The main model still writes and controls every working-context edit. Ordinary CLM is unchanged.

## Offline opportunity audit: fixed trace set (recorded 2026-10-13, before any analysis)

- **Source:** experiment 010 v3's exported evaluation, `../010-jev-initiated-review/artifacts/runs/v3/evaluation/`.
- **Selection:** **all 12 condition-A runs** (`clm_helpers-cacheon-rounds-eval-{9,10,11,12}-*`, 3 repetitions each): ordinary CLM, with no review workflow, on the current runtime settings (`blocks/1` layout, prompt caching, run isolation, a 6,000-character output cap per stream, an 8,000-token context budget).
- **Coverage:** **every observation in every one of these runs** is analysed, with no selection by size or content.
- **Why these runs:** they are the most recent incident traces, they match the control condition 012 would use (ordinary CLM with unfiltered tool results), and they come from a completed experiment, so nothing is altered.
- **Not used:** the B and C runs of 010 v3 (their review workflow changes behaviour), and older experiments (different settings).
- **Status of these instances:** `rounds-eval-9..12` and their traces are now **012 development material**. Any later 012 evaluation uses fresh instances (for example `rounds-eval-13` onward, not yet registered).
- **Inputs the audit uses:**
  - the exported events (`execution_result` stdout and stderr with byte counts);
  - the saved model requests;
  - context revisions and receipts;
  - the released fixture files.

  Scorer truth is used **only** to check whether known evidence lines appeared in observations. It is never an input to any proposed filter.

## Offline opportunity audit: findings (2026-10-13)

**Script:** `analysis/audit_observations.py`. Output in `analysis/audit_summary.txt` and `analysis/audit_output.json`. It reads only the fixed trace set above: 12 runs, 261 executions, 390 action requests.

**The stages of a tool result** (`source` → `produced` → `retained` → `received`):

| Stage | Measured | Value |
| --- | --- | --- |
| Source files released | fixture bytes released by the step | median **148 KB** (max 413 KB); 290–413 KB per instance |
| Produced by the command | stdout+stderr bytes (executor count, before the cap) | median **539**, p90 2,693, max 6,774 |
| Retained after the 6,000-char cap | observation body | median **539**, p75 1,338, p90 **2,693**, mean 938, max 6,000 |
| Truncated by the cap / spilled by the runtime | | **1** / **0** of 261 |
| Received in the next request | | 261/261 |
| Residence in later requests before removal | | 1 request: 136; 2: 22; 3: 103 (mean 1.9) |

**Size bins (retained characters):**

| < 500 | 500–2,000 | 2,000–4,000 | 4,000–6,000 | ≥ 6,000 |
| --- | --- | --- | --- | --- |
| 130 | 91 | 27 | 12 | 1 |

**The 23–41K-character logs are source sizes, not what Claude received.** Claude's code already selected what to print, as the system prompt asks ("search and filter … instead of printing whole files"). Commands, by heuristic classification of the code:

| Command class | Count | Observation characters |
| --- | --- | --- |
| filtered extraction (regex, keyword or slice) | 102 | 166,237 |
| prints a small whole file (board or change log) **and** filters logs | 49 | 56,755 |
| no direct fixture path (workspace, context, or a helper script that reads fixtures) | 108 | 21,616 |
| other | 2 | 187 |
| whole-file print only | **0** | — |

The heuristic undercounts filtered reads that go through helper scripts (for example a `scan.py` helper printing filtered lines).

**Composition of what the model received** (characters over all 390 requests; exact tokens only as totals). Exact input tokens totalled 1,730,206: 45,465 uncached, **1,263,657 cache reads** and 421,084 cache writes.

| Part | Share of request characters |
| --- | --- |
| system prompt | 31.2% |
| task | 27.4% |
| notes (Claude's own) | 13.8% |
| **tool observations** | **9.9%** |
| Claude's step actions (code) | 8.2% |
| status, receipts | 4.2% |

**Cost, counting prompt caching** (an estimate, from character shares; each observation is written to the cache once, at USD 5/M, and read from it at USD 0.20/M while it remains):
- **Observation text:** about **USD 0.62 of USD 4.18** across the 12 runs (about 15%).
- **Large observations** (≥ 2,000 characters, 40 of 261) hold **57%** of all observation characters.

**What the large observations contain** (exploratory line classes; the generator's fixed background messages are named as such):

| Line class | Share of characters |
| --- | --- |
| ERROR lines | 36% |
| "slow query" WARN (background noise) | 32% |
| routine INFO (health, heartbeat, GC, request ok; background noise) | 15% |
| board and change lines | 6% |
| other (headers, counts, listings) | 5% |
| other WARN | 5% |

**Interpretation:**
- **Removable material exists, but mostly because Claude's own filters were broad** (for example `re.search(r'WARN|ERR|…')` matching every slow-query warning).
- **It is mixed with essential evidence in the same outputs.** Scorer evidence lines appeared in those observations (492 evidence-line matches in total).
- **Evidence is not just ERROR lines:** 84 of the scorer's evidence lines are WARN lines ("disk usage high"), and the logs switch to a JSON line format mid-run. A level- or format-based rule would lose evidence.
- **Rereading:** 40 of 155 explicit file references in code reopened a file read in an earlier step.
- **No observation was spilled,** and the cap truncated one.

**Upper bound on the saving** (cache-aware estimate): if every background-noise line in the large observations vanished, input cost would fall by about **USD 0.0136 per run, 3.9% of the mean run cost (USD 0.348)**, before Jev's cost, the disclosure text and any retrieval. Downstream effects (for example fewer context edits) are not estimated.

**What this audit cannot show:**
- **Jev's filtering accuracy:** no Jev call was made, so no claim is made about which passages Jev would keep.
- **Agent outcomes:** these are replayed traces, not agent results.
- **Which lines are useful:** the line classes are author labels using knowledge of the generator; the scorer's evidence lines are not the only useful lines.

## Workload decision

**The existing incident workload does not offer a meaningful screening opportunity.**
- Tool results reach Claude short (median 539 characters), already filtered by its own code, and are usually removed from context within one to three requests.
- The removable part is at most about 4% of run cost under prompt caching, and it is interleaved with evidence that a filter could lose.

A test on this workload would mostly measure overhead and evidence-loss risk.

**Recommended bounded alternative (not built): document search that naturally returns several passages.**

- **Task:** answer about 6 questions per instance about a synthetic internal handbook: about 40 documents of 6–10 numbered sections, with policies, exceptions, effective dates and some superseded versions. Each answer is a value with citations (`doc-id §n`).
- **Tool:**
  - **Search:** a deterministic search helper, `search(query, k=8)` over the sections (stdlib BM25), at `/task/fixtures/search.py`. It prints up to *k* ranked passages, each with an id header (`=== doc-17 §4 | title | effective 2026-03-01`) and 300–600 characters of text, so a call returns about 2.5–5 KB.
  - **What makes passages hard to tell apart:** they share keywords but differ in scope, version or exception.
  - **The same access for every condition:** whole documents remain readable (`open`, grep) in all conditions, and *k* stays the model's choice.
- **Scoring (hidden, generated):**
  - per question: the value is correct, the supporting sections are cited, and no superseded version is used (stale detection);
  - strict success means all questions correct with their support.
- **Effort:** a generator, search helper and scorer (about the size of W2: roughly 800–1,000 lines with tests); the screening layer in the runtime (about 300–400 lines with tests); a component-diagnostic script.

## Fair comparison (proposed; not implemented)

**Conditions:**
- **A:** ordinary CLM with today's unfiltered tool-result presentation.
- **B:** the same CLM with automatic Jev screening of eligible observations.

**Both conditions share:**
- the same main model, task text, limits, layout, caching (5 min, per-run isolation) and tools, including the search helper and direct file access;
- **the same saved full result:** a new, versioned runtime option saves each execution's complete stdout to `/task/workspace/results/step-NNN.txt` in both conditions, and each observation names that file;
- **the same boundary:** screening applies to the observation *after* the existing 6,000-character cap, so B never sees more than A, and the saved file holds the complete output for both;
  - **this needs a runtime change:** the executor today keeps only the first 6,000 bytes per stream, so it would also have to keep the complete stdout (bounded, for example at 1 MB) for the saved file;
  - **it also changes A:** the saved-file notice makes A "ordinary CLM with saved results", versioned and not identical to the historical incident runs;
- **equivalent notices:** B's observation additionally says that it was screened, what was omitted and where it is.

**B never inspects information hidden from A.** The screener gets no scorer truth, future stages or answers.

**Ordinary CLM editing is unchanged.** Screening is opt-in and versioned (proposed name `result-screen/1`).

**Deterministic reference selector:** keep the passages that share a non-stopword term with the step's search query or `thought` (plus the always-keep rules below). It is cheap and meaningful, but **it belongs in the component diagnostic** as a baseline for Jev's chunk-level selection, **not as a third agent condition**. No larger matrix is proposed.

## Screening policy `result-screen/1` (specified before implementation; not implemented)

- **Eligible:** stdout of an `execute` step with exit code 0 and at least **2,000 retained characters**.
- **Never screened:**
  - stderr;
  - failed or timed-out executions;
  - runtime observations (stage releases, receipts, reviews);
  - anything already spilled.
- **Chunks:**
  - **For search output:** one chunk per passage, split at the `===` headers.
  - **Otherwise:** blocks of at most 8 lines or 600 characters, split at blank lines.
  - **Provenance:** every chunk keeps its original line range (`L12–L19`) and its id header, and the result keeps the original order.
- **The Jev question** (`noul`, one per chunk, batched up to 20 per request): "Is this passage needed or useful for the agent's current step?"
  - **True** if it contains facts, values, conditions, exceptions, dates or identifiers that bear on what the command was looking for or on the task.
  - **False** if it is unrelated to both.
- **Information supplied to Jev:**
  - the task text (cut at 4,000 characters);
  - the step's stated `thought`;
  - the command's code (cut at 1,500 characters);
  - the chunks.

  Nothing else: no notes, no truth, no future material.
- **Selection:**
  - keep a chunk if *p* ≥ **0.3** (lenient, favouring recall; values between 0.3 and 0.5 count as ambiguous and are kept);
  - always keep the 2 highest-scoring chunks;
  - kept text never exceeds the original.
- **Dependencies:** section and file headers (lines before the first chunk, `===` headers, and `== file ==`-style lines) are always kept, so that kept lines keep their context. A kept log line keeps its file header.
- **Always keep** (structural, independent of answers):
  - the first 2 and last 2 lines (counts and summaries);
  - lines with `Traceback`, `Error:` or `Exception` printed by the command itself.
- **No match** (nothing ≥ 0.3): keep the always-keep lines plus the top 2 chunks, with a notice.
- **Malformed or missing answer for a chunk:** keep that chunk (fail open).
- **Service error or timeout** (after the existing 1 retry): show the observation unscreened, with "screening unavailable; nothing was omitted". It is never shown as screened.
- **Disclosure in the observation:**

  ```
  [screened (result-screen/1): kept 5 of 12 passages, 2,140 of 5,880 chars; omitted doc-3 §2 (L20–L31), doc-9 §1 (L32–L44), …; complete output: /task/workspace/results/step-007.txt]
  ```
- **Retrieval:** Claude can read the saved file, as A can.
- **Current relevance is not permanence:** omitted passages stay in the saved file.
- **Timing:**
  - screening runs **sequentially** after the execution and before the next model call, with one Jev request per 20 chunks, sent one after another;
  - the latency and cost of every request are recorded, and every attempt goes in the ledger.

## Metrics (planned)

- **End-to-end (A vs B):**
  - strict success and per-question correctness;
  - evidence quality: the cited supporting sections, and stale use.
- **Screening quality (B):**
  - needed passages omitted (against generator-known support and, separately, author labels of "useful");
  - retrieval of omitted passages from the saved file, and the calls and cost it took.
- **Cost and time:**
  - total cost by provider;
  - end-to-end wall time;
  - main-model calls;
  - input and output tokens;
  - cache reads and writes.
- **Screening activity:** screening calls, failures, skipped (ineligible) outputs, and the retained versus omitted characters.
- **Kept separate:**
  - **chunk-level screening quality** (component diagnostic);
  - **mechanical integration** (smoke);
  - **end-to-end benefit** (agent pilot, then a held-out evaluation on fresh instances).

## Readiness steps (planned; none authorised or run)

1. **Build** the search workload and `result-screen/1`, with offline tests:
   - provenance and line ranges are preserved;
   - originals are saved in both conditions;
   - B never sees more than A;
   - every failure path is never shown as screened.
2. **Offline opportunity re-check** on generated search outputs, with no Jev. It reports how often eligible results occur at natural *k*, and how much text a perfect selector could omit.
3. **Component diagnostic** (TypeSafe only): about 40 search results (about 300 chunks) from development instances, with author labels (needed / useful / not needed) written before any answer, comparing Jev with the deterministic term-match selector.
4. **Integration smoke:** one explicitly prompted live run in condition B, excluded from outcomes.
5. **Agent pilot:** 2 development instances × A/B.

**Readiness criteria** (they establish exercise and evidence preservation, **not** favourable cost or correctness):
- eligible results occur in at least half of the development tasks;
- needed-passage recall of the policy is at least 0.95 on the diagnostic;
- the policy omits at least 20% of eligible characters (so screening is exercised);
- no provenance, disclosure or accounting defect.

## Estimated next phase (not authorised; no ledger change)

- **Work:** about 2–3 focused sessions (the workload, the screening layer, tests and the diagnostic).
- **Spend:**
  - **component diagnostic:** about USD 0.05 (TypeSafe);
  - **smoke:** USD 0.3–0.5;
  - **agent pilot** (4 runs): about USD 1.5–2.5, assuming about USD 0.35–0.6 per run;
  - **total:** about **USD 3**, so an authorisation of up to about USD 5 would cover retries.

---

# Implementation phase (2026-10-13): document-search workload and `result-screen/1`

**Status:** implemented in clm-lib (uncommitted at the time of writing), in `handbook.py`, `jev_screen.py` and the runner. The diagnostic, smoke and pilot follow below, in order, each only if its gate allows.

## Workload as built (`handbook-gen/1`, scorer `handbook-checks/1`)

- **The handbook:** 40 documents per instance, 158 passages (sections), median passage 362 characters.
- **Subjects:** 8 policy subjects. Each has a current policy, a superseded version, an exception memo with a carve-out, a same-subject "related budgets" distractor, and an FAQ entry restating the current standard value.
- **Questions:** 6 per instance, one per subject, covering 5 types:
  - `current`;
  - `past` (only the superseded version applies);
  - `exception`;
  - `carveout` (the memo's carve-out **plus** the standard value);
  - `additive` (the standard value **plus** an addition).

  Answers are numeric, with alternative valid support sets (the FAQ restates every current standard value).
- **Scoring:** a question is correct when the value is right (numeric comparison) **and** a complete valid support set is cited. A superseded value is counted as stale; extra citations are counted, not failed.
- **Tools (identical in A and B):**
  - `search(query, k=5)` (at most 8) prints a structured block and saves the original under `/task/workspace/search-results/` (path in the block header);
  - `show(ids)` prints passages in a never-screened format;
  - documents are readable directly.
- **Instances:**
  - `handbook-dev-1` and `handbook-dev-2` (pilot);
  - `handbook-smoke-1` (2 questions, smoke only);
  - `handbook-diag-1` (diagnostic development cases);
  - `handbook-diag-2..4` (frozen diagnostic cases).

  No evaluation instances are defined.

## Offline opportunity check (no Jev; `analysis/screen_cases.py opportunity`, output `analysis/opportunity_summary.txt`)

- **Queries:** two ordinary queries per question (*specific*: the quantity plus the situation; *short*: the quantity), at the documented default k = 5.
- **Labels:** from generator truth, before any Jev answer:
  - `support`: in a valid support set;
  - `context`: same subject, in no support set;
  - `irrelevant`: another subject, the related-budgets distractor, or general text.

| | Pilot instances (12 questions, 24 queries) | Diagnostic instances (24 questions, 48 queries) |
| --- | --- | --- |
| Eligible results (≥ 3 passages, ≥ 2,000 chars) | **24/24** (every question) | 48/48 |
| Results holding a complete support set | 17/24 | 31/48 |
| Eligible characters: support / context / irrelevant | 31% / **68%** / **1%** | 29% / **70%** / **2%** |

**Finding:**
- **Eligible results are routine.** The first readiness condition is met offline: every pilot question gets eligible results at the default k.
- **Very little is clearly irrelevant:** 1–2% of characters. BM25 at k = 5 returns the same-subject cluster.
- **The omittable material is mostly `context`:** superseded versions, other groups' exceptions, FAQ entries. No support set needs it. But the policy is required to keep exception and version information when it *could* change the answer.
- **The consequence for the ≥ 20% omission criterion:** it can be met only if Jev omits context passages that it judges unable to change this question's answer.

**Decision, recorded before any paid call:**
- **Proceed to the development diagnostic** (TypeSafe only, about USD 0.002). It is the only way to measure what `result-screen/1` actually omits.
- **The question is not reworded to omit more.** Doing so would conflict with keeping version and exception information.
- **Expectation, stated in advance:** low omission is plausible, and the gate may fail on the omission criterion.

## Component diagnostic: development run and the one recorded change (2026-10-13)

**Run `20261013T071821-screen-dev`:**
- **Cases:** 12 development cases from `handbook-diag-1`, all eligible.
- **Calls and cost:** 12 requests, 0 errors, 0 missing answers. USD 0.001759; 41,877 input and 1,068 output tokens; 0.26 s mean latency.

| Policy on development cases | Support recall | Complete sets surviving | Omitted share (all from `context`) |
| --- | --- | --- | --- |
| Jev, threshold 0.3 (the draft) | 18/18 | 8/8 | **5%** |
| Term-match baseline | 18/18 | 8/8 | 0% |
| Jev answers re-applied at 0.4 / **0.5** / 0.6 (no new calls) | 18/18 each | 8/8 each | 8% / **21%** / 33% |

**The pattern:**
- **Support passages** scored 0.80–0.98.
- **Context passages** scored 0.26–0.98: Jev treats same-subject versions and exceptions as possibly answer-changing, as its question asks.
- **At 0.3,** screening is barely exercised.

**The one change (based only on these development answers):** the threshold goes from **0.3 to 0.5**.
- **Why 0.5:** it is the programme's standard reporting threshold, already used in 011 and fixed in advance there; it is not a value searched for.
- **Not 0.6:** that would only chase omission.
- **Stated in advance:** at 0.5 the development omission is **21%, just above the 20% target**. The frozen set may therefore fail on omission, and could also show support losses.
- **Unchanged:** the question, the minimum of 2 kept passages, the selection, the failure handling and the notices.

## Component diagnostic freeze (before the frozen run)

- **Policy:** `result-screen/1`.
  - **Eligible:** a complete structured block with ≥ 3 passages and ≥ 2,000 presented characters.
  - **Boundaries:** the `===` passage headers.
  - **Keep** probability ≥ **0.5**, at least **2** passages (highest probability, then rank), in original order.
  - **A missing answer** keeps its passage. **A service error** leaves the block unscreened, with a notice.
  - **Notices:** fixed formats, "kept k of n passages …; omitted …; unscreened: show([...]) or <saved path>" or "all n passages kept".
- **Question** (`jev-screen-question/1`, the `QUESTION` and `SCOPE` texts in `jev_screen.py`): `sha256` `6332a7b4f1c62876…`.
- **Payload:**
  - `state`: the task (≤ 4,000 chars), the query, the step intent (≤ 500 chars), and all passages (id, source header, text);
  - one `noul` question per passage, with that passage's id and full text.
- **Model:** `jev-1.13.0`, a 15 s timeout, 1 retry, each attempt in the ledger.
- **Cases:** `screen-cases-v1.json`, SHA-256 `8f6c8099849e3b49…`. The frozen split is **36 cases** from `handbook-diag-2..4`: 23 with a complete support set present, 58 support passages.
- **Code fingerprints:**
  - `jev_screen.py` `b3e3317d378a2e1b`;
  - `jev_screen_diag.py` `53ecad295ededc7a`;
  - `handbook.py` `07d6c465bb67bc4c`;
  - `configs/exp012.toml` `5d6af644c4117588`.
- **Gate** (all required):
  - eligible results for ≥ 50% of the planned pilot questions: offline **12/12**, already met;
  - support-passage recall ≥ **0.95**;
  - omitted ≥ **20%** of eligible characters;
  - **complete-set criterion:** at most **1** of the 23 frozen cases with a complete support set loses every complete set (so losing a decisive exception or carve-out cannot hide behind aggregate recall);
  - **0** service errors;
  - no provenance or accounting defect.
- **Reference:** the term-match selector, computed on the same inputs.
- **The frozen split runs once.** No tuning follows.

## Component diagnostic: frozen result (run once, `20261013T072006-screen-frozen`)

**Calls and cost:** 36 requests and 36 attempts, **0 errors**, 0 missing answers. Usage was 125,566 input and 3,204 output tokens, with 0.24 s mean latency (8.7 s in total). **USD 0.005274.**

| Frozen set (36 cases) | Jev `result-screen/1` (0.5) | Term-match baseline |
| --- | --- | --- |
| Support-passage recall | **58/58** (95% interval about 0.94–1.00) | 58/58 |
| Cases keeping a complete support set | **23/23** (about 0.86–1.00) | 23/23 |
| Omitted share of eligible characters | **22.3%** | 0% |
| Omitted characters by label: support / context / irrelevant | 0 / 16,710 / **1,804 (all irrelevant text)** | 0 / 0 / 0 |

**Gate:**

| Criterion | Required | Result |
| --- | --- | --- |
| Eligible questions | ≥ 50% | 12/12 |
| Support recall | ≥ 0.95 | 1.00 |
| Omitted | ≥ 20% | 22.3% |
| Complete-set losses | ≤ 1 | 0 |
| Errors | 0 | 0 |

**The component gate passed.** The term selector omits nothing, because every returned passage shares a query term with the query.

**What this shows:** on these author-labelled search results, the screen removed about a fifth of the text without losing a support passage or a complete support set. Most of what it removed is same-subject context that no support set needs, which is not demonstrably useless to an agent. **It does not show any agent-level benefit.**

## Integration smoke (excluded from every comparison)

**Run `20261013T072054-clm_helpers-cacheon-scr-handbook-smoke-1-7f35`** (condition B, `handbook-smoke-1`, an explicitly prompted first search with k = 6):
- **Outcome:** completed, 2/2 questions correct with complete support, 3 model calls.
- **Cost:** **USD 0.038399** (Anthropic 0.038232, TypeSafe 0.000167).

**Verified live:**
- a real Jev call screened an eligible structured result (6 passages, 2,874 characters; probabilities 0.65–0.97, so all were kept);
- the next request held the result with the fixed notice `[result-screen/1: all 6 passages kept]`;
- the saved original was written and its provenance checked;
- both providers' attempts are in the ledger.

**Not exercised live:** unscreened recovery of an omitted passage, because nothing was omitted. It is covered by the sandbox test `test_recovery_reads_are_never_screened_and_are_counted`. The smoke is not repeated to force an omission.

**Measurement fix found by the smoke (before the pilot freeze):** the recovery-read counter missed document reads made with `grep` through a subprocess. Any code that touches `fixtures/handbook` now counts as a direct document read. It is tested, and behaviour is unchanged.

## Pilot freeze (before pilot run 1)

- **Conditions:**
  - **A:** `clm_helpers:on`, ordinary CLM with unscreened search results;
  - **B:** `clm_helpers+scr:on`, the same with `result-screen/1` (threshold 0.5, minimum 2 kept).

  Everything else is identical:
  - `claude-opus-5-5` (effort low), the task text, the tools and the sources;
  - limits: 90 calls, an 8,000-token context budget, a 6,000-character output cap per stream;
  - `blocks/1` layout, prompt caching (5 min), `run-tag/1` isolation.

  Model-controlled context editing is unchanged in both.
- **Instances:** `handbook-dev-1` and `handbook-dev-2`, 6 questions each. Task prompts `5537caab…` and `666c172b…`; truth `76ed06f5…` and `4ca763b0…`.
- **Order** (two-condition alternation): dev-1 A then B; dev-2 B then A.
- **Prompts:** version `2026-10-13.6`; system prompt A `f9e1588f…`, B `37703750…` (B adds `SEARCH_SCREEN_CLAUSE`).
- **Code:**
  - `runner.py` `1086c06c…`;
  - `jev_screen.py` `bc06f7a6…`;
  - `handbook.py` `07e9dc99…`;
  - `prompts.py` `8ed93d60…`;
  - `configs/exp012.toml` `5d6af644…`.

  Since the frozen diagnostic, `jev_screen.py` changed only in the recovery-read counter, and `handbook.py` only in the smoke instance's prompt. The question, payload and selection are unchanged (question hash `6332a7b4…`).
- **Metrics:**
  - strict success and per-question correctness (value plus a complete support set), stale and unsupported citations;
  - screening: blocks, eligible, screened, omitted passages and characters, notice characters, errors and missing answers;
  - recovery: show calls (and omitted ids recovered), saved-file reads, document reads;
  - total cost by provider, elapsed time, Jev latency, main-model calls, tokens, cache reads and writes;
  - context-edit activity.
- **Stopping rules:** the existing compare halts, the per-run reserve (USD 2.00) and the ceiling. No tuning between runs, and no replacement of failed runs.
- **Budget before the pilot:** USD 83.338823 spent of the 88.293391 ceiling. The estimate is about USD 0.15–0.40 per run, so USD 0.6–1.6 for the 4 runs.

## Development pilot result (comparison `20261013T072241`, run once; no run repeated or replaced)

**Cells:** 4/4 completed, not halted, in the frozen order (dev-1: A, B; dev-2: B, A). Table: `analysis/pilot_table.py`, output `analysis/pilot_summary.txt`.

| Instance | Condition | Strict | Questions | Calls | Elapsed s | Cost USD | Context edits | Steps calling `search` | Search blocks (eligible) | Screened | Saved-result reads | Steps reading documents directly |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| handbook-dev-1 | A | yes | 6/6 | 7 | 53.1 | 0.138785 | 4 | 0 | 0 | — | 0 | 6 |
| handbook-dev-1 | B | yes | 6/6 | 8 | 52.2 | 0.126753 | 4 | 0 | 0 | 0 | 0 | 5 |
| handbook-dev-2 | B | yes | 6/6 | 6 | 39.7 | 0.111749 | 4 | 0 | 0 | 0 | 0 | 5 |
| handbook-dev-2 | A | yes | 6/6 | 5 | 33.4 | 0.099807 | 3 | 3 | 5 (3) | — | 3 | 1 |

**Findings:**
- **Screening was never exercised.** Neither B run called `search`: both listed the handbook and read or grepped the documents directly, which both conditions are allowed to do. So no Jev call happened in the pilot, and **B's results say nothing about screening's effect**.
- **The one run that searched** (A, dev-2) ran several searches per execution. Two executions overflowed the 6,000-character output cap; the runtime cut each block back to whole passages and named the missing ones, and Claude then read the saved originals (3 reads). That is a live check of the presentation repair and saved-original recovery, in condition A.
- **Context editing** was active in every run (3–4 accepted edits; one runtime spill in B, dev-1). This pilot tests screening inside a CLM-capable agent; it was not able to test the interaction with screening, because no screening occurred.
- **Costs:** mean cost A USD 0.119296 vs B USD 0.119251; mean calls 6.0 vs 7.0; mean elapsed 43.2 s vs 46.0 s. These are run-to-run differences, not an effect: B had no screening and no Jev cost.

**Why the agent bypassed search (descriptive; not established):** 40 short documents fit into one or two listing and reading steps, so direct reading is cheaper and more complete for the agent than repeated top-5 searches. The B system clause (that results may be screened and passages omitted) may also have discouraged search, but A on dev-1 did not search either.

**Spend for this work:** USD **0.522526**:
- diagnostics USD 0.007033;
- smoke USD 0.038399;
- pilot USD 0.477094.

By provider: TypeSafe USD 0.007200 and Anthropic USD 0.515326. **Ledger:** USD 83.815911 spent of the 88.293391 ceiling, with nothing pending.

**Defects:** none found in the pilot runs.
- **Before any live call:** offline tests found and fixed a runtime notice being re-parsed as passage text.
- **At export:** the exporter's rescoring did not know the new `handbook` task kind. It now keeps the recorded score, as for coding and rounds tasks. Run evidence is unaffected.

---

# Protocol v2 (2026-10-13): document-service workload (`docsvc-gen/1`)

**Why a new version:**
- **What v1 showed:** v1's workload (`handbook-gen/1`) mounted the handbook as files in the sandbox. In both screening runs of the v1 pilot, Claude read those files directly and never searched, so **screening was never exercised**.
- **v1 stays as it was:** its task, configuration, prompts and evidence are unchanged. Its pilot is not evidence for or against screening's effectiveness, and it is not rerun.

**What v2 changes:** v2 models a **document service**.
- **The service boundary:** the corpus exists only in host memory. Claude reaches it only through two runtime actions, `search` and `fetch`. Nothing of the corpus is mounted; the fixture mount holds only a one-line `SERVICE.md`.
- **The same in A and B:** this is a declared service boundary, identical in both conditions and **different from v1's locally mounted task**.
- **Unchanged in both:** normal code execution and CLM context editing, no sandbox network, and no credentials in the sandbox.

## Workload v2 (implemented; uncommitted at the time of writing)

- **Corpus** (`docservice.py`, instances `docsvc-dev-1/2` for the pilot, `docsvc-smoke-1`, `docsvc-diag-1..3`): 74 documents and 232 passages.
  - **16 policy subjects with overlapping vocabulary:** 8 on travel and expenses, 8 on people and facilities. Each has a current policy, a superseded version, an exception memo with a carve-out, and a related-budgets distractor.
  - **Also:** two FAQ documents restating current standard values, and 8 general documents.
  - **Sections** carry subject-specific procedural sentences, **not v1's generic filler** (passage text median 279 characters).
  - **Questions:** 6 per instance, of the same 5 types and with the same support-set rules as v1. Answer documents are not named in the task, and no query sequence is prescribed.
- **Scorer:** `handbook-checks/1`, unchanged; it was re-validated for v2 with correct, missed-exception and superseded-version answers.
- **Actions** (both conditions, runtime-handled, one model step each):
  - `{"action": "search", "query": ..., "k": 1-8 (default 5)}` returns the v1 structured block (`=== <id> | <title> — <heading> | <meta>`) and saves the original (`.txt`, `.json`) under `/task/workspace/search-results/`;
  - `{"action": "fetch", "ids": [...]}` (≤ 10 passage or document ids) returns passages as `<<passages (unscreened): ...>>`.

  Both are capped at the existing 6,000-character output cap, with whole passages only.
- **What is screened:** only `search` results. Fetches, saved results read by code, any `execute` output, errors, runtime notices and context edits are never screened.

## Screening policy: unchanged, with one documented presentation adaptation

- **Unchanged:** `result-screen/1`, with the frozen question (`sha256 6332a7b4…`), payload, threshold 0.5, minimum of 2 kept, eligibility (≥ 3 passages, ≥ 2,000 characters), failure handling, and `jev-1.13.0`.
- **The adaptation:** v1's notice and system clause name `show()`, which does not exist in the service, so in v2 the notice reads `unscreened: fetch([...]) or <saved path>`, and B's clause is `SEARCH_SCREEN_SERVICE_CLAUSE` (the same text, naming the fetch action). v1's texts are unchanged.
- **Step intent:** the search action's `thought`.

## Offline checks v2 (no Jev; `analysis/v2_service_cases.py`, outputs `analysis/v2_opportunity_summary.txt`)

| Ordinary queries at k = 5 | Pilot instances (12 questions, 24 queries) | Compatibility instances (18 questions, 36 queries) |
| --- | --- | --- |
| Result size, characters | median 2,119 (1,955–2,504) | median 2,081 (1,853–2,400) |
| Eligible results | 21/24; every question has one | 26/36; 16/18 questions |
| Results holding a complete support set | 16/24 | 21/36 |
| Eligible characters: support / context / irrelevant | 24% / 74% / 2% | 22% / 74% / 4% |

**Findings:**
- **Results mix needed and not-needed passages,** but nearly all of them are about the same subject. A larger corpus does not make results more off-topic.
- **Ordinary results sit near the 2,000-character eligibility line,** so eligibility is common but not universal.

**Boundary and capability checks (tests in `tests/test_docservice.py`):**
- **The corpus is unreachable from the sandbox.** A whole-filesystem `grep` for corpus text finds nothing, and `/task` holds only `SERVICE.md` and the context file.
- **Fetch returns full passages or documents, unscreened.**
- **Ids and citations survive** search, screening and fetch.
- **A and B receive identical pre-screening blocks.**
- **Execute output is never screened.**
- **Context edits still drive the next request.**

## Compatibility diagnostic (fresh, small; frozen before any Jev call)

- **Why:** the service changes the corpus and the source of the step intent, though not the passage structure.
- **Cases:** `screen-cases-v2-service.json` (SHA-256 `0d0f3de9fc01897a…`): 36 cases from `docsvc-diag-1..3`, **26 eligible** (only eligible cases are sent). Labels come from generator truth, written before any answer.
- **Policy:** exactly `result-screen/1` as frozen; no development tuning.
- **Predeclared compatibility criteria** (reported separately from v1's gate):
  - support-passage recall ≥ 0.95;
  - at most 1 eligible case with a complete support set loses every complete set;
  - 0 service errors.

  The omitted share is **reported, not required**. The tool's built-in v1 gate field (which includes ≥ 20% omission) is shown for reference only.
- **It runs once.**

### Compatibility diagnostic result (run once, `20261013T081130-screen-frozen`)

**Calls and cost:** 26 eligible requests, 0 errors, 0 missing answers. Usage was 89,252 input and 2,314 output tokens, at 0.25 s mean latency. **USD 0.003747.**

| v2 compatibility (26 eligible cases) | Jev `result-screen/1` | Term-match baseline |
| --- | --- | --- |
| Support-passage recall | **28/28** | 28/28 |
| Cases keeping a complete support set | **16/16** | 16/16 |
| Omitted share (reported) | **23.1%**: all 1,965 irrelevant characters, plus 10,891 context | 0% |

**All predeclared compatibility criteria are met.**

**What the screen omitted:** mostly `§1 Scope` and `§1 Purpose` sections, and some same-subject memo sections. Several scored 0.43–0.49, just under the threshold. **The policy is compatible with the service workload. Nothing was tuned.**

## v2 integration smoke (excluded from every comparison)

**Run `20261013T081206-clm_helpers-cacheon-scr-docsvc-smoke-1-e31d`** (condition B, `docsvc-smoke-1`, an explicitly prompted first search with k = 6):
- **Outcome:** completed, 2/2 questions correct with complete support, 4 model calls.
- **Cost:** **USD 0.033546** (Anthropic 0.033227, TypeSafe 0.000319). All 6 ledger attempts are recorded.

**Verified live:**
- **Two real service searches,** both eligible, both screened by real Jev calls. SR-001 kept all 6 passages; SR-002 kept 5 of 6 and omitted `HB-58 §1` (a memo's Purpose section, probability 0.48).
- **The next request held SR-002** with the fixed notice: `[result-screen/1: kept 5 of 6 passages (2,171 of 2,577 chars); omitted HB-58 §1; unscreened: fetch(['HB-58 §1']) or …/SR-002.txt]`.
- **Recovery:** as the smoke prompt asked, Claude then **fetched `HB-58 §1`**, which came back unscreened (`<<passages (unscreened): …>>`) and was counted as an omitted passage recovered. This recovery was prompted by the smoke instructions, not spontaneous.

**The service boundary held** (the grep test). **No separate scripted recovery check was needed.**

## v2 pilot freeze (before pilot run 1)

- **Conditions:**
  - **A:** `clm_helpers:on`, ordinary CLM using the document service;
  - **B:** `clm_helpers+scr:on`, the same with `result-screen/1` (0.5, minimum 2, `jev-1.13.0`) on eligible search results.

  Identical in both:
  - `claude-opus-5-5` (effort low), the task text and the service actions;
  - limits: 90 calls, an 8,000-token context budget, a 6,000-character output cap;
  - `blocks/1` layout, caching (5 min), `run-tag/1` isolation;
  - ordinary CLM editing.

  No queries, result counts or edits are prescribed.
- **Instances (fresh):** `docsvc-dev-1` and `docsvc-dev-2`. Task prompts `2e8f74c4…` and `fe5f9b0b…`; truth `4facb63e…` and `de90df52…`; corpora `42f26b13…` and `37a578a0…`.
- **Order:** dev-1 A then B; dev-2 B then A.
- **Prompts:** version `2026-10-13.7`; system prompt A `f9e1588f…` (identical to v1's A), B `1c05e629…` (`SEARCH_SCREEN_SERVICE_CLAUSE`).
- **Code:**
  - `runner.py` `44c11c39…`;
  - `jev_screen.py` `03f0a216…`;
  - `docservice.py` `29a6fa85…`;
  - `prompts.py` `199e2a73…`;
  - `configs/exp012v2.toml` `d48c4326…`.

  The question hash is `6332a7b4…`, unchanged.
- **Metrics:**
  - correctness and evidence completeness;
  - searches, fetches and recovery;
  - eligible and screened results, kept and omitted passages and characters, notice characters;
  - needed evidence omitted (evaluator-only, against truth, afterwards) and later fetched;
  - cost by provider, elapsed time, Jev latency, main-model tokens and cache use;
  - context edits and when they happened;
  - errors and fallbacks.
- **Stopping rules:** the existing compare halts, the per-run reserve (USD 2.00) and the ceiling. No tuning or replacement.
- **Budget before the pilot:** USD 83.853203 spent of the 93.815911 ceiling. The estimate is USD 0.15–0.40 per run.

## v2 development pilot result (comparison `20261013T081314`, run once; no run repeated or replaced)

**Cells:** 4/4 completed, not halted, in the frozen order (dev-1: A, B; dev-2: B, A). Table: `analysis/v2_pilot_table.py`, output `analysis/v2_pilot_summary.txt`.

| Instance | Cond. | Strict | Calls | Elapsed s | Cost USD (Anthropic + TypeSafe) | Searches (eligible) | Fetches (ids) | Screened | Passages omitted | Omitted passages fetched back by id / by any fetch | Context edits (steps) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| docsvc-dev-1 | A | 6/6 | 16 | 70.3 | 0.124155 | 6 (5) | 4 (10) | — | — | — | 5 (2, 5, 8, 11, 14) |
| docsvc-dev-1 | B | 6/6 | 16 | 75.8 | 0.121745 + 0.000944 | 6 (6) | 4 (9) | 6/6 | 4 | 4 / 4 | 5 (2, 5, 7, 10, 13) |
| docsvc-dev-2 | B | 6/6 | 19 | 80.3 | 0.137606 + 0.000901 | 6 (6) | 7 (18) | 6/6 | 10 | 6 / 8 | 5 (4, 8, 10, 13, 16) |
| docsvc-dev-2 | A | 6/6 | 13 | 51.6 | 0.113186 | 6 (6) | 1 (3) | — | — | — | 5 (2, 4, 6, 8, 10) |

**Means (2 runs each):**

| | A | B |
| --- | --- | --- |
| Cost USD | 0.118670 | 0.130598 (TypeSafe 0.000922) |
| Elapsed s | 61.0 | 78.0 |
| Calls | 14.5 | 17.5 |
| Fetches | 2.5 | 5.5 |
| Cache-read tokens | 37,798 | 50,927 |
| Cache-write tokens | 12,916 | 14,162 |
| Uncached input tokens | 1,650 | 1,990 |
| Output tokens | 1,996 | 2,036 |

**Screening was exercised:**
- **Coverage:** all 12 searches in B were eligible and screened, with 12 Jev requests, **0 errors**, 0 missing answers, about 0.25 s each and 1.5 s per run.
- **Volume:** 28,217 screened characters, 22,655 kept (19.7% omitted), plus 1,744 notice characters.
- **What was omitted:** 14 passages, mostly `§1 Scope` and `§1 Purpose` sections.
- **No needed evidence was lost.** Evaluator-only check, after the run, against the exported truth: **none of the 14 omitted passages is in any valid support set.**

**Claude's reaction (spontaneous; not prompted):**
- **Most omitted passages were fetched back:** 10 by id (4/4 on dev-1, 6/10 on dev-2), plus 2 more inside whole-document fetches. None of them was needed.
- **On dev-2,** B made 7 fetches where A made 1 (6 more calls).
- **On dev-1,** B made the same number of fetches as A (4), but each of B's fetches included an omitted passage.

**Correctness:** every run answered 6/6 with complete support, in both conditions.

**Total efficiency:** **B cost more**: USD +0.0119 per run (+10%), +3 calls and +17 s on average. Jev's own cost and latency are small; the extra cost is Claude's recovery fetches and the longer context they bring (more cache reads). These are 2 runs per condition, so this is no estimate of an effect. But **no saving survived the full overhead** in either instance pair: dev-1 −1.2% (about equal), dev-2 +22%.

**Context editing:** active in every run, with 5 accepted edits each, typically right after each search or fetch to replace the raw result with a note. Screening and context editing therefore interacted naturally; there were no pressure steps, recoveries or spills.

**Defects:** none.

**Spend for v2:**
- compatibility diagnostic USD 0.003747;
- smoke USD 0.033546;
- pilot USD 0.498537 (from the run summaries);
- **ledger total USD 0.535821.**

**Ledger:** USD 84.351732 spent of 93.815911, with nothing pending.
