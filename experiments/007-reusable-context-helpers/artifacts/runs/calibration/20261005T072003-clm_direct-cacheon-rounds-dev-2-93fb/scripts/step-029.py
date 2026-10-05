import json,re,glob
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*.log')):
  n=p.split('/')[-1];hits=[]
  for i,l in enumerate(open(p),1):
    if re.search(r'certificate|SERVFAIL|429|max_inflight|ERROR',l):hits.append(i)
  print(n,len(hits),hits[:12])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))