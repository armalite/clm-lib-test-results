# 008 – Optional Jev assistance for model-controlled context management

**Status: designed and implemented; not run.** This session had no TypeSafe API key, so the component diagnostic and the four-run pilot were not run, and **no results exist yet**. Nothing below is a finding.

## The question

**Can a fast decision model help an agent manage its own context?**

The first capability tested is *"Which existing context entries need review because of this update?"*

**Conditions:**
- **A:** CLM alone.
- **B:** the same CLM with an optional way to ask TypeSafe's Jev model for advice.

**Equal in both:** the agent alone decides whether, when and how to edit its context. It can write reusable helpers, but is not required to.

**What Jev does:** it only answers, for each entry the agent submits, the fixed question *"Does this update require reconsidering a current assertion or planned action in this entry?"* It returns a probability per entry. It never edits anything, and the agent may ignore it.

**Prior work:**
- fast-jev-compaction already uses Jev to delete stale tool output by fixed rules.
- The Muninn post already combined Jev flags with model-written state updates.
- This experiment differs: the advice is optional and model-invoked inside a CLM loop. See `protocol.md`.

## What exists

- **The integration** (clm-lib):
  - a host-side `review_context` action, so the sandbox still has no network or keys;
  - exact entry text taken from the named context revision;
  - every request and answer recorded;
  - separate TypeSafe accounting in the shared ledger;
  - opt-in, and off in all earlier configurations.
- **Offline tests:** these show the extension is opt-in, advice cannot change context, ids and revisions are validated, failures leave the agent working, requests hold only agent-visible text, and evidence survives export.
- **`diagnostic-cases-v1.json`:** 24 frozen labelled cases (plus 6 development cases), labelled before any Jev answer.

## What has not happened

- No Jev call has been made, and no pilot run.
- **Not yet known:**
  - whether Jev's advice is accurate on these cases;
  - whether an agent would choose to use it;
  - whether it changes cost, time or correctness.

## How to run it

1. Make `TYPESAFE_API_KEY` available to the process that runs the commands. It must be **exported** into that environment; a plain assignment in a file that is sourced is not passed to child processes.
2. Never place the key in the repository, configs, prompts or artifacts.
3. **Diagnostic**, in clm-lib: `uv run clm-lib --config configs/exp008.toml jev-diagnostic --cases experiments/008-jev-context-review/diagnostic-cases-v1.json --split frozen --max-usd 1`. This costs well under one cent at USD 0.042 per million input tokens.
4. **Pilot:** `uv run clm-lib --config configs/exp008.toml compare --tasks rounds-dev-1,rounds-dev-2 --reps 1 --conditions clm_helpers:on,clm_helpers+jev:on --max-usd 9`. The estimate is about USD 1.5–2.5, based on experiment 007's direct-editing runs at about USD 0.39 each.

**Before the pilot:** fix the review-revision boundary described at the end of `protocol.md` (reviews must be limited to the agent's current context).

**Budget:** the ledger ceiling is USD 56.994, which is USD 10 authorised for this diagnostic and pilot work and still unspent. The 24-run evaluation is not authorised.
