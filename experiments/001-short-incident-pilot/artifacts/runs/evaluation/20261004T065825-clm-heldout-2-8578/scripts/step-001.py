import os
b='/task/fixtures/'
for f in ['config/payments-api.yaml','deploy/changes.log','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/front-proxy.log','logs/payments-api.log']:
  c=collections.Counter()
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or 'WARN' in l:
      k=l[20:110];
      if c[k[:40]]<2:print(f,i,l.rstrip()[:200])
      c[k[:40]]+=1
L=open(b+'metrics/pricing-core-latency.csv').readlines();print(L[:3],L[-2:])