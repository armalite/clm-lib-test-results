b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md','UPDATE.md']:
  for i,l in enumerate(open(b+f).read().splitlines()):print(f,i+1,l[:200])
L=open(b+'logs/profile-svc.log').read().splitlines()
import collections
c=collections.Counter()
for i,l in enumerate(L):
  if 'ERROR' in l or 'WARN' in l:
    k=l.split(' ',3)[-1][:60];c[k]+=1
print(c.most_common(6))
print([(i+1,l[:160]) for i,l in enumerate(L) if 'pool' in l][:2])
M=open(b+'metrics/profile-svc.csv').read().splitlines();print(M[0],M[1],M[-1])