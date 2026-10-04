b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
import collections
c=collections.Counter();f={}
for i,l in enumerate(open(b+'logs/quotes-api.log'),1):
  if 'ERROR' in l or 'exhausted' in l or 'timed out' in l:
    k=l.split(' ',3)[-1][:70];c[k]+=1;f.setdefault(k,(i,l.strip()[:200]))
for k,v in c.most_common(6):print(v,f[k])