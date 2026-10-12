import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for s in ['checkout-api','ledger-svc','payments-svc','search-api','shipping-svc']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search(r'WARN|ERROR|disk|429|pool|cache',l,re.I): print(s,i,l.strip()[:150])
