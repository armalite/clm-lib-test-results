import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; only slow-query WARNs in all 5 svcs (shipping,checkout,auth,inventory,search) = noise baseline. changes.md: line3 CHG-113 APPLIED build 6.58.8 shipping-svc sets retry.backoff_ms=0 (suspicious BAD_CONFIG); line4 CHG-114 APPLIED search-api no config. Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read().splitlines()[:5])