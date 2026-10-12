# 008 – Optional Jev assistance for model-controlled context management

**Status: component diagnostic and four-run development pilot complete; the larger evaluation is not authorised and was not run.**

**Headline:**
- **The diagnostic:** on 24 frozen labelled cases, Jev's per-entry answers to the fixed question matched our labels well. It flagged 10 of 10 affected entries and 1 of 12 unaffected entries at the 0.5 reporting threshold.
- **The pilot:** the agent **never chose to use the optional review action** (0 reviews in both condition-B runs). All four runs succeeded, at similar cost and time.
- **So far:** this experiment shows a usable component, but **no evidence that offering it changes agent behaviour or outcomes.**

## The question

**Can a fast decision model help an agent manage its own context?**

The first capability tested is *"Which existing context entries need review because of this update?"*

**Conditions:**
- **A:** CLM alone (`clm_helpers`: the model edits its own context with code and may write reusable helpers).
- **B:** the same CLM with an optional, host-mediated `review_context` action.
  - **How it works:** it sends an update and a chosen list of current context entries to TypeSafe's Jev model (`jev-1.13.0`), and returns one probability per entry for *"Does this update require reconsidering a current assertion or planned action in this entry?"*.
  - **Advice only:** it never edits anything, and the agent may ignore it.

**Prior work:**
- fast-jev-compaction already uses Jev to drop stale tool output by fixed rules.
- The Muninn post already combined Jev flags with model-written state updates.
- **This is not the first Jev and CLM combination.** What differs here is that the advice is optional and model-invoked inside a CLM loop. See `protocol.md`.

## 1. Boundary fix before any paid call

An offline design check found that `review_context` accepted **any historical revision**. A request could therefore send Jev the text of an entry the agent had already deleted. Before any paid call, this was fixed:
- Reviews are accepted **only against the current context revision**, the number shown to the model in its runtime status.
- `entry_ids` and `update_entry_id` resolve only from that revision.
- Stale revisions are rejected before any ledger reservation or Jev request.

**Tests:** regression tests cover a deleted entry used as a candidate or as the update, against both the old and the current revision. Another test confirms that a valid review naming the revision shown to the model still works. Against the old validation, the stale-revision cases fail, so the tests detect the defect.

**Unchanged:** prompts, question, case file and historical configurations. Details are in `protocol.md` ("Design check" and "Boundary fix").

## 2. Component diagnostic (Jev alone, no agent)

**Case file:** `diagnostic-cases-v1.json` (SHA-256 `68860b75…d843`, unchanged), labelled before any Jev answer. Each request carries one update and its cases, one `noul` question per entry. This is the same request builder as the agent integration.

**Development split (6 cases), run first as the API smoke check:** `artifacts/diagnostics/20261012T105929-dev`.
- **API:** the live API accepted the request shape. It reported `model: jev-1.13.0` and returned usage; output tokens are free.
- **Ledger:** each attempt was reserved and settled from reported usage, kind `jev-diagnostic`, with nothing pending. The reservation bound (about 3,950 tokens per request) was well above actual input (about 670).
- **Answers:** 2 of 2 affected flagged, 0 of 3 unaffected flagged, and the ambiguous case at 0.13.

**Frozen split (24 cases, 9 requests):** `artifacts/diagnostics/20261012T105948-frozen`. It was scored once at the pre-fixed 0.5 threshold, with nothing tuned afterwards.

| | Result |
| --- | --- |
| Affected flagged (recall) | **10 / 10** |
| Unaffected flagged (false positives) | **1 / 12** (`f-04`, 0.56) → precision 10/11 = 0.91 |
| Ambiguous (reported separately) | `f-19` 0.83, `f-21` 0.57 |
| Unanswered / errors | 0 / 0 |
| Latency | 0.24 s per request on average (max 0.28 s); 2.15 s total |
| TypeSafe tokens / cost | 7,217 input, 444 output / USD 0.000302 |

