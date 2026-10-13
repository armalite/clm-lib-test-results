import json
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip()[:200])
s=open('/task/workspace/spill/s14.obs.txt').read()
import re
from collections import Counter
c=Counter()
for l in s.splitlines():
  p=l.split(' ',2)
  if len(p)>2:
    k=re.sub(r'\d+','#',p[2])[:70]; c[(p[0],k)]+=1
for k,v in c.most_common(25): print(v,k)
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))