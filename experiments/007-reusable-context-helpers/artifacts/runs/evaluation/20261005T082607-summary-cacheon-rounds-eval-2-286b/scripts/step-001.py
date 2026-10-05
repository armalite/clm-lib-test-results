import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f: print(os.path.join(r,x))
print(open(b+'board.md').read()[:1500])
import glob
for p in glob.glob(b+'changes.md'): print(open(p).read()[:1000])
for p in glob.glob(b+'logs/*'):
  L=open(p).read().splitlines()
  print(p,len(L))
  for i,l in enumerate(L):
    if any(k in l for k in ('ERROR','WARN','error','warn')): print(i+1,l[:160])