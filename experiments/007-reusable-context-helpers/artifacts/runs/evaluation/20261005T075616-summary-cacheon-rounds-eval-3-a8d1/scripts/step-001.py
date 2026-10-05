import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:print(os.path.join(r,x))
print(open(b+'board.md').read()[:1500])
import glob
for f in glob.glob(b+'logs/*'):
  L=open(f).read().splitlines();print(f,len(L))
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l or 'error' in l:print(i,l[:160])
