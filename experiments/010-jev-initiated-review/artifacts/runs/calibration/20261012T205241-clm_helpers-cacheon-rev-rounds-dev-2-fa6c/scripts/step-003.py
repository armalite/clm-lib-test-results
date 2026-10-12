import json
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: board empty. changes.md:3 CHG-107 APPLIED retry budget idempotent GETs=1. Slow query WARNs everywhere = noise. inventory-svc DNS_RESOLUTION host=rates.internal SERVFAIL round-01/logs/inventory-svc.log:7,20,50-90 (ongoing). shipping-svc log not fully checked for errors beyond line 30 (only slow queries seen).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import re
L=open('/task/fixtures/round-01/logs/shipping-svc.log').read().splitlines()
for i,l in enumerate(L,1):
  if re.search(r'ERROR|FATAL',l):print(i,l[:140])