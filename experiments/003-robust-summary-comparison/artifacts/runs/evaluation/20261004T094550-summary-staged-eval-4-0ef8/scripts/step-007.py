import re,collections
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip()[:200])
c=collections.Counter();ex={}
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l:
    k=re.sub(r'[0-9a-f]{6,}|\d+','N',l[24:])[:60];c[k]+=1;ex.setdefault(k,(i,l.rstrip()[:170]))
for k,v in c.most_common(4):print(v,ex[k])