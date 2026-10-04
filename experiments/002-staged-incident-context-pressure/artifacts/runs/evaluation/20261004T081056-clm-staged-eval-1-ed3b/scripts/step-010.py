import re
print(open('/task/fixtures/stage-3/deploy/changes.log').read())
L=open('/task/fixtures/stage-3/logs/quotes-api.log').read().splitlines()
from collections import Counter
c=Counter();first={}
for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
    k=re.sub(r'\d+','N',l[20:120]);c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(8):print(v,first[k],k)
G=open('/task/fixtures/stage-3/logs/api-gateway.log').read().splitlines()
for i,l in enumerate(G,1):
  if ' 503' in l or 'ERROR' in l:print(i,l);break