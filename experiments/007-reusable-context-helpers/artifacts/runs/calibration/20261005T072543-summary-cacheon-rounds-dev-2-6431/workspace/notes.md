R1: CHG-107 APPLIED retry budget GETs=1 (round-01/changes.md:3). inventory-svc DNS SERVFAIL rates.internal lines 7-90 (round-01/logs/inventory-svc.log:7,85-90). board empty. slow query WARN noise everywhere.
R2: Thread A opened DNS_RESOLUTION inventory-svc+checkout-api ongoing (round-02/board.md:3). checkout dns errors round-02/logs/checkout-api.log:8-59; inventory round-02/logs/inventory-svc.log:8-74. CHG-120 APPLIED search-api http.max_inflight=-1 (round-02/changes.md:3) possible BAD_CONFIG later. CHG-121 auth no config.
R3: Thread B opened auth-svc DB_POOL_EXHAUSTED ongoing (round-03/board.md:3) BUT logs show CERT_EXPIRED peer=sso.example.net auth lines [6, 9, 15, 21, 25, 26, 33, 48, 64, 72]. DNS continues checkout [33, 37, 44, 45, 47, 54, 69, 74] inventory [3, 7, 15, 28, 34, 41, 50]. CHG-126 PROPOSED only.
R4: board empty. auth CERT lines [6,8,16,39,48,59,63,66,77]; shipping-svc also CERT_EXPIRED sso lines [3,20,27,34,42,44,58,62,66]. DNS checkout [1,8,11,13,16,21,38,43,59,60,67,71] inventory [32,36,38,43,45,52,56,57,59,64,75]. search clean.
R5: board.md:3 Thread A mitigated (CHG-143 APPLIED round-05/changes.md:3, inventory-svc). board.md:4 Thread B adds shipping-svc, cause still DB_POOL per board (logs CERT_EXPIRED). board.md:5 VENDOR_TICKET open, board.md:6 ALERT_TUNING open. Logs: auth CERT [2,8,14,22,28,30,45,51,57,59,64], shipping CERT [9,11,34,36,39,52,54,55,60,63,65]; checkout/inventory/search clean.
R6 logs: auth-svc.log [4, 10, 14, 19, 20, 30, 50, 60, 76, 79]; checkout-api.log []; inventory-svc.log []; search-api.log []; shipping-svc.log [1, 18, 21, 22, 36, 64]
R6: board.md:3 RUNBOOK_UPDATE open. CHG-144 APPLIED (log sampling, irrelevant). Log format now JSON (use level field). auth/shipping still CERT; others clean.
R7 read step19
R7: board.md:3 ThreadB cause->CERT_EXPIRED. board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing (429 tax-provider). search lines 4,5,20,22,25,47,64,66. auth 1,16,24,26,32,36,38,49,53,64. shipping 10,11,23,26,35,39,43,45,46,49,59,66.

R8: A resolved r08/board.md:3. B mitigated r08/board.md:4. C opened search-api ongoing r08/board.md:5; logs show config validation failed http.max_inflight (CHG-120 r02/changes.md:3) at round-08/logs/search-api.log:2,5,10 -> likely BAD_CONFIG_ROLLOUT. DATA_BACKFILL open r08:6; VENDOR_TICKET closed r08:7.

R9: board.md:3 C still restarting; CHG-166 APPLIED r09 changes:3 retry budget. config fail search-api r09 lines 2,9,13,19; 429 lines 1,5,11,20; B tls r09 auth 22,55 shipping 28,56

R10: board:3 D FALSE ALARM (drop D). board:4 DATA_BACKFILL CLOSED. CHG-175 log sampling. search-api config fail r10 line 1 (hits 1,4,7,8,20,30,50,54,60 mixed). auth tls r10 10,17; shipping 3,60
