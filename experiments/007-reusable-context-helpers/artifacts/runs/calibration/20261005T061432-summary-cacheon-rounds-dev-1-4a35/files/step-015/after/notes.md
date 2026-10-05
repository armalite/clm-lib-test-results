R1: only slow query noise, board empty, CHG-108 PROPOSED (search HPA) not applied.

R2: follow-ups OPEN ALERT_TUNING(b:3),RUNBOOK_UPDATE(b:4),VENDOR_TICKET(b:5). CHG-120 APPLIED notify-worker max_inflight=0 (changes.md:4). auth-svc db pool exhausted lines 1,3,15,22,23,25,44,65,69.

R3: Thread A opened DB_POOL_EXHAUSTED auth-svc+search-api ongoing (round-03/board.md:3). Logs auth-svc.log:7-19, search-api.log:1-14. CHG-125 dashboards irrelevant.

R4: Thread B opened payments-svc suspected CACHE_STAMPEDE ongoing (round-04/board.md:3). But logs show 429 upstream=fx-rates in payments-svc.log:1,3,7,25,31,45 and checkout-api.log:9,19,50,53,59,62 -> likely UPSTREAM_RATE_LIMIT. auth/search pool exhausted continues (auth 7-39, search 4-30). CHG-133 TLS tickets irrelevant?

R5: Thread A mitigated (round-05/board.md:3), CHG-143 mitigation auth-svc (round-05/changes.md:4); no pool errors in R5 logs. Thread B adds checkout-api (round-05/board.md:4), still CACHE_STAMPEDE per board but logs 429 fx-rates checkout-api.log:21-65, payments-svc.log:13-73. Follow-up OPEN CAPACITY_REVIEW (round-05/board.md:5).