**By case kind:**
- **Affected:** all were flagged, including partial changes (0.85, 0.97), a multi-fact entry (0.95), a log-format change (0.94) and a connection to an early fact (0.78).
- **The weakest true positive:** `f-14`, 0.63. A round-9 config-validation error bears on an entry saying "cause not yet identified".
- **Historical statements** (0.37, 0.29) and **unchanged parts of partial updates** (0.25, 0.20, 0.16) stayed below 0.5.
- **The one false positive** (`f-04`, 0.56): the update was *"Thread B root cause revised: … UPSTREAM_RATE_LIMIT; this supersedes the earlier suspicion of CACHE_STAMPEDE"*, and the entry was *"Open follow-ups: ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET."* A cause revision does not change follow-ups, though a reader might reasonably wonder whether VENDOR_TICKET relates to the upstream provider.

**Readable examples (frozen split):**

| Update (shortened) | Entry | Label | Jev |
| --- | --- | --- | --- |
| Thread B cause revised to UPSTREAM_RATE_LIMIT, superseding CACHE_STAMPEDE | "Thread B (payments-svc): suspected cause CACHE_STAMPEDE per round-04/board.md:3; next: confirm via cache miss logs." | affected | 0.96 |
| same | "History: at round 4 the board first suspected CACHE_STAMPEDE for thread B." | unaffected (historical) | 0.37 |
| same | "Open follow-ups: ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET." | unaffected | **0.56** |
| Round 9 log: config validation failed `http.max_inflight=0` | "Thread C: cause not yet identified; next step: inspect notify-worker restarts." | affected | 0.63 |
| Thread D closed as a false alarm (synthetic monitor misconfigured) | "Monitoring has been unreliable…; treat synthetic alerts with care." | ambiguous | 0.83 |

**Limits of the diagnostic:**
- **Our own labels:** 24 cases with labels we wrote ourselves, at one threshold.
- **Not independent of the pilot:** most update texts (6 of 9 frozen) share wording with the pilot's development instances, which come from the same generator.
- **Scope:** it shows the component answers this narrow question sensibly on these cases, not that its advice would help an agent.

## 3. Development pilot (4 runs)

**Setup:** `rounds-dev-1` (10 rounds) and `rounds-dev-2` (11 rounds) × A and B, in the order dev-1 A, B; dev-2 B, A. This is comparison `20261012T110017`, with config `configs/exp008.toml` (`claude-opus-5-5`, effort low, 8,000-token budget, 5-minute caching, cold isolated cache per run). B was never told to use the action.

| | A dev-1 | B dev-1 | B dev-2 | A dev-2 |
| --- | --- | --- | --- | --- |
| Run id | `…110017…dev-1-2871` | `…110232…jev-rounds-dev-1-6023` | `…110447…jev-rounds-dev-2-64f9` | `…110709…dev-2-d3af` |
| Strict success (14 checks) | S 14/14 | S 14/14 | S 14/14 | S 14/14 |
| **Jev reviews** | — | **0** | **0** | — |
| Cost USD (Anthropic / TypeSafe) | 0.3246 / — | 0.3552 / 0.0000 | 0.3475 / 0.0000 | 0.3874 / — |
| Elapsed / provider time (s) | 134.3 / 105.1 | 135.6 / 103.4 | 142.0 / 109.9 | 159.5 / 126.9 |
| Model calls | 30 | 30 | 33 | 34 |
| Accepted context edits | 11 | 13 | 11 | 15 |
| Pressure steps | 5 | 8 | 8 | 0 |
| Helpers | `h.py`, used for all 11 edits | none | `h.py`, used for all 11 edits | none |
| Tokens: uncached / cache read / cache write / output | 3,624 / 95,260 / 35,326 / 5,722 | 4,047 / 107,837 / 42,207 / 5,319 | 4,419 / 122,543 / 35,397 / 6,417 | 3,875 / 106,955 / 40,367 / 7,433 |

**Means:**
- A USD 0.356 and 146.9 s, with 32 calls.
- B USD 0.351 and 138.8 s, with 31.5 calls.

There were no repairs, retries, recoveries, overflows, invalid runs, Jev errors or rejected reviews.

**Was Jev used voluntarily?** **No.**
- **Visible to the model:** in both B runs, the action and its notice were in the system prompt and schema from the first request, and the status line showed the revision number and "context reviews used 0/12".
- **Unused:** neither run ever issued, mentioned or reasoned about a review.
- **Consequences:**
  - there are **no agent-loop examples of Jev advice or of edits following it**;
  - the in-loop live path (agent request → host → Jev → advice observation) was **not exercised live**; it is covered offline, and the same HTTP client and parser were exercised live by the diagnostic.
