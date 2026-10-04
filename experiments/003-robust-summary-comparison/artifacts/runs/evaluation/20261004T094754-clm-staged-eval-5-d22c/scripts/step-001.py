import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/quotes-api.yaml','deploy/deploys.log','deploy/release-notes-7.20.4-0a00.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/ingress-a.log','logs/quotes-api.log']:
  L=open(b+f).readlines();print('##',f,len(L))
  c=collections.Counter(' '.join(l.split()[2:5]) for l in L if 'ERROR' in l or 'WARN' in l);print(c.most_common(6))
  for i,l in enumerate(L,1):
    if 'ERROR' in l:print(i,l.rstrip()[:200]);break