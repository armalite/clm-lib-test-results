import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f: print(r,x)
print(open(b+'board.md').read()[:1500])
import glob
for p in glob.glob(b+'logs/*'):
  L=open(p).read().splitlines()
  print(p,len(L))
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l: print(i,l[:160])
