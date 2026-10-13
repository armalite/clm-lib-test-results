import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
json.dump(c,open('/task/workspace/context.json','w'))
s=open('/task/workspace/spill/s16.obs.txt').read().splitlines()
for l in s:
  if l.startswith(('board','changes')):print(l[:200])
from collections import Counter
k=Counter()
for l in s:
  if not l.startswith(('board','changes')):
    p=l.split(' ',2)
    if len(p)>2:
      m=p[2]
      tag='429' if '429' in m else 'pool' if 'pool' in m else 'slow' if 'slow' in m else m[:90]
      k[(p[0],tag)]+=1
      if tag not in('429','pool','slow'):print(p[0],p[1],m[:120])
print(k)