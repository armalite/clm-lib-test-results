import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
b=c['entries'][0]['body'].replace('\nNEXT: check R11 logs then advance R12.','')
b+='\nR11 logs: auth-svc tls fail bank-api (round-11/logs/auth-svc.log:11,21); ledger-svc (round-11/logs/ledger-svc.log:7,32); checkout-api config validation failed continues (round-11/logs/checkout-api.log:3,17,64); search/shipping clean.\nNEXT: advance R12.'
c['entries'][0]['body']=b
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')