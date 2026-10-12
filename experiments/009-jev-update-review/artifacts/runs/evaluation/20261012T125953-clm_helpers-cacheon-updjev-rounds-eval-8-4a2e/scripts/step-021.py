import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+=' R7: board empty, no changes; inventory pool exhausted (round-07/logs/inventory-svc.log:1,9,19,22,25); notify-worker dns ERRORs (round-07/logs/notify-worker.log:7,18,31,34); no heap WARNs auth/pricing.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
import os;print(os.path.exists('/task/fixtures/round-07/changes.md'))