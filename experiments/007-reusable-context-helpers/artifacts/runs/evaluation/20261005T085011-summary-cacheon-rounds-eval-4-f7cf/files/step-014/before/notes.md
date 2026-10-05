R1: CHG-113 APPLIED search-api cache.ttl_s=-1 (round-01/changes.md:4); inventory db pool exhausted round-01/logs/inventory-svc.log:5,9
R2: Thread A DB_POOL_EXHAUSTED inventory-svc+notify-worker ongoing round-02/board.md:3; logs round-02/logs/inventory-svc.log:3, notify-worker.log:6

R3: board.md:3 Thread D CACHE_STAMPEDE auth-svc ongoing; refs round-03/logs/auth-svc.log:1-18. Thread A continues: round-03/logs/inventory-svc.log:12-30, round-03/logs/notify-worker.log:4-23.

R4: board.md:3 Thread B MEMORY_LEAK auth-svc ongoing (suspected; logs show 429 tax-provider in auth-svc.log:12-100 and shipping-svc.log:5-61 -> likely UPSTREAM_RATE_LIMIT). board.md:4 VENDOR_TICKET OPEN. Thread D stampede continues auth-svc.log:1-74. Thread A continues inventory-svc.log:3-84, notify-worker.log:11-73.
