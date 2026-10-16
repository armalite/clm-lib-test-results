# 015 – The paper and summary arms: offline verification

_Written 2026-10-16. **Nothing has run against a model. There are no results.** Scripted sessions verify the
plumbing only; they say nothing about how any model or arm performs. No provider call, token-counting call or
ledger change was made._

**What ran:** clm-lib's p015 path. `ArmSession` with the arm's capability, Pydantic AI 2.27.1, the four bridged
docthread task tools, the accounting wrapper, the recorder and export, and for `paper_clm_shell`, the real Docker
sandbox (Docker 20.10.13, `python:3.12-slim`). The agent is the scripted `PlainInvestigator`, which knows where the facts
are and answers with the true values. The summary arm's summariser is the same scripted model, writing an
extractive summary: the calls made and the answers given, never other tool-output facts.

**Reproduce:** `.venv-p015/bin/python -m clm_lib.p015.docthread.arms_offline OUT_DIR --matrix`, in clm-lib's p015
environment. It writes the session directories and `matrix.json`. All 21 sessions were exported with
`clm_lib.p015.export`, and `verify_export` found no problem in any of them. Two complete runs of the matrix gave
identical figures, apart from latency.

## Policies and paths

- **`paper_clm_shell` policies:**
  - `tidy`: before each read, an edit-only `bash` step that deletes every earlier call and its result (questions and answers stay);
  - `keep`: edits only after a persistent nudge, a rollback or an over-limit notice;
  - `never` (stress): never edits;
  - `bad-edits` (stress): `tidy`, but the first four edits are invalid: a non-mirror file, the running command's block removed, broken call arguments, and a reply removed so that a result answers nothing.
- **The summary arm:** no context tool. Stress faults make the summariser write far over any acceptance limit, or write nothing.
- **Usage paths:**
  - `synthetic`: provider-like usage at a declared 2.6 characters of content per token, so the estimator calibrates on it;
  - `fixed`: the fixed 4 characters per token used for scripted models.
- **Failures:**
  - a scripted HTTP 503 at attempt 20 (paper) or at attempt 9, which is the summary arm's first summariser call;
  - a ledger that allows no more spend after question 5.

## Sessions

Abbreviations:
- **req:** main-model requests;
- **peak est.:** the arm's largest estimate as sent;
- **before mgmt:** the largest estimate before the arm's own management acted;
- **nudges:** size nudges / persistent nudges;
- **edits:** applied / rejected / free steps;
- **rollb.:** rollbacks / final over-limit notices;
- **press.:** sent requests that were at 70% or more of the budget before a summary;
- **summ.:** summaries applied / too large / empty;
- **s.calls:** summariser calls;
- **ref.:** refetches;
- **evidence:** characters of delivered task-tool output.

Charges are at an **offline placeholder price**, in a temporary test ledger. They are not spend, and they show only that the accounting runs.

