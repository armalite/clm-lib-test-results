import json,glob
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board.md empty. logs notify-worker,checkout-api,auth-svc,payments-svc,search-api. Only background WARN slow query ms~200-450 everywhere (noise). changes.md 3 lines (check).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read())
for p in glob.glob(b+'logs/*'):
  for i,l in enumerate(open(p),1):
    if 'slow query' not in l and ' INFO ' not in l:print(p.split('/')[-1],i,l.strip()[:140])