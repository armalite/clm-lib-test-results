# 015 – `dev-tools2`: one live development session of `paper-clm-tools/2`

_Pre-run record written 2026-10-22, before dispatch. The result is added below after the run._

## Scope and authorisation

**What runs:** one session of `paper_clm_tools` with **`paper-clm-tools/2`** ([paper-clm-tools-v2.md](paper-clm-tools-v2.md)) on docthread-dev-1, all eight turns.

**The plan:** [dev-tools2-spec.json](dev-tools2-spec.json), derived from dev-tools1's spec ([dev-tools1-spec.json](dev-tools1-spec.json)).
- **What differs:** only the paper-tools version, this run's identifiers (launch ID and authorisation path) and its note and settings status.
- **What is unchanged:**
  - the task (`docthread-task/2`), the instance, the model settings (`claude-sonnet-5`, adaptive thinking, effort high, `max_tokens` 8,192), the 5-minute cache and its breakpoints;
  - the retries (`p015-retry/1`, 2 provider retries), the tools, the budgets (32,000, limit 29,952) and the arm settings (margin rollback, 6 retries per session, readouts, 60 steps, 144 calls);
  - the scoring and the ending policy (`p015-turn-endings/1`, `p015-truncation/1`);
  - the prompts and the implementation (clm-lib `4b9ba4c`).

**What version 2 changes from the version dev-tools1 ran:**
- **Earlier-turn edits:** use the version 2 rebuilding rules. A reply the rebuild merges or alters is sent without its thinking blocks.
- **Current-turn tool results:** their text can be rewritten, for example summarised.
- **Current-turn thinking replies:** an edit that would alter a reply of the turn in progress carrying signed thinking is refused at staging with a reason. That covers deleting its calls or results, editing its text, calls or thinking, and merging it with another reply. The check is repeated at the commit, after rollback and before every dispatch. A refusal at staging is a task step.
- **The compatibility ending:** if rollback or the final guard could not keep those replies intact, the turn would end as `request_incompatible`, a harness outcome, with nothing dispatched.

**Not an interface-only ablation:** like version 1, the arm differs from the shell arm in rollback, notices and the free-step rule as well as interface. Version 2 adds the restriction above.

**Authorisation:** given by the maintainer on 2026-10-22. It covers exactly one eight-turn session, with a new US$4 block stop that includes reservations, retries and any uncertain charges, within the existing programme ceiling.
- **The launch:** new launch ID `dev-tools2` and its own block authorisation. dev-tools1's is not reused.
- **Not authorised:** replacements, other arms, confirmation runs, or any ceiling increase.
- **The effective block limit is US$4.00.** Programme room and ledger room are both US$28.608209.

**Starting state, verified:** ledger spent US$103.048867, programme 015 US$14.949121, no pending reservations, ledger ceiling US$131.657076. guarded-clm is at its pin (`cce58c1`, source `51e6dbe8…`), unused by this arm.

**The freeze:** [dev-tools2-freeze-record.json](dev-tools2-freeze-record.json), with contract sha256 `95bfb6fb…`.

## Predeclared interpretation

Each question is answered separately:
1. **Provider compatibility:** did the requests that followed accepted edits succeed?
2. **Context editing:** were substantive reductions accepted, and present in later requests?
3. **The restriction's impact:** which edits were refused, what feedback reached the model, and did it recover?
4. **The task outcome:** completion, score, context pressure, cost and ending.

**How outcomes are read:**
- **Not grounds for a replacement:** a low score, no edits, or an ordinary context-limit ending is an observed outcome.
- **Paths never exercised:** for example, no current-turn refusal or no earlier-turn merge. Compatibility for those paths is reported as **untested**.
- **A provider rejection of a rebuilt request, or `request_incompatible`:** the evidence is preserved and dispatch stops. Nothing is patched and rerun within this authorisation.

## Result (added after the run)

**The run:** launched detached at 2026-10-21T13:00:06Z (UTC; 2026-10-22 local); the launcher ended with code 0 at 13:03:00Z.
- **Time:** 174 s wall time, 167.0 s provider time.
- **Ending:** the session ended in turn 7 at its ordinary context limit (`context_limit`, outcome `arm_failure`). Turns 1–6 completed, and turn 8 never ran.
- **No compatibility incident:** no provider error, no `request_incompatible`, and nothing was patched or rerun.

**The evidence:** [dev-tools2-export/](dev-tools2-export/), which verifies (manifest problems none, checksums pass, no home paths or credentials), and the exposure report [dev-tools2-exposure.md](dev-tools2-exposure.md) (and `.json`).

### 1. Provider compatibility

**All 44 provider requests were accepted.** There were no retries, failures, truncations or refusals. Every request that followed one of the 7 committed edits succeeded.

