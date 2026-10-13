# 010 v2: offline audit of review applicability (2026-10-13, before any v3 code or paid call)

**What this covers:** all 48 started reviews, plus 5 rejected review attempts, in the four v2 B/C calibration runs (comparison `20261012T213922`).

**How it was produced:** read from the raw run artifacts (`summary.json → initiated_review`, `events.jsonl` and the `context/rev-*.json` revisions). The script is `v2-review-audit.py`, and the per-review data is in `v2-review-audit.json`.

**Status of the classifications:** they are **exploratory**, based on text heuristics. No score is changed, and no loss in an edit is inferred from final answers.

## Counts

| | |
| --- | --- |
| Started reviews | 48 (B 23, C 25), **all labelled `compaction`** by Claude |
| Rejected review attempts | 5 (B dev-2, steps 16–20): `purpose: "update"` sent **without** `new_information` |
| Why C skipped Jev | 25 of 25: purpose `compaction`, recorded as `not_applicable` (B has no Jev by design) |
| Reviews with at least one candidate entry | 48 / 48 (44 with at least one note) |
| Reviews before the last round | 47 / 48 |
| Latest released round had board or change-log lines | 42 / 48 (34 with a status, cause or follow-up change line) |
| The same latest round reviewed more than once in a run | 8 (run, round) pairs |

## What the authorised edits did (exploratory)

| Class (heuristic) | Edits |
| --- | --- |
| Incorporated newly released findings (new cause, follow-up or change ids, or a new round tag in the notes) | **36** |
| Pure compaction (notes not extended; runtime step entries removed) | 9 |
| Notes extended with other content | 3 |

## Examples (including pure compaction)

- **"Compaction" that incorporated changes** (B, `rounds-dev-1`, review at step 31, round 8).
  - **The latest round's lines:** thread A resolved; thread B's cause revised to UPSTREAM_RATE_LIMIT, superseding CACHE_STAMPEDE; thread C opened.
  - **The authorised edit:** it rewrote the rolling note to add the round-8 findings, including thread C's likely BAD_CONFIG_ROLLOUT from CHG-120.
- **"Compaction" while adding the first follow-ups** (C, `rounds-dev-1`, step 6, round 2). The thought was "Compact context with notes", and the edit recorded three newly opened follow-ups and the change records CHG-116, -120 and -121.
- **Pure compaction** (C, `rounds-dev-1`, step 35, round 9). Seven runtime entries were removed (4,840 → 2,794 characters) and the notes were not extended. The latest round still had board lines (thread B mitigated).
- **Empty latest round** (B, `rounds-dev-1`, step 27, round 7): the round had no board update lines and no change log. The edit recorded "board empty" and log findings.

## Conclusion

The mismatch is real and is an implementation issue, not a Jev result.
- **The rule was too narrow:** v2 let Claude's label decide whether Jev ran. Claude used "compaction" for edits that mostly incorporated new evidence.
- **The one alternative didn't work in practice:** the only route to Jev (purpose `update` plus self-written `new_information`) was attempted 5 times without the field and rejected each time.
- **Inputs for v3 existed:** a runtime-supplied update (the latest released round's board and change-log lines, `round-files/1`) was available at 42 of 48 reviews, with candidate entries at all 48. This supports v3's correction: make the update source deterministic and independent of Claude's label.
