import re,collections
b='/task/fixtures/stage-2/'
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip()[:220])
c=collections.Counter()
first={}
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l or 'WARN' in l or 'pool' in l or 'timed out' in l:
    k=re.sub(r'\d+','N',l.split(' ',3)[-1])[:90];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(10): print(v,first[k],k)
for i,l in enumerate(open(b+'logs/ingress-a.log'),1):
  if ' 50' in l: print(i,l.strip()[:200]);break
for i,l in enumerate(open(b+'metrics/payments-api.csv'),1):
  if i<3 or i%15==0: print(i,l.strip())