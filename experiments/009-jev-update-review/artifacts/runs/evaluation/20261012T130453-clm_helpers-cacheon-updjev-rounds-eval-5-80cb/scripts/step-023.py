import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n8': x['body']='R8: board.md:3 claims Thread D false alarm (synthetic monitor). R8 logs: checkout-api clean (no pool errors) - maybe it stopped; R6/R7 logs did show real exhaustion + CHG-113 pool_max=-4; keep watching. auth-svc cert_expired continues (round-08/logs/auth-svc.log:6-85); others clean. changes.md:3 CHG-156 PROPOSED (ignore). R8 done; next: advance.'
json.dump(c,open('/task/workspace/context.json','w'))