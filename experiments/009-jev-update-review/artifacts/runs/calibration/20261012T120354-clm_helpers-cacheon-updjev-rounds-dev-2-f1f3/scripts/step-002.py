import json
L=open('/task/fixtures/round-01/logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'ERROR' in l: print(i,l[:140])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md:3 CHG-107 APPLIED retry budget idempotent GETs=1. slow query WARNs everywhere = noise. inventory-svc DNS SERVFAIL host=rates.internal (round-01/logs/inventory-svc.log:7,20,50,54,57,62,65,85-90) -> candidate DNS_RESOLUTION, not on board yet.'}]}
json.dump(c,open('/task/workspace/context.json','w'))