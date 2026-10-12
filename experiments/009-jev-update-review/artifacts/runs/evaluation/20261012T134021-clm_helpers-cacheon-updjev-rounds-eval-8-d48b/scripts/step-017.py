import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+=' R7 logs: inventory-svc pool exhausted (round-07/logs/inventory-svc.log:1-57); notify-worker dns failed geo.internal (round-07/logs/notify-worker.log:7-41).'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
import os
for f in ['board.md','changes.md']:
  p='/task/fixtures/round-07/'+f
  if os.path.exists(p):
    for i,l in enumerate(open(p)): print(f,i+1,l.rstrip()[:200])