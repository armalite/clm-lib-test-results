import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(b+'logs/'+s),1) if 'slow query' not in l and 'INFO' not in l]
  print(s,len(ls))
  for i,l in ls[:3]+ls[-1:]:print(' ',i,l[:150])