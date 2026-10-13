import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['pricing-svc','ledger-svc','checkout-api']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search('ERROR|429|config|ttl',l):print(s,i,l.strip()[:120])