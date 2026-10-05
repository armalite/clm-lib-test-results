R1: ledger-svc CERT_EXPIRED sso.example.net round-01/logs/ledger-svc.log:14-72 ; slow query WARN is noise everywhere
R1 changes: CHG-113 APPLIED search-api http.max_inflight=-1 (possible BAD_CONFIG) round-01/changes.md:4 ; CHG-109 proposed only. No other errors R1.
R2: board Thread A CERT_EXPIRED ledger-svc+inventory-svc ongoing round-02/board.md:3 ; inventory-svc tls errors round-02/logs/inventory-svc.log:10-31 ; ledger round-02/logs/ledger-svc.log:20-57 ; CHG-117 proposed only
R3: board empty; CHG-125 APPLIED retry budget GET=1 (round-03/changes.md:3); cert errors continue inventory round-03/logs/inventory-svc.log:9-57, ledger round-03/logs/ledger-svc.log:23-61
