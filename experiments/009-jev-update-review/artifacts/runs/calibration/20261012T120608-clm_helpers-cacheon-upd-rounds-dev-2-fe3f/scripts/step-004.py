import os,json
b='/task/fixtures/round-02/'
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l]
  print(f,len(e));[print(i,l[:150]) for i,l in e[:4]]
n='R1: inventory-svc DNS SERVFAIL rates.internal round-01/logs/inventory-svc.log:7; CHG-107 APPLIED retry budget=1 (round-01/changes.md:3). slow query WARN = noise.\nR2: board.md:3 Thread A DNS_RESOLUTION inventory-svc+checkout-api ongoing. changes.md:3 CHG-120 APPLIED search-api http.max_inflight=-1 (suspect BAD_CONFIG); changes.md:4 CHG-121 auth-svc no config.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))