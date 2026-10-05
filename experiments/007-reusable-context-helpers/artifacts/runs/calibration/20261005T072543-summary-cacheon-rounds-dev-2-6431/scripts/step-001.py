import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f: print(os.path.join(r,x))
print(open(b+'board.md').read()[:1500])
import glob
for p in glob.glob(b+'*.md'):
  if 'changes' in p: print(open(p).read()[:1500])
for p in glob.glob(b+'logs/*'):
  L=open(p).read().splitlines()
  print(p,len(L))
  for i,l in enumerate(L,1):
    if any(k in l for k in ('ERROR','WARN','error')): print(i,l[:160])
