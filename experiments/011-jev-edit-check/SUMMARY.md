### [011 – Can Jev check a proposed context rewrite? (component diagnostic)](experiments/011-jev-edit-check/README.md)

- **Question:** can Jev detect important information incorrectly lost or changed in a proposed context rewrite? Jev saw the task, the current context, any released update and the proposed replacement, and answered three narrow questions (`lost`, `changed`, `evidence`). There were no agent runs and no main-model calls.
- **Cases:** 8 development and 36 frozen (16 harmful, 16 acceptable, 4 ambiguous), from 10 families. They include real and deliberately altered 010 incident edits, and a CSV → JSON example from the planned W2 workload. The labels are author-created and were written before any answer.
- **Frozen result** (run once, threshold 0.5): **16/16** harmful detected and **3/16** acceptable falsely flagged. The deterministic checks managed 7/16 and 3/16.
- **Readiness gate:** **failed** (at most 2 false flags allowed).
- **The false-flag pattern:** two of the three were real edits whose new content came from tool output the checker never saw.
- **Cost and latency:** about USD 0.00006 and 0.24 s per check; USD 0.0026 in total.
- **What it means:** Jev's narrow checks look promising on these cases, but this design is not pilot-ready. A v2 would need the checker to see the tool observations that justify an edit, with fresh cases.

**v2, evidence-complete (2026-10-13):**
- **v1's false alarms diagnosed:** two came from v1's notes-only cases dropping the context observations that held the evidence; one was a removal scored as a change.
- **The v2 checker input** (`edit-evidence/1`) is built mechanically:
  - the full current revision (including tool observations);
  - the released update;
  - the proposing execution's stdout;
  - the exact lines of newly cited released files.

  All of it is bounded, and gaps are disclosed in `evidence_notes`. The runtime already holds these inputs; the hold-and-check integration is documented, not built.
- **The questions:** four (`lost`, `changed`, `evidence`, `insufficient`), where uncertain ≠ clear. One wording correction was made during development and disclosed.
- **Cases:** fresh: 8 development and 38 frozen (16 harmful, 16 acceptable, 6 gap cases). They include 2 real and 3 real-altered 010 edits with their full revisions, and W2-style requirement changes.
- **Frozen result** (run once, threshold 0.5):
  - **16/16** harmful flagged;
  - **1/16** acceptable flagged;
  - **15/16** acceptable clear.

  The same-evidence D-any check managed 11/16 with 8/16 false flags. **Readiness gate: passed.**
- **Limits:**
  - one author's 38 cases;
  - the false-flag interval reaches 28%;
  - a narrow margin (weakest harmful 0.60, strongest acceptable 0.56);
  - every gap case was *flagged*, not *uncertain*, so the abstention output did not work separately.
- **Cost and latency:** USD 0.0045 in total; about USD 0.00009 and 0.24 s per check.
- **What it means:** an agent pilot (W2; A ordinary CLM / B confirm step / C confirm step + Jev) can now be considered. It needs its own protocol and authorisation.

**011: proposed-edit checking on the changing-requirements coding workload — development pilot (2026-10-13):**
- **Workload:** the new W2 workload, a 5-stage data-export task with a CSV → JSON change, unaffected rules, an exception, a partial change and a deferred obligation; 35 hidden checks.
- **Conditions:**
  - A, ordinary CLM;
  - B, an experimental proposal/confirmation step for context edits;
  - C, B plus Jev's check of each proposal.

  2 development instances × 3 conditions, run once.
- **Outcome:** **all 6 runs were strict successes (35/35).**
- **Mean cost and calls:** A USD 0.155 / 15.5 calls, B USD 0.177 / 18.0, C USD 0.246 / 23.0 (Jev's own share USD 0.0009).
- **Edits:** no harmful context edit was observed (exploratory blind review of 26 applied edits). Every edit in B and C went through confirmation (0 bypasses), and Jev checked 9/9 proposals in C.
- **Jev's flags:** 4 flags, all on acceptable proposals (3 accepted, 1 unnecessarily revised), and no useful warning, since nothing harmful occurred.
- **What it means:** on this workload the checking workflow added cost and calls without an observable benefit. It is a development pilot, not an evaluation.
