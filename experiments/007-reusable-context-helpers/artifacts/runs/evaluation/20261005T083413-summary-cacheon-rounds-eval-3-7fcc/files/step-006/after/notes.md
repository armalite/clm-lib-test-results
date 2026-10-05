R1: ledger-svc CERT_EXPIRED sso.example.net round-01/logs/ledger-svc.log:14-72 (ERROR lines 14,15,21,39,40,55,59,72). slow query WARNs are noise.
R1 changes: CHG-113 APPLIED search-api http.max_inflight=-1 (round-01/changes.md:4); CHG-109 PROPOSED; CHG-114 APPLIED checkout no cfg.

Round2: board.md:3 Thread A CERT_EXPIRED ledger-svc+inventory-svc ongoing. CHG-117 PROPOSED. inventory-svc cert errors lines 10-13+ (13 total), ledger-svc 20,23,28,43 (8). No search-api errors yet.
