# 009 – Update-triggered Jev context review (strategy 1)

**Status: implemented. Smoke check, diagnostics and four-run development pilot complete; the larger evaluation is not authorised and was not run.** This is strategy 1 of the [Jev-assistance roadmap](../jev-assistance-roadmap.md); strategies 2 and 3 are planned only.

**Headline:**
- **The integration works end to end.** At every round with board or change-log lines, Jev scored the agent's whole current context before the next Claude call, at about 0.25 s per update and well under USD 0.001 per run.
- **The diagnostic:** on 24 fresh labelled cases Jev flagged 12 of 13 affected entries and 1 of 9 unaffected ones.
- **The pilot:** all four runs succeeded on all 14 checks.
  - **Cost and time:** the assisted arm was cheaper (USD 0.313 vs 0.377 mean) and faster (123 s vs 152 s).
  - **But:** that comes from two pairs, mostly one of them, and the runs differed in how the model paced its work. It is **not evidence that the advice caused it**.
- **Following the advice:** where the context had several notes (one run), Claude annotated some flagged notes in place and left others unchanged. The final answer was correct either way.

## The question and design

**The question:** when meaningful new evidence arrives, does Jev's affected-entry advice help Claude review its existing working context?

**The comparison:**

| | A: control (CLM only) | B: assisted |
| --- | --- | --- |
| **Update** | At every round release, the same verbatim update block | The same |
| **Instruction** | "consider whether this update affects your working context" | The same |
| **Advice** | none | Jev's probability, for every entry of the current context, that the update requires reconsidering a current assertion or planned action in it, plus a short explanation that it can be wrong, never edits, and that a low score is not a reason to delete |
| **Edits** | Claude decides | Claude decides |

- **Model and runtime:** both arms use `claude-opus-5-5` (effort low) in mode `clm_helpers`, with the same corrected runtime as 008. Config: `configs/exp009.toml`.
- **The update payload (`round-files/1`):**
  - **Content:** that round's `board.md` and `changes.md` lines, verbatim with `file:line` references.
  - **Processing:** blank and heading lines are dropped.
  - **Not included:** logs (23–41k characters per round), which the agent reads from the files as before.
- **Why a payload:** the historical release notice ("Round k of n released…") carries no evidence, so this new presentation is used in **both** arms, for this experiment only.
- **What Jev sees:** only the payload and the exact text of the entries in the context revision current at that release. It never sees deleted entries, future rounds, logs or evaluator truth.
- **Timing:** advice is computed on the host before the next main-model call, so it adds **no Claude turn**.
- **Full details:** [`protocol.md`](protocol.md), written before any paid call.

## 1. Live integration smoke check

**Run:** `20261012T115543-…-updjev-rounds-diag-2-f112`, role `smoke`, excluded from comparisons.

- **The in-loop path 008 never exercised now works live.** 9 updates, 8 with a payload, gave 8 advised updates and 32 entries scored, with no errors.
- **Model:** `jev-1.13.0` returned each time.
- **Ledger:** each call is a settled `jev` entry. Jev took 2.0 s in total and cost USD 0.000626.
- **The run itself:** it succeeded strictly (USD 0.421 in total).

## 2. Diagnostics

**Fresh cases** (`diagnostic-cases-v1.json`, `jev-diag/2`, SHA-256 `6874c069…ae5d`):
- **Content:** 24 cases on 8 real `round-files/1` payloads from instances reserved for diagnostics (`rounds-diag-1..2`).
- **Entries:** in the forms seen in agent contexts (rolling notes, per-round notes, step actions with stated plans, runtime receipts).
- **Labels:** written before any answer.
- **Why fresh:** the request construction changed from 008. Updates now cover several threads, and candidates include runtime entries.

| At the fixed 0.5 reporting threshold | Result |
| --- | --- |
| Affected flagged (recall) | **12 / 13** |
| Unaffected flagged | **1 / 9**, so precision 12/13 |
| Missed | `u-10` (0.32): a round with five board lines marked thread A "resolved"; the entry said "mitigated at round 5" |
| False positive | `u-20` (0.78): a thread-A note citing `CHG-136 APPLIED`, in a round that **reuses the id** `CHG-136` for an unrelated *proposed* change |
| Borderline | `u-09`, historical statement, at 0.49 |
| Ambiguous (reported separately) | `u-21` 0.90 (the reused change id), `u-24` 0.53 |
| Requests / errors / latency / cost | 8 / 0 / 0.24 s mean / USD 0.000333 |

**What Jev handled well:**
- explicit cause replacements (0.84–0.96);
- a plan stated in a step's `thought` (0.95);
- false-alarm closures (0.89–0.95);
- an early change record contradicted by new failures (0.89).

