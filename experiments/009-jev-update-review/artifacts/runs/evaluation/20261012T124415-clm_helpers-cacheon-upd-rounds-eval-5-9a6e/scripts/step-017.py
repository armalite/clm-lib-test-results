import json,re
for s in ['checkout-api','auth-svc','search-api','shipping-svc','ledger-svc']:
  L=open(f'/task/fixtures/round-06/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'ERROR|pool|certif|disk|memory|heap',l,re.I) and 'slow query' not in l]
  print(s,len(h));[print(x) for x in h[:5]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=' R6: board.md:3 Thread D DB_POOL_EXHAUSTED checkout-api ongoing (likely really CHG-113 BAD_CONFIG_ROLLOUT pool_max=-4); CHG-147 dashboards ignore.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))