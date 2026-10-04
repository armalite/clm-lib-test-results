import re,collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md','UPDATE.md']:
  for i,l in enumerate(open(b+f)):print(f,i+1,l.rstrip()[:220])
L=open(b+'logs/quotes-api.log').readlines()
c=collections.Counter()
for i,l in enumerate(L):
  if 'ERROR' in l:
    k=re.sub(r'\d+','N',l[40:].strip())[:90];c[k]+=1
    if c[k]==1:print(i+1,l.strip()[:180])
print(c.most_common(6))
M=open(b+'metrics/quotes-api.csv').readlines();print(M[0].strip(),M[1].strip(),M[-1].strip())
open('/task/workspace/notes.txt','a').write('s1 dbpool waits qlog 419-851 in_use 14/14; gw 5xx first line 93\n')