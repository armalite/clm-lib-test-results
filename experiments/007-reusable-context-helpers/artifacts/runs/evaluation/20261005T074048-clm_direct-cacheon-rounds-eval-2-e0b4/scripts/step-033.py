import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
t=open('/task/workspace/spill/s32.obs.txt').read()
ls=t.splitlines()
for l in ls:
  if l.startswith('board') or l.startswith('changes'):print(l[:180])
import collections
d=collections.defaultdict(list)
for l in ls:
  p=l.split(' ',2)
  if len(p)>2 and p[0].endswith('.log'):d[p[0]].append((p[1],p[2][:90]))
for k,v in d.items():print(k,len(v),[x[0] for x in v][:8],v[0][1])