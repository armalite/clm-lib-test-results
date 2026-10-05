import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s28.obs.txt').read()
lines=t.splitlines()
print('\n'.join(lines[:8]))
from collections import defaultdict
d=defaultdict(list)
for l in lines[8:]:
    p=l.split(' ',2)
    if len(p)<3: continue
    m=re.search(r'(SERVFAIL|certificate_expired|429|ERROR)\S*.{0,40}',p[2])
    d[(p[0],m.group(0)[:50] if m else p[2][:50])].append(p[1])
for k,v in d.items(): print(k,v[:6])