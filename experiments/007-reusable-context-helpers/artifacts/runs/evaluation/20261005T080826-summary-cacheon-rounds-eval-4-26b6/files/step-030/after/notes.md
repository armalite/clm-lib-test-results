R1: changes CHG-113 APPLIED search-api build 8.23.7 cache.ttl_s=-1 (round-01/changes.md:4); CHG-114 auth-svc no config (line5); CHG-107 PROPOSED.
R1 inventory-svc db pool exhausted lines 5,9,28,30,45,52 (only WARNs besides slow query noise). search-api no warns r1. board empty r1.
R2: board Thread A DB_POOL_EXHAUSTED inventory-svc + notify-worker ongoing (round-02/board.md:3). inv pool warns r2 lines 3-78; notify pool warns r2 lines 6-57. search-api no warns r2.

R3: Thread D opened CACHE_STAMPEDE auth-svc ongoing (round-03/board.md:3); auth-svc.log:1,15,16,18,24,43. Thread A continues: round-03 inventory-svc.log:12-76, notify-worker.log:4-71.

R4: Thread B opened round-04/board.md:3 suspected MEMORY_LEAK auth-svc; logs show 429 tax-provider in auth-svc & shipping-svc. VENDOR_TICKET OPEN board:4. Thread D storms auth-svc continue.

R5: Thread A mitigated round-05/board.md:3 (CHG-143 APPLIED round-05/changes.md:4); inventory/notify no WARNs. Thread B +shipping-svc board:4, cause still MEMORY_LEAK per board, logs 429 auth-svc.log:1,2,13,33,35,53,60 shipping-svc.log:9-77. Thread D CLOSED false alarm board:5. CHG-137 APPLIED TLS ticket rotation hourly (changes:3).

R6: board no updates. CHG-142 PROPOSED. 429s auth-svc.log:8-88 (8,23,34,36,41,45,61,68,70,71,79,86,88) shipping-svc.log:11-88 (11,23,27,29,32,46,47,58,62,67,78,83,88).

R7: board.md:3 thread B revised UPSTREAM_RATE_LIMIT. Logs JSON format now. 429s auth-svc.log:3-76, shipping-svc.log:15-50.

R8: board.md:3 A resolved; :4 B mitigated; :5 C opened search-api ongoing; :6 CAPACITY_REVIEW OPEN. search-api config validation errors log:24-84 (likely BAD_CONFIG_ROLLOUT CHG-113 r01/changes.md:4). B 429 auth:29,40 ship:41,42.

R9: board.md:3 C still ongoing; :4 DATA_BACKFILL OPEN; :5 RUNBOOK_UPDATE OPEN. CHG-163 irrelevant. search-api config errs log:1-48. B 429 auth:1,6 ship:43,59.

R10 read step29

R10: board.md:3 DATA_BACKFILL CLOSED. CHG-174 proposed. search-api cfg errs log:2-70; 429 auth:1,32 ship:8,27.
