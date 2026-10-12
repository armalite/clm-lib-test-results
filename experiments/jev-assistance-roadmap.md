# Roadmap: where can a fast decision model assist model-controlled CLM?

_Written on 2026-10-13. A planning document, not a result. Each strategy gets its own experiment, protocol and evidence. Experiment 008 is separate evidence and is not one of these strategies (see below)._

## Purpose

These experiments ask where a fast decision model (TypeSafe Jev) can **usefully assist** a CLM agent that manages its own working context with code. "Usefully" covers four things:
- correctness;
- cost (both providers);
- latency;
- failures and overhead.

**Assumptions we do not make:**
- **No assumed benefit:** a working integration is not evidence that it helps, and a negative or null result is a valid finding.
- **Not a first:** the combination of Jev and CLM-style state management is not new. fast-jev-compaction filters tool history with Jev by fixed rules, and the Muninn post combined Jev flags with model-written state updates. See [008's protocol](008-jev-context-review/protocol.md#related-work-and-how-this-differs).

**Invariants in every strategy:**
- **Claude decides every edit.** The main model alone decides whether and how to edit its context, in both arms.
- **Jev only advises.** Advice is never a deletion command, and a low relevance score is never permission to forget.
- **Opt-in only.** Every addition is an explicit, versioned opt-in. Historical configurations, prompts, generators, scorers and evidence keep their behaviour.
- **The sandbox stays isolated:** no network, no credentials.

## The three strategies

| | Strategy 1: update-triggered review | Strategy 2: Claude-initiated review | Strategy 3: proposed-edit check |
| --- | --- | --- | --- |
| **Experiment** | [009](009-jev-update-review/protocol.md) | [010](010-jev-initiated-review/protocol.md) | [011](011-jev-edit-check/protocol.md) |
| **Status** | **Implemented** (2026-10-13); diagnostic and pilot only | **Planned**: not implemented, no paid runs authorised | **Planned**: not implemented, no paid runs authorised |
| **Question** | When meaningful evidence arrives, does Jev's affected-entry advice help Claude review its existing context? | When Claude itself decides a review is needed, does Jev's advice improve that review? | Before Claude applies a context edit, does a Jev check for narrow risks help Claude catch mistakes? |
| **Jev judgment** | Per current entry: does this update require reconsidering a current assertion or planned action in it? (`jev-review/1`) | The same per-entry judgment, for the update Claude names | **New, untested:** for example, does the proposed revision lose a still-current fact from a removed entry, or carry forward an assertion an update has superseded? |
| **Trigger** | Runtime: each round release with board or change-log lines | Claude chooses when to start a review | Each proposed edit that removes or rewrites entries |
| **Control (CLM only)** | Claude sees the same update and the same instruction to consider its context | Claude has the same review action and performs the review itself | Claude has the same check opportunity without Jev |
| **Who edits** | Claude | Claude | Claude (apply, revise or withdraw) |
| **Main overhead** | One Jev round trip per update, plus advice text in context; no extra Claude turn | One extra Claude turn per review in both arms, plus Jev | One extra Claude turn per checked edit in both arms, plus Jev |
| **Diagnostic needed first** | Fresh `round-files/1` payload cases (done for 009) | Whether Claude-chosen update texts resemble the cases Jev was checked on | A new labelled set for the new judgment; the 008/009 question must not be assumed to work |

## How they differ from experiment 008

In [008](008-jev-context-review/README.md), Jev was an **independently optional action**: the control had no review mechanism at all, and the assisted arm could call Jev whenever it liked.
- **Diagnostic:** Jev answered the narrow question well on 24 labelled cases.
- **Pilot:** in its four-run pilot the agent **never called it**.
- **What it remains:** evidence about optional-tool availability only. Its prompts and results are not changed, strengthened or relabelled.

The strategies here instead give **both arms the same review structure** and vary only whether Jev's advice is part of it. That separates "is review happening?" from "does the advice help?".

## Order and gating

1. **Strategy 1 (009):** implemented first, because:
   - it needs no new Jev judgment;
   - it adds no Claude turn;
   - its trigger is mechanical and identical across arms.

   Its pilot decides whether a 24-run evaluation is worth authorising.
2. **Strategy 2 or 3 next:** chosen after 009's pilot. Neither is implemented, and nothing is authorised for them. Strategy 3 needs its own diagnostic before any agent runs.
3. **A common-workload comparison, only if the initial findings justify it:**
   - **Design:** the same instances, runtime, model and budget for CLM alone and for each strategy that showed something worth comparing.
   - **Why it is needed:** improvements measured on different tasks or settings cannot establish a winning strategy, so no cross-experiment ranking will be claimed without it.

## What is out of scope

- An enormous benchmark.
- Automatic deletion or filtering policies.
- Jev-written state.
- Multi-agent infrastructure.
- Changes to old experiments or their exports.

## Note after 009's pilot (2026-10-13)

**009's findings:** strategy 1 works as a matched, low-overhead intervention, and Jev's component accuracy on real payloads was good (12/13, 1 false positive in 9). The pilot, though, showed no accuracy effect (all at the ceiling) and no reliable efficiency effect. It also showed why: in most runs Claude keeps **one rolling note that it rewrites every round**, so per-entry "which entries are affected?" advice has little to discriminate. See [009](009-jev-update-review/README.md).

**Recommendation (the decision is the maintainer's): strategy 3's component diagnostic next, before strategy 2.**
- **Strategy 3 matches what the agent actually does.** It rewrites a large note each round, and the omissions seen in 007's evaluation (a dropped early change record, missing citations) are exactly the "lost a still-current fact" risk that strategy 3 targets.
- **It can start cheaply.** A labelled component diagnostic of the new judgment needs only TypeSafe calls, and no agent run is needed until it shows useful separation.
- **Strategy 2 depends on Claude choosing to start reviews.** 008 found that an optional Jev action was never used. Giving both arms a review action would change that, but the most likely first finding, whether reviews happen at all, is cheaper to learn later.
