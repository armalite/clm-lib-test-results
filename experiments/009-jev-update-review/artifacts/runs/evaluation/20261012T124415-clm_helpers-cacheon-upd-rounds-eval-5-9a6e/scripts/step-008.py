import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|WARN|error|mem|rss|disk|pool|429|cert|dns|lag',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:4]+hits[-2:]: print(' ',i,l[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R3: round-03/board.md:3 Thread B MEMORY_LEAK auth-svc ongoing.'
json.dump(c,open('/task/workspace/context.json','w'))