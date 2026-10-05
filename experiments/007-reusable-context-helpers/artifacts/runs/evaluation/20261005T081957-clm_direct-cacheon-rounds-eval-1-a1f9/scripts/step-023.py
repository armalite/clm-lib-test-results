import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  n=0
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ('ERROR' in l or 'error' in l.lower() or 'lag' in l) and 'slow query' not in l:
      n+=1
      if n<=4:print(f,i,l.rstrip()[:200])
  print(f,'count',n)