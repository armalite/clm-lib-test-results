import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/shipping-api.yaml','deploy/deploys.log','deploy/release-notes-7.25.4-e1b3.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/ingress-a.log','logs/shipping-api.log']:
  c=collections.Counter()
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or 'WARN' in l:
      k=l[30:110];
      if c[k[:40]]<2:print(f,i,l.rstrip()[:200])
      c[k[:40]]+=1