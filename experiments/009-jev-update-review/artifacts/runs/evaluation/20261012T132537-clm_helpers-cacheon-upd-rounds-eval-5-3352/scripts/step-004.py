import json,os
n='R1: changes.md:3 CHG-110 APPLIED TLS rotation; :4 CHG-113 APPLIED checkout-api db.pool_max=-4 (BAD_CONFIG cand); search-api disk 91-97% (round-01/logs/search-api.log:4,12,38,48). Slow-query WARN = noise.\nR2: board.md:3 Thread A DISK_PRESSURE search-api+shipping-svc ongoing; :4 OPEN CUSTOMER_COMMS. changes:3 CHG-117 dashboards (irrelevant).'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-02/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'disk usage' not in l:print(f,i,l.rstrip()[:130])
