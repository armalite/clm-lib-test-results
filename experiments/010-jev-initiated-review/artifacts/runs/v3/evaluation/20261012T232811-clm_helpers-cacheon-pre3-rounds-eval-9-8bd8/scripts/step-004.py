import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round1 summary: files board.md (empty), changes.md: CHG-108 APPLIED TLS session ticket rotation hourly (round-01/changes.md:3). Logs: notify-worker, shipping-svc, ledger-svc, inventory-svc, search-api. Only background WARN slow query ms~200-440 across all services; no incident yet. Log format: "<ts> LEVEL  <svc> msg k=v".'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read().splitlines())