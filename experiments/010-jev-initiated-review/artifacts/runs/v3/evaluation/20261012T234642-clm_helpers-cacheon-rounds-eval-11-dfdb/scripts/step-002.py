import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; logs only routine slow-query WARNs (all 5 svcs: shipping-svc, checkout-api, pricing-svc, inventory-svc, search-api). Noise.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read()[:2000])