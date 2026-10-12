import json,re
t=open('/task/workspace/spill/s32.obs.txt').read()
print(open('/task/fixtures/round-07/board.md').read())
for l in t.splitlines():
  if 'auth-svc' in l or 'shipping' in l: continue
  print(l[:140])
import collections
c=collections.Counter(l.split()[0] for l in t.splitlines() if l.strip())
print(c)
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))