import json,re
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open(p,'w'))
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
import os
for f in sorted(os.listdir(b+'logs')):
  L=[i for i,l in enumerate(open(b+'logs/'+f),1) if re.search(r'error|429|fail|ERROR',l,re.I) and 'slow query' not in l]
  print(f,len(L),L[:3],L[-1:] if L else '')