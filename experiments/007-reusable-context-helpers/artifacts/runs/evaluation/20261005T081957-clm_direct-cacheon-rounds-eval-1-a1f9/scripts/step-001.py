import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);L=open(p).read().splitlines();print(p,len(L))
    for i,l in enumerate(L[:6],1):print(i,l[:150])