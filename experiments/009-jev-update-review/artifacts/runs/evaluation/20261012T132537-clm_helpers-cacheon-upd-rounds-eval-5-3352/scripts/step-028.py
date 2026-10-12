import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+='\nR11 logs: auth cert (round-11/logs/auth-svc.log:11,21); ledger cert (round-11/logs/ledger-svc.log:7,32); checkout config invalid (round-11/logs/checkout-api.log:3,17,24). Next: advance R12.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')