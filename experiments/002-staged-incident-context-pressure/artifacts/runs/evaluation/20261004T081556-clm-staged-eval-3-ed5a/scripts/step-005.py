import re,collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md','UPDATE.md']:
 for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
c=collections.Counter();first={}
for i,l in enumerate(open(b+'logs/returns-svc.log'),1):
 if 'ERROR' in l or 'WARN' in l:
  k=re.sub(r'\d+','N',l[40:])[:90];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(5):print(v,first[k],k)
for i,l in enumerate(open(b+'logs/edge-gw.log'),1):
 if ' 503' in l:print(i,l[:160]);break
print(open(b+'metrics/returns-svc.csv').readlines()[:2])