import json
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1): print(f,i,l.rstrip())
import re
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=[i for i,l in enumerate(open(f'/task/fixtures/round-09/logs/{s}.log'),1) if re.search('certificate|429|max_inflight|SERVFAIL|ERROR',l)]
  print(s,L[:12])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))