| session | label | endings | points | recall | req | peak chars | peak est. | before mgmt | nudges | edits | rollb. | press. | summ. | s.calls | ref. | evidence | main $ | summary $ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| paper-dev1-tidy-synthetic | ordinary | 8 completed | 10/10 | 3/3 | 75 | 10,244 | 3,818 | 3,818 | 0/0 | 37/0/37 | 0/0 | 0 | – | 0 | 3 | 114,364 | 0.3798 | 0 |
| paper-dev1-tidy-fixed | ordinary | 8 completed | 10/10 | 3/3 | 75 | 10,244 | 5,809 | 5,809 | 0/0 | 37/0/37 | 0/0 | 0 | – | 0 | 3 | 114,364 | 0.2150 | 0 |
| paper-dev1-keep-synthetic | ordinary | 8 completed | 10/10 | 3/3 | 36 | 69,970 | 27,920 | 27,920 | 5/1 | 1/0/1 | 0/0 | 0 | – | 0 | 0 | 106,581 | 0.8649 | 0 |
| paper-dev1-keep-fixed | ordinary | 8 completed | 10/10 | 3/3 | 37 | 84,123 | 26,916 | 26,916 | 5/1 | 1/0/1 | 0/0 | 0 | – | 0 | 1 | 113,271 | 0.4812 | 0 |
| paper-dev2-tidy-synthetic | ordinary | 8 completed | 10/10 | 3/3 | 77 | 10,133 | 3,809 | 3,809 | 0/0 | 38/0/38 | 0/0 | 0 | – | 0 | 3 | 119,817 | 0.3893 | 0 |
| paper-dev2-tidy-fixed | ordinary | 8 completed | 10/10 | 3/3 | 77 | 10,133 | 5,773 | 5,773 | 0/0 | 38/0/38 | 0/0 | 0 | – | 0 | 3 | 119,817 | 0.2203 | 0 |
| paper-dev2-keep-synthetic | ordinary | 8 completed | 10/10 | 3/3 | 37 | 69,973 | 27,920 | 27,920 | 5/1 | 1/0/1 | 0/0 | 0 | – | 0 | 0 | 112,144 | 0.9732 | 0 |
| paper-dev2-keep-fixed | ordinary | 8 completed | 10/10 | 3/3 | 38 | 88,901 | 27,604 | 27,604 | 5/1 | 1/0/1 | 0/0 | 0 | – | 0 | 1 | 118,729 | 0.4240 | 0 |
| summary-dev1-synthetic | ordinary | 8 completed | 10/10 | 3/3 | 38 | 55,932 | 21,632 | 24,077 | – | – | – | 2 | 2/0/0 | 2 | 3 | 114,364 | 0.9456 | 0.0805 |
| summary-dev1-fixed | ordinary | 8 completed | 10/10 | 3/3 | 35 | 69,825 | 21,648 | 23,606 | – | – | – | 1 | 1/0/0 | 1 | 0 | 106,581 | 0.4698 | 0.0251 |
| summary-dev2-synthetic | ordinary | 8 completed | 10/10 | 3/3 | 37 | 55,206 | 21,728 | 23,935 | – | – | – | 2 | 2/0/0 | 2 | 1 | 118,729 | 1.0253 | 0.0770 |
| summary-dev2-fixed | ordinary | 8 completed | 10/10 | 3/3 | 38 | 69,828 | 22,383 | 23,464 | – | – | – | 2 | 2/0/0 | 2 | 2 | 119,488 | 0.5822 | 0.0414 |
| paper-dev1-never-synthetic-stress | stress | step_limit | 0/10 | 0/3 | 60 | 70,262 | 28,064 | 30,390 | 3/49 | 0/0/0 | 48/0 | 0 | – | 0 | 48 | 392,874 | 3.0735 | 0 |
| paper-dev1-never-3-rollbacks-stress | stress | context_limit | 0/10 | 0/3 | 16 | 76,799 | 30,524 | 32,928 | 3/5 | 0/0/0 | 3/1 | 0 | – | 0 | 3 | 102,159 | 0.5937 | 0 |
| paper-dev1-bad-edits-stress | stress | 8 completed | 10/10 | 3/3 | 75 | 34,018 | 13,978 | 13,978 | 1/0 | 33/4/37 | 0/0 | 0 | – | 0 | 3 | 114,364 | 0.4836 | 0 |
| paper-dev1-provider-failure | failure | provider_failure | 0/10 | 0/3 | 21 | 7,623 | 3,818 | 3,818 | 0/0 | 10/0/10 | 0/0 | 0 | – | 0 | 0 | 62,976 | 0.1430 | 0 |
| paper-dev1-spend-refusal | failure | 5 completed, spend_refused | 6/10 | 1/3 | 59 | 8,970 | 3,818 | 3,818 | 0/0 | 29/0/29 | 0/0 | 0 | – | 0 | 1 | 105,329 | 0.2908 | 0 |
| summary-dev1-faulty-summaries-stress | stress | 8 completed | 10/10 | 3/3 | 38 | 55,932 | 21,632 | 24,077 | – | – | – | 2 | 2/1/0 | 3 | 3 | 114,364 | 0.9456 | 0.1184 |
| summary-dev1-overflow-stress | stress | context_limit | 0/10 | 0/3 | 9 | 51,667 | 20,480 | 22,834 | – | – | – | 0 | 0/1/1 | 2 | 0 | 56,941 | 0.2018 | 0.0758 |
| summary-dev1-summariser-failure | failure | provider_failure | 0/10 | 0/3 | 9 | 51,667 | 20,480 | 22,834 | – | – | – | 0 | 0/0/0 | 1 | 0 | 56,941 | 0.2018 | 0.1299 |
| summary-dev1-spend-refusal | failure | 5 completed, spend_refused | 6/10 | 1/3 | 30 | 55,932 | 21,632 | 24,077 | – | – | – | 2 | 2/0/0 | 2 | 1 | 105,329 | 0.8020 | 0.0805 |

