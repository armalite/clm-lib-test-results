import re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'ERROR|429|SERVFAIL|pool|OOM|disk|expired|lag',l,re.I) and 'slow query' not in l]
  print(f,len(hits))
  for i,l in hits[:3]+hits[-1:]:print(' ',i,l[:150])