- **Protocol:** the protocol did not allow strengthening the prompt or replacing runs, and none was done.

**What B did instead (an example of a missed review opportunity).** In B dev-1 the model kept append-only per-round notes (`n1`…`n9`) and deleted raw step entries every few steps.
- **Round 8:** the board revised thread B's cause ("supersedes the earlier suspicion of CACHE_STAMPEDE").
- **The model's edit** added a new note `n8` ("Thread B cause revised UPSTREAM_RATE_LIMIT (round-08/board.md:4) …").
- **Left untouched:** the older notes `n4` ("Thread B opened payments-svc CACHE_STAMPEDE ongoing … likely UPSTREAM_RATE_LIMIT") and `n5` ("still CACHE_STAMPEDE on board").
- **What a review could have done:** a review of `n4`/`n5` against the round-8 update was exactly the kind of check the action offers, and the diagnostic suggests Jev would have flagged them.
- **What happened anyway:** the final answer was still fully correct, so leaving them did no harm here.

The other runs mostly kept one rolling note that was rewritten every few steps. That leaves little for a per-entry review to discriminate.

**Overhead:** with zero reviews, B's only overhead was the extra prompt text, about 880 characters of system prompt (roughly 200–250 tokens), cached after the first call. Cost and time differences between arms are within the run-to-run variation of two pairs.

## What the results support

- **Supported:**
  - The integration works end to end at the component level: request shape, model version reporting, usage accounting, and both-provider ledger entries.
  - On these labelled cases, Jev answers the narrow question sensibly (10/10 recall, 1 false positive in 12).
- **Supported (observation, 2 of 2 runs):** with the optional action merely available, this model at this effort did not use it on this task.
- **Not supported:**
  - any claim that Jev assistance improves context management, accuracy, cost or time;
  - any claim that the combination is novel.
- **Ceiling:** with all four runs at strict success, this task cannot show accuracy gains in any case.

## Is the larger evaluation ready?

**Not as planned.**
- **No use:** with zero voluntary use, a 24-run A/B evaluation would mostly measure the effect of an unused prompt clause.
- **No headroom:** the dev runs are at the accuracy ceiling.
- **Untested live path:** the in-loop path has not run live.

**Options for the maintainer to decide (none was run):**
1. A labelled `smoke` run that exercises the in-loop live path, excluded from any comparison.
2. A separate, explicitly different question, such as an *instructed* or *recommended* review condition. This would need its own protocol revision, as in experiment 007's revised phase.
3. A task where per-entry review has more to discriminate, such as many independent context entries or no rolling summary note, or with less accuracy headroom used up.

Any of these needs fresh evaluation instances (for example `rounds-eval-5..8`) and its own budget authorisation.

## Spend

- **This experiment:** USD 1.41506 of the USD 10 authorised for the initial experiment-008 work:
  - **Anthropic:** USD 1.414675 (pilot, 127 calls);
  - **TypeSafe:** USD 0.000385 (both diagnostics, 12 requests).
- **Ledger:** USD 48.408962 spent of the unchanged USD 56.993902 ceiling. Nothing has an unknown outcome or is pending.
- **Note:** the generated `report.md` spend line counts only run-attributed ledger entries (the pilot). The diagnostic entries are in the ledger snapshot under kind `jev-diagnostic`.

## Where is the evidence?

- `protocol.md`: the design written before any paid call, the dated design check and the boundary fix.
- `diagnostic-cases-v1.json`: the frozen cases and labels.
- `artifacts/diagnostics/`: every diagnostic request and response, latency, usage and cost per request, with `summary.json` scores.
- `report.md`, `metrics.json`, `metrics.csv`: the four pilot runs (phase `pilot`), including `jev_*`, `cost_anthropic_usd` and `cost_typesafe_usd`.
- `artifacts/runs/calibration/<run_id>/`: per-run requests, context revisions, scripts, helpers and scores.
- `artifacts/comparisons/20261012T110017/`: the frozen settings, the schedule and the source patch (the boundary fix was uncommitted at run time).
- `../../ledger-snapshots/`: the ledger at export.
