import json
t=open('/task/workspace/spill/s13.obs.txt').read()
lines=t.splitlines()
print(lines[0][:300])
import collections
c=collections.Counter()
for l in lines[1:]:
  p=l.split(' ',2)
  if len(p)<3: print(l[:200]);continue
  k=p[0]+' '+__import__('re').sub(r'\d+','#',p[2])[:90]
  if c[k]<2: print(l[:170])
  c[k]+=1
print(c.most_common(12))
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))