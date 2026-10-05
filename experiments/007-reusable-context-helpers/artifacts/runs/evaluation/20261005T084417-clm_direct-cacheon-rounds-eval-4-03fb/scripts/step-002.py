import json,re
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: changes.md:3 CHG-107 PROPOSED HPA search; :4 CHG-113 APPLIED search-api cache.ttl_s=-1 (bad config?); :5 CHG-114 auth-svc no config. board empty. slow query WARNs everywhere = noise. inventory-svc db pool exhausted lines 5,9,28,30,45,52 (round-01/logs/inventory-svc.log).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
L=open('/task/fixtures/round-01/logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:print(i,l[:150])