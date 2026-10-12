import json
L=open('/task/workspace/spill/s16.obs.txt').read().splitlines()
from collections import defaultdict
d=defaultdict(list)
for l in L:
    p=l.split(' ',2)
    if len(p)<3: continue
    k=p[0]+' '+('dns' if 'dns' in l.lower() else 'pool' if 'pool' in l else 'heap' if 'heap' in l else 'restart' if ('restart' in l or 'OOM' in l) else 'other')
    d[k].append(p[1])
for k,v in d.items(): print(k,','.join(v[:12]))
for l in L:
    if 'notify' in l and ('dns' in l.lower() or 'config' in l.lower()): print(l[:100]); break
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))