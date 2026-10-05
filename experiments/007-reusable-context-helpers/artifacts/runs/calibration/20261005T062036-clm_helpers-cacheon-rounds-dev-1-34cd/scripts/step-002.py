import json,glob
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read())
for p in glob.glob(b+'logs/*'):
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:print(p.split('/')[-1],i,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; logs only benign slow-query WARNs in all 5 services (notify-worker, checkout-api, auth-svc, payments-svc, search-api). changes.md 3 lines (see next obs).'}]}
json.dump(c,open('/task/workspace/context.json','w'))