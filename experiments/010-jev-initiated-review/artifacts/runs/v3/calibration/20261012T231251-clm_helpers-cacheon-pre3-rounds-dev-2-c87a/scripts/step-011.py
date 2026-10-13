import re
b='/task/fixtures/round-03/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search('ERROR|FATAL|CRIT',l) and 'slow query' not in l.lower(): print(s,i,l.strip()[:150])