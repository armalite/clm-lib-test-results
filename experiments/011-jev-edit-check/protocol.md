# 011 – Planned protocol: Jev check of a proposed context edit (strategy 3)

**Status: PLANNED. Not implemented, not run, and no paid calls are authorised.** Written on 2026-10-13 as part of the [roadmap](../jev-assistance-roadmap.md). Any implementation would first freeze a revised version of this protocol and a new diagnostic.

## Question

**Before Claude applies a context edit, does a Jev check for narrow, specific risks help Claude catch mistakes in the edit?**

## Design

**Both arms get a defined check opportunity.**
1. When Claude's code writes a `context.json` that is valid and **removes or rewrites** at least one entry, the runtime holds it as a *proposed* revision instead of committing it at once.
2. The next observation shows the proposed change: the removed and rewritten entries, before and after.
3. Claude replies `apply`, revises the edit, or withdraws it.

Edits that only add entries are committed as today.

**The arms:**
- **A (control):** the same check opportunity, without Jev.
- **B (assisted):** the same, plus Jev's answers to a few narrow questions about the proposed change.

**The Jev judgment, which is new and untested:** it differs from affected-entry detection, so **the 008/009 question is not assumed to work for it**. Candidate questions, each one narrow yes/no:
1. **Lost requirement:** per removed or rewritten entry, "Does the proposed revision omit a fact, requirement or planned action from this entry that no later update has superseded?"
2. **Stale carry-forward:** per kept or rewritten entry, "Does this entry still assert something that a recent update has superseded?" The recent updates would be the released payloads since the last check.

| | |
| --- | --- |
| **Trigger** | Every valid proposed edit that removes or rewrites entries |
| **Information: Claude** | Its context, the proposed diff, and (B) Jev's answers |
| **Information: Jev** | The old entry text, the proposed replacement text (or "removed"), and the recent released updates. Never future rounds, truth or deleted history beyond the entry being removed |
| **Who edits** | Claude: apply, revise or withdraw. Jev never approves or rejects |
| **Overhead** | One extra Claude turn per checked edit in **both** arms (pilot runs made 11–15 edits, so this could add about a third more calls), plus Jev calls in B |

## Possible failure modes

- **False alarms** cause churn: Claude revising correct edits.
- **Anchoring:** Claude applies everything Jev does not flag.
- **Compound questions:** "omits something still current" mixes recall with currency. This may need splitting.
- **Request size:** large rewrites may exceed batch limits.
- **Overhead in both arms** may dominate any benefit.

## Diagnostics before any agent run

- **A fresh labelled set**, for example `jev-diag/3`: (old entry, proposed revision, recent updates) triples, with labels for each question, written before any Jev answer.
- **Sources:** realistic edits taken from existing CLM traces, mutated to include both risks and correct edits.
- **Readiness:** the strategy is not ready for an agent pilot unless the component shows useful separation at a pre-fixed threshold.

## Outcomes

- **Primary:**
  - strict success, especially omissions and stale facts;
  - all-attempt cost.
- **Secondary:**
  - edits revised or withdrawn after the check in each arm;
  - calls and time added by the check;
  - Jev latency and cost.

## Limitations

- **The check opportunity itself is an intervention**, and its overhead is measured in both arms.
- **Scope:** the same task family and model as 009.
- **Not comparable across experiments:** results are not comparable with strategies 1 and 2 without a [common-workload comparison](../jev-assistance-roadmap.md#order-and-gating).
