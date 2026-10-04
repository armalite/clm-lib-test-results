import collections,re
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','UPDATE.md','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:220])
L=open(b+'logs/payments-api.log').read().splitlines()
c=collections.Counter()
first={}
for i,l in enumerate(L,1):
  if 'ERROR' in l:
    k=re.sub(r'[0-9a-f]{6,}|\d+','N',l.split('ERROR',1)[1])[:120];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(6):print(v,first[k],k)
print(open(b+'metrics/payments-api.csv').read().splitlines()[:3])