R1: board empty; slow query WARN noise all svcs; payments consumer lag stock-updates (payments-svc.log:7-43) maybe noise
R1 changes.md:4 CHG-113 APPLIED auth-svc cache.ttl_s=-1 (suspect BAD_CONFIG); CHG-112 TLS, CHG-114 shipping no cfg

R2: board Thread A opened QUEUE_BACKLOG payments-svc+ledger-svc ongoing (round-02/board.md:3). CHG-117 TLS rotation hourly (noise). Lag WARNs ledger-svc.log 5-77, payments-svc.log 3-40.

R3: board empty, CHG-124 PROPOSED (ignore). No new non-INFO lines besides lag/slow.

R4: board Thread B shipping-svc suspected DB_POOL_EXHAUSTED ongoing (round-04/board.md:3). Logs actually show CERT_EXPIRED sso.example.net in shipping-svc lines [1, 2, 4, 13, 17, 18, 24, 40, 41, 48, 55, 75, 85]. Follow-up RUNBOOK_UPDATE OPEN (round-04/board.md:4). CHG-133 noise.

R5: Thread A mitigated (round-05/board.md:3), CHG-143 APPLIED mitigation payments-svc (round-05/changes.md:3). CERT_EXPIRED sso.example.net now also search-api lines [14,35,50,51,79,81]; shipping-svc lines [1,2,18,27,52,54,56,59].

R6: logs are JSON now. Board Thread B adds search-api; no other change.

R6: CERT_EXPIRED errors continue in search-api (lines 11-63) and shipping-svc (lines 4-78) of round-06 logs. No changes.md in round 6.
