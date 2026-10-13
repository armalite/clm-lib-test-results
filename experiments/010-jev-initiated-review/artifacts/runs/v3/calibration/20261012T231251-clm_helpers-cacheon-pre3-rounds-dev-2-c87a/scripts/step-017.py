import json,re
t=open('/task/workspace/spill/s15.obs.txt').read()
print(open('/task/fixtures/round-04/board.md').read())
from collections import defaultdict
d=defaultdict(list)
for l in t.splitlines()[2:]:
  p=l.split(' ',2)
  if len(p)==3:
    k=(p[0],re.sub(r'\d+','#',p[2])[40:100]);d[k].append(p[1])
for k,v in d.items():print(k,v[:5])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))