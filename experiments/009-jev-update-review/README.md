# 009 – Update-triggered Jev context review (strategy 1)

**Status: complete for strategy 1.** Smoke check, diagnostics, a four-run development pilot and the planned **24-run evaluation** (2026-10-13) are done. This is strategy 1 of the [Jev-assistance roadmap](../jev-assistance-roadmap.md); strategies 2 and 3 are planned only.

**Headline (evaluation: 4 fresh task instances × 3 repetitions × 2 conditions):**
- **The pilot's saving did not hold.** With Jev advice, runs cost **more** on average:

  | | Control (A) | Jev advice (B) |
  | --- | --- | --- |
  | Mean cost per run (USD) | 0.375 | 0.415 (+11%) |
  | Mean elapsed (s) | 149 | 158 (+6%) |

  B was cheaper in only 4 of 12 matched blocks.
- **Where the extra cost came from:**
  - about one more model call per run;
  - about 5% larger requests, consistent with the advice text sitting in context;
  - about twice as many context-pressure steps.
- **Jev itself is cheap:** USD 0.0008 and 2.5 s per run.
- **Correctness:** strict success was 8/12 (A) vs **10/12** (B), and individual checks 161/168 vs 166/168.
  - **Failures:** every one was an omission (a missing evidence reference or, once, a whole incident left out) or an invalid citation. There were no stale causes or statuses in either arm.
  - **Not established:** on matched blocks, only B succeeded in 3 and only A in 1, which is far from conclusive (sign test p ≈ 0.6). It does not establish a correctness benefit.
- **Advice and edits:**
  - **Following:** Claude often edited notes Jev flagged, but it also ignored flags, and it updated notes Jev missed.
  - **Spurious flags:** about a third of Jev's flags (36 of 114) were on runtime step entries, mostly code, which carry little meaning for the incident.

**Earlier phases** (kept separate below): the diagnostic flagged 12/13 affected and 1/9 unaffected cases. The four-run pilot showed B cheaper and faster on means, from two pairs, which the evaluation did not reproduce.

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

## 4. Pilot: advice and what followed

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

## 5. Evaluation (comparison `20261012T124415`, 2026-10-13)

### What was compared

**The scenario:** the task is a **fictional** multi-service production incident from the synthetic generator `incident-rounds-gen/1`.
- **The services are invented:** for example notify-worker, inventory-svc and checkout-api.
- **Each run** releases 10–12 hourly rounds of logs, incident-board updates and change records.
- **The final answer** names the real incidents, their causes, services, statuses and file:line evidence, plus the open follow-ups.

**The conditions:**
- **Both conditions** get the same verbatim board and change-log lines at every round release, and the same instruction to consider whether they affect the existing working context.
- **The assisted condition** also gets Jev's per-entry advisory probabilities, computed before the next Claude call.
- **In both,** Claude alone decides what to edit, and nothing is deleted or rewritten automatically.

**Frozen settings:** everything was frozen before the first evaluation call (protocol, "Evaluation freeze"): instances, seeds, versions, prompts, Jev settings, the balanced order and a code patch. The code that ran matched the frozen patch byte for byte.

**The sample:** `rounds-eval-5..8` are four fresh instances, never used before.
- **Twelve matched blocks:** each instance ran **three times per condition**, in alternating order. B went first in 6 of the 12 blocks.
- **Four instances, not twelve:** these are **four task instances with repeated runs, not twelve independent task designs**, and the repetitions mainly measure run-to-run variability.

**Execution:** all 24 runs completed, with no halts, invalid runs, repairs, API retries, recoveries, rejected edits or Jev errors. All 117 Jev calls succeeded and returned `jev-1.13.0`. Nothing was replaced, repeated or excluded.

### Results by condition (all 12 runs each; mean, with median in brackets)

