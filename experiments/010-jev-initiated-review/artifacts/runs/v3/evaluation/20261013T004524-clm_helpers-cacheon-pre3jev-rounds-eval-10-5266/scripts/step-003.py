import json
print(open('/task/fixtures/round-01/changes.md').read()[:1500])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round1: board empty; all 5 services (shipping-svc, checkout-api, auth-svc, inventory-svc, search-api) only baseline WARN slow query ms~200-450, no ERRORs. Log format: ts LEVEL svc msg. changes.md content printed in step 3 obs.'}]}
json.dump(c,open('/task/workspace/context.json','w'))