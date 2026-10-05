R1: CHG-113 APPLIED round-01/changes.md:4 auth-svc build 4.51.3 sets cache.ttl_s=-1 (possible BAD_CONFIG_ROLLOUT). CHG-114 shipping no config. board empty. payments consumer lag stock-updates fluctuating (noise?). slow query WARNs everywhere = noise.

R2: board Thread A QUEUE_BACKLOG payments-svc+ledger-svc ongoing (round-02/board.md:3). CHG-117 APPLIED TLS rotation. lag topic=stock-updates in ledger+payments.

R3: board empty, CHG-124 PROPOSED only. lag continues ledger+payments.
