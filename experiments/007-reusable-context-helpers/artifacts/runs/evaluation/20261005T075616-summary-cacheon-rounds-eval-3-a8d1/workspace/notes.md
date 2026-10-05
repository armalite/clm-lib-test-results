R1: ledger-svc CERT_EXPIRED sso.example.net round-01/logs/ledger-svc.log:14-72 ; slow query WARN is noise everywhere
R1 changes: CHG-113 APPLIED search-api http.max_inflight=-1 (possible BAD_CONFIG) round-01/changes.md:4 ; CHG-109 proposed only. No other errors R1.
R2: board Thread A CERT_EXPIRED ledger-svc+inventory-svc ongoing round-02/board.md:3 ; inventory-svc tls errors round-02/logs/inventory-svc.log:10-31 ; ledger round-02/logs/ledger-svc.log:20-57 ; CHG-117 proposed only
R3: board empty; CHG-125 APPLIED retry budget GET=1 (round-03/changes.md:3); cert errors continue inventory round-03/logs/inventory-svc.log:9-57, ledger round-03/logs/ledger-svc.log:23-61

R4: board A mitigated (board.md:3, CHG-136 changes.md:4 mitigation ledger). B opened checkout-api suspected UPSTREAM_RATE_LIMIT (board:4) but logs show heap usage high lines 18-90 -> likely MEMORY_LEAK. D opened DISK_PRESSURE search-api (board:5), logs search-api 12-62 disk high. FU open: CUSTOMER_COMMS, POSTMORTEM_DRAFT, CAPACITY_REVIEW (board 6-8).

R5: FU OPEN DATA_BACKFILL (round-05/board.md:3). checkout heap high lines 6-77; search disk high 14-76. No status changes.

R6: FU CLOSED CUSTOMER_COMMS (round-06/board.md:3). CHG-147 APPLIED TLS ticket rotation (r06 changes:3). checkout heap 17-66; search disk 6-74.

R7: A RESOLVED (round-07/board.md:3). Thread C opened search-api ongoing (board:4); logs search 17-58 config validation failed -> BAD_CONFIG_ROLLOUT (CHG-113 r01 changes:4). D closed false alarm (board:5). FU OPEN VENDOR_TICKET (board:6). checkout heap 6-67.

R8: board:3 B=MEMORY_LEAK confirmed (round-08/board.md:3). C ongoing (board:4). VENDOR_TICKET closed (board:5). CHG-160 proposed. Log format is now JSON. checkout heap at r08 checkout:9-69; payments-svc heap at r08 payments:13-62 (possibly thread B). search-api config failure at r08 search:2-76.

R9: board:3 Thread B adds payments-svc; board:4 B mitigated. CHG-164 noise. search config validation failed r09 search:5-58 (http.max_inflight=-1, 4.16.4). checkout heap r09 checkout:27-56, payments heap r09 payments:45-55.
