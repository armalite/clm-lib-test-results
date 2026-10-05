import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for s in ['auth-svc','search-api','shipping-svc','payments-svc','ledger-svc']:
  L=[(i,l) for i,l in enumerate(open(f'/task/fixtures/round-10/logs/{s}.log'),1) if re.search(r'ERROR|cert|config|lag|restart',l,re.I)]
  print(s,len(L),L[0][0] if L else '',L[-1][0] if L else '',L[0][1][:150] if L else '')