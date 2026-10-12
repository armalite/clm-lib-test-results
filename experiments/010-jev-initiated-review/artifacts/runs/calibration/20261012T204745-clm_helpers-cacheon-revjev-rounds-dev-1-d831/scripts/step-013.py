import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search(r'ERROR|WARN|429|exhaust|cert|dns|lag|memory|disk|inflight',l,re.I) and not re.search('slow query',l,re.I): print(s,i,l.strip()[:150])