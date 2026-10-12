import json,re
L=open('/task/workspace/spill/s28.obs.txt').read().splitlines()
from collections import defaultdict
d=defaultdict(list)
for l in L:
  p=l.split(' ',2)
  if len(p)<3: continue
  k=(p[0],re.sub(r'[0-9:T.\-Z]+','',p[2])[:60])
  d[k].append(p[1])
for k,v in d.items(): print(k[0],','.join(v[:8]),k[1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))