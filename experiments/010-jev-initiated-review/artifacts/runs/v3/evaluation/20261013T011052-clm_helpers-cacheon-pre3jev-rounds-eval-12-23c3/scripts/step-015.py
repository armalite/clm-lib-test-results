import json,re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
t=open('/task/workspace/spill/s13.obs.txt').read().splitlines()
from collections import defaultdict
d=defaultdict(list)
for l in t:
  p=l.split(' ',2)
  if len(p)<3 or not p[0].endswith('.log'):continue
  m=re.search(r'(certificate_expired|429|exhaust\w*|ttl\S*|timeout|oom\w*|disk\S*|lag\S*|stampede|miss\w*|dns\S*|NXDOMAIN)',p[2],re.I)
  d[(p[0],m.group(1) if m else p[2][:40])].append(p[1])
for k,v in d.items():print(k,len(v),v[0],v[-1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
json.dump(c,open('/task/workspace/context.json','w'))