import collections,re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip()[:200])
c=collections.Counter();first={}
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l[24:])[:90];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(4):print(first[k],v,k)
L=open(b+'metrics/payments-api.csv').readlines();print(L[1],L[-1])
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'pool exhausted' in l:print(i,l.rstrip()[:160]);break