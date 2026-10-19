# 015 – `paper_clm_shell` in smoke-dev2: fidelity review of the turn-4 failure

_Written 2026-10-19, offline. It is reconstructed from the frozen export ([smoke-dev2-export/](smoke-dev2-export/)) and the
public sources cited in [paper-clm-shell-fidelity.md](paper-clm-shell-fidelity.md): the paper (arXiv 2609.37725v1,
§4.1 and Appendices D and E) and the harness README at `18dc111`. No reference source code was read. No call was made,
and nothing was changed in the arm, the task or the scorer._

**The scope:** turn 4 of the paper session, which ended at the arm's context limit. Turns 5–8 never ran, under the common stop-on-first-incomplete-turn policy, and nothing is inferred about how they would have scored. This is a context-limit ending, not a step or call limit, so the separate turn-continuation question does not apply.

## 1. The failure, step by step

**The setting:**
- **The limit:** 29,952 tokens (a 32,000 budget, less 2,048).
- **The reminder point:** 27,904.
- **Estimates against reported input:** the estimates below are the arm's; the reported input of the same requests was within about 2% (attempts 12–19).

| Attempt | Request estimate | What happened |
| --- | --- | --- |
| 8–10 | 18,282 → 23,788 | Turn 4 begins; the model reads journal pages 7, 2 and 15. |
| 11 | 27,310 | Below the reminder point, so no notice. The model reads pages 5 and 6 together. |
| — | 33,021 | **Rollback 1:** the last step (both page reads) is removed → 27,679. |
| 12 | 27,769 | The notice says the last step was rolled back: "Edit … to make room". The model lists the mirror's block headers (`wc -l`, `grep -n CTX_TURN`; 863 bytes). |
| 13 | 29,074 (878 tokens of room) | The reminder ("within 2,048 tokens of the limit"). **The model's edit:** a Python script that replaced the bodies of eight tool blocks with its own one-line summaries, each followed by `<<end result>>` but without the `<<result id=… tool=…>>` opening line. |
| — | 30,774 | **The edit is rejected:** "a tool block must hold only result sections". The command's result (12 bytes of output) ended with the receipt `[context] edit rejected, nothing changed: a tool block must hold only result sections.` Adding the edit step took the request over the limit, so **rollback 2** removed that whole step: the script, its output and the receipt → 28,900. |
| 14 | 28,990 | The model sees only "your last 1 step(s) were rolled back and their results removed". It inspects the mirror (`sed | awk | sort`, 4,544 bytes) → 31,291 → **rollback 3**. |
| 15 | 28,937 | It inspects (`head -c 3000`, 3,000 bytes) → 30,719 → **rollback 4**. |
| 16 | 28,910 | It inspects (a loop over block headers, 1,338 bytes) → 30,166 → **rollback 5**. |
| 17 | 28,897 | It inspects (`head -c 2000`, 2,000 bytes) → 30,335 → **rollback 6**. |
| 18 | 28,890 | It inspects (`sed -n 1,30p`, 1,437 bytes) → 30,184. The six rollbacks are used, so this becomes the one permitted over-limit request. |
| 19 | 30,284 | The notice: "nothing more can be rolled back. Edit … in this step; if the next request is still over the limit, the turn ends." It inspects again (`tail -40`, 1,709 bytes). |
| — | 32,272 | Over the limit, after the final allowance (and over the 32,000 budget), so the turn ends with `context_limit`. |

**Why every inspection was rolled back:**
- After each rollback the request sat at 28,800 to 29,000 tokens: about 950 to 1,150 tokens of room.
- Each inspection step added 1,256 to 2,301 tokens: its command, the replayed thinking signature and the output.
- So no inspection could fit. Only an edit that the arm accepted, and that shrank the conversation, could have.

**The model's error, against the difficulty the rules imposed:**
- **Model error:** the edit was malformed against the instructions it had. The instructions say "a tool block holds the results (`<<result id=... tool=...>>`, the result, `<<end result>>`)" and "every call is answered in the next block". The script removed the result headers. They gave no worked example, and did not say that text outside a result section is rejected.
- **Imposed by the arm's rules:** the model never learned why its edit failed, because the rollback removed the receipt. After that, the margin-less rollback left too little room for anything except a correct, shrinking edit made blind.

## 2. The mechanisms against the sources

