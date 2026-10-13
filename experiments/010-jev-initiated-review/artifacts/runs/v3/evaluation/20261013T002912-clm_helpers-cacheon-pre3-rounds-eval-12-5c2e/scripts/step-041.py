import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  hits=[(i,l.strip()[:110]) for i,l in enumerate(open(b+'logs/'+f),1) if re.search('ERROR|429|certificate|validation',l)]
  print(f,len(hits),hits[:3])