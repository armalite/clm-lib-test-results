import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+=' R8 board: Thread A RESOLVED (round-08/board.md:3); Thread B cause revised DB_POOL_EXHAUSTED inventory-svc (round-08/board.md:4); Thread D closed FALSE ALARM (round-08/board.md:5) -> drop DNS incident. Still open question: CHG-113 notify-worker pool_max=-4 not on board.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
import re
for s in ['inventory-svc','notify-worker']:
  for i,l in enumerate(open(f'/task/fixtures/round-08/logs/{s}.log')):
    if re.search(r'ERROR|WARN|pool|config|exhaust',l,re.I): print(s,i+1,l.rstrip()[:150])