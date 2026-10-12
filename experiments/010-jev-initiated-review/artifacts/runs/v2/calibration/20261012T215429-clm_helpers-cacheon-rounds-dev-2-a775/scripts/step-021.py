import json
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
import collections
for l in open('/task/workspace/spill/s20.obs.txt'):
  if 'board' in l: continue
import os
for f in sorted(os.listdir(b+'logs')):
  hits=[(i,l) for i,l in enumerate(open(b+'logs/'+f),1) if 'ERROR' in l and 'slow query' not in l]
  print(f,len(hits),[i for i,_ in hits][:6],hits[0][1].strip()[:110] if hits else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))