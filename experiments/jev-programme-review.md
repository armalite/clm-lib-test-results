# Jev-assistance programme review (008–014)

**Written** 2026-10-13, after 012 v2. **Updated** 2026-10-14 to include experiment 014 and to close the current phase. This is an offline review of recorded results; no new runs or paid calls were made for it.

**Programme status: PAUSED after the 014 R1 matched pilot. No further paid work is authorised.** The reopening criteria are at the end of this file.

**Scope:** what each experiment tested, what it showed, why component results did not become agent benefits, and the decisions taken.

**Sources:** each experiment's README, protocols and exported evidence: [008](008-jev-context-review/README.md), [009](009-jev-update-review/README.md), [010](010-jev-initiated-review/README.md), [011](011-jev-edit-check/README.md), [012](012-jev-result-screening/README.md), [014](014-jev-helper-primitives/README.md) (including its [retrospective review](014-jev-helper-primitives/r1-pilot-review.md)), and the [roadmap](jev-assistance-roadmap.md).

**The question behind the programme:** can a fast decision model (TypeSafe Jev, `jev-1.13.0`) improve a CLM agent (`claude-opus-5-5`, effort low), where Claude writes code to edit its own working context?

**Three kinds of integration were tested:**
- **Advice that Claude reads and acts on in another turn** (008–011).
- **A runtime filter beside CLM** (012).
- **Jev as a primitive inside Claude's own code** (014). Model-written code calls Jev during an execution and uses the answers to edit context in the same execution. This is the mechanism the programme originally had in mind, and only 014 tested it.

## Navigation

**These rows are not pooled.** Each row has its own workload, control and sample size. Demonstrations, diagnostics, development pilots and evaluations are different kinds of evidence. Repeated runs on one workload are not independent task designs.

| Phase | Question tested | Evidence level | Main finding |
| --- | --- | --- | --- |
| 008 diagnostic | does an update require reconsidering this entry? | component diagnostic (24 labelled cases) | 10/10 affected and 1/12 unaffected flagged |
| 008 pilot | would Claude use an optional Jev review action? | development pilot (4 runs) | never used; all runs correct |
| 009 | does automatic per-entry advice at each update help? | diagnostic + evaluation (24 runs) | no end-to-end benefit established; strict success 10/12 vs 8/12 favoured B but is inconclusive (p ≈ 0.6); B +11% cost |
| 010 v1–v2 | would Claude start reviews, or route them to Jev? | calibration (gates failed) | optional reviews unused, or labelled around Jev |
| 010 v3 | does Jev help within a required review? | evaluation (36 runs) | nothing measurable over the review alone; the review itself +30% cost |
| 011 diagnostics | can Jev flag harmful context rewrites? | component diagnostics (v1 gate failed, v2 passed) | 16/16 flagged, 1/16 false flags (v2) |
| 011 W2 pilot | does checking proposed edits help? | development pilot (6 runs) | nothing to catch; checking added cost |
| 012 | can Jev screen incoming search results? | offline audit, diagnostics, development pilots | no required evidence lost in the tested diagnostic cases and pilots; bypassed (v1) or no saving (v2, +10%) |
| 013 | Claude-directed screening | not implemented | not run; no convincing design |
| 014 demonstration | can Claude's code call Jev mid-execution and use the answer? | capability demonstration (1 run) | works; Jev's role was marker-only |
| 014 W3 pilot | does a configured Jev helper change cost or correctness? | development smoke + pilot (5 runs) | Jev called, but no edit depended on it (non-delegation under a loose instruction) |
| 014 R1 smoke | under an explicit contract, do Jev's answers select the edits? | development smoke (1 run) | the code shows delegation; the frozen counterfactual was unsupported; a post-hoc check shows dependence |
| 014 R1 matched pilot | does configured delegation help against ordinary CLM? | development pilot (4 runs, 2 instances) | delegation occurred; equal correctness; B cost +61% and +98% and was slower |
| 014 R1 review | why did it cost more, and were the edits right? | retrospective review (exploratory, offline) | judgments mostly right; overhead linked to larger text and extra steps; broad questions caused some wrong amendments |

