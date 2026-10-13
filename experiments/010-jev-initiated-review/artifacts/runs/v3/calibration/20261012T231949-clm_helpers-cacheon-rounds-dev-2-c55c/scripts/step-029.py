import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
for e in c['entries']:
  if e['id']=='n9':e['body']='R9: board Thread C note pods restarting (round-09/board.md:3). CHG-166 noise. search-api 429 round-09/logs/search-api.log:1,5,11,20; cfg max_inflight=-1 lines 2,9,13,19,25. CERT continues auth round-09/logs/auth-svc.log:22,55; shipping round-09/logs/shipping-svc.log:28,56. Next: advance to R10.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')