**Notes on the table:**
- **Endings:** every session that ended early has unfinished questions scored as missing.
- **The overflow sessions:** the last request before the summary was never sent, so `press.` is 0. The trace holds the pressure record.
- **The summariser failure:** the HTTP 503 has an unknown billing outcome, so it is charged at its full reservation (0.1299), as the accounting rules require.
- **The guarded-clm arm** on the same instances and plan: [docthread-workload.md](docthread-workload.md). With `tidy`, its peak requests are 12,341 to 12,447 characters; with `keep`, 67,079 to 99,148 characters.

## What the sessions and tests verify

The tests are in clm-lib (`tests/p015/test_paper_shell.py`, 23; `test_summary_arm.py`, 8; `test_arm_fairness.py`, 3). The whole p015 suite runs with network access blocked.

- **8 turns and 10 values, with continuity:** every ordinary session completes all eight questions in one conversation and scores 10/10 and 3/3. The pinned request (system prompt and question 1) leads every request, and each later question reaches the model in order.
- **Edits shape later requests:** after an accepted edit, the deleted calls and results are absent from every later request. The receipt states the block counts and the new size.
- **Rejected edits keep the prior state:** in the `bad-edits` session, each of the four rejected edits gives a next request equal to the previous one plus the rejected command and its result. The test checks every rejection reason.
- **Deleted history does not reappear:**
  - a rolled-back step's call is in no later request;
  - after a summary, the summarised calls are in no later request, and the summary is in the pinned request.
- **Reminders and limits:**
  - nudges at 25, 50 and 75%, with re-arming, and the adaptive persistent nudge, tested against the documented rule;
  - the finalize notice;
  - the step limit, which also ends the `never` stress session at 60 steps;
  - the call cap, which counts free steps as calls;
  - only the first `bash` call of a response runs.
- **Recovery and rollback:** in the 3-rollback stress session, three rollbacks each bring the estimate under the limit minus 2,048. Then one final over-limit request is sent, and the turn ends as `context_limit`.
- **Summary paths:**
  - a too-long summary is rejected, and the retry, at half the length, is applied;
  - a too-long summary followed by an empty one ends as `context_limit`;
  - a per-turn summariser cap of 1 ends as `summary_call_cap`;
  - when the current question was in the summarised part, it is restated after the summary. This happened in three sessions.
- **Summariser boundary and accounting:**
  - summariser requests carry only the summariser text and the `token-tail/1` layout, with no tools;
  - every fact given to the summariser had already been in an agent request;
  - summariser attempts are recorded as category `summary`, with ledger kind `p015:summary`, in one attempt numbering with the agent's;
  - per-turn counters show summariser calls apart from steps;
  - a refused summariser call ends as `spend_refused`.
- **Isolation:** the sandbox runs as a non-root user, with a read-only root, no network and no Docker socket. The host home is not visible, the environment holds only the image's own variables, the mirror is writable and `/work` persists. Without Docker, the command is refused, the turn ends as `sandbox_unavailable`, and nothing runs.
- **Fairness:** across the three arms, the system prompt, the first question, the task tools' names, descriptions and schemas, the invalid-argument retry, the tool results and the output contract are identical. Only each arm's own tool and instructions differ.
- **Records and exports:** the manifests of the paper and summary sessions carry `arm`, with attempts and charges by category and by cost basis. Those of guarded-clm sessions are unchanged.

## Sizes and pressure by arm