**Its two errors** both come from multi-line payloads: a status change buried among other lines, and an id coincidence.

**Reference rerun:** 008's frozen cases, rerun unchanged as a stability check. These cases were already observed, so this is not new evidence.
- **Classifications:** identical to 2026-10-12 (10/10, the same single false positive).
- **Probabilities:** 13 of 24 moved, by at most 0.05. Jev's probabilities are close but **not identical across days**.

## 3. Development pilot (comparison `20261012T115926`)

**Setup:** order dev-1 A, B; dev-2 B, A. Every run completed with **14/14 checks**: no stale causes or statuses, no missing incidents, no invalid citations, and no repairs, retries, recoveries or invalid runs.

| | A dev-1 | B dev-1 | B dev-2 | A dev-2 |
| --- | --- | --- | --- | --- |
| Run id | `…115926…upd-rounds-dev-1-68c7` | `…120202…updjev-rounds-dev-1-284f` | `…120354…updjev-rounds-dev-2-f1f3` | `…120608…upd-rounds-dev-2-fe3f` |
| Strict success | S | S | S | S |
| Cost USD: Anthropic / TypeSafe | 0.3645 / — | 0.2621 / 0.0006 | 0.3617 / 0.0009 | 0.3898 / — |
| Elapsed / Anthropic time (s) | 155.3 / 122.7 | 111.9 / 88.7 | 134.2 / 106.7 | 148.7 / 121.2 |
| Jev time (s) | — | 2.2 | 2.0 | — |
| Model calls / accepted edits | 32 / 18 | 22 / 11 | 28 / 15 | 30 / 16 |
| Tokens: uncached / cache read / cache write / output | 3,686 / 95,864 / 35,574 / 7,634 | 2,506 / 71,129 / 26,210 / 5,342 | 3,314 / 93,243 / 39,238 / 6,679 | 3,501 / 96,068 / 41,566 / 7,436 |
| Updates (with payload) | 9 (8) | 9 (8) | 10 (8) | 10 (8) |
| Entries scored by Jev | — | 32 | 66 | — |
| Context style | one rolling note | one rolling note | append-only per-round notes | one rolling note |

**Means:**

| | A | B |
| --- | --- | --- |
| Cost (USD) | 0.377 | 0.313 (−17%) |
| Elapsed (s) | 152 | 123 (−19%) |
| Calls | 31 | 25 |

**Per pair:** cost −28% on dev-1 and −7% on dev-2.

**Reading this carefully:**
- **The main driver is dev-1.** B finished in 22 calls, against A's 32, because it mostly read each round's logs and edited its note in one step, where A took two. Both arms saw the same update text. With two pairs, and with 008's pilot showing similar run-to-run spread on these instances (USD 0.32–0.39), **this does not show that the advice saves cost or time**.
- **Advice overhead:**
  - **Text:** 2.8–3.2k characters per run, about 350 characters (≈120 tokens) per update. The payload itself adds about 4.4k characters per run in both arms.
  - **Request growth:** requests right after a release were about 430 input tokens larger in B on average (4,957 vs 4,525), with about 150 more cache-write tokens. Much of that difference comes from B dev-2's larger append-only context rather than from the advice text.
  - **Cache:** no cache disruption is visible. The advice is appended at the end of a new entry, after the cached prefix.
- **Jev:** 2.0–2.2 s of latency (under 2% of elapsed time) and USD 0.0006–0.0009 per run.
- **No saving is claimed** for context the model had already read.

**Activation check:**
- **Updates while work remained:** substantive updates arrived in every run: 8 per run, in rounds 2–10 or 2–11, each before the final answer.
- **Non-empty context:** in B, every update with a payload was scored against a non-empty current context (4–12 entries).
- **Not forced:** no edit was forced.

## 4. Advice and what followed

**Not attribution:** "followed by an edit" means only that an accepted edit came before the next update.

**Rolling-note runs (A dev-1, B dev-1, A dev-2):** Claude rewrote its single note `n1` and deleted the previous step's raw entries at almost every round, so nearly every candidate "changed" whatever the advice said. In those runs the per-entry advice had little to discriminate between: one note plus three runtime entries.

**B dev-2 (append-only notes):** the informative case.
- **Counts:** 19 entries were flagged at 0.5 or above. Claude later changed 10 of them and left 9 unchanged, and it changed 19 unflagged entries, mostly raw step entries it routinely deletes.
- **Round 7 example (cause revised):**
  - **Update:** `round-07/board.md:3: - Thread B root cause revised: an expired TLS certificate on a dependency (CERT_EXPIRED); this supersedes the earlier suspicion of DB_POOL_EXHAUSTED.`
  - **Jev:** `n5` 0.95, `n3` 0.75, `n4` 0.68; other notes at most 0.21.
  - **Claude's next edit** annotated two of the flagged notes in place and kept their history:
    - `n3`: "…Thread B says auth-svc DB_POOL_EXHAUSTED ongoing, **(R7 board revised to CERT_EXPIRED, round-07/board.md:3)** …";
    - `n5`: "…Thread B adds shipping-svc **(cause now CERT_EXPIRED per round-07/board.md:3)** …".
  - **Also:** it wrote a new note `n7`. It left `n4`, a list of log observations, unchanged.
