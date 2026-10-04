import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/quotes-api.yaml','deploy/deploys.log','deploy/release-notes-8.19.0-ff7b.md','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/api-gateway.log','logs/quotes-api.log']:
  c=collections.Counter()
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or 'WARN' in l:
      k=l[24:110];
      if c[k[:40]]<2:print(f,i,l.rstrip()[:200])
      c[k[:40]]+=1