| | A: control | B: Jev advice |
| --- | --- | --- |
| Strict success | **8 / 12** | **10 / 12** |
| Checks passed | 161 / 168 | 166 / 168 |
| … causes / services / status | 47/48 · 35/36 · 35/36 | 48/48 · 36/36 · 36/36 |
| … evidence / unresolved follow-ups | 32/36 · 12/12 | 34/36 · 12/12 |
| Stale causes or statuses | 0 | 0 |
| Runs with an invalid citation | 1 | 2 |
| **Total cost per run (USD, incl. Jev)** | **0.375** (0.366) | **0.415** (0.400) |
| of which TypeSafe (Jev) | — | 0.0008 (0.0008) |
| **Elapsed per run (s)** | **149.2** (146.2) | **158.0** (157.8) |
| Anthropic provider time (s) | 118.8 (116.8) | 123.2 (121.4) |
| Jev time (s) | — | 2.46 (2.49) |
| Main-model calls | 30.8 (31) | 31.8 (31.5) |
| Code executions / accepted context edits | 19.5 / 17.7 | 20.6 / 18.8 |
| Context-pressure steps / spills | 1.6 / 0.25 | 3.1 / 0.33 |
| Tokens: uncached / cache read / cache write / output | 3,569 / 94,652 / 40,368 / 7,003 | 3,754 / 101,632 / 45,184 / 7,630 |
| Jev: entries scored / input tokens / advice characters | — | 46 / 19,444 / 3,524 |
| Repairs, API retries, recoveries, rejected edits | 0 | 0 |

**Failed runs**, all kept:

| Run | Arm | Checks | What failed |
| --- | --- | --- | --- |
| eval-6 rep 1 | A | 13/14 | Thread C status evidence missing |
| eval-7 rep 2 | A | 13/14 | Thread A cause evidence missing |
| eval-8 rep 2 | A | 10/14 | One whole incident (thread A, MEMORY_LEAK) left out of the answer |
| eval-6 rep 3 | A | 13/14 | Thread C status evidence missing, plus an invalid citation |
| eval-5 rep 2 | B | 13/14 | Thread C status evidence missing, plus an invalid citation |
| eval-6 rep 3 | B | 13/14 | Thread C status evidence missing, plus an invalid citation |

Thread C's status evidence on eval-6 failed in 3 of its 6 runs, in both arms, so that looks like a property of the instance.

### Matched blocks (B − A)

| Block (A/B first) | Strict A / B | Cost A → B (USD) | Elapsed A → B (s) | Calls A / B | Edits A / B |
| --- | --- | --- | --- | --- | --- |
| eval-5 rep 1 (A) | S / S | 0.442 → 0.410 (−7%) | 175 → 162 | 35 / 32 | 21 / 17 |
| eval-5 rep 2 (B) | S / F | 0.455 → 0.516 (+13%) | 169 → 176 | 35 / 36 | 21 / 23 |
| eval-5 rep 3 (A) | S / S | 0.384 → 0.457 (+19%) | 146 → 160 | 31 / 33 | 17 / 20 |
| eval-6 rep 1 (B) | F / S | 0.359 → 0.373 (+4%) | 137 → 157 | 29 / 30 | 17 / 18 |
| eval-6 rep 2 (A) | S / S | 0.348 → 0.417 (+20%) | 144 → 143 | 28 / 30 | 15 / 19 |
| eval-6 rep 3 (B) | F / F | 0.350 → 0.386 (+10%) | 143 → 146 | 29 / 31 | 17 / 17 |
| eval-7 rep 1 (A) | S / S | 0.437 → 0.333 (−24%) | 163 → 144 | 33 / 29 | 20 / 16 |
| eval-7 rep 2 (B) | F / S | 0.370 → 0.361 (−2%) | 157 → 144 | 31 / 29 | 19 / 17 |
| eval-7 rep 3 (A) | S / S | 0.306 → 0.438 (+43%) | 129 → 159 | 27 / 33 | 14 / 20 |
| eval-8 rep 1 (B) | S / S | 0.245 → 0.506 (+107%) | 106 → 194 | 25 / 36 | 11 / 23 |
| eval-8 rep 2 (A) | F / S | 0.361 → 0.390 (+8%) | 146 → 165 | 31 / 33 | 18 / 19 |
| eval-8 rep 3 (B) | S / S | 0.444 → 0.389 (−12%) | 174 → 146 | 35 / 30 | 22 / 17 |

**Summary of the blocks:**
- **Cost:** B was cheaper in **4 of 12** blocks. The median paired difference is +9% and the mean +15%; the ratio of means is +11%.
- **Time:** B was faster in 5 of 12, and used fewer calls in 4 of 12.
- **Strict success:** both succeeded in 7 blocks, only B in 3, only A in 1, and neither in 1.
- **The largest gap** (eval-8 rep 1) pairs an unusually short control run (25 calls) with a long assisted one. Leaving that control run out, A's mean is USD 0.387, still below B's 0.415.
- **Order:** no order effect is visible (A USD 0.380 first vs 0.371 second; B 0.422 vs 0.408).

### By instance (mean of 3 repetitions)

