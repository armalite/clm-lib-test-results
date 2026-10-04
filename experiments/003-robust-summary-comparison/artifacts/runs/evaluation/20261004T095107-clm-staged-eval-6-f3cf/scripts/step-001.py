import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/billing-svc.yaml','deploy/deploys.log','deploy/release-notes-6.24.0-4314.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/billing-svc.log','logs/front-proxy.log']:
  L=open(b+f).readlines();c=collections.Counter(' '.join(l.split()[2:4]) for l in L);print(f,c.most_common(8))
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l:
      print(i,l.rstrip()[:160]);break