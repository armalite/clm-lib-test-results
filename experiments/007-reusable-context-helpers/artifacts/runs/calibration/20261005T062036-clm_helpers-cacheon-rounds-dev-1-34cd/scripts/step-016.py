import json,re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1): print(f,i,l)
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  h=[(i,l[:110]) for i,l in enumerate(L,1) if re.search('ERROR|WARN|429|pool|cert|dns|lag|memory|disk|config|inflight',l,re.I)]
  print(f,len(h))
  for x in h[:5]: print(' ',x)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))