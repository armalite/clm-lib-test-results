import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|429|cache|miss|pool|batch|config|cert|dns|disk|memory|lag',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:6]: print(' ',i,l[:150])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+='\nR3: board Thread B CACHE_STAMPEDE payments-svc ongoing (round-03/board.md:3). CHG-124 APPLIED retry budget GETs=1 (round-03/changes.md:3).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))