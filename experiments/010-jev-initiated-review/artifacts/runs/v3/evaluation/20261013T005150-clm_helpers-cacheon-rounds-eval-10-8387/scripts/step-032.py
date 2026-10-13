import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-11/'+f),1):print(f,i,l.rstrip())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=[i for i,l in enumerate(open(f'/task/fixtures/round-11/logs/{s}.log'),1) if re.search('ERR|429|fail|SERVFAIL',l)]
  print(s,len(L),L[:3],L[-2:])