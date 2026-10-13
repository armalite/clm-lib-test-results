import os,json,re
R='/task/fixtures/round-01/logs'
out=[]
for f in sorted(os.listdir(R)):
  for i,l in enumerate(open(os.path.join(R,f)),1):
    if not re.search(r'heartbeat|health ok|gc cycle|slow query|request ok',l):out.append(f'{f}:{i} {l.strip()[:130]}')
print('\n'.join(out[:40]))
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md:3 CHG-110 APPLIED retry budget=1; :4 CHG-113 APPLIED pricing-svc build 3.22.4 sets cache.ttl_s=-1 (suspicious BAD_CONFIG); :5 CHG-114 ledger-svc no config. Routine log noise: heartbeat/health/gc/slow query/request ok. Services: checkout-api pricing-svc ledger-svc inventory-svc search-api.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))