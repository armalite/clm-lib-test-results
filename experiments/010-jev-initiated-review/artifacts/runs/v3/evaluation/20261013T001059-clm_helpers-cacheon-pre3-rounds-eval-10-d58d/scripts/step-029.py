import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[i for i,l in enumerate(L,1) if re.search('error|ERROR|429|fail|WARN',l)]
  print(f,len(hits),hits[:3],hits[-1:] if hits else '')
  if hits:print(' ',L[hits[0]-1][:160])