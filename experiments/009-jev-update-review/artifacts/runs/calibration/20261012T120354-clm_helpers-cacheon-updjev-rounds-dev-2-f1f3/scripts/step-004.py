import json
for s in ['search-api','auth-svc','checkout-api']:
  L=open(f'/task/fixtures/round-02/logs/{s}.log').read().splitlines()
  for i,l in enumerate(L,1):
    if 'ERROR' in l: print(s,i,l[:120])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: CHG-107 APPLIED (round-01/changes.md:3) retry budget GETs=1. slow query WARNs = noise. inventory-svc DNS SERVFAIL rates.internal round-01/logs/inventory-svc.log:7,20,50,85-90.'},{'id':'n2','role':'note','body':'R2: board.md:3 Thread A DNS_RESOLUTION inventory-svc+checkout-api ongoing. changes.md:3 CHG-120 APPLIED search-api http.max_inflight=-1 (suspect BAD_CONFIG_ROLLOUT). changes.md:4 CHG-121 auth-svc no config.'}]}
json.dump(c,open('/task/workspace/context.json','w'))