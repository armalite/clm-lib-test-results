import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|error|429|exhaust|fail|invalid',l) and 'slow' not in l]
  print(s,len(h),[x[0] for x in h][:30])
  for x in h[:2]: print(' ',x[0],x[1][:200])