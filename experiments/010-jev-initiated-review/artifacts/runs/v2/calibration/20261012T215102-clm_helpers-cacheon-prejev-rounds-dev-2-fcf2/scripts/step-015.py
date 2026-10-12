import json,re
s=open('/task/workspace/spill/s13.obs.txt').read()
lines=s.splitlines()
print('\n'.join(lines[:6]))
from collections import defaultdict
d=defaultdict(list)
for l in lines:
  m=re.match(r'(\S+\.log) (\d+) (.*)',l)
  if m:
    k=(m.group(1),re.sub(r'[\d:.TZ-]{6,}','',m.group(3))[:70]);d[k].append(m.group(2))
for k,v in d.items(): print(k[0],v[:6],k[1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))