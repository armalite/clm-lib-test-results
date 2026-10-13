# Provenance of `../pilot-edit-review.md`

**The question:** what changed in the review after its first export, and when relative to Jev's verdicts.

**The first exported version is recovered.** [`pilot-edit-review.as-first-exported.md`](pilot-edit-review.as-first-exported.md) was reconstructed from the author's session record of the command that wrote the file. Its SHA-256 is `bd3b6845f2d9499828a8cd3c79ac46c8d73ac1ee4a3da07b681d3ab6a066a4a1`, **identical** to the checksum the first export recorded for `analysis/pilot-edit-review.md`, so it is the exported text byte for byte.

**Chronology** (UTC, 2026-10-13, from the session record's timestamps):

| Time | Event |
| --- | --- |
| 06:00:17 | the model's step-23 thought ("P5 flagged …") seen while comparing P5 and P6. Already disclosed in the review: P5's classification is not blind |
| 06:00:43 | Part 1 (the blind classification) written |
| 06:00:50 | **Jev's verdicts first read** |
| 06:01:57 | first export, which computed the checksum above; Part 1 was still unchanged |
| 06:03:49 | **after the verdicts:** Part 1's closing paragraph replaced, and Part 2 appended |
| 06:03:59 | **after the verdicts:** one line of that new paragraph corrected |
| (session 12) | re-export: the checksums regenerated for the current file |

**What the later edits changed** ([`pilot-edit-review.post-export.diff`](pilot-edit-review.post-export.diff)):
- **Classifications:** unchanged. Every Part 1 table row, class and example is identical, and so is the conclusion "no harmful context edit (rule-level loss or change) occurred in any condition".
- **Wording:** one Part 1 paragraph was replaced. The original read: "Task-code changes and context-only changes were made in separate steps or in the same step as the proposal. Code was always written (and tested) before the notes that describe it were compacted." It became per-condition counts of where code and context changes happened (A 10/10 in the same execution, B 7/7 in the same step, C 8/8 applied proposals from context-only steps). This is a **factual** statement from the step accounting, written **after** the verdicts had been read; it is not a relevance or harm judgement. The removed sentence was vaguer and, for A, imprecise: A wrote, tested and compacted in one execution.
- **Added:** Part 2, written entirely after the verdicts and labelled as such.

**What the checksums do and do not show:**
- **They do show integrity:** the regenerated checksums verify that the current file is the one exported.
- **They do not show chronology:** they cannot show when parts were written relative to the verdicts. The table above, and the recovered first version, are the record for that.
