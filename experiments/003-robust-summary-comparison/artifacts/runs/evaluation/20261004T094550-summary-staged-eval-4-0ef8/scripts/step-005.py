import re,collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
c=collections.Counter();ex={}
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l or 'pool' in l:
    k=re.sub(r'[0-9a-f]{6,}|\d+','N',l[24:])[:70];c[k]+=1;ex.setdefault(k,(i,l.rstrip()[:170]))
for k,v in c.most_common(5):print(v,ex[k])
print(open(b+'metrics/payments-api.csv').readlines()[:3])