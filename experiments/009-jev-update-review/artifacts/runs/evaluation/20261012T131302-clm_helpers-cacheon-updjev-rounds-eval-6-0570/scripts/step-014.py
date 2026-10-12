import json,re,collections
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
d=collections.defaultdict(list)
for l in open('/task/workspace/spill/s13.obs.txt'):
  p=l.split(None,2)
  if len(p)<3: continue
  k=p[0]+' '+re.sub(r'\d+','N',p[2])[:70]
  d[k].append(p[1])
for k,v in d.items(): print(k,','.join(v[:8]),len(v))