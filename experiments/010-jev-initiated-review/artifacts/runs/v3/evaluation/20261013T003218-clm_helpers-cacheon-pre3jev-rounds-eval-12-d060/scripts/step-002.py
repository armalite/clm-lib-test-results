import re
b='/task/fixtures/round-01/logs/'
for s in ['checkout-api','pricing-svc','ledger-svc','inventory-svc','search-api']:
  L=open(b+s+'.log').read().splitlines()
  print(s,len(L))
  for i,l in enumerate(L,1):
    if re.search(r'ERROR|WARN|error|fail|429|timeout',l):print(i,l[:160])
