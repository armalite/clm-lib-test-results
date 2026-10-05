import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f:
    p=os.path.join(r,x);L=open(p).read().splitlines();print('##',p,len(L))
    for i,l in enumerate(L[:8],1):print(i,l[:160])