import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=' R3 logs: auth-svc tls certificate_expired peer=bank-api round-03/logs/auth-svc.log:1,16,21 (contradicts board MEMORY_LEAK? check mem lines later); disk still 96-98% search-api.log:16,77, shipping-svc.log:80. Next: advance R4.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')