R1: CHG-113 APPLIED round-01/changes.md:4 auth-svc build 4.51.3 sets cache.ttl_s=-1 (possible BAD_CONFIG_ROLLOUT). CHG-114 shipping no config. board empty. payments consumer lag stock-updates fluctuating (noise?). slow query WARNs everywhere = noise.

R2: board Thread A QUEUE_BACKLOG payments-svc+ledger-svc ongoing (round-02/board.md:3). CHG-117 APPLIED TLS rotation. lag topic=stock-updates in ledger+payments.

R3: board empty, CHG-124 PROPOSED only. lag continues ledger+payments.

R4: board.md:3 Thread B shipping-svc DB_POOL_EXHAUSTED ongoing (logs contradict: tls certificate_expired peer=sso.example.net round-04/logs/shipping-svc.log:1,2,4 -> real CERT_EXPIRED). board.md:4 follow-up OPEN RUNBOOK_UPDATE. CHG-133 dashboards irrelevant. lag continues.

R5: board.md:3 Thread A mitigated; changes.md:3 CHG-143 APPLIED mitigation payments. lag gone. cert errors now also search-api: search-api:[14, 35, 50, 51, 79, 81] shipping-svc:[1, 2, 18, 27, 52, 54, 56, 59]

R5: search-api cert lines round-05/logs/search-api.log:14,35,50; shipping round-05:1,2,18. R6: board.md:3 Thread B adds search-api (cause/status unchanged). cert search-api round-06:11,14,25; shipping round-06:4,35,40. no lag.

R7: board.md:3 POSTMORTEM_DRAFT OPEN, :4 DATA_BACKFILL OPEN. CHG-154 applied (retry, irrelevant). cert search-api round-07:8,10,11; shipping round-07:3,16,21. no lag.

R8 read step22
