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
