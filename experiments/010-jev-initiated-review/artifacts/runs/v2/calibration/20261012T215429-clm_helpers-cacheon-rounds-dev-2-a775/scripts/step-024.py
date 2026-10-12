import json,re
b='/task/fixtures/round-08/'
for i,l in enumerate(open(b+'board.md').read().splitlines(),1):print(i,l)
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines();e=[(i,l) for i,l in enumerate(L,1) if ('ERROR' in l or 'error' in l.lower()) and 'slow query' not in l]
  print(f,len(e),[i for i,_ in e][:8]);
  if e:print(e[0][1][:180])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))