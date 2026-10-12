import os,json,glob
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if ' INFO ' not in l and 'slow query' not in l: print(p.split('/')[-1],i,l.strip()[:140])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes CHG-107 APPLIED retry budget GETs=1. services: shipping-svc checkout-api auth-svc inventory-svc search-api. log fmt: ts LEVEL svc msg k=v. slow query WARNs are noise.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))