import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l) for i,l in enumerate(open(b+'logs/'+f),1) if ('ERROR' in l or 'WARN' in l) and 'slow' not in l]
  if L:print(f,len(L),L[0][0],L[-1][0],L[0][1][:160])