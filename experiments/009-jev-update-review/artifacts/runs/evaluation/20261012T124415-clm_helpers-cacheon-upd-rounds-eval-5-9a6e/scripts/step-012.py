import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=' R4 logs: auth-svc certificate_expired peer=bank-api round-04/logs/auth-svc.log:3,5,7,20,40,42,55; slow query WARNs everywhere = noise. Next: advance R5.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')