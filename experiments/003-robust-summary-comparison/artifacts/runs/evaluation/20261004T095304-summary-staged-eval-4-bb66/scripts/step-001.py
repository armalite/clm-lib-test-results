import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/payments-api.yaml','deploy/deploys.log','deploy/release-notes-6.25.3-646f.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/ingress-a.log','logs/payments-api.log']:
  ls=open(b+f).readlines()
  c=collections.Counter(l.split()[2] if len(l.split())>2 else '' for l in ls)
  print(f,c.most_common(5))
  for i,l in enumerate(ls,1):
    if any(k in l for k in ['ERROR','WARN','error','timeout']):print(i,l.rstrip()[:200]);break