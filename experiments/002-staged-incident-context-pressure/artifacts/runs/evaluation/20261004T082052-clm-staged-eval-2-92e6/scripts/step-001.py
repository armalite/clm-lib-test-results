import os
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/payments-api.yaml','deploy/deploys.log','deploy/release-notes-5.36.1-f33d.md','ops/oncall-notes.md']:
 print('##',f)
 for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
import collections
for f in ['logs/ingress-a.log','logs/payments-api.log']:
 c=collections.Counter()
 L=open(b+f).readlines()
 for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
   k=' '.join(l.split()[2:6]);
   if c[k]<1:print(f,i,l.rstrip()[:200])
   c[k]+=1
 print(len(c))