import collections
b='/task/fixtures/stage-2/'
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
L=open(b+'logs/quotes-api.log').readlines()
c=collections.Counter()
first={}
for i,l in enumerate(L,1):
  if 'ERROR' in l or 'WARN' in l:
    k=' '.join(l.split()[2:6]);c[k]+=1;first.setdefault(k,i)
for k,v in c.most_common(6):print(v,first[k],k)
M=open(b+'metrics/quotes-api.csv').readlines();print(M[0],M[1],M[-1])