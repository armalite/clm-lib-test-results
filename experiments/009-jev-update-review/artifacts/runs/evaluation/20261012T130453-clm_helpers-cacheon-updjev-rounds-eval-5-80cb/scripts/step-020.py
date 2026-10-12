import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n7': x['body']+=' R7 logs: auth-svc cert_expired continues (round-07/logs/auth-svc.log:12-79); checkout-api db pool exhausted in_use 16/16 (round-07/logs/checkout-api.log:2-66); others clean. R7 done; next: advance.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')