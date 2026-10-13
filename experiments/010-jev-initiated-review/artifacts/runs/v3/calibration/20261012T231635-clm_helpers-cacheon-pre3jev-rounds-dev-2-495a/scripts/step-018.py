import re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+s).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|WARN|error|fail',l) and 'slow' not in l.lower()]
  print(s,len(hits))
  for i,l in hits[:3]+hits[-1:]:print(' ',i,l[:150])