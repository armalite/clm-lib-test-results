import json,re
b='/task/fixtures/round-03/'
print(open(b+'board.md').read())
t=open('/task/workspace/spill/s9.obs.txt').read().splitlines()
from collections import defaultdict
d=defaultdict(list)
for l in t:
  p=l.split(' ',2)
  if len(p)==3 and p[1].isdigit(): d[p[0]].append((p[1],p[2]))
for f,v in d.items():
  print(f,len(v),[x[0] for x in v][:30]);print(' ',v[0][1][:140])
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open(p,'w'))