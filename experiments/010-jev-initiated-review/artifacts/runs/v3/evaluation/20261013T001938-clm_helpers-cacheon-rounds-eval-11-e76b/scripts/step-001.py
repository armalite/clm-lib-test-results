import os
for r,d,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);print('==',p)
    for i,l in enumerate(open(p),1):
      if 'ERROR' in l or 'WARN' in l or not p.endswith('.log'): print(i,l.rstrip()[:160])