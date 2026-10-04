import re,collections
I=open('/task/fixtures/stage-1/logs/ingress-a.log').readlines()
c=collections.Counter();b=[]
for i,l in enumerate(I,1):
  m=re.search(r'status=(\d+)',l)
  s=m.group(1) if m else 'NA'
  c[s]+=1
  if s.startswith('5') or s=='NA':b.append(i)
print(c);print(b[:8])
for i in b[:3]:print(i,I[i-1].strip()[:200])
open('/task/workspace/notes.md','a').write('db pool wait in_use 12/12 at quotes-api.log:150,177,219,357 (few WARN only).\n')