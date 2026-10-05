import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print('==',p)
    for i,l in enumerate(open(p),1):
      if 'board' in p or 'changes' in p or any(k in l for k in ('ERROR','WARN','error','warn')): print(i,l.rstrip()[:200])