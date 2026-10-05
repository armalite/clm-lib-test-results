import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print(p,sum(1 for _ in open(p)))
print(open('/task/fixtures/round-01/board.md').read()[:1500])
import glob
for p in glob.glob('/task/fixtures/round-01/logs/*'):
  for i,l in enumerate(open(p),1):
    if 'INFO' not in l: print(os.path.basename(p),i,l.strip()[:150])