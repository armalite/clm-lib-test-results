import os
for r,d,f in os.walk('/task/fixtures'):
  for x in f:print(os.path.join(r,x))
print(open('/task/fixtures/round-01/board.md').read()[:1500])
import glob
for p in glob.glob('/task/fixtures/round-01/*.md')+glob.glob('/task/fixtures/round-01/logs/*'):
  L=open(p).read().splitlines()
  print(p,len(L))
  for i,l in enumerate(L,1):
    if any(k in l.lower() for k in ['error','warn','fail','429','applied']):print(i,l[:160])