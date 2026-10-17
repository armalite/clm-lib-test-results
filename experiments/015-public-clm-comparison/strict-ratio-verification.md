# 015 – guarded-clm with `strict_ratio_learning` enabled: offline verification

> **Superseded (2026-10-16, later).** guarded-clm `3f18473` (0.2.0.dev1) removed `strict_ratio_learning` and made an implausible-ratio backstop always on. This record stays valid only for `db619a8` and the settings it records. The configuration it verified is kept byte-identical as clm-lib `configs/p015/superseded/proposed-comparison-strict-db619a8.json` (sha256 `e76f7cb98072f6d76639a4df2433ab6a38df86fdb6224f75e3f71fb0a0a6ffba`), and the launcher refuses it. Successor: [backstop-verification.md](backstop-verification.md).

_Written 2026-10-16. **Offline and scripted only. There are no live results.** This is new verification evidence. It
does not replace the earlier offline verification, which used guarded-clm 0.1.0 with the option absent
([docthread-workload.md](docthread-workload.md), [arms-offline.md](arms-offline.md))._

## The library revision

| Item | Value |
| --- | --- |
| guarded-clm revision | `db619a8a61eb2aebd4f127c05c9ab12f98ba8b6d`, "Add strict_ratio_learning (off by default) and align versions at 0.2.0.dev0" |
| checkout state | clean (no tracked or untracked changes); not modified by this work |
| package and module version | `0.2.0.dev0` and `0.2.0.dev0`. The earlier mismatch (module 0.1.0, distribution 0.1.0.dev0) is resolved in the library |
| source fingerprint (`library_provenance()`) | `ed22df2936cfd3cd170a967a42a71518677b6ee66157e2ac84e81f63b5fbfcc1` |
| how clm-lib uses it | imported from the sibling checkout, editable, in clm-lib's p015 environment. clm-lib's `uv.lock` entry was refreshed from 0.1.0.dev0 to 0.2.0.dev0 (one line); nothing else changed |
| the library's own default | `strict_ratio_learning=False` in `clm_context()` and `ClmContext` |
| the 015 comparison configuration | `strict_ratio_learning=True`, set explicitly (clm-lib `configs/p015/proposed-comparison.json`), whatever the library's default becomes |

**Not a final pin.** The library-default decision is pending, so this is the revision used for this offline checkpoint, not the final live dependency.

## What the option does (from the library's code at that revision)

**With the option on, only the shared estimator's new-text ratio is affected:**
- It learns only from a request that **extends the last answered one**, by the guard's own test: the same task, with the old entry lines a prefix of the new. An empty working context counts as a prefix.
- It ignores an observation **below 0.5 characters per token**.

**Unchanged by the option** (guarded-clm SPEC 13.16, decisions P6):
- the overall characters-per-token update;
- the anchor (the last request and its reported input);
- the estimate methods;
- the guard's own ratio and its conservative fit formula;
- notices, records and endings.

**The per-run clone** created for each user turn receives the setting.

**This is not behaviour-neutral.** With the option on, estimates can differ after a step that does not extend the last answered request, and the guard and over-limit decisions that depend on those estimates can differ with them. It does not make token counting accurate. It only removes one route by which the new-text ratio could fall far below any real text density.

## How clm-lib carries it

- **`GuardedSettings.strict_ratio_learning`** has a harness default of **False**: the integration's behaviour before the option existed, fixed in clm-lib whatever the library's default is. It is always passed explicitly to `clm_context()`. An older spec that omits it runs with False.
- **Recorded in:**
  - the launch contract (`arm_settings.guarded_clm`), and so the contract's configuration fingerprint;
  - each session's `session.json` (`settings`), together with the library's revision, version and source fingerprint;
  - the exported session.
- **The library's trace variant label is unchanged** (`clm_lite_v3_3`). The configuration is identified by the explicit setting and the provenance, not by a renamed variant.
- **Unchanged:** the paper and summary arms.

## Checks (clm-lib `tests/p015/test_strict_ratio.py`; network blocked)

| Check | Result |
| --- | --- |
| the harness default is False; True and False are passed to the imported `ClmContext` | pass |
| the setting reaches the per-run clone, checked in two turns through a tool reading the bound capability | pass |
| **the collapse shape, with provider-like usage** (guarded-clm's own regression: a read, then one response that deletes it and reads about the same amount while reported input rises, then a large read), **strict off** | the direct library run and `GuardedSession` give identical transcripts; the run ends as `context_limit`, "over the budget itself", with an estimate above 32,000 tokens, although no reported input exceeded 10,000 |
| the same, **strict on** | identical transcripts directly and through the session; the run completes, the edit is accepted, and there is no over-limit or context-limit record |
| a purely appending run, strict off against strict on | the transcripts are identical: the library's rule that append-only learning is unchanged |
| four existing equivalence cases (edits, guard burst, pressure re-arm, answers retained) with strict on | the direct and session transcripts are identical |
| contract, run metadata and export, with True | recorded in the contract, `session.json` and the export (`verify_export` clean); the library version is recorded as 0.2.0.dev0 |
| flipping the setting in a contract (digest recomputed) | refused: the configuration fingerprint differs |
| an older-style spec without the field | the session records False |

**The existing equivalence cases** (with the option absent, so False) still give identical direct and session transcripts.

## docthread sessions, strict off against strict on (scripted)

**What was run:** guarded-clm on both development instances, with the scripted `tidy` and `keep` policies and both usage paths, synthetic and fixed: 16 sessions in 8 pairs. Raw records are in clm-lib, in the ignored `runs/strict-ratio-2026-10-16/`, with all 16 exported and verified.

**Results:**
- **All 8 pairs gave identical requests, traces, tool results and turns,** after removing timestamps and run ids.
- **The figures match the earlier table:** 10/10 everywhere; peak estimates of 6,220, 4,544, 27,236 and 25,034 (dev-1) and 6,172, 4,508, 27,253 and 26,598 (dev-2); and the same pressure counts and holds.

**Why nothing changed:**
- the scripted synthetic usage is proportional to message content, so no step reports a rise out of line with its growth;
- the `tidy` policy's edits make requests shrink, and shrinking requests are not learnt from in either mode;
- the fixed path does not calibrate at all.

**What this does and does not show:** the option changes nothing on these scripted docthread sessions. **It does not show** that the option is neutral under real provider usage. That is what the collapse check above exercises.

## Remaining limitations

- **All usage is synthetic or provider-like.** Real reported usage, and the frequency of non-extending steps with real models, are unknown until a separately authorised development smoke.
- **The library-default decision is pending.** The final live revision pin waits for it. Whatever is decided, the 015 configuration sets the option to True explicitly.
- **guarded-clm's own tests** were not run here. They belong to the library, which records its own results (32 stored transcripts unchanged, per its decisions P6).
