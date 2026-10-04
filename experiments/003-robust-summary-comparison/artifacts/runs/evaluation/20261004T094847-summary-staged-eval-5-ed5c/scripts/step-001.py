import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/quotes-api.yaml','deploy/deploys.log','deploy/release-notes-7.20.4-0a00.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1): print(i,l.rstrip())
import collections
for f in ['logs/ingress-a.log','logs/quotes-api.log']:
  L=open(b+f).read().splitlines()
  c=collections.Counter(l.split(' ',3)[2] if len(l.split())>3 else l for l in L)
  print('##',f,c.most_common(6))
  for i,l in enumerate(L,1):
    if any(k in l for k in ['ERROR','WARN','timeout','refused']):print(i,l);break