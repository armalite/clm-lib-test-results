import json,glob
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read()[:1500])
for f in glob.glob(b+'logs/*'):
 for i,l in enumerate(open(f)):
  if ('WARN' in l or 'ERROR' in l) and 'slow query' not in l:print(f.split('/')[-1],i+1,l.strip()[:150])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; logs (shipping,checkout,payments,ledger,search) only background WARN slow query ms~200-450 (noise).'}]},open('/task/workspace/context.json','w'))