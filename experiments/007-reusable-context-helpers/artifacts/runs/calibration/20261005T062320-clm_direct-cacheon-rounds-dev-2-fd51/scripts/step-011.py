import re
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search(r'ERROR|FATAL|WARN',l) and 'slow query' not in l:
      print(s,i,l.strip()[:150])
