import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search(r'WARN|ERROR|429|exhaust|fail|invalid',l,re.I) and 'slow' not in l.lower(): print(s,i,l.strip()[:150])