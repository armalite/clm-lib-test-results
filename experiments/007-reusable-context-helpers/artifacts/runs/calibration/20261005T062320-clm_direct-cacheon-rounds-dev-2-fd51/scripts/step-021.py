import json,re
t=open('/task/workspace/spill/s20.obs.txt').read()
lines=t.splitlines()
print('\n'.join(lines[:6]))
from collections import defaultdict
d=defaultdict(list)
for l in lines[6:]:
    p=l.split(' ',2)
    if len(p)<3: continue
    k=(p[0],re.sub(r'\d','',p[2])[40:110])
    d[k].append(p[1])
for k,v in d.items(): print(k,len(v),v[:3])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))