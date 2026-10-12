import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n3','n4','n5')]
for e in c['entries']:
  if e['id']=='n5': e['body']+=' R5 logs: auth/pricing heap high WARNs (round-05/logs/auth-svc.log:6, round-05/logs/pricing-svc.log:3); inventory pool exhausted (round-05/logs/inventory-svc.log:6). R5 board empty. Next: advance to R6.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')