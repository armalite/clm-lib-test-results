import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
r='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
import os
for s in os.listdir(r+'logs'):
  L=[i for i,l in enumerate(open(r+'logs/'+s),1) if any(k in l for k in ['ERROR','429','max_inflight','cert','SERVFAIL','CERT'])]
  print(s,L[:15])