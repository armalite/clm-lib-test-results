import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
for e in c['entries']:
  if e['id']=='n10':e['body']+=' R10 search-api cfg max_inflight=-1 round-10/logs/search-api.log:1,4,7,8,20; CERT auth round-10/logs/auth-svc.log:10,17; shipping round-10/logs/shipping-svc.log:3,60.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')