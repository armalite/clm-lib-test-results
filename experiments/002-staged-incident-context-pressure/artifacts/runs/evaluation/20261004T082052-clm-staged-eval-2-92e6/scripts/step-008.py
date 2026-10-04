p='/task/fixtures/stage-3/'
for i,l in enumerate(open(p+'deploy/changes.log'),1):print(i,l.rstrip()[:200])
L=open(p+'logs/payments-api.log').readlines()
import collections
c=collections.Counter()
first={}
for i,l in enumerate(L,1):
  if 'ERROR' in l:
    k=l.split(']',1)[1][:40];c[k]+=1;first.setdefault(k,(i,l.strip()[:200]))
for k,v in c.items():print(v,first[k])
print(open(p+'metrics/payments-api.csv').readlines()[:3])