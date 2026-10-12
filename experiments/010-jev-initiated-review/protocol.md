# 010 – Planned protocol: Claude-initiated review with Jev assistance (strategy 2)

**Status: PLANNED. Not implemented, not run, and no paid calls are authorised.** Written on 2026-10-13 as part of the [roadmap](../jev-assistance-roadmap.md). Any implementation would first freeze a revised version of this protocol.

## Question

**When Claude itself decides that its context needs review, does consulting Jev as part of that review improve it?**

## Design

**Both arms get the same, versioned `review` action.** Its use is Claude's choice in both arms, and the runtime never forces it.
- **The request:** Claude names an update, either as text or as the id of a current entry, and the current entries it wants reviewed.
- **The runtime returns:** the named entries' exact text from the **current** revision (008's boundary rule), as a structured review prompt.
- **The next step:** Claude decides whether and how to edit.

**The arms:**
- **A (control):** the review action returns the structured review prompt only. Claude performs the review itself.
- **B (assisted):** the same action also returns Jev's per-entry `jev-review/1` probabilities for the named entries, against the named update.

**How this differs from 008:** in 008 the control had **no** review mechanism, and B's Jev action was an independently optional extra, which the agent never used. Here the review mechanism and its wording are identical in both arms, so how often reviews happen can be compared directly. Advice is the only difference.

| | |
| --- | --- |
| **Jev judgment** | The same as 008 and 009: whether the update requires reconsidering a current assertion or planned action in each named entry |
| **Trigger** | Claude's own decision, at most N per run (for example 12) |
| **Information: Claude** | Its own context; the review prompt (both arms); the advice (B) |
| **Information: Jev** | The update Claude named, and the named current entries only |
| **Who edits** | Claude, in a later step, through the normal validated edit path |
| **Overhead** | Each review is one extra Claude turn in **both** arms, plus a Jev round trip in B |

## Possible failure modes

- **Reviews are rarely or never initiated**, as 008 found for an optional tool. This is the first thing to measure, and no prompt strengthening is allowed after results.
- **Paraphrased updates:** Claude-named update texts may be paraphrases. The update text then is not the original evidence, unlike 009's payload.
- **Selective review:** Claude may name only entries it already intends to change, which makes the advice redundant.
- **Bias toward agreeing with the advice.**
- **Overhead** from extra turns, in both arms.

## Diagnostics before any evaluation

- **Jev side:** 009's `jev-diag/2` results cover the question on real payloads. A small check is still needed of whether the update texts Claude writes in the pilot look like the payloads Jev was checked on. Those texts would be labelled after the pilot, so they are development evidence only.
- **Logging:** review frequency, timing (steps after a release) and the scope chosen.

## Outcomes

- **Primary:**
  - the number of reviews initiated per run in each arm;
  - strict success;
  - all-attempt cost.
- **Secondary:**
  - edits following reviews;
  - flagged-then-changed and flagged-not-changed;
  - calls, time and cache use.

## Limitations

- **Arms with different numbers of reviews are not matched on review count.** Differences are reported per run rather than adjusted.
- **Scope:** the same synthetic task family and model as 009.
