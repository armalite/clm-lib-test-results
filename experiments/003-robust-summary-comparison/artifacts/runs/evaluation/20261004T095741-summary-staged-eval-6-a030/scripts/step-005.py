import re,collections
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open('/task/fixtures/stage-2/'+f).read().splitlines(),1):print(f,i,l[:220])
L=open('/task/fixtures/stage-2/logs/billing-svc.log').read().splitlines()
c=collections.Counter();first={}
for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
    k=re.sub(r'\d+','N',l[30:])[:90];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(6):print(v,first[k],k)
open('/task/workspace/notes.md','a').write('S1 db pool wait WARN billing log lines 248,387 (in_use 10/10).\n')