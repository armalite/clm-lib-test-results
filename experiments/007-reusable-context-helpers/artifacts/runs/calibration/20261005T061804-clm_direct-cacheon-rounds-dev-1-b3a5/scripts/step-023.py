import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7')]
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s22.obs.txt').read()
import re
for l in t.splitlines():
  if l.startswith(('board','changes')):print(l[:200])
  else:
    m=re.match(r'(\S+) (\d+) (.*)',l)
    if m:print(m[1][:6],m[2],m[3][20:110])