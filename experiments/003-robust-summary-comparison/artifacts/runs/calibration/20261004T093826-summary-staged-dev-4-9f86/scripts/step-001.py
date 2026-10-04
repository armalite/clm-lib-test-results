import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/profile-svc.yaml','deploy/deploys.log','deploy/release-notes-8.15.4-7744.md','ops/oncall-notes.md']:
 print('##',f)
 for i,l in enumerate(open(b+f),1): print(i,l.rstrip())
import collections
for f in ['logs/api-gateway.log','logs/profile-svc.log']:
 L=open(b+f).read().splitlines()
 c=collections.Counter(' '.join(l.split()[2:5]) for l in L)
 print('##',f,c.most_common(6))
 for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
   print(i,l[:200]);break