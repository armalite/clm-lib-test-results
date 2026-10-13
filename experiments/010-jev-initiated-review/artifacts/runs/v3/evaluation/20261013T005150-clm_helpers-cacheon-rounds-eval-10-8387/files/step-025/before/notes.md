R1: CHG-113 APPLIED shipping-svc retry.backoff_ms=0 (round-01/changes.md:3); CHG-114 search-api no cfg. R1 logs only slow-query WARN noise. board empty.
R2: board OPEN DATA_BACKFILL (round-02/board.md:3), POSTMORTEM_DRAFT (:4). auth-svc DNS SERVFAIL host=geo.internal round-02/logs/auth-svc.log:4-15,37-72. No incident thread on board yet.
R3: board A DNS_RESOLUTION auth-svc+checkout-api ongoing (round-03/board.md:3). B search-api suspected DB_POOL ongoing (:4) but logs show 429 upstream=fx-rates round-03/logs/search-api.log:16-62 -> likely UPSTREAM_RATE_LIMIT. DNS errs auth-svc.log:2-59, checkout-api.log:14-63. CHG-123 dashboards irrelevant.
R4: board empty. DNS continues auth-svc.log:3-57, checkout-api.log:2-64; 429 fx-rates search-api.log:4-90. inventory/shipping clean.
R5: board empty; CHG-140 log sampling irrelevant. auth-svc.log:1-60 n=8; checkout-api.log:2-66 n=11; search-api.log:5-64 n=10; inventory-svc ERR []; shipping-svc ERR []
R6: board A mitigated (round-06/board.md:3), CHG-150 APPLIED auth-svc mitigation (round-06/changes.md:3); B cause UPSTREAM_RATE_LIMIT (board.md:4); OPEN ALERT_TUNING (:5). auth-svc n=0 []-[] set(); checkout-api n=0 []-[] set(); search-api n=13 [6]-[69] {'upstream returned 429 '}; inventory-svc n=13 [3]-[69] {'upstream returned 429 '}; shipping-svc n=0 []-[] set()
R7: auth-svc n=0 []-[] set(); checkout-api n=0 []-[] set(); search-api n=9 [14]-[70] {'upstream returned 429 '}; inventory-svc n=7 [5]-[66] {'upstream returned 429 '}; shipping-svc n=0 []-[] set()
R7 board: B +inventory-svc (round-07/board.md:3)
R8: auth-svc n=0 []-[] set(); checkout-api n=0 []-[] set(); search-api n=2 [42]-[59] {'upstream returned 429 '}; inventory-svc n=2 [27]-[31] {'upstream returned 429 '}; shipping-svc n=0 []-[] set()
R8 board: A resolved (round-08/board.md:3); B mitigated (:4); CHG-157 PROPOSED irrelevant.