| Instance | Strict A / B | Cost A / B (USD) | Elapsed A / B (s) | Calls A / B |
| --- | --- | --- | --- | --- |
| eval-5 | 3/3 · 2/3 | 0.427 / 0.461 | 163 / 166 | 33.7 / 33.7 |
| eval-6 | 1/3 · 2/3 | 0.352 / 0.392 | 141 / 149 | 28.7 / 30.3 |
| eval-7 | 2/3 · 3/3 | 0.371 / 0.377 | 150 / 149 | 30.3 / 30.3 |
| eval-8 | 2/3 · 3/3 | 0.350 / 0.428 | 142 / 168 | 30.3 / 33.0 |

B's mean cost was higher on all four instances.

### What coincides with the cost difference (observed, not proven causes)

- **Calls:** B made about one more call per run (+3.5%), and each call cost about 7% more (USD 0.0130 vs 0.0121).
- **Requests:** B's requests were about 5% larger (4,722 vs 4,494 input tokens per call). Right after each release they were about 320 tokens larger, with about 150 more cache-write tokens.
- **The advice text:** about 3.5k characters per run (≈1.1k tokens over 10 updates). It stays in context until Claude removes the observation that carries it, which matches the larger requests and the doubled pressure steps (3.1 vs 1.6 per run).
- **Jev itself is negligible:** about 0.2% of B's cost and 1.6% of its elapsed time.
- **What it does not show:** that the advice "made Claude do more work". Edits and executions also differ by about one per run, within the run-to-run spread, and the context style varied between runs. Append-only per-round notes, rather than one rolling note, appeared in 3 A runs and 2 B runs.
- **No visible cache disruption:** cache reads were 68% of input in both arms (68.3% and 67.5%).

### Advice and edits (temporal association only)

**Counts:**
- **Flags:** across the 12 B runs Jev made 114 flags at the 0.5 reporting threshold.
  - **On runtime entries:** 36, of which 34 were step actions whose body is mostly the code Claude ran.
  - **On notes:** 78, of which 64 were changed before the next update. Of the 125 unflagged notes, 36 were changed.
- **Base rate:** in the control arm, 34% of existing notes were changed before the next update, against 49% in B. B therefore edited existing notes somewhat more often, but this is confounded by note style and is not evidence that the advice caused the edits.

**Examples** (fictional scenario; trace ids in brackets):

1. **Advice followed by a relevant edit** (eval-8 rep 2 B, `…132252…eval-8-a64b`, round 8).
   - **The update:** *"Thread B root cause revised: database connection pool exhausted (DB_POOL_EXHAUSTED); this supersedes the earlier suspicion of CERT_EXPIRED"* and *"Thread D closed: false alarm (synthetic monitor misconfigured)"*.
   - **Jev:** flagged `n3` (0.72), the round-3 note saying *"B suspected CERT_EXPIRED inventory-svc ongoing"*.
   - **Claude's next edit:** it appended *"[HIST: B cause revised R8]"* to `n3` and wrote a new note `n8` with the revised cause and the closure.
   - **What it shows:** the interaction working. It does not show that Claude would otherwise have missed it.
