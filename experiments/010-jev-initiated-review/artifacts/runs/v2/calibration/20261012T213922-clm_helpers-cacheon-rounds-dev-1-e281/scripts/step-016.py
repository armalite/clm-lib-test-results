import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  hits=[]
  for i,l in enumerate(open(b+'logs/'+s),1):
    if 'slow query' in l.lower() or 'INFO' in l: continue
    hits.append((i,l.rstrip()[:110]))
  print(s,len(hits))
  for h in hits[:4]:print(' ',h)
  print('  lines',[h[0] for h in hits])