import json,re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in os.listdir(b+'logs'):
  L=[i for i,l in enumerate(open(b+'logs/'+s),1) if re.search(r'429|max_inflight|CERT|certificate|SERVFAIL|ERROR',l)]
  print(s,L[:15])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))