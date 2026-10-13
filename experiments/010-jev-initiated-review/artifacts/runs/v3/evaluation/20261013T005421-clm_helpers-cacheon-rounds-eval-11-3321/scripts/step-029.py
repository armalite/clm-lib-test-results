import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+s),1) if 'slow query' not in l and 'INFO' not in l and 'info' not in l.lower()[:40]]
  print(s,len(L))
  for i,l in L[:2]+L[-1:]:print(' ',i,l[:150])