import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']+=' R5 logs: same pattern (auth/pricing heap WARNs, inventory pool exhausted round-05/logs/inventory-svc.log:6,17); board r5 empty. Next: advance to r6.'
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')