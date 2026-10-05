R1: ledger-svc CERT_EXPIRED sso.example.net round-01/logs/ledger-svc.log:14-72 (ERROR lines 14,15,21,39,40,55,59,72). slow query WARNs are noise.
R1 changes: CHG-113 APPLIED search-api http.max_inflight=-1 (round-01/changes.md:4); CHG-109 PROPOSED; CHG-114 APPLIED checkout no cfg.

Round2: board.md:3 Thread A CERT_EXPIRED ledger-svc+inventory-svc ongoing. CHG-117 PROPOSED. inventory-svc cert errors lines 10-13+ (13 total), ledger-svc 20,23,28,43 (8). No search-api errors yet.

R3: board empty. CHG-125 APPLIED retry budget GET=1 (round-03/changes.md:3?). Cert errors continue: inventory r3 lines 9,13,18 (9 errs); ledger r3 23,24,32 (10 errs). No search errors.

R4: board A mitigated (round-04/board.md:3); B checkout UPSTREAM_RATE_LIMIT ongoing (b:4); D search DISK_PRESSURE ongoing (b:5); FU open CUSTOMER_COMMS, POSTMORTEM_DRAFT, CAPACITY_REVIEW (b:6-8). CHG-136 APPLIED A mitigation ledger (round-04/changes.md:4). checkout heap warns 18-20; search disk 12,13,21.

R4 logs: checkout-api shows heap usage high (MEMORY_LEAK?), not 429: round-04/logs/checkout-api.log:18-20,35,38,41,42,44,60,86,88,90. search disk: round-04/logs/search-api.log:12,13,21,38,54,62. Board B claims UPSTREAM_RATE_LIMIT; logs disagree.
