import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n3','n4')]
c['entries'][-1]['body']+=' R4 logs: inventory-svc db pool exhausted WARNs (round-04/logs/inventory-svc.log:19-37,57,80) -> possible DB_POOL_EXHAUSTED inventory-svc (vs board CERT suspicion).'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')