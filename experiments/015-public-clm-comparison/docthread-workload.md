# 015 – The docthread incident-thread workload (design and offline verification)

_Written 2026-10-16. **Nothing has run against a model. There are no results.** Scripted sessions verify the
plumbing only; they say nothing about how any model or arm performs._

**Versions:** generator `docthread-gen/1`, task `docthread-task/1`, scorer `docthread-score/1`. The code is in clm-lib, at `src/clm_lib/p015/docthread/`, and is specified in clm-lib SPEC §29.

## The scenario

A fictional document-processing service accepts uploaded documents and passes each one, as a job, through seven components:
- `intake`;
- `scan`;
- `split`;
- `ocr`;
- `extract`;
- `index`;
- `notify`.

Each component consumes its own queue. On the incident day, a configuration change on one processing component sets a limit too low:
- a worker lease shorter than processing takes;
- or a worker memory limit below what large documents need;
- or a page cap below normal document sizes.

That component then fails jobs, retries them, and finally rejects them, so customers see their uploads come back rejected.

The support desk asks eight questions in one conversation. The agent investigates with four read-only tools over one evidence collection, all available from the start:

| Tool | What it returns |
| --- | --- |
| `read_journal(component, hour, page)` | one page (up to 58 events) of a component's job-event journal |
| `list_changes(component)` | the component's configuration changes that day |
| `queue_stats(queue, hour)` | ten-minute rows (throughput, rejections, depth, waits) and hour totals |
| `read_playbook(section)` | a playbook section: contents, the symptom catalogue, or one procedure |

## Why this design

The workload tests whether an agent can keep, or deliberately recover, information across a long, multi-turn investigation while its context fills up. It does not test staged evidence or changing requirements; those are different experiments. The properties:

- **Eight related questions and ten scored values,** in one conversation.
- **Three recall questions** (5, 7 and 8) ask for details that were visible only in outputs read for questions 2, 1 and 3, which those questions didn't ask about:
  - the id of the change made shortly before the incident on another component;
  - the internal id of the first rejected job;
  - the queue's longest wait during the incident hour.

  Nothing earlier says these will be needed.
- **Volume:** the failing component's incident-hour journal runs to 15 pages. The first rejection is on page 8 to 11 and the explicit evidence line 2 to 4 pages later; both are drawn per instance. Question 1 alone reads 13 to 15 pages.
- **Distractors:**
  - a legitimate burst of malware-quarantine rejections by `scan` two hours earlier;
  - the unrelated change shortly before the incident;
  - a scheduled backlog on the `index` queue;
  - six decoy playbook symptoms with similar procedures.
- **Unique support:** every scored fact is held by a declared set of tool outputs and by no other. This is checked over all 171 possible calls. A recall fact is held only by outputs its source question's natural investigation reads, and by none that a later question needs.
- **Refetching is allowed and measured:** a repeat of the same tool with the same normalised arguments counts as a refetch.

## Fixed parameters

| Parameter | Value |
| --- | --- |
| questions / scored values / recall values | 8 / 10 / 3 (questions 5, 7, 8 recall from 2, 1, 3) |
| tool outputs | 171 possible calls; about 780,000 characters in total |
| journal pages | up to 58 events, at most about 7,100 characters (kept under 7,800 by design) |
| output cap | the shared `tool-output-cap/1`, 8,000 code points; no fixture output reaches it |
| evidence a natural investigation reads | about 112,000 to 126,000 characters over the eight questions |
| answer format | a fenced `json` block holding exactly the question's fields, the same for every arm |
| development instances | `docthread-dev-1` (seed 7301, lease mechanism) and `docthread-dev-2` (seed 7302, memory mechanism) |
| confirmation instances | none yet: a proposed rule (below) draws them when the protocol is frozen; never used in development |

## Scoring

