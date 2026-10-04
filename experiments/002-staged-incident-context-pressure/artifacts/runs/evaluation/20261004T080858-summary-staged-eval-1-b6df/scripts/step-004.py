import re,collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:220])
c=collections.Counter()
for i,l in enumerate(open(b+'logs/quotes-api.log'),1):
  if 'ERROR' in l:
    k=re.sub(r'[0-9a-f]{10}|\d+','N',l[40:])[:70]
    if c[k]<1:print(i,l.rstrip()[:200])
    c[k]+=1
print(c)
open('/task/workspace/notes.md','a').write('S2 read\n')