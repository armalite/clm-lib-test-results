import json,re
L=open('/task/fixtures/round-01/logs/shipping-svc.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'ERROR' in l:print(i,l[:150])
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: board empty. changes.md:3 CHG-107 APPLIED retry budget GETs=1. slow query WARNs everywhere = noise. inventory-svc DNS SERVFAIL host=rates.internal round-01/logs/inventory-svc.log:7,20,50-90 (DNS_RESOLUTION candidate). Workflow: per round print board, changes, ERROR lines (skip slow query), then update this note and drop old entries.'}]}
json.dump(c,open('/task/workspace/context.json','w'))