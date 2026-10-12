### [010 – Claude-initiated context review with Jev assistance (strategy 2)](experiments/010-jev-initiated-review/README.md)

- **Question (v2):** when Claude decides to edit its working context, does a Jev-assisted review improve the outcome enough to justify its overhead? The conditions were A (ordinary CLM), B (review required before every context edit) and C (the same with Jev advice). v1 (review optional) is kept separately.
- **v1 (4 calibration runs):** Claude never started an optional review; it always edited directly.
- **v2 (6 calibration runs):** the required workflow worked, with 48/48 edits preceded by a review and no bypass. But Claude declared **every** review a compaction review, so Jev was never applicable (**0 Jev calls**) and C was B in practice.
- **Calibration means:** the review workflow cost more than ordinary CLM (USD 0.425–0.463 vs 0.370; about 46 vs 33 calls; about 4× the context-pressure steps). All six runs were strictly correct.
- **Outcome:** both versions stopped at their predeclared readiness gates, and no evaluation was run. Nothing here shows whether Jev's advice helps.
- **Main lesson:** letting Claude classify reviews ("update" vs "compaction") let it avoid the update path entirely. A v3 would need a runtime-supplied update source, such as the evidence released since the last review.
