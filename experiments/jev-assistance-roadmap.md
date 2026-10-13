# Roadmap: can Jev improve a CLM agent, and where in the workflow is its assistance useful?

_First written on 2026-10-13 and revised on 2026-10-13 (session 5). A planning document, not a result. Each experiment has its own protocol and evidence. The dated notes at the end are kept as written._

## The question

**Can a fast decision model (TypeSafe Jev) improve a CLM agent, and where in the workflow is its assistance useful?**

"Useful" covers correctness, cost (both providers), latency, failures and overhead. The programme studies two kinds of assistance:
- **Model-controlled assistance:** Jev advises and **Claude decides** every working-context edit. These are experiments 008–011 and 013.
- **Complementary runtime policies:** a declared runtime rule uses Jev's scores to decide what **initially enters** Claude's context, while Claude still controls all later working-context edits. This is experiment 012.

These are different interventions. Results from one say nothing directly about the other.

**Ground rules for every experiment:**
- **Each experiment compares one strategy with its own matched control** (CLM with the same mechanism but without Jev's advice). That establishes whether the strategy helps *its* control.
- **Comparing strategies directly** requires shared workloads and compatible settings: the same instances, model, effort, prompts, caching, limits and budget. Numbers from different experiments are **not** compared directly.
- **A useful result need not favour Jev.** Null and negative results are findings.
- **Not a first:** these experiments do not establish that combining Jev and CLM is novel. fast-jev-compaction filters tool history with Jev by fixed rules, and the Muninn post combined Jev flags with model-written state updates. See [008's protocol](008-jev-context-review/protocol.md#related-work-and-how-this-differs).
- **Invariants:**
  - every addition is opt-in and versioned;
  - historical configurations, prompts, generators, scorers and evidence keep their behaviour;
  - Jev calls are host-side only, and the sandbox has no network or credentials;
  - Jev never sees future evidence, hidden answers or deleted history.

## Programme overview

| | Kind | Where Jev acts | Status |
| --- | --- | --- | --- |
| [008](008-jev-context-review/README.md) | model-controlled | an optional Jev tool Claude may call | Complete: the tool was never used (evidence about optional-tool availability) |
| [009](009-jev-update-review/README.md) | model-controlled | automatically at every incoming update, before Claude's next turn | Complete: no cost, time or established correctness benefit in 24 evaluation runs |
| [010](010-jev-initiated-review/README.md) | model-controlled | at **Claude's** context-edit decisions (v1 optional; v2 required, Claude-labelled; v3 required, runtime-supplied update) | **v3 complete (36 runs):** Jev added nothing measurable over the review alone; the review workflow costs about 30% more than ordinary CLM. v1 and v2 stopped at their gates |
| [011](011-jev-edit-check/README.md) | model-controlled (checking) | on a proposed context rewrite | **v1 diagnostic: gate failed. v2 diagnostic: gate passed.** **Development pilot on W2** (2 instances × 3 conditions): all 6 runs strict success; no harmful edit occurred; Jev flagged 4/9 proposals, all acceptable; checking cost +58% (C vs A), almost all Claude-side |
| W2 workload | a workload, not a strategy | changing requirements that interact | **Implemented** (`export-gen/1`, 2 development instances); used by the 011 development pilot |
| 012 | runtime policy beside CLM | automatic screening of incoming tool results | Planned: the first proposed screening experiment |
| 013 | model-controlled | Claude-directed screening of tool results | Planned |

### 010: Claude-initiated context review

- **Question:** when Claude itself decides that its working context needs review, does Jev's advice, given automatically as part of that review and before Claude chooses its edits, improve agent performance?
- **Hypothesis:** advice at Claude-chosen review points targets real reconsideration moments better than reviewing every update (009), with less overhead.
- **Control and assisted conditions:** both have the same neutral `begin_review` action and the same instructions. The assisted condition's review also includes Jev's per-entry probabilities.
- **What it is not:** this is not 008. In 008 Claude had to choose to call Jev; here Claude chooses to review, and Jev is part of every review in the assisted condition.
- **Workload:** the incident-rounds family. There is a meaningful opportunity to help when an update supersedes or partly changes something already in Claude's notes.
- **Outcomes:** strict success and scored categories, cost, time and calls, review frequency, edits after reviews, and advice volume and residence in context.
- **Confounds:**
  - review frequency can differ between arms;
  - Claude writes the review's "new information" text itself;
  - the review protocol itself changes CLM behaviour, so the control is "CLM with the review protocol", not 009's or older controls.
- **Readiness gate:** calibration must show reviews initiated while work remains, in both arms, with real Jev calls in the assisted arm. **Status: gate failed (2026-10-13).** There were 0 reviews in 4 calibration runs, and no evaluation was run.

### 011: Proposed-edit checking

- **Question:** does a Jev check of a proposed context rewrite help Claude catch losses or incorrect changes before the rewrite is accepted?
- **Hypothesis:** the observed failures (008/009) are omissions, so a check for lost still-current information targets them.
- **Control and assisted conditions:** both get the same check opportunity on proposed rewrites (apply, revise or withdraw). The assisted condition adds Jev's answers to narrow questions about the change.
- **Preservation of obligations** (an unchanged requirement silently dropped) belongs here.
- **Still to design:** the intervention and correction workflow.
- **Workload:** incident rounds first; the changing-requirements workload (W2) later, under shared settings.
- **Opportunity to help:** a rewrite that drops or alters still-current facts.
- **Outcomes:** omissions and stale facts, edits revised or withdrawn, and the extra turns and cost of the check.
- **Confounds:**
  - the check opportunity is itself an intervention;
  - false alarms can cause churn.
- **Readiness gate:** a fresh labelled component diagnostic for the new judgment must show useful separation first. **Status: the component diagnostic ran (2026-10-13) and its gate failed; see the note below.**

### W2: Changing-requirements workload (a workload extension, not a new strategy)

- **Example:** an app switches from CSV to JSON export. The format-specific requirements change, while permissions, filtering and other obligations stay valid.
- **Purpose:**
  - test missed updates (a format rule not changed);
  - test unnecessary changes to unaffected requirements (permissions or filtering altered or dropped);
  - test downstream task correctness when several distinct requirements interact.
- **How it would be used:** it could exercise 010 (Claude reviews when a requirement changes) and 011 (checks of proposed rewrites for lost obligations) **under shared settings**. It is also the natural workload for a later common-workload comparison of strategies.
- **Relation to existing generators:** experiments 004 and 005 have coding generators with changing rules. W2 would need a generator where interacting obligations persist across a format switch.
- **Readiness gate:** a versioned generator and scorer with separate categories for "missed change" and "unnecessary change", validated offline. **Status: planned, not implemented.**

### 012: Automatic screening of incoming tool results (runtime policy beside CLM)

- **Question:** can a declared runtime policy that uses Jev to screen tool results before they enter Claude's context reduce cost and latency without losing needed evidence?
- **Design:** Jev scores passages or chunks of a tool result, and a fixed, declared policy (for example a threshold plus always-keep rules) selects what initially enters the context.
  - **Nothing is lost:** the full original result stays accessible on disk, and Claude can re-read it.
  - **Claude still controls** all later working-context edits.
- **Control and assisted conditions:** the control is CLM with the full results entering as today. The assisted condition is the same CLM with the screening layer.
- **Workload:** tasks with large tool outputs, such as the incident-rounds logs (23–41k characters per round). There is an opportunity to help where most of a result is noise.
- **Outcomes:**
  - cost, latency and correctness;
  - **missed evidence**: needed lines screened out;
  - **recovery work**: re-reads of the originals, and extra calls.
- **Confounds:**
  - the policy's threshold is a design choice, so it is fixed before evaluation;
  - screening also changes context pressure.
- **Readiness gate:** an offline replay of existing traces showing what the policy would drop, against the scorer's evidence lines, before any agent run. **Status: planned, the first proposed screening experiment.**

### 013: Claude-directed screening of incoming tool results

- **Question:** when Claude chooses the screening question, does Jev-assisted passage screening help Claude find and keep the right evidence?
- **Design:** Claude receives a reference to the result file rather than its full text, writes a screening question, and gets Jev's per-passage scores. It then decides what to inspect and retain.
- **Control and assisted conditions:** the control is CLM with the **same file access and browsing tools** (for example grep, head and line ranges). It must not be forced to read entire results. The assisted condition is the same plus the Jev screening call.
- **Opportunity to help:** results where the relevant passages are hard to find by simple search.
- **Outcomes:** correctness, missed evidence, cost, time, calls, and screening questions used.
- **Confounds:**
  - the quality of Claude's question;
  - tool-use differences;
  - the extra turns per screening.
- **Readiness gate:** 012's findings, plus a passage-level diagnostic for the question type. **Status: planned**, distinct from 012.

## Order and gating

1. **009** (done): update-triggered review gave no benefit on this task.
2. **010** (done): Claude-initiated review stopped at its calibration gate. Claude never started a review.
3. **011's component diagnostic** next, then possibly 011 itself. W2 is developed when 010 or 011 needs a workload with interacting obligations.
4. **012** then **013**, the screening experiments, each behind its own readiness gate.
5. **A common-workload comparison**, only if separate results justify it: the same instances and settings for CLM alone and each promising strategy. Without it, no ranking of strategies is claimed.

## Out of scope

- An enormous benchmark.
- Jev-written state, and multi-agent infrastructure.
- **Automatic deletion of working-context entries.** 012's screening policy is limited to what *enters* the context initially; it never removes what Claude has kept.
- Changes to old experiments or their exports.

## Note after 009's pilot (2026-10-13)

**009's findings:** strategy 1 works as a matched, low-overhead intervention, and Jev's component accuracy on real payloads was good (12/13, 1 false positive in 9). The pilot, though, showed no accuracy effect (all at the ceiling) and no reliable efficiency effect. It also showed why: in most runs Claude keeps **one rolling note that it rewrites every round**, so per-entry "which entries are affected?" advice has little to discriminate. See [009](009-jev-update-review/README.md).

**Recommendation (the decision is the maintainer's): strategy 3's component diagnostic next, before strategy 2.**
- **Strategy 3 matches what the agent actually does.** It rewrites a large note each round, and the omissions seen in 007's evaluation (a dropped early change record, missing citations) are exactly the "lost a still-current fact" risk that strategy 3 targets.
- **It can start cheaply.** A labelled component diagnostic of the new judgment needs only TypeSafe calls, and no agent run is needed until it shows useful separation.
- **Strategy 2 depends on Claude choosing to start reviews.** 008 found that an optional Jev action was never used. Giving both arms a review action would change that, but the most likely first finding, whether reviews happen at all, is cheaper to learn later.

## Note after 009's evaluation (2026-10-13)

**Strategy 1's frozen 24-run evaluation** (4 fresh instances × 3 repetitions) **did not reproduce the pilot's savings.**
- **Cost and time:** with Jev advice, mean cost was USD 0.415 vs 0.375 and mean elapsed time 158 s vs 149 s. The assisted arm was cheaper in 4 of 12 matched blocks.
- **Correctness:** strict success was 10/12 vs 8/12, which is not conclusive.
- **Failure types:** every failure in both arms was an **omission** (missing evidence references, once a whole incident) or an invalid citation. **None was a stale fact**, which is the error affected-entry advice targets. See [009](009-jev-update-review/README.md).

**The recommendation above stands, with one adjustment: strategy 3's component diagnostic (011) next, still before strategy 2.**
- **Why strategy 3:** the observed failures are the "lost a still-current fact" kind that strategy 3 targets.
- **Overhead:** strategy 3 adds a Claude turn per checked edit, and runs made about 18 edits, so its design must keep overhead in view. Checking only edits that remove or rewrite notes would help. 009 showed that small per-run additions cost money: about 11% here.
- **Strategy 2** also adds Claude turns, and its value depends on Claude choosing to review.
- **Neither is implemented or authorised.**

**Comparing strategies:** each experiment uses its own controls. A ranking needs the [common-workload comparison](#order-and-gating): the same instances, runtime, model, prompts, caching, budget and metrics for CLM alone and each strategy. Numbers from 009, 010 and 011 are not to be compared directly with one another.

## Note after 010's calibration (2026-10-13)

**010's calibration:** Claude never used the shared `begin_review` step, in either condition, in 4 runs. It integrated updates by direct context edits instead. Following the protocol, no evaluation was run and the instructions were not strengthened. See [010](010-jev-initiated-review/README.md).

**Across the Jev experiments so far:**
- **008:** an optional Jev tool went unused.
- **009:** automatic review gave no benefit.
- **010:** an optional review step went unused.

On this workload, optional steps that cost Claude a turn are not adopted, and the observed failures are omissions and miscitations rather than stale facts.

**Recommendation (the decision is the maintainer's):** 011's component diagnostic next, as before.
- **Why:** 010's exploratory check found one omission that was never recorded and one that was miscited at answer time. Neither was a loss during an edit, so 011 should also confirm that edit-time losses occur at all on this workload, before agent runs.
- **A workload with interacting obligations (W2)** may be needed to create that opportunity.
- **Revising 010:** any revised 010 design, for example making review the route for note rewrites, would be a new, labelled protocol version, and is close to 011.

## Note after 010 v2's calibration (2026-10-13)

**010 v2** made a review mandatory before every context edit. A was ordinary CLM, B the review only, and C the review with Jev.
- **The workflow worked:** 48/48 edits were preceded by a review, with no bypass.
- **Jev never acted:** Claude declared every review "compaction", including the per-round consolidations that brought in new evidence. Jev was therefore never applicable and made **0** calls.
- **The review's cost:** even inactive, the required review cost about 15% more, took 28% longer, and raised context pressure about fourfold on the calibration instances.
- **No evaluation was run.** See [010](010-jev-initiated-review/README.md).

**What the programme has learned so far** (incident-rounds workload):
- **What makes Jev act:** it runs only when the update source is mechanical and runtime-supplied (009). Every design that relied on Claude choosing to invoke or classify an update left it unused: 008, 010 v1 and 010 v2.
- **What 009 showed:** automatic advice ran but brought no efficiency or established correctness benefit.

**Recommendation (the decision is the maintainer's):**
- **A 010 v3 is possible:** a required pre-edit review whose update source is the evidence released since the previous review, supplied by the runtime. It would test advice at Claude's edit decisions without depending on Claude's classification. It would need its own protocol and authorisation.
- **The stronger next step is still 011's component diagnostic:** it targets the observed failures (omissions and miscitations) and can be checked cheaply before any agent run.

## Note after 010 v3's evaluation (2026-10-13)

**010 v3** made the review's update runtime-supplied, the latest released round's board and change-log lines, so Jev ran at every applicable review (131/131).
- **The evaluation:** 4 fresh instances × 3 repetitions × 3 conditions.
- **Jev's increment over the same review workflow without it was nil:** cost −2%, time −1 s, identical correctness.
- **The workflow's overhead is large:** the required review cost about 30% more and took about 28% longer than ordinary CLM.
- **Correctness:** its 12/12 vs 10/12 strict success is not established. A's two misses were adjacent-line citation errors.

See [010](010-jev-initiated-review/README.md).

**What the programme has now shown on the incident-rounds workload:**
- **Jev runs when the runtime supplies the update mechanically** (009, 010 v3).
- **It does not run when Claude must choose or label** (008, 010 v1, 010 v2).
- **Where it ran, its per-entry affected-entry advice did not measurably change outcomes,** either at incoming updates (009) or at Claude's edit decisions (010 v3).

**The failures across experiments** are omissions and miscitations, not stale facts, which is the error this advice targets.

**Recommendation (the decision is the maintainer's):**
- **011's component diagnostic** (TypeSafe only): a different judgment, aimed at omissions in proposed rewrites.
- **Or a workload with real staleness risk (W2)**, before more agent runs of the affected-entry question.
- **Comparing strategies:** separate results establish each strategy only against its own control. 009 and 010 v3 used different controls, presentations and instances, so they are not directly comparable.

## Note after 011's component diagnostic (2026-10-13)

**011's diagnostic** asked Jev three narrow questions (`lost`, `changed`, `evidence`) about proposed context rewrites, on 36 author-labelled frozen cases. No agent runs were made.
- **The result:** **16/16** harmful rewrites detected, but **3/16** acceptable ones flagged, failing the predeclared limit of 2. The deterministic checks managed 7/16 with the same 3 false flags.
- **What it shows:** this is the first Jev judgment in the programme that clearly beats simple checks on its own task, including semantic losses (exceptions, conditions, swapped citations, "not done" → "done") that leave references and numbers intact.
- **Why the gate failed:** two of the false flags were real edits whose new content came from tool output the checker never saw.
- **Next step:** this is not a basis for an agent pilot. If pursued, a **diagnostic v2** would include the tool observations since the last revision in the checker's input, with **fresh** labelled cases, followed only then by a W2-workload pilot (A ordinary CLM / B confirm step / C confirm step + Jev).
- **Unchanged:** 012 and 013 remain planned.

## Note after 011's v2 diagnostic (2026-10-13)

**What v2 changed:** the checker now sees the evidence a runtime has at edit time (`edit-evidence/1`):
- the full current revision, including tool observations;
- the released update;
- the proposing execution's stdout;
- the lines of newly cited released files.

**It also gained a fourth `insufficient` question.** The cases and families were fresh, and the frozen set was run once.

**The result:** **16/16** harmful flagged, **1/16** acceptable flagged and **15/16** acceptable clear, so **the gate passed**. The deterministic checks given the same evidence managed 11/16 with 8/16 false flags.

**Caveats:**
- one author's 38 cases;
- a narrow margin;
- the uncertain output never appeared: all 6 gap cases were flagged, with `insufficient` and `changed` both high.

**Next (the maintainer's decision; not started):** an agent pilot on the **W2** workload can now be considered. It would:
- implement the documented hold-and-check integration;
- compare A (ordinary CLM), B (the confirm step without Jev) and C (the confirm step with Jev);
- first measure whether harmful edits occur at all;
- treat flags as advice to inspect.

**Building W2 comes first.**

**Unchanged:** 012 and 013 remain planned.

## Note after 011's development pilot (2026-10-13)

**What ran:** 011: proposed-edit checking on the changing-requirements coding workload — development pilot. That is A (ordinary CLM), B (an experimental proposal/confirmation step) and C (B plus Jev's check of each proposal), on 2 W2 development instances, run once each.

**Results:**
- **Outcome:** all six runs were strict successes (35/35 hidden checks).
- **Edits:** no harmful context edit was observed.
- **Coverage:** every B and C edit went through confirmation, and Jev checked all 9 C proposals.
- **Jev's flags:** 4 flags (all from the `evidence` question near its threshold, on routine transcript compaction), all on acceptable proposals. There were no useful warnings.
- **Cost:** C cost +58% over A and +39% over B. Jev's own API cost was negligible; the difference is Claude's confirmation, revision and longer notes.

**What it means:**
- **On this workload,** proposed-edit checking had nothing to catch and only added work.
- **A larger 011 evaluation would mainly measure overhead and false alarms,** and is not recommended unless a workload is shown to produce harmful edits under ordinary CLM.
- **The workflow's overhead** belongs to the experimental confirmation step, not to CLM.

**Next (the maintainer's decision):** **012 remains the next planned approach**, starting with its offline replay readiness gate (no agent runs). 013 remains planned after 012.

