### [007 – Reusable context-management helpers](experiments/007-reusable-context-helpers/README.md)

- **Problem:** a multi-service incident investigation with evidence in 10–12 rounds. Three conditions: the robust summary baseline (A), CLM with direct editing (B), and CLM **instructed** to make its edits through reusable functions it writes (C).
- **Two phases:**
  - **Initial calibration:** helpers optional; the model created none, which stopped that phase.
  - **Revised phase:** a documented protocol revision made after the initial calibration, with an instructed strategy, 7 calibration runs and a **24-run evaluation** (4 fresh instances × 2 repetitions × 3 conditions).
- **Headline (evaluation):**
  - **Strict success:** A 4/8, B 6/8, C 7/8. A's failures were all missing evidence references.
  - **Mean cost:** A USD 0.582, B 0.386, C 0.361. C was 38% cheaper than A and B 34% cheaper, each in 8 of 8 blocks.
  - **Time:** both CLM conditions were about 25% faster than A.
  - **C vs B:** 6% cheaper on means, but cheaper in only 4 of 8 blocks, with the same time.
- **Helpers:** C complied in all 8 runs, with one small `ctx.py` written at step 1 and used in every edit step. The helpers were note writers or simple entry filters, never revised.
- **Main finding:** both CLM strategies beat the baseline on cost and time here; instructing reusable functions showed no measurable benefit over direct editing.
- **Most important limitation:** 8 matched blocks on one synthetic task family and one model. Two CLM-only runtime defects were found and fixed during the work.
