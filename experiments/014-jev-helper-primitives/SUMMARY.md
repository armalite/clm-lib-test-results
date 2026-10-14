### [014 – Jev as a primitive inside Claude's own context helpers](experiments/014-jev-helper-primitives/README.md)

- **Question:** can Claude's own context-management code call Jev during an execution and use the answers to edit its working context, with no extra Claude turn (`jev-primitive/1`)?
- **Prompted live demonstration** (one instructed run on W2): the capability works end to end.
  - Claude's helper called real Jev 4 times, and its threshold decided which notes received a review marker.
  - The task scored 35/35, with 14 model calls and USD 0.184.
  - Jev's influence was marker-only.
- **Comparison phase** (new W3 register workload with uncited change notices, plus a register objective in both conditions; B smoke + development pilot, 2 instances × A/B, frozen protocol):
  - **Correctness:** all runs code-correct, with no register harm.
  - **The mechanism:** Jev was called 37 times across the B runs, but an offline replay found **no register change that depended on its answers** in any of the 15 Jev-using executions. The helpers printed Jev's flags, and Claude wrote the edits itself.
  - **Cost:** B cost 18.5–32% more than A.
- **What it means:** configured this way, Claude used Jev as a printed cross-check, not as an input to its own editing logic. So **no benefit was shown, and the mechanism was not exercised.** The evaluation was not run.
- **Development revision R1** (one configured delegation smoke, under an explicit contract):
  - **The helper:** Claude's helper read the register, asked Jev about every entry, and its own 0.6 threshold chose which entries to amend. The callers passed only the stage.
  - **The selections:** at the notices they matched the truth (7 of 7, no misses). There was one false hit at stage 2, and replaced rules were kept as overridden amendments.
  - **The verdict:** the frozen counterfactual test was unsupported, because the helper's requests are sequential, so **R1 is not demonstrated under its frozen criteria.** A post-hoc last-request diagnostic shows answer-dependent selection at all three notices.
  - **The outcome:** 42/42 code checks, register harm 0, USD 0.275.
- **R1 matched development pilot** (2 fresh instances × A/B, frozen protocol, unchanged R1 instruction, shared 12k budget):
  - **Delegation was used:** in both B runs, Claude's helper executed keep, amend or retire branches on Jev's answers. Last-response replays were substantive at 2 and 4 notice stages.
  - **Correctness:** all runs were fully correct, with no register harm.
  - **Cost:** B cost 61–98% more (means: A USD 0.293, B USD 0.528) and took 45–78 s longer, mainly because its registers grew 1.7–3.5 times larger.
  - **The conclusion:** no benefit in this pilot, so no larger evaluation is justified.

