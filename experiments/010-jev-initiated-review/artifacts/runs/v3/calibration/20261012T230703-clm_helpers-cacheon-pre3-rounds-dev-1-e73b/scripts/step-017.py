import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  c={}
  for i,l in enumerate(L,1):
    if 'slow query' in l: continue
    k=re.sub(r'[0-9]+','#',l)[-70:]
    c.setdefault(k,[]).append(i)
  print(f)
  for k,v in c.items(): print(' ',v[0],v[-1],len(v),k)