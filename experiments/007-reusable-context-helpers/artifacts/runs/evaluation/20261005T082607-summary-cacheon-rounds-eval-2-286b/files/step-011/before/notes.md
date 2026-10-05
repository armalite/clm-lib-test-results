R1: no board items. CHG-112 applied (log sampling, benign). auth-svc heap warnings rss 2-3.8GB (watch MEMORY_LEAK) round-01/logs/auth-svc.log:3,40. slow query noise everywhere.
R2: Thread A MEMORY_LEAK auth-svc+payments-svc ongoing (round-02/board.md:3). FU OPEN CUSTOMER_COMMS (board.md:4). CHG-120 APPLIED inventory-svc retry.backoff_ms=0 (round-02/changes.md:3) - watch BAD_CONFIG. CHG-121 ledger no cfg. payments heap warns round-02/logs/payments-svc.log:5-43; auth round-02/logs/auth-svc.log:5-21.

R3: CUSTOMER_COMMS CLOSED (round-03/board.md:3). CHG-121 APPLIED retry budget GETs=1 (round-03/changes.md:3). Leak continues auth round-03/logs/auth-svc.log:19-26, payments round-03/logs/payments-svc.log:8-24. No other errors seen.
