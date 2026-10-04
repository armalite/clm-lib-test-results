import collections,re
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md','UPDATE.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:220])
c=collections.Counter();first={}
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l[24:])[:110];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(5):print(first[k],v,k)
L=open(b+'metrics/payments-api.csv').readlines();print(L[0],L[1],L[30],L[-1])
open('/task/workspace/notes.txt','a').write('s1 symptom: stage-1/logs/payments-api.log:179 risk-score timeouts\n')