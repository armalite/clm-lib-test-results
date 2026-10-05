import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print('==',p)
    for i,l in enumerate(open(p),1):
      if x.endswith('.md') or any(k in l for k in ('ERROR','WARN','error','warn')): print(i,l.rstrip()[:160])