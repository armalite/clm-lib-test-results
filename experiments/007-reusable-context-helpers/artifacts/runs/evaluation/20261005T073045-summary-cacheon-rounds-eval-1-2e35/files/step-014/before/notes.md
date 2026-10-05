R1: CHG-113 APPLIED round-01/changes.md:4 auth-svc build 4.51.3 sets cache.ttl_s=-1 (possible BAD_CONFIG_ROLLOUT). CHG-114 shipping no config. board empty. payments consumer lag stock-updates fluctuating (noise?). slow query WARNs everywhere = noise.

R2: board Thread A QUEUE_BACKLOG payments-svc+ledger-svc ongoing (round-02/board.md:3). CHG-117 APPLIED TLS rotation. lag topic=stock-updates in ledger+payments.

R3: board empty, CHG-124 PROPOSED only. lag continues ledger+payments.

R4: board.md:3 Thread B shipping-svc DB_POOL_EXHAUSTED ongoing (logs contradict: tls certificate_expired peer=sso.example.net round-04/logs/shipping-svc.log:1,2,4 -> real CERT_EXPIRED). board.md:4 follow-up OPEN RUNBOOK_UPDATE. CHG-133 dashboards irrelevant. lag continues.
