# 015 – Confirmation `confirm1`: findings and interpretation

_Written 2026-10-20 from the frozen confirm1 evidence only: [confirm1-record.md](confirm1-record.md), [confirm1-export/](confirm1-export/), [confirm1-exposure.md](confirm1-exposure.md) and the fidelity sources in [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md). No model was called. The official scores are unchanged. The smokes are not pooled with the confirmation: they ran different arm or task versions and are reported separately._

## 1. Results

**What it is:** one session per arm per instance, on one model (Claude Sonnet 5) and one task family (docthread, eight questions). The six instances are the independent units.

**The score:** the preregistered primary outcome, exact-format points out of 10, with recall out of 3.

| instance (template) | guarded-clm | token-tail summary | paper shell (`paper-clm-shell/2`) |
| --- | --- | --- | --- |
| 1 (lease) | 10, 3/3; 8 of 8 turns | 10, 3/3; 8 of 8 | 4, 0/3; **stopped in turn 4** (3 of 8 completed) |
| 2 (memory) | 10, 3/3; 8 of 8 | 10, 3/3; 8 of 8 | 0, 0/3; **stopped in turn 1** (0 of 8) |
| 3 (pages) | 10, 3/3; 8 of 8 | 10, 3/3; 8 of 8 | 4, 0/3; **stopped in turn 4** |
| 4 (lease) | 9, 3/3; 8 of 8 | 9, 3/3; 8 of 8 | 4, 0/3; **stopped in turn 4** |
| 5 (memory) | 10, 3/3; 8 of 8 | 10, 3/3; 8 of 8 | 4, 0/3; **stopped in turn 4** |
| 6 (pages) | 9, 3/3; 8 of 8 | 10, 3/3; 8 of 8 | 4, 0/3; **stopped in turn 4** |

**guarded-clm against the summary baseline (paired by instance):**
- 0, 0, 0, 0, 0 and −1 points;
- cost +$0.32, +$0.88, +$0.72, +$0.42, +$0.50 and +$0.59 for guarded-clm.

So they tie in points on five instances, and the summary baseline is one point ahead on the sixth. All 18 recall values of each arm were correct (3 per session, 36 across the two arms; corrected 2026-10-20). **No accuracy difference between them is established.**

**The paper arm's sessions all ended early** at the arm's context limit, under the common stop-on-first-incomplete-turn policy. Its points come only from the turns before the stop. Its later turns are unanswered, and nothing is inferred about them.

### The three quote misses (no rescoring)

**All three cause lines had been retrieved.**

| session | what was given | kind |
| --- | --- | --- |
| guarded-clm, instance 4 | the cause line with a `seq ` prefix and the column padding collapsed | format only |
| guarded-clm, instance 6 | the cause line with the column padding collapsed | format only |
| summary, instance 4 | the cause line with the same format changes, **and a different tenant id** (`tn-4735` for `tn-4951`) | format, plus an identifier changed by the arm's summariser: its fifth summary had rewritten the line with an id that occurs elsewhere in the evidence |

### guarded-clm's context management, as recorded

| instance | peak reported input | PRESSURE notices | edits accepted / rejected | protected-entry refusals | holds (records / distinct outputs) | re-reads of held outputs | held outputs eventually admitted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 26,908 | 5 | 3 / 1 | 0 | 2 / 2 | 1 | 1 |
| 2 | 26,684 | 7 | 6 / 1 | 1 | 7 / 5 | 6 | 4 |
| 3 | 28,122 | 6 | 3 / 1 | 1 | 3 / 2 | 3 | 2 |
| 4 | 27,796 | 5 | 4 / 0 | 0 | 4 / 3 | 3 | 2 |
| 5 | 25,548 | 3 | 4 / 0 | 0 | 1 / 1 | 0 | 0 |
| 6 | 26,583 | 3 | 4 / 0 | 0 | 3 / 3 | 2 | 2 |
| **total** | | 29 | 24 / 3 | 2 | 20 / 16 | 15 | **11 of 16** |

**How "admitted" is read:** a re-read with no new hold record for the same output at that step. The other 5 held outputs were not read again: the model continued without them.

**The rejected edits:** one reused an existing note id. The two protected-entry refusals were edits that tried to delete earlier turns' requests and answers, which the library refused whole.

**Estimates:** guarded-clm's request estimates were within about 1.5% of the provider's reported input (median ratio 1.006 to 1.015).

**One recorded sequence** (instance 1, `confirm1.s01…guarded_clm`, `trace.jsonl`):
1. At step 7, journal page 2 was **held back**: it needed about 4,532 tokens, with 3,733 free.
2. In the same step the model's `edit_context` was **accepted**. It deleted 14 entries and added a note (`facts1`).
3. At step 9 the model **read page 2 again**, and this time it was admitted.

### Cost and time

| arm | sessions completed | turns completed / attempted / planned | provider attempts | confirmed cost | wall time |
| --- | --- | --- | --- | --- | --- |
| guarded-clm | 6 of 6 | 48 / 48 / 48 | 176 | $6.404 | 949 s |
| token-tail summary | 6 of 6 | 48 / 48 / 48 (+20 summariser calls) | 172 | $2.960 | 742 s |
| paper shell | 0 of 6 (all stopped) | 15 / 20 / 48 | 125 | $1.509 | 675 s |