| Mechanism | What the sources say | `paper-clm-shell/1` | Classification | Affected this run? |
| --- | --- | --- | --- | --- |
| Rewriting the context | Paper §4.1: the model may "freely edit" the context file with Bash. README: a changed file is "parsed back into a valid message list". | Any block may be deleted, shortened or rewritten, if the result is a valid conversation. | **Explicitly source-supported** | No (allowed) |
| The tool-result format and its validation | Not stated. Neither source says how tool results are written in the file. | Our encoding: a tool block must hold only `<<result>>` sections, so that each native call stays paired with its result. | **A documented adaptation** (necessary for native tool pairing; the encoding is ours) | **Yes:** the edit broke it and was rejected |
| Feedback on a rejected edit | README: "A rejected edit is not applied, and the model is told why." | A receipt with the reason, appended to the command's result. | **Explicitly source-supported** | Given, then removed (next row) |
| Whether the feedback survives rollback | Not stated by either source. | The step holding the receipt is rolled back with it. The rollback notice gives no reason. | **Unspecified by the sources.** In this run it defeated the README's stated property that the model is told why. | **Yes** |
| The rollback unit and retries | Paper App. E (BrowseComp-Plus): "rolls back the last turn and retries, up to six times". README: the newest turns until 2,048 tokens are free; 50 retries. | The last step (one reply and its results), retried while over the limit, up to 6 per turn. | **Explicitly source-supported** (the paper's rule; "turn" read as one model step, consistent with the paper's free "editing turns") | **Yes:** 6 rollbacks |
| Room to edit again after a rollback | The paper does not say. The README's 2,048-token margin addresses it. | None: the request returns to the state just before the last step, here about 1,000 tokens under the limit. | **Unspecified by the paper.** The README's margin is the documented alternative (`readme` profile, not chosen under the agreed source-priority rule). | **Yes** |
| The terminal rule | Paper: not stated after the six retries. README: one final turn, then the run stops if still over. | One final over-limit request, then `context_limit`. A request over the budget itself ends the turn at once. | **A documented adaptation** (the README's rule where the paper is silent) | **Yes** |
| The editing reminder | Paper App. E: "its editing reminder 2,048 tokens before the budget". | One reminder at 27,904, once per crossing. | **Explicitly source-supported** (budget read as the usable limit; documented) | **Yes:** it came only at attempt 13. The first overflow came from a single 5,700-token step that started below the reminder point. |

**Nothing involved is inconsistent with the stated sources.** The one interaction that matters is unspecified: rollback removing the rejection receipt. It is the only point where the arm, as built, contradicted a property a source states.

**The margin-less rollback** is the paper's rule followed literally. It made recovery hard here, but it is not a defect.

## 3. Recommendation

**Propose one narrow source-alignment correction, and nothing else:** when a rolled-back step held an edit receipt, carry that receipt's text into the rollback notice. For example, "… your last 1 step(s) were rolled back and their results removed; the edit in it was rejected: a tool block must hold only result sections. Edit … to make room".

- **The source basis:** README, "A rejected edit is not applied, and the model is told why." The paper says nothing about receipts. The rollback unit, the count, the margin, the reminder and the terminal rule stay exactly as they are.
- **The expected effect:** only on the path where a step holding a rejected edit is rolled back. The model is told the reason it would otherwise lose. Every other request is unchanged. Whether it would change any outcome is not known and is not inferred.
- **Offline verification it would need:**
  - a scripted session in which a rejected edit's step is rolled back, so that the next request's notice carries the reason;
  - an accepted edit, and a rollback with no edit, keep their current notices;
  - the paper-arm tests and the three-arm fairness tests still pass;
  - a new arm version label (`paper-clm-shell/2`), and the fidelity document updated.
- **Live verification:** none needed for compatibility. The change is plain text in an existing notice, and the request shape and provider interface do not change. A development smoke would not reliably reach the path either: it occurred once, in one turn. The first live exercise would be the confirmation runs. The record should say so.
- **Not recommended:** switching to the README's rollback margin. That would override the agreed rule that the paper's settings come first. The margin-less rollback stays, as a stated limitation.

**Approval is needed before implementation.** The paper arm's rules were confirmed only as provisional for the smokes. This change and the existing open questions in the fidelity document should be decided together, before the confirmation design is frozen.

## 4. Interpreting the other results (checked against the export)

**guarded-clm, the held output:**
- page 6 was held back at step 7 (it needed about 4,529 tokens with 3,951 free);
- the model then deleted earlier steps, and read page 6 again at step 13;
- the guard's projection was 20,403 tokens (conservative 25,645) against the 29,952 limit, so it was admitted;
- **so the output was recovered.**

**`token_tail_p015`, the quote:**
- the given line equals the cause line exactly once whitespace is collapsed;
- it passes the length rule (167 characters) and the cause-signature rule (`worker.lease_seconds=45`), and page 12 holding it had been retrieved;
- it fails only the exact-substring rule, because the column padding after `diagnostic` was collapsed;
- **so it is correct in fact and retrieval, and an exact-format miss.**

**The scores stay as exported:** guarded-clm 10/10, `paper_clm_shell` 4/10, `token_tail_p015` 9/10. The scorer is not loosened, and no adjusted score is given.

**Exact-format compliance, separately from correctness:**

| | values answered | correct in fact and retrieval | in the exact required form |
| --- | --- | --- | --- |
| guarded-clm | 10 | 10 | 10 |
| `token_tail_p015` | 10 | 10 | 9 (the quote's spacing) |
| `paper_clm_shell` | 4 (turns 1–3) | 4 | 4 |

The paper arm's remaining six values are unanswered: turn 4 failed, and turns 5–8 were never attempted.

**Turn counts:** 24 turns were planned (8 per session), 20 were attempted (8, 4 and 8) and 19 completed (8, 3 and 8). The 73 attempts were made in the 20 attempted turns.

## 5. Is the comparison suitable for confirmation?

**Not yet, as frozen.** Nothing found is a harness defect, and nothing contradicts a stated source.

**What should happen first:**
- **One known unspecified interaction should be decided:** the receipt lost to rollback. It removes a source-stated property and would bias the paper arm against itself on this path.
- **Then decide its version** together with the fidelity document's open questions.

Once the receipt change is decided and verified offline, no further development smoke is needed for compatibility.

## Note added 2026-10-19 (the review above is kept as written)

**The recommended correction is implemented offline as `paper-clm-shell/2`** (clm-lib SPEC §36), and proposed for the confirmation. The smoke-dev2 paper result remains a result of `paper-clm-shell/1`.

