import re,collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:250])
c=collections.Counter();first={}
for i,l in enumerate(open(b+'logs/billing-svc.log'),1):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l[25:])[:70];c[k]+=1;first.setdefault(k,(i,l.rstrip()[:200]))
for k,n in c.most_common(4):print(n,first[k])
open('/task/workspace/notes.txt','a').write('stage1 errors: pricing timeout 800ms billing log line 152.\n')