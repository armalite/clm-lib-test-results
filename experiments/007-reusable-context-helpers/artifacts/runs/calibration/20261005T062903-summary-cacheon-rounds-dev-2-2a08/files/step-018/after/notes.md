R1: CHG-107 APPLIED retry budget GET=1 (round-01/changes.md:3). inventory-svc DNS SERVFAIL rates.internal lines 7-90 of round-01/logs/inventory-svc.log. Board empty. slow query WARN noise everywhere.

R2: DNS errors checkout-api.log 8,24,29,38,46,59; inventory-svc.log 8-74 (8,12,14,19,20,37,42,53,60,70,74). search-api no errors yet after CHG-120 (changes.md:3). Thread A DNS ongoing board.md:3.

R3: board.md:3 Thread B auth-svc suspected DB_POOL (board), but logs show CERT_EXPIRED peer=sso.example.net round-03/logs/auth-svc.log:6-26. CHG-126 PROPOSED (ignore). DNS continues round-03/logs/checkout-api.log:33-54, inventory-svc.log:3-41.

R4: board empty. CERT_EXPIRED auth-svc round-04/logs/auth-svc.log:6-77 and NEW shipping-svc round-04/logs/shipping-svc.log:3-66 (peer sso.example.net). DNS continues checkout-api.log:1-71, inventory-svc.log:32-75. search-api 0 errors.

R5: board.md:3 Thread A mitigated after CHG-143 (round-05/changes.md:3). board.md:4 Thread B adds shipping-svc. board.md:5-6 OPEN VENDOR_TICKET, ALERT_TUNING. CERT errors auth-svc.log:2-64, shipping-svc.log:9-65. checkout/inventory 0 errors.

R6: board.md:3 OPEN RUNBOOK_UPDATE. CHG-144 log sampling (noise). Log format now JSON. CERT errors auth-svc.log:4-79, shipping-svc.log:1-64. others 0 errors.
