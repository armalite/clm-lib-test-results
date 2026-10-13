import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for s in ['checkout-api','ledger-svc','pricing-svc','inventory-svc','search-api']:
  ls=[i for i,l in enumerate(open(f'/task/fixtures/round-10/logs/{s}.log'),1) if re.search('429|cert|ttl|valid|ERROR',l)]
  print(s,ls[:8])