**Correctness**, per value:
- **Names, ids and codes:** exact, ignoring case and surrounding space.
- **Times:** the journal time with milliseconds; a date prefix and `Z`/`UTC` are allowed.
- **Counts and seconds:** numeric; thousands separators and units are allowed.
- **The quote:** at least 24 characters, a substring of a real line of the failing component's incident-hour journal, and containing the changed setting at its new value. Exactly one line contains it.

**Diagnostics**, reported apart from correctness:
- **A status for wrong values:**
  - `missing`;
  - `malformed`;
  - `distractor`;
  - `other_evidence` (the value appears somewhere in the evidence);
  - `not_in_evidence`;
  - for quotes: `too_short`, `not_a_journal_line` and `wrong_line`.
- **Recall values only:** whether an earlier reply already carried the fact, and whether the question refetched its source.

No status claims a cause for an error.

## Offline verification (2026-10-16, scripted only)

**The tests:** the 20 workload tests run in clm-lib's p015 environment with network access blocked. They cover:
- determinism;
- unique support;
- recall isolation;
- answers kept out of prompts, schemas and errors;
- correct answers and every permitted alternative form;
- targeted faulty answers: distractor entities, ids, times, symptoms and jobs; an unsupported id; a real line without the cause; a fabricated quote; a short quote; malformed and missing answers;
- recall diagnostics;
- tool errors;
- end-to-end sessions.

**The sessions:** a scripted investigator ran on the real p015 path: guarded-clm's capability, Pydantic AI, the bridged task tools, accounting, records and export.
- **Policies:**
  - `tidy` deletes earlier steps' entries as it goes;
  - `keep` edits only when the guard holds an output back.
- **Usage paths:**
  - `synthetic`: provider-like usage at a declared 2.6 characters per token, so the capability calibrates on it;
  - `fixed`: the capability's fixed ratio for scripted models.

The default settings were used (budget 32,000, limit 29,952). Nothing was enlarged or tuned.

| session | endings | points | recall | requests | peak request (chars) | peak estimate (tokens) | PRESSURE requests | held back | refetches | evidence read (chars) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dev-1 tidy synthetic | 8 completed | 10/10 | 3/3 | 38 | 12,447 | 6,220 | 0 | 0 | 3 | 114,364 |
| dev-1 tidy fixed | 8 completed | 10/10 | 3/3 | 38 | 12,447 | 4,544 | 0 | 0 | 3 | 114,364 |
| dev-1 keep synthetic | 8 completed | 10/10 | 3/3 | 36 | 67,079 | 27,236 | 3 | 1 | 1 | 112,638 |
| dev-1 keep fixed | 8 completed | 10/10 | 3/3 | 39 | 92,969 | 25,034 | 13 | 1 | 4 | 120,916 |
| dev-2 tidy synthetic | 8 completed | 10/10 | 3/3 | 39 | 12,341 | 6,172 | 0 | 0 | 3 | 119,817 |
| dev-2 tidy fixed | 8 completed | 10/10 | 3/3 | 39 | 12,341 | 4,508 | 0 | 0 | 3 | 119,817 |
| dev-2 keep synthetic | 8 completed | 10/10 | 3/3 | 37 | 67,138 | 27,253 | 10 | 1 | 1 | 118,177 |
| dev-2 keep fixed | 8 completed | 10/10 | 3/3 | 40 | 99,148 | 26,598 | 14 | 1 | 4 | 126,418 |
| dev-1 provider failure at attempt 20 | completed, provider_failure | 2/10 | 0/3 | 21 | 8,913 | 4,859 | 0 | 0 | 0 | 84,074 |
| dev-1 spend refusal after question 5 | 5 completed, spend_refused | 6/10 | 1/3 | 30 | 10,801 | 5,588 | 0 | 0 | 1 | 105,329 |

