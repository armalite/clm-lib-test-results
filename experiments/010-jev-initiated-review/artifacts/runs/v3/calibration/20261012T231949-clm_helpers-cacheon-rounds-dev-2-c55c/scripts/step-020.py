import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-07/board.md').read())
from collections import defaultdict
d=defaultdict(list)
for l in open('/task/workspace/spill/s19.obs.txt'):
  p=l.split(' ',2)
  if len(p)<3 or not p[1].isdigit(): continue
  k=p[0]+' '+re.sub(r'\d','',p[2])[:70]
  d[k].append(p[1])
for k,v in d.items(): print(k,v[:8])