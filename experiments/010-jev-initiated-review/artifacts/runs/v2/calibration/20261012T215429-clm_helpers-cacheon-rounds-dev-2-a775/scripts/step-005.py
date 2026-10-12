import json
R='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(R+f).read().splitlines(),1):print(f,i,l[:200])
import os
for s in sorted(os.listdir(R+'logs')):
  for i,l in enumerate(open(R+'logs/'+s).read().splitlines(),1):
    if ('ERROR' in l or 'error' in l.lower()) and 'slow query' not in l:print(s,i,l[:140])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))