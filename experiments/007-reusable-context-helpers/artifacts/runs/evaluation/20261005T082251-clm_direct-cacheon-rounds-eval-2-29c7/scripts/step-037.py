import re
b='/task/fixtures/round-12/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['inventory-svc','ledger-svc','pricing-svc','auth-svc','payments-svc']:
  hits=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('SERVFAIL|dns|config validation|tls|ERROR|error',l)]
  print(s,len(hits),hits[:15])