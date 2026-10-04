import collections,re
p='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
 for i,l in enumerate(open(p+f),1):print(f,i,l.rstrip()[:250])
L=open(p+'logs/billing-svc.log').readlines()
c=collections.Counter()
first={}
for i,l in enumerate(L,1):
 if 'ERROR' in l or 'WARN' in l:
  k=re.sub(r'\d+','N',l[25:].split(']',1)[-1])[:80];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(8):print(v,first[k],k)
import csv
r=list(csv.reader(open(p+'metrics/billing-svc.csv')));print(r[0],r[1],r[-1])