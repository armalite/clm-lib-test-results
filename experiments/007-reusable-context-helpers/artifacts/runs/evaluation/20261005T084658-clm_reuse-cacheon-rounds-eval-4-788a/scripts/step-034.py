import ctx
L=open('/task/workspace/spill/s33.obs.txt').read().splitlines()
for l in L:
  if l.startswith(('board','changes')):print(l[:150])
import collections
c=collections.defaultdict(list)
for l in L:
  p=l.split(' ',2)
  if len(p)==3 and p[0].endswith(('svc','api','worker')):c[p[0]].append(p[1])
for k,v in c.items():print(k,len(v),v[:6])
for l in L:
  if 'search-api' in l[:11]:print(l[:120]);break
ctx.keep_notes(open('/task/workspace/context.json').read() and __import__('json').load(open('/task/workspace/context.json'))['entries'][0]['body'])