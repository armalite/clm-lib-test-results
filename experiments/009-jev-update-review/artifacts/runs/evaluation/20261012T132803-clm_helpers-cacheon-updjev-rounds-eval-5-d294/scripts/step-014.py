import json,re
for f in ['checkout-api','auth-svc','search-api','shipping-svc','ledger-svc']:
  L=open(f'/task/fixtures/round-06/logs/{f}.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|pool|disk|cert|FATAL',l,re.I) and 'slow' not in l]
  print(f,len(h));[print(i,l[:150]) for i,l in h[:4]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR6: board.md:3 Thread D DB_POOL_EXHAUSTED checkout-api ongoing (likely from CHG-113 pool_max=-4 -> BAD_CONFIG_ROLLOUT?). changes.md:3 CHG-147 dashboards irrelevant.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))