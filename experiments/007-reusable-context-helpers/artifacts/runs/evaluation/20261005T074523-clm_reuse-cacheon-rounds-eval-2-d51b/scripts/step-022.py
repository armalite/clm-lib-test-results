import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+s),1) if not re.search('slow query|INFO|/v1/health',l)]
  print(s,len(L))
  for i,l in L[:3]+L[-1:]:print(' ',i,l[:150])