**The paper arm's cost and time cover stopped sessions.** It completed 15 of 48 turns. Its lower cost is not a cost of doing the same work, and it is not compared with the others as "cheaper".

**The guarded-clm and summary costs, by billing component** (the recorded usage at the frozen price; the components reproduce every charge exactly):

| component (price per million tokens) | guarded-clm | summary: agent calls | summary: summariser calls | difference (guarded − summary) |
| --- | --- | --- | --- | --- |
| uncached input ($2.00) | 176 tokens, $0.0004 | 304, $0.0006 | 40, $0.0001 | −$0.0003 |
| cache writes, 5 min ($2.50) | 2,220,529, $5.551 | 423,227, $1.058 | 401,497, $1.004 | **+$3.490** |
| cache reads ($0.20) | 389,981, $0.078 | 1,384,829, $0.277 | 0, $0 | −$0.199 |
| output, incl. thinking ($10.00) | 77,464, $0.775 | 33,344, $0.333 | 28,698, $0.287 | +$0.154 |
| **total** | **$6.404** | $1.669 | $1.291 | **+$3.444** |

**Arithmetic attribution:** the whole difference is in cache writes. guarded-clm's +$3.49 there is slightly offset by its smaller cache-read charges (−$0.20) and slightly raised by more output (+$0.15).
- **guarded-clm:** 85% of its input tokens were billed as cache writes.
- **The summary arm's agent calls:** 23%.
- **Its summariser calls:** 100%. They never read from the cache, so caching made them dearer than uncached input would have been.
- **Input volume:** guarded-clm also sent about 18% more input tokens in total (2.61M against 2.21M).

**Causal explanation: not established by this design.** The documented mechanism is the request layout. guarded-clm rebuilds the whole request each call, so the cache prefix changes and is written again. The summary arm appends, so its prefix is mostly re-read. The recorded split is consistent with that, but no run varied the layout or the caching policy, so the share due to layout, as against the extra volume or the summariser's uncached-prefix behaviour, is not measured.
- **An arithmetic illustration only:** billed at the plain $2 input price with no caching, the recorded tokens would cost about $5.99 for guarded-clm and $5.04 for the summary arm, about 19% apart.
- **That is not a prediction:** behaviour and token counts could differ without caching.

## 2. The paper arm's editing contract, reviewed narrowly

### What the model was told

**The whole instruction,** sent as system text by the arm:

> Context management. Your conversation context is limited to about 29,952 tokens. Before each bash command runs, the conversation so far (every message after the system prompt and the first question) is written to /tmp/.live_ctx/LIVE_CTX_MAIN.txt, one block per message, each headed [[CTX_TURN i role=user|assistant|tool]]. An assistant block holds your text and your tool calls (<<call id=... tool=...>>, the JSON arguments, <<end call>>); a tool block holds the results (<<result id=... tool=...>>, the result, <<end result>>). You can change the file with any shell command: delete blocks, shorten them or rewrite them. When the command finishes, a changed file becomes your context from the next request on, if it is a valid conversation and fits the limit: assistant blocks and user or tool blocks alternate, starting with an assistant block; every call is answered in the next block; and the last block, which holds the running command, is unchanged. Otherwise the edit is not applied, and the command's result says why. […]

**Other help:** a single-line `bash` tool description. There was no worked example of a valid edit, and no example of how to summarise a tool result while keeping it valid.

**The model did see the format itself:** in five of the six sessions, it read the mirror file (with `grep`, `sed`, `head` or `cat`) before its first edit.

### Which requirements caused the 12 rejections

**The recorded reasons:**

| requirement | rejections (first failure recorded) |
| --- | --- |
| a tool block holds only `<<result id=… tool=…>>` sections | 8 |
| blocks start with an assistant block | 2 |
| every result answers a call in the previous block | 1 |
| the last block (the running command) unchanged | 1 |

**Most edits broke several rules:** each command was replayed offline on the mirror rebuilt from its frozen request, in the isolated sandbox, with no network and no model call. 11 of 12 replays reproduced the recorded reason exactly; the twelfth, on instance 5's final request, could not be reconstructed reliably and is reported by its recorded reason only.
- 6 of the 11 left **no** result section at all;
- 7 replaced the running command's block;
- 2 began with a user block re-creating the pinned first question.

### Where each requirement comes from

