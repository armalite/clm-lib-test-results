b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
L=open(b+'logs/returns-svc.log').read().splitlines()
import collections
c=collections.Counter()
for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
    k=l.split(' ',3)[-1][:60];c[k]+=1
print(c.most_common(8))
p=[i for i,l in enumerate(L,1) if 'pool' in l.lower()];print(len(p),p[:5]);print(L[p[0]-1] if p else '')
print(open(b+'metrics/returns-svc.csv').read().splitlines()[:3])