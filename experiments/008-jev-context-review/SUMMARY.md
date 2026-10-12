### [008 – Optional Jev assistance for model-controlled context management](experiments/008-jev-context-review/README.md)

- **Question:** can a fast decision model (TypeSafe Jev) help an agent manage its own context? CLM alone (A) vs the same CLM with an optional, host-mediated `review_context` action (B) that asks Jev, per entry, whether an update requires reconsidering it. Advice only.
- **Boundary fix first:** reviews are limited to the current context revision, so deleted entries cannot be sent. This was found offline and fixed before any paid call.
- **Component diagnostic (24 frozen labelled cases):** 10/10 affected entries flagged, 1/12 unaffected flagged at 0.5, about 0.24 s per request, USD 0.0003.
- **Pilot (2 dev instances × 2 conditions):** all 4 runs strict successes at similar cost (A USD 0.356, B 0.351 mean) and time. **B never used the review action** (0 reviews in 2 runs).
- **Main finding:** the component works and answers the narrow question sensibly on these cases, but when merely available the agent did not use it, so there is no evidence of an effect on context management.
- **Most important limitation:** 4 development runs at the accuracy ceiling, and diagnostic labels we wrote ourselves. The 24-run evaluation is not authorised and, as designed, would mostly measure an unused option.
