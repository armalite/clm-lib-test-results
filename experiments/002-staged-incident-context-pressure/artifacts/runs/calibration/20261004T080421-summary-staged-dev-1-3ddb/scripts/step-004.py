b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md','UPDATE.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:220])
import collections,re
c=collections.Counter();first={}
for i,l in enumerate(open(b+'logs/shipping-api.log'),1):
  if 'ERROR' in l or 'WARN' in l:
    k=re.sub(r'\d+','N',l[24:])[:90];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(6):print(first[k],v,k)
print(open(b+'metrics/shipping-api.csv').readlines()[:2])