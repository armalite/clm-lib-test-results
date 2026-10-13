### [010 – Claude-initiated context review with Jev assistance (strategy 2)](experiments/010-jev-initiated-review/README.md)

- **Question (v3):** when Claude decides to edit its working context, does a Jev-assisted review improve the outcome enough to justify its overhead? The conditions were A (ordinary CLM), B (review required before every context edit) and C (the same plus Jev's advice). In B and C the runtime supplies the update (the latest released round's board and change-log lines), so Jev runs regardless of how Claude labels the edit.
- **History:**
  - **v1** (review optional): Claude never reviewed.
  - **v2:** Claude labelled every review "compaction", so Jev never ran (an offline audit found most of those edits incorporated new findings).
  - **v3:** fixed the update source; it passed its smoke check and calibration gate.
- **Evaluation:** 4 fresh instances × 3 repetitions × 3 conditions = 36 runs. Means per run:

  | | A | B | C |
  | --- | --- | --- | --- |
  | Strict success | 10/12 | 12/12 | 12/12 |
  | Cost (USD) | 0.348 | 0.457 | 0.448 |
  | Elapsed (s) | 152 | 195 | 194 |
  | Calls | 32.5 | 45.9 | 43.8 |

  Jev advised all 131 applicable reviews, at about USD 0.001 and 2.7 s per run.
- **Main findings:**
  - **C vs B:** Jev added nothing measurable within the review workflow (cost −2%, the same correctness).
  - **C vs A:** the review workflow itself costs about 30% more and takes about 28% longer.
  - **Correctness:** A's two failures (adjacent-line miscitations of one early change record) vs none in B and C is not established (p = 0.5).
- **Verdict:** on this workload the benefit does not justify the overhead.
- **Limitation:** four synthetic task instances with repeated runs, one model.
