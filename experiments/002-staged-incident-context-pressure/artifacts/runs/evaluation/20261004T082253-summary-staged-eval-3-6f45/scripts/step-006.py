b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
 for i,l in enumerate(open(b+f),1):print(f,i,l.strip()[:200])
L=open(b+'logs/returns-svc.log').readlines()
import collections
c=collections.Counter()
first={}
for i,l in enumerate(L,1):
 if 'ERROR' in l:
  k=l.split('] ',1)[-1][:70];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(5):print(v,first[k],k)
E=open(b+'logs/edge-gw.log').readlines()
for i,l in enumerate(E,1):
 if ' 503' in l or 'status=503' in l:print('edge',i,l.strip()[:160]);break