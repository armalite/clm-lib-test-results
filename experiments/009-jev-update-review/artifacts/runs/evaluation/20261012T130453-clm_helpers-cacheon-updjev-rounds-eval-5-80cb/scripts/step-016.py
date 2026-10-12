import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n6': x['body']+=' R6 logs: checkout-api WARN db pool exhausted (round-06/logs/checkout-api.log:8-76, in_use varies 10-20); auth-svc cert_expired continues (round-06/logs/auth-svc.log:2-81). R6 done; next: advance.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')