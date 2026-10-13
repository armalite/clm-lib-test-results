import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|FATAL|429|SERVFAIL|pool|OOM|disk|cert',l,re.I)]
  print(f,len(hits))
  for i,l in hits[:3]+hits[-1:]:print(' ',i,l[:150])