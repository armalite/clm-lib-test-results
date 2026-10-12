import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f: print(os.path.join(r,x))
for f in ['board.md','changes.md']:
  p=b+f
  if os.path.exists(p):
    for i,l in enumerate(open(p),1): print(f,i,l.rstrip()[:200])
import glob
for p in glob.glob(b+'logs/*'):
  L=open(p).read().splitlines()
  print(p,len(L))
  for i,l in enumerate(L,1):
    if any(k in l for k in ['ERROR','WARN','error','warn']): print(i,l[:160])