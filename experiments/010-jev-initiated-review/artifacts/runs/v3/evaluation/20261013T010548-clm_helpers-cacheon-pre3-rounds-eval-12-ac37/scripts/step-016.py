import json
b='''R1: changes.md:3 CHG-110 APPLIED retry budget; changes.md:4 CHG-113 APPLIED build 3.22.4 pricing-svc sets cache.ttl_s=-1 (possible BAD_CONFIG_ROLLOUT); changes.md:5 CHG-114 APPLIED 3.22.4 ledger-svc no config. Services: checkout-api, pricing-svc, ledger-svc, inventory-svc, search-api. R1 logs noise only.
R2: board.md:3 OPEN CAPACITY_REVIEW. changes.md:3 CHG-115 APPLIED retry budget. search-api.log 11-57 cert_expired peer=sso.example.net.
R3: board.md:3 Thread A CERT_EXPIRED search-api + inventory-svc ongoing. board.md:4 OPEN RUNBOOK_UPDATE; board.md:5 OPEN POSTMORTEM_DRAFT. changes.md:3 CHG-126 noise. Errors: inventory-svc.log:1-75, search-api.log:9-78 cert_expired.
R4: board.md:3 Thread B ledger-svc QUEUE_BACKLOG ongoing (suspected). changes.md:3 CHG-129 PROPOSED (ignore). Logs: ledger-svc.log:2 429 upstream=tax-provider (UPSTREAM_RATE_LIMIT? check vs queue); cert_expired continues inventory-svc.log:3, search-api.log:89.
Next: advance to round 5.'''
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))