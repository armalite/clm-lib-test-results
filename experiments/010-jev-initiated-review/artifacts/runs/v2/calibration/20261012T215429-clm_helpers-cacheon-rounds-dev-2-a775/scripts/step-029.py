import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s28.obs.txt').read().splitlines()
for l in t:
  if l.startswith(('board','changes')):print(l[:160])
seen=set()
for l in t:
  if l.startswith(('board','changes')):continue
  p=l.split()
  if not p:continue
  k=(p[0],l[-60:][:30])
  print(l[:130]) if p[0] not in seen or len([x for x in seen if x==p[0]])<1 else None
  seen.add(p[0])
import collections
print(collections.Counter(l.split()[0] for l in t if l.split()))