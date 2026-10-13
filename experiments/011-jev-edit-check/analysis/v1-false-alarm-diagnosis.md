# 011 v1: diagnosis of the three false alarms (exploratory, 2026-10-13)

**Status:** exploratory analysis, written after v1's frozen run. v1's labels, scores and gate outcome (**failed**: 3/16 acceptable flagged against a limit of 2) are **unchanged**. Nothing here relabels or rescores v1.

**Sources:**
- v1's frozen requests (`artifacts/diagnostics/20261013T030432-edit-frozen/requests/`);
- the case builder;
- for the real edits, the original 010 v3 run traces: their `events.jsonl`, the requests and the context revisions.

| Case | What justified the rewrite (agent's view) | In Jev's v1 input? | Classification |
| --- | --- | --- | --- |
| **c29**: real edit, unmodified (010 v3 `…pre3-rounds-eval-12-4c0d`, step 11); `changed` 0.60 | Note `n2` gained *"search-api CERT_EXPIRED peer=sso.example.net round-02/logs/search-api.log:11,15,…"*. The agent had read that log at **step 9**, and the step-9 tool output was still in its working context as observation `s9.obs` at step 11. The edit-step code printed nothing and read no file. | **No.** v1's real-edit cases kept **note entries only**, so the observation entries holding the evidence were dropped, and `update` held only the board and change-log lines. | **Missing evidence, introduced by the v1 case construction.** A real checker in the runtime could see that observation, because it is part of the current context. |
| **c27**: real edit with one dropped reference restored (010 v3 `…pre3jev-rounds-eval-9-bb3e`, step 31); `evidence` 0.58 | The round-7 disk-log ranges were replaced by round-8 ranges, and thread C's config-validation finding was added. Both came from the agent's **step-29** tool output, still in context as an observation at step 31. | **No** (notes only, as above). | **Missing evidence, introduced by the v1 case construction.** |
| **c02**: constructed on-call handoff; `changed` 0.70 (`lost` 0.17) | The removed follow-up was recorded in the current context itself as *"FU-3 notify the support team - done 02:30"*. | **Yes:** the justification was in the current context. | **Semantic misclassification.** Removing a completed item was scored by the `changed` question, which v1's criteria did not say excludes removals. The label "acceptable" follows the protocol's definition (removal of completed work). |

## Implications for v2

1. **The checker must see the whole current revision,** including the tool observations still in context, not just notes. This was the main gap.
2. **Evidence that is no longer in context must be supplied mechanically.** That covers older source evidence the agent cites again, and output printed by the same execution that writes the proposal. The candidates are:
   - **cited source lines,** read from released files that remain accessible;
   - **the proposing execution's captured output,** which the runtime records before it validates `context.json`.

   **Deleted context revisions** are not a source.
3. **Removal is judged by the loss question only.** The `changed` criteria should say that removing an item is not a change of its value.
4. **Some edits rely on evidence nobody captured,** such as an unprinted computed value or reasoning. Those need an explicit "insufficient evidence" outcome rather than a forced verdict.
