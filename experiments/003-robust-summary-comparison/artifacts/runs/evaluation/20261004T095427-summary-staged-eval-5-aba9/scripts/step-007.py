import re,collections
B='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(B+f),1):print(f,i,l.rstrip()[:220])
L=open(B+'logs/quotes-api.log').readlines()
c=collections.Counter(re.sub(r'\d+','N',l[25:])[:90] for l in L if 'ERROR' in l)
for k,v in c.most_common(6):print(v,k.strip())
e=[i for i,l in enumerate(L,1) if 'ERROR' in l][:3]
for i in e:print(i,L[i-1].strip()[:200])
I=open(B+'logs/ingress-a.log').readlines()
b=[i for i,l in enumerate(I,1) if 'status=5' in l];print(len(b),b[:3]);print(I[b[0]-1].strip()[:200])
open('/task/workspace/notes.md','a').write('advanced to stage2\n')