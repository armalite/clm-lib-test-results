# Jev-assistance programme review (008–013)

**Written:** 2026-10-13, after 012 v2. This is an offline review of recorded results; no new runs or paid calls.

**Scope:** what each experiment tested, what it showed, why component results did not become agent benefits, and whether 013 is worth running.

**Sources:** each experiment's README, protocol and exported evidence: [008](008-jev-context-review/README.md), [009](009-jev-update-review/README.md), [010](010-jev-initiated-review/README.md), [011](011-jev-edit-check/README.md), [012](012-jev-result-screening/README.md), and the [roadmap](jev-assistance-roadmap.md).

**The question behind the programme:** can a fast decision model (TypeSafe Jev, `jev-1.13.0`) improve a CLM agent (`claude-opus-5-5`, effort low), where Claude writes code to edit its own working context?

**Two kinds of mechanism were tested:**
- **Model-controlled advice:** Claude decides what to do with Jev's answers.
- **A runtime filter beside CLM:** 012.

**Mandatory review and confirmation steps (010 v2–v3, 011's B and C) are experimental additions around CLM, not requirements of it.** Their overhead belongs to those interventions. Ordinary CLM (condition A throughout) is unchanged, and the earlier CLM sense check found no core implementation defect requiring historical reruns.

## Evidence by phase

These rows are **not pooled and not ranked**. Each experiment uses its own workload, control and sample. Percentages from different workloads are not comparable.

### Affected-entry advice (incident-rounds workload: a fictional multi-service incident over 10–12 evidence rounds)

| Phase | Question and conditions | Sample and status | Jev participated? | Findings | Main limitation; supported conclusion |
| --- | --- | --- | --- | --- | --- |
| 008 diagnostic | Does an update require reconsidering this entry? | 24 frozen labelled cases; component diagnostic | yes | 10/10 affected and 1/12 unaffected flagged at 0.5 | author labels; **a usable component** |
| 008 pilot | A: CLM; B: CLM plus an *optional* `review_context` action | 2 instances × 2; development pilot | **no: 0 reviews** | all 4 strict; A USD 0.356 / 147 s, B USD 0.351 / 139 s | the optional tool was unused, and every run succeeded; **no agent effect could be observed** |
| 009 diagnostic | as 008 | 22 labelled cases; diagnostic | yes | 12/13 affected and 1/9 unaffected flagged | author labels |
| 009 evaluation | A and B both get the update at every release; B also gets Jev's per-entry advice | 4 fresh instances × 3 reps × 2 = **24 runs**; evaluation | yes (USD 0.0008 per run) | B cost +11% (USD 0.415 vs 0.375) and +6% time; strict 10/12 vs 8/12 (not established, p ≈ 0.6) | the 4-run pilot's saving did not reproduce; **no demonstrated agent benefit** |
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
| 012 v1 diagnostic | Is this search passage needed for the query? | 36 frozen labelled search results; diagnostic (threshold set to 0.5 from development cases) | yes | 58/58 support passages and 23/23 complete evidence sets kept; 22.3% of text omitted | most omitted text is same-subject context; **a safe component on these examples** |
| 012 v1 pilot | handbook as local files. A: CLM; B: CLM plus screening of search results | 2 × 2; development pilot | **no: B never called search** | all correct; A USD 0.119, B USD 0.119 | the intervention was bypassed by direct file reads |
| 012 v2 compatibility | the v1 policy on the document-service corpus | 26 eligible labelled results; diagnostic | yes | 28/28, 16/16, 23.1% omitted | — |
| 012 v2 pilot | handbook behind `search`/`fetch` actions (the same boundary in both conditions) | 2 fresh × 2; development pilot | **yes: 12/12 searches screened** | all correct; 14 passages omitted, **0 needed**, **12 fetched back**; B USD 0.131 vs A 0.119 (+10%), 17.5 vs 14.5 calls, 78 vs 61 s | **screening was safe but produced no saving** |

### Claude-directed screening (013)

**Planned only; not implemented or run.** See the decision below.

**Summary across phases:**
- **Components:** the Jev components were often accurate on labelled examples (008, 009, 011 v2, 012).
- **Agents:** **no demonstrated agent benefit in the tested settings.**
- **Cost:** each time Jev took part in agent runs (009, 010 v3, 011, 012 v2), costs and calls were equal or higher.

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

**Decision:** **do not run 013.** No convincing design emerges on the available workloads.
- The intervention would either be bypassable (optional) or pure overhead (required).
- A fair control can perform the same selection.
- Any version that "works" would have to be a deliberately configured workflow on a workload built for it. That would answer a different question from whether Jev helps a CLM agent in ordinary use.

**Recommendation:** **stop the Jev-assistance agent-integration programme here** and write up the results.

**What remains untested:** settings where Claude cannot cheaply do the judgment itself, for example very large candidate sets, long noisy tool outputs, or tasks with frequent harmful context edits. These are untested, not excluded.

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
   - runtime screening of search results (012 v1 and v2).
3. **Where the components looked good:** on labelled examples, Jev separated affected from unaffected entries (008, 009) and harmful from acceptable rewrites (011 v2: 16/16 flagged, 1/16 false flags), and it screened search results without losing needed passages (012: 58/58, 28/28).
4. **Why that did not become an agent benefit in these settings:**
   - Claude did not use optional mechanisms, or routed around them;
   - required steps cost more than they saved;
   - Claude's own context management was already good enough that there was little to catch;
   - when screening did remove text, Claude checked the omissions.

   Correctness was similar across conditions, near ceiling.
5. **Honest limits:**
   - synthetic workloads and author labels;
   - mostly 2 instances per pilot, evaluations of only 24–36 runs;
   - one main model and effort level;
   - the earlier calibration failures (010 v1 and v2, 011 v1) are kept in the history but are not the main story.
6. **What remains untested:** large or noisy candidate sets, long tool outputs, workloads with frequent harmful edits, other main models. **No novelty claim and no generalisation beyond these settings.**
