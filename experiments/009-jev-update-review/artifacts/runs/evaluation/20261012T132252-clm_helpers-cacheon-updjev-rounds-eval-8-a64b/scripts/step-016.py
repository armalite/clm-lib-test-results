import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n3','n4','n5','n6')]
for e in c['entries']:
  if e['id']=='n6': e['body']+=' R6 logs: notify-worker dns lookup failed ERROR (round-06/logs/notify-worker.log:7); inventory pool exhausted (round-06/logs/inventory-svc.log:7,9). Next: advance to R7.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')