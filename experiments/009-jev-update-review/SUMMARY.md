### [009 – Update-triggered Jev context review (strategy 1)](experiments/009-jev-update-review/README.md)

- **Question:** when new evidence arrives, does Jev's affected-entry advice help Claude manage its own context? Both arms see the same verbatim round update (board and change-log lines) and the same instruction to consider their context. Only the assisted arm also gets Jev's per-entry probabilities, computed before the next Claude call. Claude decides every edit.
- **Evaluation:** 4 fresh instances × 3 repetitions × 2 arms = 24 runs, frozen in advance. Means per run:

  | | Control | Jev advice |
  | --- | --- | --- |
  | Cost (USD) | 0.375 | 0.415 |
  | Elapsed (s) | 149 | 158 |
  | Strict success | 8/12 | 10/12 |
  | Checks passed | 161/168 | 166/168 |

  Jev's own cost is about USD 0.0008 and its latency 2.5 s per run.
- **Main finding:** the pilot's cost and speed advantage did not hold. The assisted arm was cheaper in only 4 of 12 matched blocks, and its extra cost coincides with about one more call per run and advice text in context. The correctness difference (3 blocks only B succeeded vs 1 only A) is not conclusive, and neither arm made a stale-fact error.
- **Advice and edits:** Claude often edited flagged notes, but also ignored flags and fixed notes Jev missed. About a third of flags were on runtime code entries.
- **Earlier phases:** smoke check; fresh diagnostic (12/13 affected and 1/9 unaffected flagged); a 4-run pilot, which suggested savings.
- **Most important limitation:** four task instances (repeated runs, not twelve independent designs), one synthetic family, one model.
