import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round1: board empty. changes.md:3 CHG-108 APPLIED TLS session ticket rotation hourly (possible later CERT link). Logs (notify-worker, shipping-svc, ledger-svc, inventory-svc, search-api) only baseline WARN slow query ms 200-450; no incidents yet. Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read().splitlines())