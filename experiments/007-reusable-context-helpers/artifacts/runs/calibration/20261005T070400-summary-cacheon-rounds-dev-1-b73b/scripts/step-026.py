import json,re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip(): print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=[(i,l) for i,l in enumerate(open(b+'logs/'+f),1) if 'ERROR' in l or 'WARN' in l]
  ms={}
  for i,l in L:
    m=re.search(r'"msg":"([^"]*)"',l); k=m.group(1) if m else l[:80]
    ms.setdefault(k,[]).append(i)
  print(f,len(L),{k:(v[0],v[-1],len(v)) for k,v in ms.items()})