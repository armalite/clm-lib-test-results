import json,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=[(i+1,l.strip()[:110]) for i,l in enumerate(open(f)) if 'INFO' not in l]
  print(f.split('/')[-1],len(L))
  for x in L[:4]:print(x)