import re,collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
c=collections.Counter();first={}
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l or 'WARN' in l:
    k=re.sub(r'req=\S+','',re.sub(r'\d+','N',l[24:]))[:90].strip();c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(5):print(first[k],v,k)
open('/task/workspace/notes.txt','a').write('S1: pool 14 waits at payments-api.log:206; timeout 800ms at 179.\n')