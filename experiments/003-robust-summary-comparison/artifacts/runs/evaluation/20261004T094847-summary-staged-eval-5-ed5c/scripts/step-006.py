import collections
b='/task/fixtures/stage-2/'
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
L=open(b+'logs/quotes-api.log').read().splitlines()
c=collections.Counter();first={}
for i,l in enumerate(L,1):
  if 'ERROR' in l or 'pool' in l:
    k=l[60:130];c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(8):print(v,first[k],k)
I=open(b+'logs/ingress-a.log').read().splitlines()
for i,l in enumerate(I,1):
  if ' 503' in l or 'status=5' in l:print('ing',i,l[:200]);break
M=open(b+'metrics/quotes-api.csv').read().splitlines();print(M[0]);print(M[30])