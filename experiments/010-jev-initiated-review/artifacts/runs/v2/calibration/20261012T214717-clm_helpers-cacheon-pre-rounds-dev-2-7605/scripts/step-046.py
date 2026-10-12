import json
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))
s=open('/task/workspace/spill/s44.obs.txt').read()
lines=s.splitlines()
for l in lines:
  if l.startswith(('board','changes','b8')):print(l[:160])
import collections
c=collections.defaultdict(list)
for l in lines:
  p=l.split()
  if len(p)>2 and p[0].endswith('.log'):
    k=p[0]+(' 429' if '429' in l else ' inflight' if 'max_inflight' in l else ' cert' if 'certificate' in l else ' dns' if 'SERVFAIL' in l else ' other')
    c[k].append(p[1])
for k,v in c.items():print(k,v[:6])