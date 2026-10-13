import json,glob,re
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='notes']
json.dump(d,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if not re.search(r'INFO|info|slow query',l)]
  print(f.split('/')[-1],len(hits),[h[0] for h in hits][:3],hits[-1][0] if hits else '')
  for h in hits[:2]: print(h[1][:180])