import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  r=[]
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'INFO' not in l and 'slow' not in l:r.append(i)
  print(f,r[:15])
  if r:print(open(b+'logs/'+f).readlines()[r[0]-1][:200])