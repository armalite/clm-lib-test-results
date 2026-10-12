import json,re
L=open('/task/fixtures/round-06/logs/checkout-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if re.search(r'pool|config|ERROR',l,re.I): print(i,l[:160])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R6: Thread D opened DB_POOL_EXHAUSTED checkout-api ongoing (round-06/board.md:3); likely really BAD_CONFIG_ROLLOUT via CHG-113 pool_max=-4. CHG-147 dashboards irrelevant.'})
json.dump(c,open('/task/workspace/context.json','w'))