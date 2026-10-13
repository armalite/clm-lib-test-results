import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','pricing-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  hits=[(i+1,l[:140]) for i,l in enumerate(L) if re.search(r'ERROR|WARN|429|cert|lag|cache|pool|dns|disk|mem',l,re.I) and 'slow' not in l.lower()]
  print(s,len(hits));[print(h) for h in hits[:5]]