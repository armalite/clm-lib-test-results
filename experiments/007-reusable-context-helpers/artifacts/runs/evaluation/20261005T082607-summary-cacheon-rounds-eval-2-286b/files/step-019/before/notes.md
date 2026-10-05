R1: no board items. CHG-112 applied (log sampling, benign). auth-svc heap warnings rss 2-3.8GB (watch MEMORY_LEAK) round-01/logs/auth-svc.log:3,40. slow query noise everywhere.
R2: Thread A MEMORY_LEAK auth-svc+payments-svc ongoing (round-02/board.md:3). FU OPEN CUSTOMER_COMMS (board.md:4). CHG-120 APPLIED inventory-svc retry.backoff_ms=0 (round-02/changes.md:3) - watch BAD_CONFIG. CHG-121 ledger no cfg. payments heap warns round-02/logs/payments-svc.log:5-43; auth round-02/logs/auth-svc.log:5-21.

R3: CUSTOMER_COMMS CLOSED (round-03/board.md:3). CHG-121 APPLIED retry budget GETs=1 (round-03/changes.md:3). Leak continues auth round-03/logs/auth-svc.log:19-26, payments round-03/logs/payments-svc.log:8-24. No other errors seen.

R4: Thread A mitigated (round-04/board.md:3), CHG-136 mitigation auth-svc (round-04/changes.md:4). Thread B opened ledger-svc suspected CACHE_STAMPEDE (round-04/board.md:4) but logs show DNS SERVFAIL host=rates.internal round-04/logs/ledger-svc.log:10-28,47-64,79-83 -> likely DNS_RESOLUTION. FU DATA_BACKFILL OPEN (round-04/board.md:5). CHG-133 TLS ticket rotation hourly.

R5: board empty. ledger DNS SERVFAIL continues round-05/logs/ledger-svc.log:14-49 (6 errs). Auth/payments no heap errs.

R6: Thread A RESOLVED round-06/board.md:3. FU OPEN ALERT_TUNING board:4, RUNBOOK_UPDATE board:5. CHG-142 APPLIED retry GETs=1 round-06/changes.md:3. DNS SERVFAIL rates.internal ledger round-06/logs/ledger-svc.log:13-68 and pricing-svc round-06/logs/pricing-svc.log:5-67 (new svc).