- **Round 8 example (statuses changed; advice not followed in place):**
  - **Update:** thread A resolved, thread B mitigated, thread C opened, DATA_BACKFILL opened, VENDOR_TICKET closed.
  - **Jev:** `n2` 0.92, `n5` 0.90, `n3` 0.81, `n4` 0.79, `n7` 0.67.
  - **Claude edited none of them.** It recorded the new statuses in a new note `n8` ("Thread A (DNS) RESOLVED … Thread B (CERT) MITIGATED … VENDOR_TICKET CLOSED"), consistent with its newest-note-wins log.
  - **Outcome:** the final answer was correct, so leaving the older notes stale did no harm here.
- **Round 10 example:** thread D closed as a false alarm. Jev flagged `n7` (0.79, the thread-D note) and `n6` (0.80, an unrelated follow-up note, apparently a false alarm). Claude annotated `n7` "(CLOSED false alarm R10 board.md:3)" and left `n6`.

**The control arm:** every run used the rolling-note style, so it gives no matching append-only example.

## What the results support

- **Supported:**
  - Update-triggered review is implementable as a mechanical, matched intervention, with no extra Claude turn and negligible Jev cost and latency.
  - On fresh cases built from real payloads, Jev's answers to the fixed question were mostly right. Its errors came from multi-line payloads and an id coincidence.
- **Observed (one run):** Claude sometimes used the advice to annotate superseded statements in place, and sometimes ignored it when its own note structure already handled supersession.
- **Not supported:**
  - any accuracy effect: all runs were at the ceiling;
  - any cost or time effect: two pairs, with differences tied to pacing;
  - any causal reading of edits after advice;
  - any claim of novelty.

## Is strategy 1 ready for the larger evaluation?

**Technically yes; scientifically marginal on this task.**
- **Ready:** the plumbing, accounting and evidence work. The planned sample (4 fresh instances `rounds-eval-5..8`, registered uninspected, × 3 repetitions × 2 arms = 24 runs) could measure cost, time and call differences with paired blocks.
- **Estimated cost:** USD (0.377 + 0.313) × 12 × 1.25 ≈ **USD 10.4**, plus a small diagnostic reserve.
- **Limits it would face:**
  - **Accuracy headroom:** on dev instances this task is at the ceiling for both arms (007's evaluation showed some citation omissions on other instances).
  - **Little to discriminate:** the model's usual rolling-note style leaves the per-entry advice little to work with.
- **Decision:** whether the efficiency question is worth about USD 10 is the maintainer's call. Nothing is authorised.

## Spend

- **This experiment:** **USD 1.801066** of the USD 10 newly authorised:

  | Item | Anthropic | TypeSafe |
  | --- | --- | --- |
  | Smoke run | USD 0.420221 | USD 0.000626 |
  | Pilot | USD 1.378036 | USD 0.001548 |
  | Diagnostics (009 fresh and 008 reference) | — | USD 0.000635 |

- **Ledger:** USD 50.210028 spent of the USD 58.408962 ceiling. Nothing is pending and nothing has an unknown outcome.
- **Note:** the generated `report.md` counts run-attributed entries only. The diagnostic entries are kind `jev-diagnostic` in the ledger snapshot.

## Where is the evidence?

- `protocol.md`: the design, written before any paid call, and the session record.
- `diagnostic-cases-v1.json`: the frozen cases.
- `artifacts/diagnostics/20261012T115847-frozen` (fresh) and `…115851-frozen` (008 reference rerun).
- `report.md`, `metrics.json` and `metrics.csv`: all five runs. The `ur_*` columns cover updates, entries scored, appended and advice characters, Jev attempts, tokens, cost and latency, and flagged, changed and not-changed counts.
- `artifacts/runs/smoke/` and `artifacts/runs/calibration/` (pilot), per run:
  - `summary.json → update_review.records`: exact payloads and hashes, revisions, candidate ids, answers, and the edits that followed;
  - `jev/NNNN.json`: every Jev request and response;
  - `events.jsonl` (`update_review` events), plus context revisions and requests.
- `artifacts/comparisons/20261012T115926/`: the frozen settings, the schedule and the source patch (the implementation was uncommitted at run time).
