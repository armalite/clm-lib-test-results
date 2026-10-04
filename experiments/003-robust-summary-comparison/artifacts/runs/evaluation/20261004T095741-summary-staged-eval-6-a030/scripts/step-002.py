import collections,re
b='/task/fixtures/stage-1/logs/'
L=open(b+'billing-svc.log').read().splitlines()
c=collections.Counter()
for i,l in enumerate(L,1):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l[40:120]);c[k]+=1
    if c[k]<=2:print(i,l[:200])
print(c.most_common(8))