- **With `tidy`,** the paper arm's peak request is about 10,100 to 10,200 characters. guarded-clm's is 12,341 to 12,447. The paper arm needs two responses per read (an edit, then the read), so it makes 75 to 77 requests, against guarded-clm's 38 to 39. The edit steps are free.
- **With `keep`,** the paper arm grows to 70,000 to 89,000 characters, about 27,000 to 28,000 estimated tokens. One persistent nudge leads to one edit, and no rollback is needed.
- **The summary arm** summarises once or twice per session. It peaks at 55,000 to 70,000 characters, at about 21,600 to 22,400 tokens as sent; before the summaries, the peak was 23,500 to 24,100.
- **The estimators:** under synthetic usage, the paper and summary arms' estimator calibrates to about 6.4 characters per token in `tidy` sessions, and to about 4 in `keep` and summary sessions. The synthetic usage counts only message content, so many small framed messages give a higher ratio. These ratios are properties of the synthetic usage, not of any tokenizer.

## Limits

- **The scripted agent knows where the facts are.** A real agent has to search for them.
- **The scripted summariser is extractive.** A model's summary may carry more or fewer facts.
- **Every live setting is open:** see [arm-settings.md](arm-settings.md) and [decisions.md](decisions.md).

## Rerun after the source-priority review (2026-10-16, later)

**What changed:** the paper arm's default is now the `paper` profile: one editing reminder 2,048 tokens before the limit, and last-step rollback up to six times ([paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md)). The README rules are the `readme` profile. The matrix now has 23 sessions, two of them new.

**Results:** all 23 were exported and verified without a problem. Sessions not listed below gave the same endings, points, requests and peak sizes as before.

**Abbreviations:**
- **notices:** editing reminders / size nudges / persistent nudges;
- **rollb.:** rollback events / steps rolled back / final over-limit notices.

| session | label | endings | points | req | peak chars | peak est. | notices | edits (applied/rejected/free) | rollb. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| paper-dev1-keep-synthetic | ordinary | 8 completed | 10/10 | 37 | 70,016 | 27,963 | 0/0/0 | 1/0/1 | 1/1/0 |
| paper-dev1-keep-fixed | ordinary | 8 completed | 10/10 | 37 | 85,145 | 28,032 | 1/0/0 | 1/0/1 | 0/0/0 |
| paper-dev2-keep-synthetic | ordinary | 8 completed | 10/10 | 38 | 70,019 | 27,960 | 0/0/0 | 1/0/1 | 1/1/0 |
| paper-dev2-keep-fixed | ordinary | 8 completed | 10/10 | 38 | 89,376 | 27,964 | 1/0/0 | 1/0/1 | 0/0/0 |
| paper-dev1-never-synthetic-stress | stress | context_limit | 0/10 | 19 | 76,802 | 30,518 | 1/0/0 | 0/0/0 | 6/6/1 |
| paper-dev1-never-3-rollbacks-stress | stress | context_limit | 0/10 | 16 | 76,802 | 30,518 | 1/0/0 | 0/0/0 | 3/3/1 |
| paper-dev1-never-readme-stress (new) | stress | step_limit | 0/10 | 60 | 70,240 | 28,055 | 0/3/49 | 0/0/0 | 48/48/0 |
| paper-dev1-keep-synthetic-readme (new) | alternative | 8 completed | 10/10 | 36 | 69,970 | 27,916 | 0/5/1 | 1/0/1 | 0/0/0 |

**Notes:**
- **A reminder can be skipped.** With synthetic usage, one journal page adds about 2,500 estimated tokens, more than the reminder's 2,048-token margin. The `keep` sessions therefore went from below the reminder point to over the limit in one step: they got no reminder, one step was rolled back, and the rollback notice led to the edit. With the fixed ratio, a page adds less, and the reminder came first. This follows from the paper's margin and the size of the outputs, and it bears on the open reminder questions.
- **The never-editing agent** now ends as `context_limit`, after six one-step rollbacks and one final over-limit request. Under the README profile it reaches the 60-step limit after 48 rollbacks, as before.
- **The launcher:** its offline proof is in clm-lib, `tests/p015/test_launcher.py`. It covers a three-arm matrix with the real sandbox, restarts, interruption with an attempt in flight, stops, spend refusals (the summariser included), competing launchers, fingerprint changes, and complete and partial exports. See [launcher.md](launcher.md).
