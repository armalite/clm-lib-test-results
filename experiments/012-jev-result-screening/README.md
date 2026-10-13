# 012 – Jev screening of incoming tool results

**Status:**
- **v1** (local handbook, `handbook-gen/1`): the component gate passed and the smoke passed. **In its pilot, screening was never exercised:** Claude read the mounted files instead of searching. v1 is kept unchanged and is not evidence for or against screening.
- **v2** (document service, `docsvc-gen/1`): the compatibility diagnostic met its criteria and the smoke passed. **In its pilot, screening was exercised** (12/12 searches screened in B). All runs were correct, no needed passage was omitted, and Claude fetched most omitted passages back, so **B cost about 10% more**.
- **Not run:** no larger evaluation.

## v2: document-service workload (2026-10-13)

**What changed and why:**
- **v1 exposed the corpus as files,** so agents bypassed search.
- **v2 models a document service.** The corpus is held only by the runtime, and Claude reaches it only through `search` and `fetch` actions: a declared service boundary, identical in A and B. Claude still writes code and edits its context normally.
- **The corpus:** 74 documents, 16 overlapping policy subjects, subject-specific text without generic filler.
- **Unchanged:** the questions, the scorer and the screening policy. The only adaptation is that the notice says `fetch([...])` instead of `show([...])`.

**Comparison:**
- **A:** ordinary CLM with unscreened search results.
- **B:** the same, with `result-screen/1` on eligible search results.

Fetches and saved results are never screened.

**Offline:** ordinary k = 5 searches return about 2,100 characters; 21/24 pilot queries were eligible. Results mix needed passages (24% of text) with same-subject context (74%); only 2% is off-topic.

| v2 compatibility diagnostic (26 eligible labelled results, run once) | Jev | Term-match baseline |
| --- | --- | --- |
| Support passages kept | 28/28 | 28/28 |
| Complete evidence sets kept | 16/16 | 16/16 |
| Text omitted | 23.1% | 0% |

**Smoke (B):**
- **Searches:** two real searches, both screened; one passage was omitted with the notice.
- **Recovery:** Claude fetched the omitted passage back unscreened, as the smoke prompt asked.

| v2 development pilot (mean of 2 runs per condition) | A | B |
| --- | --- | --- |
| Strict success (6 questions each) | 2/2 | 2/2 |
| Cost USD (all providers) | 0.118670 | 0.130598 |
| Elapsed s | 61.0 | 78.0 |
| Model calls | 14.5 | 17.5 |
| Searches / fetches | 6.0 / 2.5 | 6.0 / 5.5 |
| Searches screened | — | 6/6 per run |
| Text omitted by screening | — | 19.7% of screened characters (plus notices) |
| Omitted passages needed by any answer (evaluator-only) | — | **0 of 14** |
| Omitted passages fetched back | — | 12 of 14 (10 by id) |
| Context edits per run | 5 | 5 |

**What it shows:**
- **The integration works during real task execution.** Screening was exercised and lost no needed evidence.
- **No efficiency gain:** the screen removed text the answers did not need, but Claude then fetched most of it back, so B used more calls, time and money.
- **This is a completed test with no benefit.** It is two development instances, not an evaluation.

**The earlier v1 sections follow, unchanged.**

## v1: local-corpus workload

**Question:** can Jev screen document-search results before they enter Claude's context, reducing total work while preserving task correctness? Screening is a filter beside CLM; Claude still makes every working-context edit.

## The comparison

- **Task:** answer 6 questions about a synthetic 40-document handbook, with current and superseded versions, exception memos with carve-outs, additions, and a FAQ that restates values. Each answer needs a value and the passages that support it.
- **Tools:** `search(query, k)` returns ranked passages with ids, and saves each original result. `show(ids)` and direct document reading are unscreened. Both are the same in every condition.
- **A:** ordinary CLM with unscreened search results.
- **B:** the same, with `result-screen/1`.
  - **Eligible:** a search result with ≥ 3 passages and ≥ 2,000 characters.
  - **Screening:** Jev scores every passage, given the task, the query and the step's intent. Passages scoring below 0.5 are omitted, at least 2 are always kept, and a fixed notice names the omitted ones and the saved original.

## Results

**Kept separate:**
1. **Component accuracy:** labelled search results, TypeSafe only.
2. **Working integration:** the smoke.
3. **End-to-end effect:** the pilot.

| Component diagnostic (frozen, 36 cases, run once) | Jev `result-screen/1` | Term-match baseline |
| --- | --- | --- |
| Support-passage recall | **58/58** | 58/58 |
| Cases keeping a complete support set | **23/23** | 23/23 |
| Eligible characters omitted | **22.3%** (all irrelevant text and some same-subject context) | 0% |

**The gate passed.** Two caveats:
- **The threshold** was raised from the draft 0.3 to 0.5 using only the development answers: at 0.3, only 5% was omitted. It was then frozen.
- **Little to remove:** offline, only 1–2% of eligible text was clearly irrelevant. Most of what the screen omits is same-subject context that no answer needs.

| Development pilot (2 instances × A/B, run once) | A | B |
| --- | --- | --- |
| Strict success | 2/2 (6/6 questions each) | 2/2 (6/6 each) |
| Mean cost USD (all providers) | 0.119296 | 0.119251 |
| Mean elapsed s / model calls | 43.2 / 6.0 | 46.0 / 7.0 |
| Steps calling `search` | 3 (one run) | **0** |
| Search results screened / Jev calls | — | **0 / 0** |
| Context edits (accepted) | 7 | 8 |

**What happened:**
- **Search was bypassed:** in 3 of 4 runs, including both B runs, Claude listed and read the handbook files directly instead of searching. With 40 short documents that is cheaper and more complete, so **no search result reached the screen.**
- **The one searching run** (A) overflowed the output cap twice. It was cut back to whole passages, and Claude read the saved originals.

**Savings:** none, because nothing was screened.

**Spend:** USD **0.522526** in total. Details, evidence and limitations are in [`protocol.md`](protocol.md); the analysis scripts and outputs are in `analysis/`.
