R1: changes CHG-113 APPLIED search-api build 8.23.7 cache.ttl_s=-1 (round-01/changes.md:4); CHG-114 auth-svc no config (line5); CHG-107 PROPOSED.
R1 inventory-svc db pool exhausted lines 5,9,28,30,45,52 (only WARNs besides slow query noise). search-api no warns r1. board empty r1.
R2: board Thread A DB_POOL_EXHAUSTED inventory-svc + notify-worker ongoing (round-02/board.md:3). inv pool warns r2 lines 3-78; notify pool warns r2 lines 6-57. search-api no warns r2.
