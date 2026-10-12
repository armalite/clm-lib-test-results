import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes round-01/changes.md: CHG-113 APPLIED build 7.35.5 ledger-svc sets db.pool_max=0 (line ~3); CHG-114 APPLIED checkout-api no config. Logs: only routine WARN slow query noise in all services (checkout-api, ledger-svc, payments-svc, search-api, shipping-svc). Scan method: grep ERROR/WARN excluding "slow query".'}]}
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-01/changes.md'),1):print(i,l.strip())