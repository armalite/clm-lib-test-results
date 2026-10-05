import json,glob
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read())
for p in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: print(p.split('/')[-1],i,l.strip()[20:130])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. slow query WARNs everywhere = noise. inventory-svc db pool exhausted WARN r01 inventory-svc.log:5,9,28,30,45,52.'}]}
json.dump(c,open('/task/workspace/context.json','w'))