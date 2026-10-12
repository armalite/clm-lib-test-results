import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
for e in c['entries']:
  if e['id']=='n7':e['body']='R7: board.md:3 Thread B cause=CERT_EXPIRED. board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing. Logs confirm 429 tax-provider round-07/logs/search-api.log:4,5,20,22,25,47,64,66 (no max_inflight errors; CHG-120 seems no effect). R7 auth/shipping cert errors continue. Next: advance to R8.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')