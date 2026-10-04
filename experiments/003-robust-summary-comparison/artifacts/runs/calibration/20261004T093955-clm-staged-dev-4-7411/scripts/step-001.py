import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/profile-svc.yaml','deploy/deploys.log','deploy/release-notes-8.15.4-7744.md','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/api-gateway.log','logs/profile-svc.log']:
  c=collections.Counter()
  L=open(b+f).readlines()
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l:
      k=l[30:110]
      if c[k[:40]]<2:print(f,i,l.rstrip()[:200])
      c[k[:40]]+=1