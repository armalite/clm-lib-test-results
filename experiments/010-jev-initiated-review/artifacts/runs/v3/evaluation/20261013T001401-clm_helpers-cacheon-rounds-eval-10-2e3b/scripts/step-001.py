import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);L=open(p).read().splitlines();print(p,len(L))
    for i,l in enumerate(L,1):
      if x.endswith('.md') or any(k in l for k in ('ERROR','WARN','error','warn')):print(i,l[:150])