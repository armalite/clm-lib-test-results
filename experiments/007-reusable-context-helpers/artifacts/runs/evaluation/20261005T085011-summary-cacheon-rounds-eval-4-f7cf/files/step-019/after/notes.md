R1: CHG-113 APPLIED search-api cache.ttl_s=-1 (round-01/changes.md:4); inventory db pool exhausted round-01/logs/inventory-svc.log:5,9
R2: Thread A DB_POOL_EXHAUSTED inventory-svc+notify-worker ongoing round-02/board.md:3; logs round-02/logs/inventory-svc.log:3, notify-worker.log:6

R3: board.md:3 Thread D CACHE_STAMPEDE auth-svc ongoing; refs round-03/logs/auth-svc.log:1-18. Thread A continues: round-03/logs/inventory-svc.log:12-30, round-03/logs/notify-worker.log:4-23.

R4: board.md:3 Thread B MEMORY_LEAK auth-svc ongoing (suspected; logs show 429 tax-provider in auth-svc.log:12-100 and shipping-svc.log:5-61 -> likely UPSTREAM_RATE_LIMIT). board.md:4 VENDOR_TICKET OPEN. Thread D stampede continues auth-svc.log:1-74. Thread A continues inventory-svc.log:3-84, notify-worker.log:11-73.

R5: board.md:3 Thread A mitigated (CHG-143 changes.md:4). board.md:4 Thread B +shipping-svc. board.md:5 Thread D false alarm. Logs: 429 tax-provider auth-svc.log:1-60, shipping-svc.log:9-77; no db pool errors.

R6 logs:
auth-svc.log 8 88 13 auth-svc upstream returned # upstream=tax-provider retry_after_s=#
shipping-svc.log 11 88 13 shipping-svc upstream returned # upstream=tax-provider retry_after_s=#

R6: board empty; CHG-142 PROPOSED. 429 continues auth 8-88 ship 11-88.
R7 board:
# Incident board: updates in round 07

- Thread B root cause revised: an upstream provider rejecting requests with 429 (UPSTREAM_RATE_LIMIT); this supersedes the earlier suspicion of MEMORY_LEAK.

R7 logs:
auth-svc.log 3 76 12 #","upstream":"tax-provider","retry_after_s":#}
shipping-svc.log 15 50 9 #","upstream":"tax-provider","retry_after_s":#}

R7: board.md:3 Thread B cause revised to UPSTREAM_RATE_LIMIT. Log fmt now JSON. 429 auth-svc.log:3-76, shipping-svc.log:15-50.
