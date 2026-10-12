import re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['notify-worker','checkout-api','payments-svc','auth-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('429|validation|exhaust|ERROR|error',l)]
  print(s,h[:12])
  if h: print(L[h[0]-1][:200])