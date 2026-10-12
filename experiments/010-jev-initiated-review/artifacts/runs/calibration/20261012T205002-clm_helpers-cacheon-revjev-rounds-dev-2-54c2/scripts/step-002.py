import os,json,re
b='/task/fixtures/round-01/'
out=[]
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'WARN|ERROR|FATAL',l) and 'slow query' not in l: out.append(f'{f}:{i} {l.strip()[21:150]}')
print('\n'.join(out[:60]))
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-107 APPLIED retry budget GETs=1. Logs format: ts LEVEL svc msg k=v. Services: shipping-svc checkout-api auth-svc inventory-svc search-api. Noise: slow query WARNs, gc, heartbeat. inventory-svc.log:7 dns SERVFAIL rates.internal.'}]}
json.dump(c,open('/task/workspace/context.json','w'))