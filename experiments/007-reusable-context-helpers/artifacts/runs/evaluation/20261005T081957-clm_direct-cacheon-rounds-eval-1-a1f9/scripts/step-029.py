import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in os.listdir(b+'logs'):
  L=[(i,l) for i,l in enumerate(open(b+'logs/'+s),1) if 'ERROR' in l or 'error' in l]
  print(s,len(L),[i for i,_ in L][:8]);
  if L:print(L[0][1][:200])