import re,collections
b='/task/fixtures/stage-1/'
c=collections.Counter();ex={}
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l or 'pool' in l or 'latency' in l:
    k=re.sub(r'[0-9a-f]{6,}|\d+','N',l[24:])[:70]
    c[k]+=1;ex.setdefault(k,i)
for k,v in c.most_common(10):print(v,ex[k],k)
for i,l in enumerate(open(b+'logs/ingress-a.log'),1):
  if ' 50' in l and i<200:print(i,l[:150]);break
open('/task/workspace/notes.txt','w').write('s1: tax timeout 800ms errors payments-api.log:153-207; release-notes:5 timeout 2500->800; :17 pool 48->10; deploys.log:1\n')