| Path exercised | Live result |
| --- | --- |
| earlier-turn deletions whose rebuild merged or altered replies, with thinking omitted (version 2's rule) | **accepted**: 4 commits, omitting 1, 3, 1 and 2 thinking blocks |
| earlier-turn deletions without merged thinking, an inserted note, and an earlier-turn assistant-text rewrite | **accepted**: 3 commits |
| current-turn edits that would change a signed-thinking reply | **refused before dispatch** (2) |
| current-turn tool-result rewrite (allowed by version 2) | **untested**: the model never attempted one |
| commit-time refusal, and a rollback that could not keep the turn's replies intact | **untested**: neither occurred |

### 2. Context editing

**All seven accepted edits were made during turn 4,** and all removed or rewrote earlier-turn material (turns 1 and 2). None changed the current turn.

| # | Staged after attempt | Operation | What it removed or changed | Request size (chars) |
| --- | --- | --- | --- | --- |
| 1 | 15 | delete 7 blocks | turn 1's `queue_stats` calls and results | 84,959 → 77,736 |
| 2 | 17 | delete 3 blocks | two turn-1 `read_journal` pages (a call with its result, and a result with its call) | 91,059 → 72,086 |
| 3 | 19 | delete 12 blocks | turn 2's six `list_changes` calls and results | 81,326 → 75,959 |
| 4 | 21 | delete 4 blocks | two more turn-1 `read_journal` pages | 91,657 → 73,511 |
| 5 | 29 | delete 2 blocks, insert a note | the turn-1 page 9 read, replaced by a `[notes]` block with its key fact | 107,678 → 100,000 |
| 6 | 31 | `replace_block` | a turn-1 reply text rewritten as a page-9 summary | 99,422 → 99,482 |
| 7 | 33 | delete 2 blocks | one turn-2 `list_changes` exchange | 109,030 → 107,046 |

**Delivery:** in every case the deleted calls are absent from the request that carried the commit and from every later request. The inserted note and the rewritten text appear in every later request.

### 3. The restriction's impact

**Four edits were refused at staging.** Each was a task step under the existing rules.

| After attempt | Refused set | Reason | Did the reason reach the model? |
| --- | --- | --- | --- |
| 23 | delete block 29: the model's own earlier `context_apply` call in this turn | **current-turn thinking** (blocks 28, 29, 31, 32: altering that reply and merging it with the next) | yes, requests 24–27 |
| 24 | `replace_block` on block 29 with journal-summary text (apparently mistaking the call for a tool result) | the call's text must remain a JSON object (an ordinary operation rule) | yes, requests 25–30 |
| 27 | delete blocks 32–33: this turn's `context_read` call and its 8,000-character view | **current-turn thinking** (blocks 31, 32, 34, 35) | **no**: the next request was over the limit, and the rollback undid that step with its receipt |
| 38 | `replace_block` on an earlier block | the result would have been over the limit (31,654 tokens) | **no**: undone by the final-turn rollback |

**Recovery:** after the refusals the model went on editing earlier-turn material (edits 5–7) and completed turn 4. The refused current-turn deletions targeted this turn's own edit call and its own `context_read` copy. Rewriting that view's text would have been allowed, but was not attempted.

### 4. Pressure and task outcome

**Turn 4 carried the pressure:** 30 attempts, 23 task steps and 7 free steps, 8 reminders.
- **Rollbacks:** 7 rollback events undid 15 steps, mostly the model's own `context_read` views. That used all 6 per-session retries, and the seventh gave the last-turn note.
- **Turn 4 still completed**, as did turns 5 and 6.
- **Turn 7:** its first request was about 30,018 estimated tokens, over the 29,952 limit. With the final turn already given, it ended at the context limit with no attempt.
- **Peaks:** reported input 29,923 tokens; estimated request 29,824 tokens.

**Score: 7/10, recall 1/3.**
- **Correct:** questions 1–3, 5 (a recall field) and 6.
- **Wrong:** question 4 (the wrong evidence line).
- **Missing:** questions 7 and 8 (both recall fields).

**Attempts:** 44 main attempts (30 in turn 4). There were 22 task-tool calls.

### Charges

| | USD |
| --- | --- |
| confirmed (provider usage, 44 entries) | **0.947527** |
| assumed at the reservation | 0 |
| pending | 0 |

**The block:** US$0.947527 of the US$4 block.

**The ledger after the run:**
- spent 103.996394 (from 103.048867);
- programme 015 at 15.896648 (from 14.949121);
- ceiling unchanged at 131.657076;
- nothing pending.

### Reading against the predeclared interpretation

1. **Provider compatibility:** established for the paths exercised. Requests carrying earlier-turn rebuilds, including four with thinking omitted, were all accepted. Current-turn rewrites of tool results, commit-time refusals and an incompatible rollback were not exercised and remain **untested**.
2. **Context editing:** substantive reductions were accepted and present in every later request.
3. **The restriction:** it refused two current-turn edits before dispatch. One reason reached the model. The other was lost when the overflow rollback undid its step, which is existing rollback behaviour. The model recovered by editing earlier turns.
4. **The task outcome:** six of eight turns completed. The session ended at an ordinary context limit in turn 7, scoring 7/10, at US$0.947527.

### Is a comparison technically ready?

**No harness or provider defect remains on the paths exercised,** so the arm can technically run in a comparison as a separately labelled adaptation. A comparison must state these limits:
- **The restriction:** within a turn, the arm cannot delete this turn's tool exchanges, including its own `context_read` views, which drove most of the overflow here. It can only rewrite their results.
- **Retries per session:** the six rollback retries are counted per session, and this session used them all in turn 4.
- **Lost refusal reasons:** a refusal's reason is lost when its step is rolled back.
- **Untested paths:** as listed in §1.
- **The evidence:** one session on one development instance; not a comparison result.

**No further session is authorised.**
