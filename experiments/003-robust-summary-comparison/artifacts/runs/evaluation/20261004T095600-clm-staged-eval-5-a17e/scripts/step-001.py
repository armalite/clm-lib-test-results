import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/quotes-api.yaml','deploy/deploys.log','deploy/release-notes-7.20.4-0a00.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/ingress-a.log','logs/quotes-api.log']:
  L=open(b+f).readlines()
  c=collections.Counter(' '.join(l.split()[2:4]) for l in L)
  print(f,c.most_common(6))
  for i,l in enumerate(L,1):
    if 'WARN' in l or 'ERR' in l:
      print(i,l.strip()[:200]);break