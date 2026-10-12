import os,json
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read()[:1500])
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l]
  print(f,len(e));[print(i,l[21:140]) for i,l in e[:5]]
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. slow query WARNs everywhere (noise). inventory-svc DNS SERVFAIL host=rates.internal at round-01/logs/inventory-svc.log:7'}]}
json.dump(c,open('/task/workspace/context.json','w'))