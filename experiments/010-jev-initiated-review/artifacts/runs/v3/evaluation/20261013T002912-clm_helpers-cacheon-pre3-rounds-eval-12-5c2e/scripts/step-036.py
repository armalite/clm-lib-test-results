import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  hits=[(i,l) for i,l in enumerate(open(p),1) if re.search('429|certificate|config validation|ERROR',l)]
  print(p.split('/')[-1],len(hits),[i for i,_ in hits[:6]])
  if hits:print('  ',hits[0][1][:160].rstrip())