**Reading the table:**
- **What the figures are:** properties of scripted policies, not findings. Every session that finished scored 10/10 only because the script answers with the true values.
- **The context-management challenge is real:** an agent that doesn't tidy reaches 25,000 to 27,300 estimated tokens, against the 29,952 limit, and is held back once: in question 1 (journal page 7) with synthetic usage, in question 4 (its first journal page) with the fixed ratio.
- **Recall behaviour:** a tidying agent must refetch all three recall facts.
- **Endings:** the failure and refusal sessions end explicitly, with their unfinished questions scored as missing.
- **The two usage paths differ** (corrected 2026-10-16; the earlier wording said the `fixed` rows show more pressure because they underestimate size, which the records do not support as a general rule). From the recorded sessions, rerun with identical figures:
  - **The estimates:** the `fixed` rows estimate a scripted model at a fixed 4 characters per token, as guarded-clm specifies; the `synthetic` rows calibrate on reported usage at 2.6 characters per token. The same context therefore counts as fewer tokens in the `fixed` rows.
  - **When pressure starts and ends:** with synthetic usage, PRESSURE first appears at request 9, during question 1's journal pages, and the guard holds an output back two requests later, at about 67,000 characters. With the fixed ratio, PRESSURE first appears at request 13, and the hold-back comes only in question 4, at about 93,000 (dev-1) and 99,000 (dev-2) characters.
  - **Why the counts differ:** between those points, questions 2 and 3 add only small outputs while the request stays above 70% of the budget. The scripted `keep` policy reacts to a hold-back, not to PRESSURE notices, so 13 and 14 requests carry PRESSURE in the `fixed` rows, against 3 and 10 with synthetic usage. The dev-2 synthetic run's 10 include 7 later requests, after the context grew again.
  - **What this does not show:** a lower estimate does not by itself produce more PRESSURE requests. The count depends on where the larger outputs fall and on how the policy reacts, so it is a property of these scripted runs.

## Confirmation instances (proposed rule, 2026-10-16; not applied)

Confirmation instances are drawn **at protocol freeze**, by this rule, and never used in development. None has been generated, inspected or run, and no answer is looked at to select one.

1. **How many and which mechanisms:** six instances, two per failure template, in the fixed order `lease`, `memory`, `pages`, `lease`, `memory`, `pages` (the number is proposed and open).
2. **Seeds:** instance *k* (1 to 6) is `docthread-confirm-k`, with seed 7400 + *k*: 7401 to 7406. The development seeds (7301 and 7302) and any seed already used are excluded.
3. **Generation:** `generate(name, seed, mechanism)` with the frozen `docthread-gen/1`, which already re-draws deterministically when a generated number collides.
4. **Mechanical validity checks**, none of which reads or prints an answer:
   - the generator returns without error;
   - `uniqueness_problems(fx)` is empty, so every scored fact has exactly its declared sources among all possible calls;
   - every tool output is at most 7,800 characters, so the shared 8,000-code-point cap never cuts it;
   - the failing component's incident-hour journal has 15 pages, with the first rejection on page 8 to 11 and the evidence line 2 to 4 pages later;
   - the evidence a natural investigation reads (`agent.plan`, measured as output sizes only) lies within the development instances' range, widened by 10%: about 100,000 to 139,000 characters;
   - no component name, change id or job id equals one in a development instance.
5. **Invalid instances:** a seed that fails a check is skipped and recorded, with the failed check. The next seed is 7400 + *k* + 6 *j* for *j* = 1, 2, and so on, keeping the instance's mechanism. Skipped seeds and reasons are published with the freeze.
6. **Recording:** the freeze records each instance's name, seed, mechanism, generator version, check results and a fingerprint of its rendered outputs. It does not record the answers.

## Limits and open points

- **The difficulty compared with other incident tasks is unknown.** The story, layout and retrieval differ, so no comparison to any other task's results is claimed.
- **The scripted investigator knows where the facts are.** A real agent has to search for them.
- **Confirmation instances** have a proposed rule (above) but none exist. The lite-arm mapping and every live setting are still open (see decisions.md).
