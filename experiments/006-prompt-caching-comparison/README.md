# 006 – Prompt-caching comparison (planned)

**Status: draft plan. Not implemented and not run.** Nothing below is frozen, and the design, workload, sample size and budget are not agreed.

## Question

Does CLM's efficiency advantage persist with ordinary provider prompt caching?

## Why

In experiments 003 and 004, against the robust baseline, CLM was about 25% cheaper per run, and the gap closely matched the baseline's spending on separate summary calls. Those runs sent no `cache_control`, so every input token was billed uncached. Prompt caching could change the picture:
- repeated request prefixes become cheap;
- both a CLM edit and a baseline summary rewrite earlier context, which invalidates cached content after the change point;
- the baseline's summary calls have their own prompts.

## Scope

- **In scope:** ordinary provider prompt caching through the API (`cache_control`).
- **Out of scope:** the CLM paper's separate **suffix-cache reuse** optimisation (reusing cached computation after an edited span). It needs model-server support and is not part of this experiment.

## Comparison (proposed)

A 2 × 2 matched design: {CLM, robust `token-tail/1` summary baseline} × {caching off, caching on}, with the same model, effort, tasks, tools and limits throughout. The task family is to be chosen, most likely the experiment-004 coding task or a variant of it.

## What will be measured

- **Provider-reported tokens:** cache-read, cache-write (creation) and uncached input tokens; output tokens.
- **Cost:** total, priced with the dated cache rates.
- **Other:** latency; correctness and completion; context-management activity.
- **Cache behaviour:** how much cache reuse is lost after each CLM edit or baseline summary, including the summary calls themselves.

## What outcomes would and would not establish

- Whether, and by how much, CLM's cost gap changes with caching on this workload and request layout.
- It would not establish behaviour for other layouts, providers, models or the paper's suffix-cache reuse.

## Unresolved decisions

See `protocol.md`.
