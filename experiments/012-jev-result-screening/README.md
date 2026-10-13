# 012 – Jev screening of incoming tool results

**Status:**
- **Offline assessment:** done.
- **Document-search implementation:** built.
- **Component diagnostic:** gate **passed**.
- **Integration smoke:** passed.
- **Four-run development pilot:** complete. All 4 runs succeeded, but **screening was never exercised**, because Claude did not use search in the screening condition.
- **Not run:** no larger evaluation.

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
