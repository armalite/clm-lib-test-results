import json,re
b='/task/fixtures/round-09/'
for f in['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  seen=set()
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|429|fail|exhaust|invalid',l):
      k=re.sub(r'\d','',l)[:80]
      if k in seen:continue
      seen.add(k);print(f,i,l.rstrip()[:160])
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open(p,'w'))