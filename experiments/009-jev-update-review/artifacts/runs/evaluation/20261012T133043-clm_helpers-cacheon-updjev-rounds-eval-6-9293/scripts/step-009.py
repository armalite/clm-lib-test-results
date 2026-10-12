import json,re
for s in ['payments-svc','pricing-svc','checkout-api']:
  L=open(f'/task/fixtures/round-03/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'ERROR|cache|miss|batch|429|stampede',l,re.I)]
  print(s,len(h));[print(i,l) for i,l in h[:8]]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R3: board.md:3 Thread B CACHE_STAMPEDE payments-svc ongoing; changes.md:3 CHG-124 APPLIED retry budget=1.'
json.dump(c,open('/task/workspace/context.json','w'))