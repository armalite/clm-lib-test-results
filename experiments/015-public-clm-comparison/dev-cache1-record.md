# 015 – `dev-cache1` record: guarded-clm's original and recommended caching configurations

_Run 2026-10-23, under [dev-cache1-protocol.md](dev-cache1-protocol.md) (sha256 `45c834b6e712d0a2836e8dc74d12d248819ad52fe3b3324e85ea481b441c8394`, in both freeze records). Two live sessions, one per configuration, on docthread-dev-1. Readiness: [dev-cache1-readiness.md](dev-cache1-readiness.md)._

## In short

- **Both sessions completed all eight turns,** and the provider accepted all 70 requests. A scored 9/10, B 10/10, recall 3/3 each.
- **B reused its working context as designed,** within turns and at every new-turn start. Every one of B's 36 requests read exactly the prefix that the documented caching rules make eligible. A read only its tools and system prompt, as predicted.
- **After each of B's six accepted edits,** the next request fell back to the furthest earlier boundary that was still unchanged: three times to the first request's head, and three times to a later marker.
- **B cost US$0.613616 against A's US$1.129792,** although B did more work: 25% more input tokens, 22% more output tokens and two more calls. One pair of sessions is not an average saving.

## What ran

| | A (original) | B (recommended) |
| --- | --- | --- |
| launch | `dev-cache1-a` | `dev-cache1-b` |
| request layout | `single` | `segmented_task_last` |
| context cache point | none | 5m |
| message-level caching | automatic (5m) | none |
| tool and instruction breakpoints | 5m each | 5m each |
| contract sha256 | `5c602af565577760…` | `12b47d9c11564f5a…` |
| frozen | 2026-10-23T01:43:22Z | 2026-10-23T01:53:08Z |
| session | 01:43:30Z to 01:46:37Z (187 s) | 01:53:09Z to 01:56:51Z (222 s) |
| block stop (effective) | US$2.50 | US$2.50 |

- **Shared:** guarded-clm 0.2.0.dev2 at d1d6d1d (source `5da97515…`, installed metadata 0.2.0.dev2, clean), clm-lib 8fcec77 and clm-lib-test-results 6baeaa8c (both clean at freeze), and confirm1's shared settings. Freeze records: [A](dev-cache1-a-freeze-record.json), [B](dev-cache1-b-freeze-record.json).
- **Order and gap:** A ran first. B's first attempt came **397 s** after A's last ledger entry (01:46:37Z to 01:53:14Z); at least 360 s was required. B's first request read nothing, so it did not reuse A's tool-definition cache entry.
- **The procedure:** an ignored, resumable script ran A, checked it for defects, waited, then planned, froze and ran B. The key was loaded only in that process, through the documented `api.env` procedure with tracing off. Nothing was stopped or rerun, and no source changed during the runs.

## Results

| | A | B |
| --- | --- | --- |
| outcome | complete, 8/8 turns | complete, 8/8 turns |
| points (recall) | 9/10 (3/3) | 10/10 (3/3) |
| missed | question 4's evidence field (a reformatted journal line) | none |
| attempts | 34, all accepted | 36, all accepted |
| provider errors, retries | none | none |
| task tool calls by turn | 11, 7, 1, 16, 1, 3, 0, 1 (40) | 12, 7, 0, 26, 1, 2, 0, 1 (49) |
| accepted edits | 4 | 6 |
| held-back outputs, refetches | 0, 0 | 7, 4 |
| requests at PRESSURE | 4 | 5 |
| over-limit requests | 0 | 0 |
| input tokens | 461,038 | 577,450 |
| output tokens | 15,118 | 18,407 |
| summed model latency | 182.1 s | 217.0 s |
| confirmed cost | **US$1.129792** | **US$0.613616** |

**Spend:** US$1.743408 in all, every charge confirmed from provider usage; none was assumed and no reservation is open. The ledger now stands at US$109.561054 spent of its unchanged US$131.657076 ceiling; programme 015 at US$21.461308 of US$43.55733.

| | allowance | spent | remaining |
| --- | --- | --- | --- |
| A block | 2.50 | 1.129792 | 1.370208 |
| B block | 2.50 | 0.613616 | 1.886384 |
| programme 015 | 43.55733 | 21.461308 | 22.096022 |

## Cache use per call

The per-call tables come from the predeclared [dev-cache1-analysis.py](dev-cache1-analysis.py): [dev-cache1-analysis.md](dev-cache1-analysis.md) and [.json](dev-cache1-analysis.json).

