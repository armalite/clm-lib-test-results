import re
b='/task/fixtures/round-09/'
print(open(b+'board.md').read())
for s in ['inventory-svc','pricing-svc','checkout-api','search-api','shipping-svc']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search('ERROR|429|SERVFAIL|heap|rss|restart|OOM',l): print(s,i,l.strip()[:110])