2. **Advice ignored, or followed only in a new note** (eval-5 rep 2 B, `…130453…eval-5-80cb`, round 7).
   - **The update:** thread A resolved; thread B's cause revised from MEMORY_LEAK to CERT_EXPIRED.
   - **Jev:** flagged `n2` (0.89, "Thread A DISK_PRESSURE … ongoing"), `n4` (0.77, "Thread A mitigated"), `n5` (0.61) and `n1` (0.52).
   - **Claude** changed none of them. It wrote a new note `n7` ("Thread A … RESOLVED; Thread B cause revised to CERT_EXPIRED"), keeping a newest-note-wins log.
   - **Outcome:** this run later failed one check (thread C's status evidence), unrelated to these notes.
3. **Incorrect or unhelpful suggestions:**
   - **A miss** (the same eval-8 rep 2 update): `n6` said *"D DNS_RESOLUTION notify-worker ongoing"*, and the update closed thread D as a false alarm. Jev gave it **0.34**, below the threshold. Claude updated it anyway, to *"D DNS (later false alarm R8)"*.
   - **A spurious flag** (eval-7 rep 1 B, `…125729…eval-7-d17c`, round 4): the update only opened a new thread. Jev scored the previous step's action entry (`s8.act`, the code that rewrote the note) at **0.73**, above the note itself (0.46). Such step-action flags are about a third of all flags.

## What the results support

**Pilot and evaluation are kept separate.** The pilot (two development instances, one run each) suggested lower cost and time with advice. The evaluation, frozen in advance on four fresh instances with three repetitions, is the result to rely on.

- **Supported:**
  - Update-triggered Jev review is a working, matched, low-overhead intervention, with no extra Claude turn. Jev's own cost and latency are negligible, and all 117 evaluation calls succeeded.
  - **On this task, with this model and wording, adding the advice did not reduce cost or time.** The assisted arm averaged about 11% more cost and 6% more elapsed time, and was cheaper in only 4 of 12 matched blocks. The pilot's saving did not repeat.
  - The extra cost coincides with about one more call per run and slightly larger requests while advice text is in context. The evidence is consistent with advice overhead, but does not isolate it.
- **Not established:**
  - **A correctness benefit:** 10/12 vs 8/12 strict success, and 166 vs 161 of 168 checks, is a small difference over four instances. Only B succeeded in 3 blocks and only A in 1 (sign test p ≈ 0.6). Every failure in both arms was an omission or an invalid citation, never a stale fact, which is the error the advice targets.
  - **That the advice caused any edit:** flagged notes were often edited, but Claude also ignored flags and fixed notes Jev missed.
  - **Generality:** one synthetic task family, one model and effort setting, and one question wording.
  - **Any novelty claim.**

## Is strategy 1 ready for the larger evaluation? (assessment written after the pilot, before the evaluation)

**Technically yes; scientifically marginal on this task.**
- **Ready:** the plumbing, accounting and evidence work. The planned sample (4 fresh instances `rounds-eval-5..8`, registered uninspected, × 3 repetitions × 2 arms = 24 runs) could measure cost, time and call differences with paired blocks.
- **Estimated cost:** USD (0.377 + 0.313) × 12 × 1.25 ≈ **USD 10.4**, plus a small diagnostic reserve.
- **Limits it would face:**
  - **Accuracy headroom:** on dev instances this task is at the ceiling for both arms (007's evaluation showed some citation omissions on other instances).
  - **Little to discriminate:** the model's usual rolling-note style leaves the per-entry advice little to work with.
- **Decision:** whether the efficiency question is worth about USD 10 is the maintainer's call. Nothing is authorised.

**Outcome:** the evaluation was authorised and run on 2026-10-13 (section 5). Its actual cost was USD 9.48.

## Spend

- **Initial phase** (smoke, diagnostics, pilot): **USD 1.801066** of the USD 10 authorised then:

  | Item | Anthropic | TypeSafe |
  | --- | --- | --- |
  | Smoke run | USD 0.420221 | USD 0.000626 |
  | Pilot | USD 1.378036 | USD 0.001548 |
  | Diagnostics (009 fresh and 008 reference) | — | USD 0.000635 |

- **Evaluation:** **USD 9.477545** of the USD 20 authorised for it: Anthropic USD 9.467744 and TypeSafe USD 0.009801, over 24 runs, 751 Anthropic calls and 117 Jev calls. All settled; none assumed or pending.
- **Ledger:** USD 59.687573 spent of the USD 70.210028 ceiling, which was set explicitly for the evaluation (spend 50.210028 + 20). The unused remainder does not carry over.
- **Note:** the generated `report.md` counts run-attributed entries only. The diagnostic entries are kind `jev-diagnostic` in the ledger snapshot.

## Where is the evidence?

- `protocol.md`: the design, written before any paid call; the pilot session record; the **evaluation freeze**, written before any evaluation call; and the evaluation execution notes.
- `diagnostic-cases-v1.json`: the frozen diagnostic cases.
- `artifacts/diagnostics/20261012T115847-frozen` (fresh) and `…115851-frozen` (008 reference rerun).
- `report.md`, `metrics.json` and `metrics.csv`: all 29 runs, labelled by phase (`smoke`, `pilot`, `evaluation`), with the `ur_*` columns (updates, entries scored, appended and advice characters, Jev attempts, tokens, cost, latency, and flagged, changed and not-changed counts).
- `artifacts/runs/evaluation/` (24 runs), `artifacts/runs/calibration/` (the pilot) and `artifacts/runs/smoke/`, per run:
  - `summary.json → update_review.records`: exact payloads and hashes, revisions, candidate ids, answers, and the edits that followed;
  - `jev/NNNN.json`: every Jev request and response;
  - `events.jsonl`, context revisions, requests and scores.
- `artifacts/comparisons/20261012T124415/` (evaluation) and `…115926/` (pilot): the frozen settings, the schedule and the source patch.
- `artifacts/fixtures/`: the task instances.
