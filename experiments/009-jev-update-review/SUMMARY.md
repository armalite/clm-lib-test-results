### [009 – Update-triggered Jev context review (strategy 1)](experiments/009-jev-update-review/README.md)

- **Question:** when new evidence arrives, does Jev's affected-entry advice help Claude review its own context? Both arms see the same verbatim round update (board and change-log lines) and the same instruction to consider their context. Only the assisted arm also gets Jev's per-entry probabilities, computed before the next Claude call. Claude decides every edit.
- **Smoke check:** the in-loop live path works (8 advised updates, about 0.25 s each, under USD 0.001 per run).
- **Fresh diagnostic (24 labelled cases on real payloads):** 12/13 affected flagged, 1/9 unaffected flagged.
- **Pilot (2 dev instances × 2 arms):** 4/4 strict successes. The assisted arm was cheaper and faster on means (USD 0.313 vs 0.377; 123 s vs 152 s), driven mostly by one pair whose pacing differed, so this is not evidence of an effect.
- **Advice and edits:** in the one run with several notes, Claude annotated some flagged notes in place and left others unchanged.
- **Main finding:** strategy 1 is a cheap, matched, working intervention, but this pilot shows no accuracy effect (ceiling) and no reliable efficiency effect.
- **Most important limitation:** four runs at the accuracy ceiling. The model's usual single rolling note leaves per-entry advice little to discriminate.
