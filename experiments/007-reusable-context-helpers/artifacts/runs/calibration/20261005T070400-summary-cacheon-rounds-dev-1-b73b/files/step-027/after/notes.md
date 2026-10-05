R1: board empty; only slow query WARNs in all logs (noise).

R2: board.md:3-5 follow-ups OPEN ALERT_TUNING, RUNBOOK_UPDATE, VENDOR_TICKET. changes.md:4 CHG-120 APPLIED notify-worker http.max_inflight=0 (possible BAD_CONFIG); changes.md:5 CHG-121 payments no config. auth-svc db pool exhausted WARNs at lines 1,3,15,22,23,25 + 3 more (9 total); no board thread yet. Other services: only noise.

R2 auth-svc db pool exhausted also at lines 44,65,69 (in_use grows 12->20). Notify-worker R2 log shows only INFO lines (gaps at 5,7,17-19,33,39,42,45,50,53,56 not checked).

R3: board.md:3 Thread A DB_POOL_EXHAUSTED auth-svc+search-api ongoing. auth-svc.log:7-19 pool exhausted; search-api.log:1-14. changes CHG-125 dashboards only.

R4: board.md:3 Thread B payments-svc CACHE_STAMPEDE suspected ongoing; but logs show 429 fx-rates in payments-svc (lines 1,3,7,25,31,45) and checkout-api (9,19,50,53,59,62) -> likely UPSTREAM_RATE_LIMIT. changes.md:3 CHG-133 APPLIED TLS ticket rotation. Pool exhaustion continues auth 7-39, search 4-30.

R5: board:3 A mitigated; board:4 B adds checkout-api; board:5 CAPACITY_REVIEW; changes:4 CHG-143 applied auth-svc mitigation; changes:3 CHG-138 TLS rotation. B 429s r05 payments 13,19,47,50,55,73; checkout 21,23,30,38,42,59.

R6: board:3 CLOSED ALERT_TUNING; board:4 OPEN CUSTOMER_COMMS; changes:3 CHG-147 retry budget (not config of notify). B 429s r06 payments 3,10,11,16,18,33 (11 hits); checkout 19,30,56,73,76,77. A none; notify none.

R7: board empty. B 429s continue payments 1..82 (10), checkout 11..66 (12). A none, notify none.

R8: Thread A resolved r08/board.md:3. Thread B UPSTREAM_RATE_LIMIT confirmed r08/board.md:4, ongoing; r08 logs payments-svc 2-83 (429), checkout-api 1-54. Thread C r08/board.md:5 notify-worker ongoing; logs show config validation failed http.max_inflight=0 (r08 notify-worker.log:5,45,50,58,72) -> BAD_CONFIG_ROLLOUT traced to CHG-120 r02/changes.md:4. CHG-159 proposed only.

R9: Thread B mitigated r09/board.md:3; 429s still at r09 payments-svc.log:34-42, checkout-api.log:34-55. Thread C still restarting r09/board.md:4; notify-worker config validation failed r09 notify-worker.log:3-67. CHG-164 applied (retry budget).
