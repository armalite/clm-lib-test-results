import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'].startswith('n') and e['id']!='n10a']
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
s=open('/task/workspace/spill/s49.obs.txt').read()
lines=s.splitlines()
for l in lines:
  if l.startswith('board') or l.startswith('changes'): print(l[:150])
import collections
c=collections.defaultdict(list)
for l in lines:
  p=l.split(' ',2)
  if len(p)==3 and p[0].endswith('.log'): c[(p[0],p[2][20:70])].append(p[1])
for k,v in c.items(): print(k,','.join(v))