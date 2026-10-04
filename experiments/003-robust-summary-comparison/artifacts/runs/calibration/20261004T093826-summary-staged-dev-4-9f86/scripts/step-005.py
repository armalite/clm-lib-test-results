import collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md','UPDATE.md']:
 print('==',f)
 for i,l in enumerate(open(b+f),1):print(i,l.rstrip()[:220])
L=open(b+'logs/profile-svc.log').read().splitlines()
c=collections.Counter()
first={}
for i,l in enumerate(L,1):
 if 'ERROR' in l or 'WARN' in l:
  k=l.split(']',1)[-1][:60];c[k[:40]]+=1;first.setdefault(k[:40],(i,l[:200]))
for k,v in c.most_common(8):print(v,first[k])
G=open(b+'logs/api-gateway.log').read().splitlines()
for i,l in enumerate(G,1):
 if '503' in l: print(i,l[:200]);break
open('/task/workspace/notes.txt','a').write('S2 read\n')