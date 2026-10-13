import json,glob
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read())
for p in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(p)):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'dns lookup' not in l:print(p.split('/')[-1],i+1,l.strip()[:140])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. slow query WARNs everywhere (noise). inventory-svc DNS SERVFAIL host=rates.internal round-01/logs/inventory-svc.log:7,20,50,54,57,62,65. changes.md see s2 obs.'}]}
json.dump(c,open('/task/workspace/context.json','w'))