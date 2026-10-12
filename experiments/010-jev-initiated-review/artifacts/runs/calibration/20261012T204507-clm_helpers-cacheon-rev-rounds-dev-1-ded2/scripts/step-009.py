import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
json.dump(c,open('/task/workspace/context.json','w'))
L=open('/task/workspace/spill/s8.obs.txt').read().splitlines()
import collections
for l in L:
  if l.startswith(('board','changes')):print(l[:200])
cnt=collections.defaultdict(list)
for l in L:
  p=l.split(' ',2)
  if len(p)==3 and p[0].endswith('.log'):
    import re
    m=re.sub(r'[0-9:T.\-Z]{6,}|\d+','#',p[2])[:90]
    cnt[(p[0],m)].append(p[1])
for k,v in cnt.items():print(k,v[:12])