| call class | A attempts | A read share | B attempts | B read share |
| --- | --- | --- | --- | --- |
| first | 1 | 0.00 | 1 | 0.00 |
| ordinary | 22 | 0.155 | 22 | **0.771** |
| new-turn start | 7 | 0.169 | 7 | **0.945** |
| after an accepted edit | 4 | 0.243 | 6 | 0.440 |
| retry | 0 | not exercised | 0 | not exercised |

- **A:** every request after the first read exactly 2,292 tokens, the tools and system prompt, and wrote the rest of its single block. 84% of its input was written (385,368 of 461,038 tokens).
- **B:** each ordinary call and new-turn start read the previous request's cached prefix, and wrote only what was appended. The task and status, 318–512 tokens per request, were sent as uncached input.
- **Over the whole session:** A read 16.4% of its input from cache (75,636 of 461,038 tokens), B 75.7% (437,408 of 577,450).
- **Within turns:** demonstrated (22 of 22 ordinary calls read the previous marker).
- **At new-turn starts:** demonstrated (7 of 7). A new turn wrote only 165–563 tokens: the previous answer, the previous question and the first step's entries.

## Observed reads against the predicted boundaries (post hoc)

[dev-cache1-boundary-check.py](dev-cache1-boundary-check.py) was written after the run, not predeclared. Its output is [dev-cache1-boundary-check.txt](dev-cache1-boundary-check.txt). For each request it computes the furthest eligible earlier breakpoint under the documented rules, using only the recorded requests and the provider's own token figures.
- **A:** 33 of 33 requests after the first read the predicted tools-and-system prefix.
- **B:** **36 of 36 read exactly the predicted prefix.**
- **The figures are the provider's;** the match is between them and a rule applied to the recorded requests. B's head marker covered 80 more tokens than A's tools-and-system prefix: the first user block and its message framing.

## After accepted edits (B)

Each edit deleted earlier steps' entries (most also added a note). The next request read:

| edit at step | entries deleted | next request read | from |
| --- | --- | --- | --- |
| 5 | s2–s4 | 4,223 | attempt 1's marker (after s1.obs, the last unchanged entry) |
| 11 | s1, s7–s11 | 2,372 | the first request's head (the first entry changed) |
| 15 | s13–s15 | 11,237 | attempt 15's marker |
| 19 | s12, s16–s19 | 2,372 | the head |
| 22 | s21, s22.act (the latest steps) | 8,227 | attempt 23's marker |
| 23 | s20, a note | 2,372 | the head |

- **Observed:** after an edit, reuse ended at the furthest earlier marker whose prefix was unchanged. Where no earlier request had a marker inside the unchanged text, B fell back to the head. On the next ordinary call it read the new prefix again.
- **Inferred:** the size of each fallback depends on where earlier markers happened to fall, not on how much text stayed unchanged. The record does not show how much unchanged text lay past each reused boundary.
- **A** wrote its whole user block after every edit, as on every call.

## How much of the cost difference is the configuration

| | A | B |
| --- | --- | --- |
| written | 0.963420 | 0.309912 |
| read | 0.015127 | 0.087482 |
| uncached input | 0.000068 | 0.032154 |
| output (incl. thinking) | 0.151180 | 0.184070 |
| total | 1.129795 | 0.613618 |

_Component sums at the dated prices; the confirmed totals differ only by rounding._

- **Volume, not only price:** B processed more input (+116k tokens, +25%) and output (+3.3k, +22%), with 9 more task calls. Its 7 holds and 4 refetches are a likely, but not established, part of that. So the configurations' costs are not on the same work.
- **Same requests, other billing (an estimate):** billed the way A's configuration bills (tools and system read, everything else written), B's own input would have cost about US$1.26 instead of US$0.43. Most of the difference comes from that change in billing.
- **Output:** B's larger output made it US$0.033 dearer, which offsets a little.
- **Not established:** a typical saving. That needs more sessions; this pair shows the mechanism works and gives one data point.

## What this does and doesn't show

- **Shown:**
  - the recommended configuration was accepted by the provider;
  - its cached working context was read on every ordinary call and every new-turn start, exactly at the predicted boundaries;
  - edits invalidated reuse in the documented way;
  - neither configuration had any provider or harness failure.
- **Not shown:**
  - that B's higher score or extra tool use come from the configuration (one session each, and B changes the order, segmentation and marker together);
  - a typical cost difference;
  - behaviour on other instances.
- **Not exercised:** retries, rejected edits, over-limit allowances, output truncation and the `p015-turn-endings/2` continuation. This record does not schedule another run.
