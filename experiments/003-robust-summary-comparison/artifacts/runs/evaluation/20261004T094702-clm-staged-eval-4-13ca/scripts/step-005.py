import re
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
L=open(b+'logs/payments-api.log').read().splitlines()
c={}
for i,l in enumerate(L,1):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l[60:140]);c.setdefault(k,[0,i]);c[k][0]+=1
for k,v in sorted(c.items(),key=lambda x:-x[1][0])[:6]:print(v,k)
L=open(b+'metrics/payments-api.csv').read().splitlines();print(L[0]);print(L[30])