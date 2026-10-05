import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print('==',p)
    L=open(p).read().splitlines()
    for i,l in enumerate(L[:15],1):print(i,l[:160])
    print('lines',len(L))