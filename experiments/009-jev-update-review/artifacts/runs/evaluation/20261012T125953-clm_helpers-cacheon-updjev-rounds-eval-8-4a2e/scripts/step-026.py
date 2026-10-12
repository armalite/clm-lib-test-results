import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+=' R9 logs: inventory pool exhausted (round-09/logs/inventory-svc.log:11,24,36,49); payments-svc NEW db pool exhausted (round-09/logs/payments-svc.log:3,5,13,17,32,72) -> likely add payments-svc to Thread B; notify/auth/pricing clean.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')