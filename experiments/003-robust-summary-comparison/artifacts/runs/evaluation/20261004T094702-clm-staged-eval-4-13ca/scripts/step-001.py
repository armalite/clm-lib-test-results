import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/payments-api.yaml','deploy/deploys.log','deploy/release-notes-6.25.3-646f.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip()[:150])
import collections
for f in ['logs/ingress-a.log','logs/payments-api.log']:
  c=collections.Counter()
  for i,l in enumerate(open(b+f),1):
    if any(k in l for k in ('ERROR','WARN','error','timeout')):
      c[l[20:90]]+=1
      if c[l[20:90]]==1:print(f,i,l.rstrip()[:200])