# 015 – `supp-tools1`: supplemental evaluation of `paper-clm-tools/2` on confirm1's instances (protocol)

_Pre-registered 2026-10-22, before any dispatch. The results are added in [supp-tools1-record.md](supp-tools1-record.md) after the run. This protocol is not edited after launch; its sha256 is in the freeze record._

## What this is, and what it is not

- **A later, supplemental evaluation** of `paper_clm_tools` with `paper-clm-tools/2`, one session on each of confirm1's six frozen instances. It is not part of confirm1, and its results are reported apart from confirm1 and from every development run.
- **The instances were already used** in confirm1 ([confirm1-record.md](confirm1-record.md)), and are taken unchanged from its frozen manifest ([confirm1-instance-manifest.json](confirm1-instance-manifest.json)): docthread-confirm-1 … 6, seeds 7407, 7402, 7403, 7404, 7405, 7496. They are not regenerated, replaced or selected by outcome, and their answers were not inspected for this block.
- **The arm was developed after confirm1,** using feedback from development instances: dev-v3a, dev-tools1 and dev-tools2, all on docthread-dev-1 ([dev-tools1-record.md](dev-tools1-record.md), [paper-clm-tools-v2.md](paper-clm-tools-v2.md), [dev-tools2-record.md](dev-tools2-record.md)). It did not use confirm1's instances. The other arms had no such second development round, so this is not a contemporaneous comparison.
- **guarded-clm and the summary arm are not rerun.** Their frozen confirm1 results are the comparison. confirm1's `paper_clm_shell` (version 2) results are kept as they are.
- **Not an exact reproduction of the paper,** and **not an interface-only ablation.** `paper_clm_tools` is a structured-tools adaptation ([paper-clm-tools.md](paper-clm-tools.md)). It differs from the shell arm in its interface, rollback, notices, free-step rule and the version 2 thinking restriction. No difference is attributed to the paper's method or to the editing interface alone.

## The arm, frozen

**`paper-clm-tools/2` exactly as validated in dev-tools2,** from clm-lib `414bd49`, whose arm source is unchanged since `4b9ba4c`. Arm settings:

| Setting | Value |
| --- | --- |
| budget | 32,000 (limit 29,952; reserve and rollback margin 2,048) |
| task steps and calls per turn | 60 and 144 |
| rollback retries | 6 per session, then a final-turn note |
| readouts | on |
| `context_read` page cap | 8,000 characters |
| finalize notice | at 3 steps left |
| version | `paper-clm-tools/2` |

**Its rules:**
- edits that would change a current-turn reply carrying signed thinking are refused, at staging, at the commit, in rollback and before dispatch;
- earlier-turn replies that were merged or altered are sent without their thinking;
- the existing rejection feedback and the existing prompts, estimator and editing operations apply;
- an unsupported rebuild would end the turn as `request_incompatible`.

## Shared settings, checked against the recorded configurations

These were compared field by field against confirm1's contract and dev-tools2's, and match both:

| Setting | Value |
| --- | --- |
| model | `claude-sonnet-5`, adaptive thinking, effort high, `max_tokens` 8,192 |
| caching | 5-minute cache, breakpoints `automatic`, `tool_definitions`, `instructions` |
| session tag | on |
| retry policy | `p015-retry/1`, 2 provider retries, 600 s timeout |
| task | `docthread-task/2`, eight questions |
| ending policy | `p015-turn-endings/1` (the first incomplete turn ends the session), `p015-truncation/1` |
| scoring | `docthread-score/1` (exact format), generator `docthread-gen/1` |
| tools and output cap | the shared docthread task tools |
| budgets | 32,000 tokens, 144 calls, 60 steps per turn, the same for all arms |

**Only the session tags differ:** they are generated for each launch, as for every launch. They are not a setting.

**The specification:** [supp-tools1-spec.json](supp-tools1-spec.json). It is dev-tools2's spec with only the instances, launch ID, authorisation path, note and status changed.

## Reporting, decided in advance

**Primary, per instance and in total:**
- exact-format points (out of 10) and recall (out of 3);
- completion: turns completed, and the ending;
- **paired differences** against each confirm1 arm on the same instance: guarded-clm, the summary arm and `paper_clm_shell` v2. These are given in points and in confirmed cost;
- confirmed cost, elapsed time (wall and provider), main calls and provider retries.

**The mechanism, per session:**
- accepted edits, and whether each reached later requests;
- current-turn versus earlier-turn edits, and thinking omitted;
- refusals by reason: current-turn thinking, other operation rules, over the limit;
- rollbacks, exhausted retry allowances and final turns, and refusal reasons lost when their step was rolled back;
- context exposure and pressure: peak estimate and reported input, reminders.

**Every outcome is kept.** A context-limit ending, a low score, a refused model edit or a session with no editing is a result, and none is grounds for a replacement or a repeat. With six sessions on one model and one task family, differences are described per instance. Instances are the units. No significance claim is made.

**Stops:**
- **A provider compatibility error** (a provider 400 on a rebuilt request) or a `request_incompatible` ending stops the block for review. The evidence is preserved, nothing is patched, and nothing resumes under this authorisation.
- **Ordinary arm outcomes** do not stop the block: the remaining instances run while the allowance permits.
- **If the block stop is reached,** the remaining sessions are reported as not run, with actual denominators.

## Spending

**The authorisation:** maintainer, 2026-10-22. At most US$10 of new spending for exactly these six sessions, including retries, reservations and uncertain charges. It sits within the unchanged programme ceiling (US$43.55733) and ledger ceiling (US$131.657076). There are no replacements, repeats or other arms.
- **The launch:** new launch ID `supp-tools1`, with its own block authorisation. No earlier authorisation is reused.

**The estimate:** about US$4–9 for the six sessions. dev-tools2 cost US$0.95 on a development instance, and confirm1's complete sessions averaged US$0.49 (summary) to US$1.07 (guarded-clm).
- **The reservation:** each attempt reserves up to about US$0.4.
- **Running short:** if the allowance runs short, a session ends as `spend_refused` and the remaining sessions are not run.

## A bookkeeping note: dev-tools2's seven rollbacks

dev-tools2 recorded seven rollback events against a six-retry allowance. Its trace shows the six rollbacks that used the retries (`retry` 1 to 6). The seventh came when no retry was left: the arm still rolled back to the margin, but gave the last-turn note instead of a retry (`retry` 6, `final_turn` true). The next over-limit request, turn 7's first, then ended the turn at its context limit. This is the documented rule (six retries, then one final turn), and it is unchanged here.
