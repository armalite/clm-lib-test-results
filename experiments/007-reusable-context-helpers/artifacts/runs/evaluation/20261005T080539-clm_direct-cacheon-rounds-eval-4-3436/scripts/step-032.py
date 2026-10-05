import re
b='/task/fixtures/round-11/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['search-api','auth-svc','shipping-svc','inventory-svc','notify-worker']:
  L=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('429|ttl|pool|exhaust|memory',l)]
  print(s,L[:12])
import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))