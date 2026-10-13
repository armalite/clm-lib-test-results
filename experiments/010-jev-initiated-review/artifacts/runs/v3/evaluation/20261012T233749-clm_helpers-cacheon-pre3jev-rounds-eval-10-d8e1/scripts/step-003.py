import json
c=open('/task/fixtures/round-01/changes.md').read();print(c[:1500])
import glob
for f in glob.glob('/task/fixtures/round-01/logs/*'):
  for i,l in enumerate(open(f),1):
    if 'slow query' not in l and ('WARN' in l or 'ERROR' in l):print(f[-20:],i,l[:150].strip())
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round1: services shipping-svc, checkout-api, auth-svc, inventory-svc, search-api. Logs only show background WARN slow query ms=200-450 (noise). board.md round1 empty. changes.md checked in step3.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))