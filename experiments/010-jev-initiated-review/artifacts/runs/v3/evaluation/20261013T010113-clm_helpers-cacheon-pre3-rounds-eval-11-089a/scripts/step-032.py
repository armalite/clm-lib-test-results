import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['checkout-api','inventory-svc','pricing-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|error|FATAL|CRIT',l)]
  print(s,len(e))
  for x in e[:4]:print(x)
  print([i for i,_ in e])