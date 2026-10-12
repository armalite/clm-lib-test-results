### [010 – Claude-initiated context review with Jev assistance (strategy 2)](experiments/010-jev-initiated-review/README.md)

- **Question:** when Claude decides its working context needs review, does Jev's advice, given automatically as part of that review and before Claude's edits, improve agent performance? Both conditions share the same `begin_review` action and instruction. Only the assisted condition's review includes Jev's per-entry probabilities.
- **Outcome:** stopped at the predeclared calibration gate. In 4 calibration runs (2 dev instances × 2 conditions), **Claude never started a review** in either condition. It integrated each round's updates by direct context edits (12–15 per run) instead.
- **No comparison was possible:** the 24-run evaluation was not run, as the protocol requires, and the instructions were not strengthened.
- **Main finding:** an optional review step that costs a model call was not adopted when direct editing was available. This is consistent with 008's unused optional tool. It says nothing about the value of Jev's advice.
- **Implementation:** `initiated-review/1` is opt-in, with 10 tests. Calibration cost USD 1.52.
