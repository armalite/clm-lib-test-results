import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
import os
for s in os.listdir(b+'logs'):
  L=open(b+'logs/'+s).read().splitlines()
  hits=[i for i,l in enumerate(L,1) if re.search(r'ERROR|lag|cert|config|429|pool',l,re.I)]
  print(s,len(hits),hits[:1],hits[-1:] if hits else '', L[hits[0]-1][:150] if hits else '')