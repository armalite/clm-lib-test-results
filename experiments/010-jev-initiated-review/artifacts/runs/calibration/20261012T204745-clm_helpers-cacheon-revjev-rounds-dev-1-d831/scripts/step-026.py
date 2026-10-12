import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1):print(f,i,l.rstrip()[:250])
for p in sorted(glob.glob('/task/fixtures/round-09/logs/*')):
  ls=[i for i,l in enumerate(open(p),1) if re.search(r'ERROR|429|exhaust|fail',l)]
  print(p.split('/')[-1],len(ls),ls[:12])
  if ls:print(open(p).read().splitlines()[ls[0]-1][:200])