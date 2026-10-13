# 012 – Jev screening of incoming tool results

**Status: PLANNED. Only the offline opportunity assessment is done** (2026-10-13). No paid call or agent run has been made, and no screening code exists in clm-lib.

**Question:** can Jev screening of incoming tool results improve a CLM agent by reducing unnecessary input before the main model processes it? The screening would be a filter beside CLM; Claude still makes every working-context edit.

**Offline finding** (`analysis/audit_observations.py`, fixed trace set: the 12 ordinary-CLM runs of 010 v3's evaluation, 261 executions):
- **Small observations:** tool results reached Claude small. The median was 539 characters (90th percentile 2,693), 1 of 261 was cut by the output cap, and none was spilled.
- **Already filtered:** Claude's own code filtered almost all of them.
- **Short-lived:** they were usually removed from context within 1–3 requests.
- **A small share of input:** observations were about 10% of request characters.
- **Little removable material:** generator background noise inside the larger observations is the main removable material. Removing all of it would save at most about **3.9% of run cost** under prompt caching, and it is mixed with evidence (including WARN-level and JSON-format evidence lines).

**Decision:** the incident workload offers **no meaningful screening opportunity**. The recommended alternative is a **document-search workload** whose tool naturally returns several passages. Its design, fair comparison (A ordinary CLM vs B with screening, identical saved originals and tools), screening policy `result-screen/1`, metrics, readiness steps and estimate are in [`protocol.md`](protocol.md). **All of it is unimplemented and unrun.**

**Next step (needs the maintainer's decision and authorisation):** build the search workload and the screening layer offline. Then re-check the opportunity on generated search outputs, before any paid component diagnostic.
