import os
for r,d,f in os.walk('/task/fixtures/stage-1'):
  for x in f:
    p=os.path.join(r,x)
    if 'logs' in p: continue
    print('##',p);print(''.join(f'{i+1}:{l}' for i,l in enumerate(open(p))))
import collections
for n in ['api-gateway','quotes-api']:
  L=open(f'/task/fixtures/stage-1/logs/{n}.log').readlines()
  c=collections.Counter(' '.join(l.split()[2:4]) for l in L)
  print(n,c.most_common(6))
  for i,l in enumerate(L):
    if 'ERROR' in l or 'WARN' in l: print(i+1,l.strip()[:200]);break