import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith('s22')]
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s22.obs.txt').read()
from collections import Counter
k=Counter()
for l in t.splitlines():
    p=l.split(' ',2)
    if len(p)==3: k[(p[0],re.sub(r'\d+','N',p[2])[40:90])]+=1
for x,n in k.most_common(15): print(n,x)
for l in t.splitlines():
    if 'notify' in l or 'pool_max' in l: print(l[:100]); break