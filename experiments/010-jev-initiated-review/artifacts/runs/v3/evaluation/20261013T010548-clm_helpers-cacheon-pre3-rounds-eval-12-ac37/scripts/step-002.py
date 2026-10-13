import re
for s in ['checkout-api','pricing-svc','ledger-svc','inventory-svc','search-api']:
  L=open(f'/task/fixtures/round-01/logs/{s}.log').read().splitlines()
  print('==',s,L[0][:150])
  for i,l in enumerate(L,1):
    if re.search(r'ERROR|WARN|error|fail|429|ttl',l):print(i,l[:150])