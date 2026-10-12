import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR6 logs: checkout-api db pool exhausted (round-06/logs/checkout-api.log:8,25,27,72,76); auth cert_expired continues (round-06/logs/auth-svc.log:2,81).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')