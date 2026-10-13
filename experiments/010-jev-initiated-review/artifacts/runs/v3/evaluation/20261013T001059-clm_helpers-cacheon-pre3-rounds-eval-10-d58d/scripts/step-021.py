import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[i+1 for i,l in enumerate(L) if re.search('error|ERROR|WARN|warn|429|fail|FAIL',l)]
  print(s,len(e),e[:3],e[-1:] if e else '')
  if e: print(L[e[0]-1][:200])