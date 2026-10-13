import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-12/board.md').read())
for s in ['checkout-api','shipping-svc','inventory-svc','pricing-svc','search-api']:
  L=open(f'/task/fixtures/round-12/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'batch_size|dns|SERVFAIL|429|heap',l,re.I)]
  print(s,h[:12])