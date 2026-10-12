import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR6 logs: checkout-api db pool exhausted WARNs in_use 16/16,12/12,10/10 (round-06/logs/checkout-api.log:8,25,27,34) pool shrinking; auth-svc cert_expired continues (round-06/logs/auth-svc.log:2,31). Next: advance to R7.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')