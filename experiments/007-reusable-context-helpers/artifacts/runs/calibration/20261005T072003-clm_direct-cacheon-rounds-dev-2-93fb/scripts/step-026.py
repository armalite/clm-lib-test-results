import json,re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  n=p.split('/')[-1];hits=[]
  for i,l in enumerate(open(p),1):
    if re.search(r'INFO|slow query',l):continue
    hits.append((i,l.strip()[:110]))
  print(n,len(hits))
  for h in hits[:4]:print(' ',h)
  print('  lines',[h[0] for h in hits])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))