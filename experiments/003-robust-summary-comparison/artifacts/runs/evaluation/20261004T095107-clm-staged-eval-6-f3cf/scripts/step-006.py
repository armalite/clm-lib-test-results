import re
b='/task/fixtures/stage-2/'
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  print(f);[print(i+1,l.rstrip()) for i,l in enumerate(open(b+f))]
from collections import Counter
c=Counter()
for i,l in enumerate(open(b+'logs/billing-svc.log')):
  if 'ERROR' in l or 'WARN' in l:
    k=re.sub(r'\d+','N',l[20:120]);
    if k not in c: print(i+1,l.rstrip()[:200])
    c[k]+=1
print(c.most_common(5))
print(open(b+'metrics/billing-svc.csv').readlines()[:3])