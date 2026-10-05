import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:
    p=os.path.join(r,x);L=open(p).read().splitlines();print(p,len(L))
print(open(b+'board.md').read()[:1500])
import glob
for p in glob.glob(b+'logs/*'):
  for i,l in enumerate(open(p),1):
    if any(k in l for k in ('ERROR','WARN','error','429','fail')):print(p[-20:],i,l.strip()[:160])