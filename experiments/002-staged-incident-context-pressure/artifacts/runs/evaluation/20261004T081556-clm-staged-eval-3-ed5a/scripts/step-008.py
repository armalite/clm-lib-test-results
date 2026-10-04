import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip()[:300])
L=open(b+'logs/returns-svc.log').readlines()
import collections
c=collections.Counter()
first={}
for i,l in enumerate(L,1):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l.split(']')[1][:60]);c[k]+=1;first.setdefault(k,i)
for k,v in c.items():print(v,first[k],k)
print(L[first[list(c)[0]]-1][:200] if c else '')
for i,l in enumerate(open(b+'metrics/returns-svc.csv'),1):
  if i<3:print(i,l.strip())