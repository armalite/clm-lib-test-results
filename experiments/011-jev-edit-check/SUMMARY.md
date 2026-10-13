### [011 – Can Jev check a proposed context rewrite? (component diagnostic)](experiments/011-jev-edit-check/README.md)

- **Question:** can Jev detect important information incorrectly lost or changed in a proposed context rewrite? Jev saw the task, the current context, any released update and the proposed replacement, and answered three narrow questions (`lost`, `changed`, `evidence`). There were no agent runs and no main-model calls.
- **Cases:** 8 development and 36 frozen (16 harmful, 16 acceptable, 4 ambiguous), from 10 families. They include real and deliberately altered 010 incident edits, and a CSV → JSON example from the planned W2 workload. The labels are author-created and were written before any answer.
- **Frozen result** (run once, threshold 0.5): **16/16** harmful detected and **3/16** acceptable falsely flagged. The deterministic checks managed 7/16 and 3/16.
- **Readiness gate:** **failed** (at most 2 false flags allowed).
- **The false-flag pattern:** two of the three were real edits whose new content came from tool output the checker never saw.
- **Cost and latency:** about USD 0.00006 and 0.24 s per check; USD 0.0026 in total.
- **What it means:** Jev's narrow checks look promising on these cases, but this design is not pilot-ready. A v2 would need the checker to see the tool observations that justify an edit, with fresh cases.
