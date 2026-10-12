import json,re,collections
t=open('/task/workspace/spill/s18.obs.txt').read().splitlines()
cnt=collections.Counter();first={}
for l in t:
  p=l.split(' ',2)
  if len(p)<3: continue
  k=(p[0],re.sub(r'[0-9]+','N',p[2])[:70])
  cnt[k]+=1; first.setdefault(k,p[1])
for k,v in cnt.items(): print(k[0],first[k],v,k[1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith('s18')]
json.dump(c,open('/task/workspace/context.json','w'))