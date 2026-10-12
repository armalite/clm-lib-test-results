# 008 – Protocol: optional Jev assistance for model-controlled context management

_Written on 2026-10-12, before any paid experiment-008 call. Later notes are appended below; earlier sections are not rewritten afterwards._

## Question

**Can a fast decision model help an agent manage its own context?**

The first capability is: **"Which existing context entries need review because of this update?"**

Two conditions are compared:
- **A: CLM alone.**
- **B: the same CLM with optional Jev assistance.**

**Equal in both:**
- The main model alone decides whether, when and how to edit its context.
- It can inspect the context directly and write reusable context-management helpers; neither condition requires helpers (mode `clm_helpers`, the experiment-007 "optional" wording).
- Jev only advises. It never removes, rewrites or keeps entries, and the main model can ignore it.

**Purpose:** this is our own exploratory experiment. It is designed to produce useful evidence, including negative results.

## Related work, and how this differs

- **TypeSafe Jev** ([introduction](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [docs](https://docs.typesafe.ai/)): a "System One" model for fast, structured decisions. A `noul` question returns the probability that a yes/no question is answered yes. Several questions can be batched against one `state` and are evaluated independently.
- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**: replaces Claude Code's compaction summary with the original transcript minus the tool calls and results that Jev judges stale.
  - **Questions:** **predefined** rules pin recent and first messages. For each remaining call, two fixed `noul` questions decide whether to keep the call or result, at a 0.5 threshold.
  - **Automatic:** the decisions are applied automatically.
  - **No model-written state:** the README states that nothing is summarised.
- **[Handing context between agent calls](https://muninn.austegard.com/blog/handing-context-between-agent-calls.html)** (Muninn):
  - It uses Jev to select verbatim transcript chunks for a subagent.
  - In a CLM-inspired relay, it **already combines Jev flags with model-written state updates**: Jev flagged likely handovers, the subagent updated its own table with the flags in view, and code validation guarded the edits.
  - **This experiment is therefore not the first Jev and CLM combination.**
- **What differs here:**
  - Jev is an **optional, model-invoked** advisory action inside a CLM loop, where context edits are the model's own code.
  - Nothing is filtered automatically, and the main model chooses whether to ask, which update and which entries.
  - The comparison is matched, with and without the option, under one runtime.

## Integration (clm-lib)

### Boundary

- **The sandbox is unchanged:** the model-written Python sandbox still has no network and no credentials.
- **Host-mediated action:** Jev is called **only by the host runtime**, through a new, versioned action, `review_context`. It is enabled per run and off in every historical configuration.
- **Limitation:** sandboxed helper code cannot call Jev synchronously. A model that wants Jev advice inside a helper workflow must ask for it as a separate action and use the result in a later step.

### The action

The action exists only in condition B's schema and system prompt:

```json
{"action": "review_context", "revision": <int>, "entry_ids": ["<id>", ...], "update": "<text>"}
```

Instead of `update`, the action may give `"update_entry_id": "<id>"`, the id of an entry in the same revision that contains the update.

**The runtime validates:**
- that the revision exists;
- that all ids are in **that** revision, with no duplicates and at most 40;
- that exactly one update source is given, non-empty and at most 4,000 characters;
- that the review limit (12 per run) is not reached.

**Rejected requests** cost no Jev call; the observation says "Context review not performed: … Your context is unchanged."

**What is sent:**
- the **exact entry text from the referenced revision**, never retyped by the model and never taken silently from a newer revision;
- the update text, or the referenced entry's text.

**What is never sent:** future stages, evaluator truth, hidden labels or audit history. All of these are outside what the agent can see, and a test checks this.

**Status line:** both arms' runtime status gains one line, "context revision N", so that the condition-B model can name a revision. Condition B also gains "context reviews used k/12".

### The fixed question (`jev-review/1`)

There is one `noul` question per entry, batched up to 20 per HTTP request:

- **State:** `{"update": "<update text>"}`.
- **Instructions:**

  ```json
  {"question": "Does this update require reconsidering a current assertion or planned action in this entry?", "entry": "<entry text>"}
  ```

- **Criteria:**
  - **true:** "Yes if the update explicitly replaces or contradicts something the entry currently asserts or plans, or changes part of it (for example a cause, status, value, requirement or next step), even when other parts of the entry remain valid. Reconsidering does not mean the whole entry is wrong or should be deleted."
  - **false:** "No if the entry is unrelated to the update, if the update only adds information without changing what the entry asserts or plans, or if the entry describes a historical fact or a failed approach that is still correctly described as historical after the update."

**Why it is worded this way:**
- The wording is fixed for this experiment, and the main model does not write rubrics.
- **One judgment per question:** one narrow yes/no per entry, with high meaning yes. This follows the `noul` guidance and the Jev 1.13 known issues (literal reading, compound questions, context rot).
- **Not a single score:** the probability is advisory output, not a guarantee of correctness. It is not a single score combining relevance, validity and retention. "Affected" does not mean "incorrect" or "delete".

### The observation

The model receives the following, with every submitted entry listed in submitted order:

```
Context review advice (jev-review/1; Jev <model>; revision N; update: <source>). Probability that the
update requires reconsidering a current assertion or planned action in each entry. Advisory only:
your context is unchanged.
  <id>: 0.91
  <id>: no answer
Coverage: k of n entries answered.
[Service problem: <reason>]
```

- **Nothing is filtered:** no low-probability entry is dropped from the advice.
- **Failures:** a service failure or malformed response becomes "no answer" with a service notice, and the agent continues.
- **The action itself changes no entry.** The runtime appends the step's action and observation, as for every step. Any later edit goes through the existing execute-and-validate path.

### Calls, limits and accounting

**Main-model calls:** the turn that requests advice and the turn that reads it are both ordinary main-model calls, and count in `max_calls` (60).

**Jev calls:**
- **Limits:** at most 12 reviews per run, a 15 s timeout, and 1 runtime retry for 429/529/5xx and timeouts.
- **Retries:** the official SDK retries twice by default. This client uses plain HTTP, so there are no hidden retries.
- **Ledger:** every attempt has its own ledger entry (kind `jev`, with the provider, `typesafe`, in the note). Each is reserved before the call, at most one token per request byte plus 2,048 tokens, and settled from reported usage. Rejected requests (401, 422, 429, 529) are charged USD 0; unknown outcomes are charged the full reservation.
- **Price:** `jev-1.13.0` costs USD 0.042 per million input tokens, and output tokens are free ([models](https://docs.typesafe.ai/models), retrieved 2026-10-12).

**Model:** pinned to `jev-1.13.0`. The aliases `jev-latest` and `jev-preview` can move. The response's `model` field (the version that answered) is recorded.

**Credentials:** `TYPESAFE_API_KEY` is read from the host process environment and is never printed, saved in traces or passed to the sandbox.

**Evidence per run:**
- `jev/NNNN.json`: each attempt's request body (without headers), the response, latency, usage and cost.
- The `context_review` events.
- `summary.json → jev`: reviews, attempts, errors, retries, TypeSafe tokens (kept separate from Anthropic tokens, since the tokenizers differ), cost and latency.
- **Review records:** the revision, the entries and update sent, every answer, and the models, plus:
  - the entries flagged at the reporting threshold;
  - the accepted edits that followed before the next review;
  - flagged entries that were later changed;
  - unflagged entries that were later changed.
  - **"Followed by an edit" is temporal association, not attribution.**
- `cost.by_provider` (Anthropic and TypeSafe).

## Conditions and shared controls

**Config:** `configs/exp008.toml`, which is the latest corrected runtime (`exp007r.toml`) with:
- `status_shows_revision` on for both arms;
- the `[jev]` settings;
- this experiment's ceiling.

**The same for both arms:**
- `claude-opus-5-5`, effort `low`, an 8,000-token request budget, 4,096 output tokens, 60 main-model task calls;
- the same task inputs and file access;
- mode `clm_helpers` (direct editing, optional helpers);
- the `blocks/1` layout with 5-minute prompt caching, and cold-cache `run-tag/1` isolation per run;
- the spill and pressure-notice fixes;
- the scorer (`rounds-score/1`) and the validation.

**What differs (B only):**
- The `review_context` action in the schema and the status line.
- This neutral notice, appended to the system prompt:

  ```
  CONTEXT REVIEW ADVICE (optional, this run):
  - Reply {"action": "review_context", "revision": <context revision number from <runtime_status>>,
    "entry_ids": ["<id>", ...], "update": "<the new information>"} to ask a fast classifier (Jev)
    whether that update requires reconsidering a current assertion or planned action in each listed
    entry of that context revision. Instead of "update" you may give "update_entry_id": the id of
    an entry in the same revision that contains the update.
  - The runtime sends only the update text and the listed entries' text. The next observation gives
    one probability per entry. The advice is probabilistic and can be wrong; it never edits your
    context, and you decide whether and how to edit. A review uses one of your model calls (at most
    12 reviews per task); if the service fails you get a notice instead of advice.
  ```

- The resulting observations.

**What the notice avoids:** it does not say Jev must be used, or suggest that it improves the score. **Prompt version:** `2026-10-12.1`; earlier prompt texts are byte-identical.

## Component diagnostic

**Purpose:** a component test, not evidence about end-to-end agent performance.

**Case file:** `diagnostic-cases-v1.json` (SHA-256 `68860b7579fdeb7bd08f9ff60c9159802394bd0a9322a02f00600d1d3ff9d843`), labelled on 2026-10-12 before any Jev answer existed.
- **The labels:**
  - **affected:** the update requires reconsidering a current assertion or planned action in the entry;
  - **unaffected:** it does not;
  - **ambiguous:** reasonable readers could disagree.
- **Justifications:** each case carries one, based on the supplied text.
- **Development split (6 cases, 3 updates):** for wording checks only, never scored with the frozen set.
- **Frozen split (24 cases, 9 updates):**
  - **Labels:** 10 affected, 12 unaffected, 2 ambiguous.
  - **Kinds:** explicit replacement (5), partial change (2), unchanged part of a partial change (3), unrelated (6), historical statement (2), a multi-fact entry (1), connection to an early fact (1), a log format change (1), consistent (1) and ambiguous (2).

**Run:** `clm-lib --config configs/exp008.toml jev-diagnostic --cases experiments/008-jev-context-review/diagnostic-cases-v1.json --split frozen`. This makes one request per update, with the same request builder as the integration.

**Report:**
- affected entries flagged and missed;
- unaffected entries flagged unnecessarily;
- the ambiguous cases separately (their probabilities only);
- unanswered cases;
- latency, TypeSafe tokens and cost.

**Threshold:** precision and recall are reported at the **reporting threshold of 0.5**, fixed in the case file before scoring. This threshold is not an editing policy, and the agent never acts on it.

## Development pilot (four fresh runs)

**Task:** experiment 007's multi-round incident task (`incident-rounds-gen/1`), on development instances `rounds-dev-1` (10 rounds) and `rounds-dev-2` (11 rounds). These instances were already used in experiment 007's calibration; the pilot runs are fresh.

**Why it suits the capability:** each round's board updates create real review opportunities:
- a suspected cause revised;
- a status superseded (mitigated, then resolved);
- a partial update adding a service;
- follow-ups closed;
- a false alarm closed;
- a late log line that must be connected to a round-1 or round-2 change.

**Runs:** 2 instances × 2 conditions = **4 runs**.
- **Command:** `compare --tasks rounds-dev-1,rounds-dev-2 --reps 1 --conditions clm_helpers:on,clm_helpers+jev:on`.
- **Order:** dev-1 A then B; dev-2 B then A.

**Use of Jev:** B is never told to use Jev.
- **If B does not use it:** that is reported as the outcome. Prompts are not strengthened and runs are not replaced.
- **Optional plumbing smoke test:** a forced-use test of at most one run, labelled `smoke`, may verify the live plumbing. It is excluded from the comparison.

**Measured:**
- strict success and categories, especially stale facts, omissions and citation errors;
- total cost by provider;
- elapsed time and each provider's latency;
- main-model calls, tokens, and cache reads and writes;
- Jev calls, usage, retries and errors;
- every Jev request and answer, and the versions;
- subsequent accepted edits linked by revision and entry id;
- recoveries, rereads and extra work visible in traces.

**Reporting:**
- Unsuccessful runs stay in all totals.
- The main model has already paid to read its context before it asks, and each review adds a round trip. No input saving from Jev is claimed.
- Perfect scores would limit accuracy claims but not usage and efficiency findings.

## Larger evaluation: a plan only, not authorised and not run

**Sample and order:**
- **Runs:** about **4 fresh instances × 3 repetitions × 2 conditions = 24 runs**.
- **Instances:** these would need **new evaluation instances**. `rounds-eval-1..4` were used by experiment 007's evaluation and are not fresh. They would be four new seeds of the same generator (for example `rounds-eval-5..8`), registered when the plan is frozen and never inspected before then.
- **Order:** within each instance and repetition block, the order alternates by (instance + repetition), so each instance runs A first in some repetitions and B first in others. The realised balance would be reported.

**What it could establish:** whether optional Jev review changes cost, time, call counts, context-edit behaviour and (if not at ceiling) strict success, on this task family with this model, wording and capability.

**What it could not establish:**
- generality across task families: fresh instances are variants of one synthetic family, not independent families;
- whether a different question, or an automatic policy, would help;
- the effect of Jev beyond this model and this effort setting.

**Metrics:**
- **Primary:** strict success and mean all-attempt cost per run.
- **Secondary:**
  - categories (stale, omission, citation);
  - elapsed and provider time;
  - main-model calls;
  - review usage;
  - flagged-then-changed rates;
  - per-provider tokens.
- **Paired:** differences by block, shown with individual runs.

**Failure handling:** invalid runs are labelled and kept. An infrastructure defect halts the comparison and is recorded. There are no reruns, tuning on evaluation instances, or sample changes after results.

**Budget estimation:** the mean pilot cost per run of each arm (all attempts) × 12 per arm × 1.25. It needs its own explicit authorisation before running.

**Possible follow-ups (not part of this build):**
- a second task scenario;
- comparing Jev against another cheap advisor, for example a small LLM asked the same question.

## Budget

- **This session:** at most **USD 10** across Anthropic and TypeSafe, covering smoke checks, the diagnostic and the four-run pilot. This is an upper bound, not a target.
- **Ledger:** USD 46.993902 spent. The ceiling was set once, explicitly, to **USD 56.993902** (spend + 10).
  - This lowered it from USD 63.713, because earlier unused authorisation does not carry over.
  - Every older config has a higher ceiling and cannot raise it; only `budget --set-ceiling` can.

## Session record (2026-10-12)

**No paid call was made.** `TYPESAFE_API_KEY` was available neither in the host environment nor in the maintainer's configured private credential file, and no other file was searched.

**Completed:**
- this protocol;
- the integration and offline tests;
- the frozen, labelled diagnostic set.

**Not run** (each needs Jev access):
- the diagnostic;
- the pilot;
- any smoke test.

**The pilot was not run with only arm A,** because a comparison without B would not answer the question.

## Design check before paid runs (2026-10-12)

**The finding:** the review validation does **not** yet enforce the intended active-context boundary. It accepts **any revision that exists** in the host's revision history, not only the current one. So a review can name an older revision and an entry the agent has since deleted. An offline check with a fake advisor confirmed that:
- the deleted entry's text is then sent to Jev, either as a reviewed entry or as the update via `update_entry_id`;
- the agent receives a probability about it.

The deleted text itself is not echoed back into the agent's context.

**Why it matters:** this does not match the intent that Jev receives only information the agent can currently see.

**Before any diagnostic-into-pilot or pilot run:**
- restrict reviewed entries and `update_entry_id` to the agent's current context, for example by accepting only the current revision;
- add a regression test;
- record the change here.

The component diagnostic does not use the agent loop, so it is unaffected.

## Boundary fix (2026-10-12, before any paid experiment-008 call)

The design check above was resolved before the diagnostic and pilot. The note above is kept unchanged.

**The rule now:** a `review_context` request is accepted only against the **current** context revision, which is the number the runtime status shows the model at that step.
- A request naming an older revision is rejected with "revision N is no longer current; reviews use only the current context revision (M)". A revision that never existed is rejected as "does not exist".
- `entry_ids` and `update_entry_id` resolve only from the current revision. An entry the agent has deleted therefore cannot be reviewed or used as the update, by naming an older revision or by its id.
- All validation happens before any ledger reservation or Jev request, so a rejected request costs nothing and leaves no `jev/` trace.

**Regression coverage** (`tests/test_jev.py`):
- `test_deleted_entries_never_reach_jev`: after the agent deletes an entry, four requests are rejected with no Jev call, no `jev` ledger entry and no deleted text in the observation. They are the deleted entry as a candidate or as the update, each against the old revision and against the current one.
- `test_current_revision_review_uses_the_revision_shown_to_the_model`: the revisions shown to the model are 0, 1, 3 and 4, and a review naming 3 is accepted. It sends the exact text of the current entries, and the advice reports revision 3.
- Against the earlier validation, both old-revision cases fail, with the deleted text sent as an entry or as the update. This confirms that the tests detect the defect.

**Unchanged:** the prompt text (it already asked for the revision from `<runtime_status>`), the prompt version, the question, the case file and every historical configuration.

## Live session record (2026-10-12 UTC)

Run in the order the protocol fixed, after the boundary fix. No case, label, threshold or question wording was changed after seeing any answer.

1. **Development-split diagnostic (API smoke check):** `20261012T105929-dev`. The request shape was accepted, `model` reported `jev-1.13.0`, and usage was reported and settled in the ledger (kind `jev-diagnostic`). It cost USD 0.000083.
2. **Frozen diagnostic:** `20261012T105948-frozen`, 9 requests and no errors. At 0.5: 10/10 affected flagged, 1/12 unaffected flagged (`f-04`, 0.56); ambiguous 0.83 and 0.57. It cost USD 0.000302. This revealed no substantial question-design problem, so the pilot went ahead.
3. **Pilot:** comparison `20261012T110017`, 4 runs, all strict successes.
   - **Condition B made 0 reviews in both runs.** Per this protocol, that is reported as the outcome; the prompt was not strengthened and no run was replaced.
   - No forced-use smoke run was made.

**Spend:** USD 1.41506 (Anthropic 1.414675, TypeSafe 0.000385) of the USD 10. The ledger is at USD 48.408962 of USD 56.993902, unchanged. The larger evaluation was not run and is not authorised. Findings are in `README.md`.
