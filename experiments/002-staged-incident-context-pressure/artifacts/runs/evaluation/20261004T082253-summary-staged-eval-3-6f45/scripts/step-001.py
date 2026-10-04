import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/returns-svc.yaml','deploy/deploys.log','deploy/release-notes-6.33.4-cb27.md','ops/oncall-notes.md']:
 print('##',f)
 for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/edge-gw.log','logs/returns-svc.log']:
 c=collections.Counter()
 L=open(b+f).readlines()
 for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
   c[l[20:90]]+=1
 print(f,len(L));[print(k,v) for k,v in c.most_common(6)]