| requirement | source |
| --- | --- |
| one `[[CTX_TURN i role=…]]` block per message, after the pinned system prompt and task | **the README** |
| the file is parsed back into a valid message list; `fit` gate; the model is told why an edit was rejected | **the README** |
| the model may edit the file freely with shell commands | **the paper** (§4.1) and the README |
| the `<<call …>>` and `<<result …>>` section syntax; a tool block may hold nothing else | **our encoding** (documented adaptation): it keeps each native tool call paired with its result |
| every call answered in the next block | **forced by native tool calls** (the provider's pairing rule), given our use of native tools; how the reference represents tools is unspecified in the sources |
| blocks start with an assistant block and alternate | **our adaptation**; stricter than the provider strictly needs, since consecutive user turns could be merged |
| the running command's block unchanged | **our adaptation** (documented): keeps the running call answered and its reasoning signature intact |

### Were the rejected edits meaningful context reductions?

**Yes, in size, and the representation could not accept them.** In the replays:
- **7 of the 11** cut the mirror by 91 to 97% of its characters (for example 57,744 to 4,785), replacing the tool exchanges with short prose notes;
- **three** cut 23 to 61% (instance 3 twice, instance 6 once);
- **one** cut 7% (instance 5's first edit).

The notes kept facts such as queue totals and the component, as the commands show. Their completeness against the answers was not assessed here.

**An accepted path existed:** delete a call/result pair and keep notes as assistant text, leaving the last block alone. The instructions permit this ("delete blocks, shorten them or rewrite them"), but they do not show it, and the model never took it.

### What this implies

**The validator was correct:** every rejection applied a documented rule to an edit that broke it. **This is not a harness defect.** It is a genuine failure of the model to produce an edit in this format.

**The comparison is not reference-aligned for the editing contract.** The rules that rejected the edits are mostly our encoding and adaptations, not requirements stated by the paper or the README. The paper describes free editing, and the sources do not say how the reference treats prose that replaces tool exchanges.

**What the paper arm here is:** a paper-inspired shell-editing arm with our own representation. Its confirm1 result shows that, **with this representation and Claude Sonnet 5, the model did not produce an accepted edit**. It does not show how the paper's method performs, and it does not show that the method fails.

**A second, separate factor:** the near-limit last-step rollback, which removed inspection output (see [paper-arm-smoke-dev2-review.md](paper-arm-smoke-dev2-review.md)). The two are not separated here.

## 3. Remaining uncertainty

- **No accuracy difference between guarded-clm and the summary baseline is resolvable** at this size: five ties and one one-point difference, on one model and task family.
- **The cost difference's cause is not isolated** (see above), and it would differ under other caching policies or prices.
- **The `pages` instances** come from the smaller part of their template's range, because of the size filter, which was derived from the lease and memory development instances.
- **The paper arm's outcome is confounded:** its representation and its rollback rule, both partly our adaptations, act together, and neither was varied.
- **One model only:** whether other models comply with the mirror format, or behave differently under pressure, is not tested.

**A paid follow-up would be justified only for a specific question this evidence cannot answer.** For example: does a representation that accepts prose summaries of tool exchanges change the paper arm's completion? That is a new arm design, decided before seeing any of its results. None is proposed by default.

## 4. Evidence outline for a narrowly scoped blog post

Each claim below rests on a public artifact here, and its limit is stated.

1. **The idea: the model manages its own working context.** The model edits a structured context, and the runtime keeps every request within a fixed budget.
   - *Source:* guarded-clm's README and SPEC (public library).
   - *Limit:* this is a design description, not a result.
2. **What guarded-clm adds, and what the runtime enforces:**
   - structured edits applied all or nothing;
   - protected earlier turns;
   - a guard that holds back a tool output that would not fit, with a conservative estimate;
   - PRESSURE notices from 70%;
   - one request allowed into the reserve, then a hard stop.

   *Source:* the library SPEC. In confirm1 the enforcement was observed: 29 PRESSURE notices, 20 holds, 2 protected-entry refusals, and no over-limit request. *Limit:* 6 sessions.
3. **One hold, edit and re-read sequence:** instance 1, steps 7 to 9 (above).
   - *Source:* `confirm1-export/sessions/confirm1.s01-docthread-confirm-1-guarded_clm.r1/trace.jsonl`.
   - *Limit:* an illustration, not a statistic. 11 of 16 held outputs were eventually admitted, and 5 were never re-read.
4. **The confirmation results:** guarded-clm 58/60 and the token-tail summary baseline 59/60 on six fresh instances, every session completing all eight turns, with all 18 recall values of each arm correct (36 across the two; corrected 2026-10-20).
   - *Source:* [confirm1-record.md](confirm1-record.md).
   - *Limit:* one model, one task family, six instances, one session each. Five ties: **no accuracy advantage either way.**
5. **The summary baseline is competitive, and cheaper here:**
   - $2.96 against $6.40 for the same 48 completed turns;
   - the arithmetic difference is in cache-write charges.

   *Source:* the cost table above. *Limit:* the cause is not isolated. The summary arm also had one fact corrupted by its summariser.
6. **The limits of the paper-arm comparison:**
   - every session stopped at its context limit;
   - no mirror edit was accepted;
   - the rejected edits were large prose rewrites that our tool-pairing representation does not accept.

   *Source:* section 2 here, [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md). *Limit:* a result about this implementation, not about the paper's method.
7. **What remains untested:**
   - other models;
   - other task families;
   - caching policies;
   - a reference-aligned editing representation;
   - larger samples.

**Not to be claimed:**
- an overall accuracy advantage;
- superiority in general;
- that the original paper's method fails;
- any result pooled across the smokes and the confirmation.
