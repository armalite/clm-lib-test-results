import json,re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
s=open('/task/workspace/spill/s20.obs.txt').read()
from collections import defaultdict
d=defaultdict(list)
for l in s.splitlines():
  m=re.match(r'(\S+\.log) (\d+) (.*)',l)
  if m:
    k=(m[1],re.sub(r'[\d:.TZ-]{6,}','',m[3])[:60]);d[k].append(m[2])
for k,v in d.items():print(k[0],','.join(v[:12]),k[1])
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open(p,'w'))