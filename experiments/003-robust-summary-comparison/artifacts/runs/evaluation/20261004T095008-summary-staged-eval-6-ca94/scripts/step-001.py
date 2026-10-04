import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/billing-svc.yaml','deploy/deploys.log','deploy/release-notes-6.24.0-4314.md','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/billing-svc.log','logs/front-proxy.log']:
  c=collections.Counter()
  for i,l in enumerate(open(b+f),1):
    if 'INFO' not in l:
      k=l[20:90]
      if c[k[:30]]<2:print(f,i,l.rstrip()[:200])
      c[k[:30]]+=1