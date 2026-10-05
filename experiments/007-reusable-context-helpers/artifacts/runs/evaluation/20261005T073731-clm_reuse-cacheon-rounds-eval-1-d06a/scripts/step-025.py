import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  c={}
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'INFO' in l or 'slow' in l: continue
    k=re.sub(r'\d+','#',l)[:90]
    c.setdefault(k,[]).append(i)
  for k,v in c.items():print(f,v[0],v[-1],len(v),k.strip())