**Mandatory review and confirmation steps (010 v2–v3, 011's B and C) are experimental additions around CLM, not requirements of it.** Their overhead belongs to those interventions. Ordinary CLM (condition A throughout) is unchanged, and the earlier CLM sense check found no core implementation defect requiring historical reruns.

## Evidence by phase

These rows are **not pooled and not ranked**. Each experiment uses its own workload, control and sample. Percentages from different workloads are not comparable.

### Affected-entry advice (incident-rounds workload: a fictional multi-service incident over 10–12 evidence rounds)

| Phase | Question and conditions | Sample and status | Jev participated? | Findings | Main limitation; supported conclusion |
| --- | --- | --- | --- | --- | --- |
| 008 diagnostic | Does an update require reconsidering this entry? | 24 frozen labelled cases; component diagnostic | yes | 10/10 affected and 1/12 unaffected flagged at 0.5 | author labels; **a usable component** |
| 008 pilot | A: CLM; B: CLM plus an *optional* `review_context` action | 2 instances × 2; development pilot | **no: 0 reviews** | all 4 strict; A USD 0.356 / 147 s, B USD 0.351 / 139 s | the optional tool was unused, and every run succeeded; **no agent effect could be observed** |
| 009 diagnostic | as 008 | 22 labelled cases; diagnostic | yes | 12/13 affected and 1/9 unaffected flagged | author labels |
| 009 evaluation | A and B both get the update at every release; B also gets Jev's per-entry advice | 4 fresh instances × 3 reps × 2 = **24 runs**; evaluation | yes (USD 0.0008 per run) | B cost +11% (USD 0.415 vs 0.375) and +6% time; strict 10/12 vs 8/12 (not established, p ≈ 0.6) | the 4-run pilot's saving did not reproduce; **no end-to-end benefit established** |
| 010 v1 | Claude may start a review, and B's reviews include Jev | calibration; gate failed | **no: 0 reviews** | — | an optional mechanism, unused |
| 010 v2 | review required before edits; Claude's label decides whether Jev runs | calibration; gate failed | **no: all reviews labelled "compaction"** | — | the label routed around Jev |
| 010 v3 | A: CLM; B: required review; C: required review plus Jev (runtime-supplied update) | 4 fresh × 3 reps × 3 = **36 runs**; evaluation | yes (in C) | C vs B: −2% cost, equal correctness (12/12 each). The review workflow cost +30% (A USD 0.348, B 0.457, C 0.448) and +42 s; A was 10/12 strict (not established, p = 0.5) | **Jev added nothing measurable within the workflow; the workflow's overhead outweighed any benefit** |

### Proposed-edit checking

| Phase | Question and conditions | Sample and status | Jev participated? | Findings | Main limitation; supported conclusion |
| --- | --- | --- | --- | --- | --- |
| 011 diagnostic v1 | Does a proposed context rewrite lose or change needed information? (3 questions) | 36 frozen labelled rewrites; diagnostic | yes | 16/16 harmful detected, 3/16 acceptable flagged; **gate failed** (limit 2) | 2 false alarms were caused by evidence missing from the checker's input |
| 011 diagnostic v2 | the same, with an evidence contract and an `insufficient` question | 38 fresh frozen cases; diagnostic | yes | 16/16 flagged, 1/16 false flags, 15/16 clear; **gate passed**; the uncertain output never separated from flagging | one author's cases; **a strong component on labelled examples** |
| 011 W2 pilot | changing-requirements coding workload. A: CLM; B: proposal/confirmation; C: B plus a Jev check | 2 instances × 3 = 6 runs; development pilot | yes (9 checks in C) | all 35/35 strict; A USD 0.155, B 0.177, C 0.246; calls 15.5 / 18 / 23; **no harmful edit occurred**; Jev's 4 flags were all on acceptable proposals | **nothing to catch**; the checking workflow added cost |

### Incoming-result screening (012)

| Phase | Question and conditions | Sample and status | Jev participated? | Findings | Main limitation; supported conclusion |
| --- | --- | --- | --- | --- | --- |
| 012 offline audit | Do incident tool results carry removable input? | 12 ordinary-CLM runs, 261 observations; offline | no | median observation 539 chars (p90 2,693); already filtered by Claude's code; removable at most about 3.9% of run cost | **insufficient opportunity on that workload** |
| 012 v1 diagnostic | Is this search passage needed for the query? | 36 frozen labelled search results; diagnostic (threshold set to 0.5 from development cases) | yes | 58/58 support passages and 23/23 complete evidence sets kept; 22.3% of text omitted | most omitted text is same-subject context; **no support passage or complete evidence set lost on these labelled cases** |
| 012 v1 pilot | handbook as local files. A: CLM; B: CLM plus screening of search results | 2 × 2; development pilot | **no: B never called search** | all correct; A USD 0.119, B USD 0.119 | the intervention was bypassed by direct file reads |
| 012 v2 compatibility | the v1 policy on the document-service corpus | 26 eligible labelled results; diagnostic | yes | 28/28, 16/16, 23.1% omitted | — |
| 012 v2 pilot | handbook behind `search`/`fetch` actions (the same boundary in both conditions) | 2 fresh × 2; development pilot | **yes: 12/12 searches screened** | all correct; 14 passages omitted, **0 needed**, **12 fetched back**; B USD 0.131 vs A 0.119 (+10%), 17.5 vs 14.5 calls, 78 vs 61 s | **no needed passage was lost in this 2-instance pilot, but there was no saving** |

### Claude-directed screening (013)

**Planned only; not implemented or run.** See the decision below.

### Jev as a primitive in Claude's own code (014; the W3 workload is a fictional records-export service whose requirements change across 7 stages, and the agent keeps a requirements register in its context)

| Phase | Question and conditions | Sample and status | Did Jev decide edits? | Findings | Supported conclusion |
| --- | --- | --- | --- | --- | --- |
| Demonstration | an instructed helper calls Jev mid-execution (W2 workload) | 1 run; capability demonstration | only a review marker | 35/35; the accepted edits reached the next request | **the mechanism works** |
| W3 pilot | A: CLM; B: CLM plus a configured Jev helper (loose instruction) | B smoke + 2 × A/B; development pilot | **no:** replay with answers withheld gave identical context in 15/15 executions | all code-correct; B +18.5% and +32% cost | **non-delegation under that instruction** |
| R1 smoke | an explicit contract: the helper reads the register, Jev's answers govern keep/amend/retire, and callers pass only the stage | 1 run; development smoke | yes, in the code; at the change notices the frozen valid-substitution test was unsupported | 42/42; 7/7 notice selections correct | **delegation shown in code and trace; not shown under the frozen criteria** (the post-hoc check is exploratory) |
| R1 matched pilot | A: ordinary CLM; B: the same plus the unchanged R1 instruction | 2 fresh instances × A/B; development pilot | **yes:** last-response replay substantive at 2 and 4 notice stages | all code-correct and **passed the current register scorer**; B cost USD 0.599 vs 0.303 and 0.457 vs 0.283, 45–78 s longer | **no practical benefit on this workload** |
| R1 review | reconstruction of 288 delegated decisions; cost by step role | offline; exploratory | — | 20 correct amend/retire, 0 missed; 4 activations recorded as amendments; 3 ambiguous links; B's register already 1.4–1.9× larger at stage 1 | **overhead is associated with larger text and more steps, not a clean causal decomposition** |

**Notes on 014:**
- **Register correctness** here means **passing `register-checks/1`.** That scorer checks citations, labels and probe literals. It does not check claimed relations ("AMENDED by"), information items labelled current, or duplication, so it accepted misplaced amendments that a hand reading found. The checks it lacks are described in the [review](014-jev-helper-primitives/r1-pilot-review.md) and are not implemented.
- **Broad questions caused unsuitable amendments.** "Does this modify any part of…?" also caught obligations that a change merely *triggers*. The helpers had no "this now applies" branch, so they appended the change as an amendment.
- **Some claimed errors did not survive inspection:**
  - a viewer-change link to the scope rule is **ambiguous** (ordinary CLM made the same link);
  - a statement that dev-4 B attached the residency withdrawal to an obligation was **wrong**, and was corrected in the 014 write-up.
- **The overhead attribution is descriptive.** B's registers were larger from the first stage, before any Jev call, because the helpers quoted requirement text. B also split each stage into more steps that carried that larger context. Per-notice recurring costs were higher for B (USD 0.061–0.112 vs 0.031–0.055). These are associations in two runs, not a causal split.

**Summary across phases:**
- **Components:** the Jev components were often accurate on labelled examples (008, 009, 011 v2, 012). The judgments made inside 014's helpers were mostly correct.
- **Agents:** **we did not establish an end-to-end benefit in the tested settings,** including configured delegation (014). The one favourable correctness difference, 009's strict success of 10/12 against 8/12, was not established (p ≈ 0.6).
- **Cost:** where Jev took part in agent runs, the Jev condition usually cost more than its comparison condition: 009 (+11%), 011 C (+58% vs A), 012 v2 (+10%) and 014 (+18.5% to +98%).
  - **The exception is 010 v3.** Against B (the same review without Jev), C cost about 2% less on means and made 2 fewer calls per run; it was cheaper in 6 of 12 pairs, which is not an established advantage.
  - **Against ordinary CLM (A),** the same C workflow cost +29% and made 11 more calls per run.

## Failure modes, from the traces

**Observed behaviour:**

1. **Optional mechanisms that were never used:**
   - 008: 0 reviews;
   - 010 v1: 0 reviews;
   - 010 v2: every review labelled "compaction", so Jev never ran;
   - 012 v1: the search tool was bypassed for direct file reads.

   When a capability is optional, or can be routed around, Claude used its ordinary tools instead and still succeeded.
2. **Advice that duplicated work Claude already did well:**
   - **009:** Claude edited notes that Jev flagged, ignored other flags, and updated notes Jev missed. Outcomes were similar in both arms.
   - **010 v3:** C and B were indistinguishable.
   - **011:** no harmful edit occurred in any condition, so the checker had nothing to prevent.
3. **Review and confirmation overhead:**
   - 010 v3's required review: +30% cost, +11–13 calls;
   - 011's confirmation step: +14% (B vs A); with Jev, +58% (C vs A);
   - a held shrink pushed 011's B and C runs over the limit once each.

   The overhead was paid on every edit, whether or not anything was wrong.
4. **False alarms and unnecessary revisions:**
   - **011 C:** all 4 flags were on acceptable proposals; 3 were accepted (correctly) and 1 was revised without changing any requirement.
   - **009:** 36 of 114 flags were on runtime step entries.
5. **Screening followed by retrieval (012 v2):** Claude fetched 12 of 14 omitted passages back (10 by id), and none was needed.
   - **Claude's notes show checking, not need.** In B dev-1, after the first screened search: "SR-001 omitted HB-48 §1 (check maybe)"; after fetching it: "(HB-48 irrelevant)". In B dev-2: "HB-46 is the exceptions memo; only §1 (purpose) seen so far, so Q2 is probably 350 …", followed by fetching the whole memo to confirm that no exception applied.
   - **The fetch actions themselves** carried no stated thought.
   - **Condition A fetched too:** A also fetched whole documents to verify answers (4 fetches on dev-1, 1 on dev-2). Verification is part of Claude's ordinary behaviour on this task.
6. **Insufficient opportunity:**
   - incident tool outputs were already short and filtered by Claude's own code;
   - handbook search results were mostly same-subject passages (1–4% clearly off-topic).

   Screening could only omit context that no answer needed.

**Hypotheses (not established):**
- **Listing omitted ids may invite checking.** It is consistent with the "check maybe" note, but no condition omitted passages *without* listing them, and this programme would not test hiding omissions or removing access to originals.
- **Jev's added value may depend on Claude being unable to do the same judgment cheaply itself.** In every tested setting Claude could: the passages were short, the headers informative, and the edits careful.
- **Without failures to prevent, accuracy gains cannot appear.** Several workloads (008, 011 W2, 012) had near-ceiling correctness in every condition.

## Does 013 add a distinct question?

**013 as planned:** Claude writes a screening question, Jev scores candidate passages, and Claude decides what to inspect and retain.

**What it would replace:** Claude's own reading of candidate passages to pick the relevant ones.

**What Claude must already process:** to ask a useful question, Claude must know what it is looking for. To act on Jev's scores, it must see at least candidate ids and headers. On the document-service workload those headers already name the document, the section and its status ("Memo: … exceptions — Carve-out", "superseded"), which is enough for Claude to choose without Jev.

**What it adds:**
- one extra model turn per screening request, plus the scores in context;
- Jev calls per candidate set;
- in the 012 v2 traces, Claude's own verification fetches would likely remain.

**How it differs from 012:** Claude chooses when to screen and what to ask, instead of every eligible result being screened automatically.

**Why that does not avoid repeating known failures:**
- **Optional:** an optional "screen these" action is the 008 and 010 v1 pattern, an unused optional mechanism. The existing workload gives Claude no reason to use it: k = 5 results of about 2,100 characters are cheap to read.
- **Required:** a required screening step is the 010 v3 and 011 pattern, overhead on every search.
- **A fair control** must have the same candidates and headers and the same fetch access. That control can make the same selection itself, quickly, as both 012 conditions did.

**What would give 013 an opportunity:** candidate sets too large or too uninformative for Claude to triage from headers. The existing workloads do not have that. Building one now (much larger result lists, or uninformative headers) would mean designing the workload so that the intervention can help, which this programme has avoided.

> _Qualified 2026-10-14 (see Methodological notes below):_ building a workload with real opportunity is not in itself illegitimate, if it is disclosed, justified independently of the intervention, and followed by a fresh evaluation. The 013 decision rests on the absence of a convincing design, not on a ban.

**Decision:** **do not run 013.** No convincing design emerges on the available workloads.
- The intervention would either be bypassable (optional) or pure overhead (required).
- A fair control can perform the same selection.
- Any version that "works" would have to be a deliberately configured workflow on a workload built for it. That would answer a different question from whether Jev helps a CLM agent in ordinary use.

**Recommendation (2026-10-13):** **stop the Jev-assistance agent-integration programme here** and write up the results.
- **What happened next:** 014 was then opened as a distinct direction, the mechanism the programme had originally intended. Its results are above.
- **Current status:** see "Programme status" below.

**What remains untested:** settings where Claude cannot cheaply do the judgment itself, for example very large candidate sets, long noisy tool outputs, or tasks with frequent harmful context edits. These are untested, not excluded.

## Methodological notes (corrected 2026-10-14)

Some earlier statements in this programme were stricter than the method requires. They are qualified here; the frozen protocols are not edited.

- **Development iteration is permissible.** Revising an instruction, helper or workload after seeing development results is allowed when:
  - the revision is disclosed and separately versioned (as 014's R1 was);
  - its claims are tested afterwards on fresh evaluation instances under a protocol frozen beforehand.

  What is not allowed is changing a frozen protocol mid-run, or reporting development runs as an evaluation. Statements that further rewording "would be tuning, so it is not done" (in 014's [delegation revision](014-jev-helper-primitives/revision-delegation.md) and [R1 review](014-jev-helper-primitives/r1-pilot-review.md)) describe what was authorised in those phases, not a general rule.
- **Generic efficiency improvements do not invalidate a fair comparison.** A configured approach may use compact representations, deduplication or fewer steps, even though ordinary CLM could adopt them too. What a fair comparison needs is that the control is not deliberately handicapped, and that any improvement available to both is reported for what it is.
- **Neither point is evidence that another iteration would show a benefit.**

## Programme status

**Paused after the 014 R1 matched pilot. No further paid work is authorised.**

| Category | Items |
| --- | --- |
| **Completed experiments** (results stand as recorded) | 008, 009, 010 (v1–v3), 011 (diagnostics v1–v2, W2 pilot), 012 (audit, v1, v2), 014 (demonstration, W3 pilot, R1 smoke, R1 matched pilot, R1 review) |
| **Configurations not pursued further** | optional review actions (008, 010 v1); label-gated review (010 v2); required review plus Jev (010 v3); proposed-edit confirmation plus a Jev check (011); automatic search-result screening (012); 014's loose-instruction helper (the W3 pilot); 014's R1 configuration (no further paid work recommended by its review) |
| **Never tested** | 013 Claude-directed screening (designed, not implemented); a workload where ordinary CLM makes frequent register or context errors; delegation with compact, Claude-summarised entries; the revised register-scorer checks; other main models or effort levels; very large or noisy candidate sets and long tool outputs |

**What would justify reopening:** a concrete delegation opportunity, or an implementation change, with a plausible and measurable advantage that can be stated before any run. For example:
- a workload where ordinary CLM demonstrably makes register or context errors that a narrow judgment could catch;
- or a design whose recurring per-update cost is plausibly below ordinary CLM's, with that plausibility argued from recorded traces.

**A wish for a positive result is not a reason to reopen.** Any reopening needs its own authorisation and a protocol frozen beforehand.

## Outline for the blog sequel (facts only; not the article)

1. **What we wanted Jev to contribute:** cheap, narrow yes/no judgments that might help a CLM agent:
   - which notes an update affects;
   - whether a context rewrite loses something;
   - which search passages to keep.
2. **What we tested (each against ordinary CLM, with its own controls):**
   - optional advice (008);
   - automatic advice at updates (009);
   - advice inside a required review (010);
   - proposed-edit checking (011);
   - runtime screening of search results (012 v1 and v2);
   - Jev as a primitive inside Claude's own context-management code (014): first a capability demonstration; then a loose configuration in which Claude did not delegate; then an explicit contract in which it did.
3. **Where the components looked good:** on labelled examples, Jev separated affected from unaffected entries (008, 009) and harmful from acceptable rewrites (011 v2: 16/16 flagged, 1/16 false flags), and it screened search results without losing needed passages (012: 58/58, 28/28).
4. **Why that did not become an agent benefit in these settings:**
   - Claude did not use optional mechanisms, or routed around them;
   - required steps cost more than they saved;
   - Claude's own context management was already good enough that there was little to catch;
   - when screening did remove text, Claude checked the omissions.

   Correctness was similar across conditions, near ceiling.
   - **Even genuine delegation (014 R1)** was correct but cost 61–98% more in two matched pairs. The extra cost was associated with larger quoted registers and more steps, and broad questions sometimes led to unsuitable amendments.
5. **Honest limits:**
   - synthetic workloads and author labels;
   - mostly 2 instances per pilot, evaluations of only 24–36 runs;
   - one main model and effort level;
   - the earlier calibration failures (010 v1 and v2, 011 v1) are kept in the history but are not the main story;
   - 014's register correctness means passing the current register scorer, which misses misleading amendment links.
6. **What remains untested:** large or noisy candidate sets, long tool outputs, workloads with frequent harmful edits, other main models. **No novelty claim and no generalisation beyond these settings.**
