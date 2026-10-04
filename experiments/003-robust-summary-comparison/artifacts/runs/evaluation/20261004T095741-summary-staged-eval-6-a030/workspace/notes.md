S1: release-notes-6.24.0-4314.md:9 timeout 2500->800; :18 pool 48->10. billing log ERROR pricing-core timed out after 800ms lines 152-220 (95 errors). deploys.log:5.
S1 db pool wait WARN billing log lines 248,387 (in_use 10/10).
S2: changes.log:2 CHG-5123 APPLIED timeout=4000. billing log s2 db pool exhausted first line 187,194,216 (~110). Hypothesis DB_POOL_EXHAUSTED pool 10 from release-notes:18.
