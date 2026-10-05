import re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  h=[(i,l[:140]) for i,l in enumerate(L,1) if re.search(r'ERROR|WARN|exhaust|inflight|429|cert|dns|disk|memory|lag',l,re.I)]
  print(f,len(h))
  for x in h[:5]:print(' ',x)