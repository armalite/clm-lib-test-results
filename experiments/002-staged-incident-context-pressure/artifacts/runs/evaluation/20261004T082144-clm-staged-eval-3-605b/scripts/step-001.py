import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/returns-svc.yaml','deploy/deploys.log','deploy/release-notes-6.33.4-cb27.md','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/edge-gw.log','logs/returns-svc.log']:
  c=collections.Counter()
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or 'WARN' in l:
      c[l[30:90]]+=1
      if c[l[30:90]]<2:print(f,i,l.rstrip()[:200])