import json,re
t=open('/task/workspace/spill/s25.obs.txt').read()
print(open('/task/fixtures/round-07/board.md').read())
from collections import defaultdict
d=defaultdict(list)
for l in t.splitlines():
  p=l.split(' ',2)
  if len(p)==3 and p[1].isdigit():
    k=re.sub(r'\d+','#',p[2])[:70]
    d[(p[0],k)].append(p[1])
for k,v in d.items(): print(k[0],v[:4],len(v),k[1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))