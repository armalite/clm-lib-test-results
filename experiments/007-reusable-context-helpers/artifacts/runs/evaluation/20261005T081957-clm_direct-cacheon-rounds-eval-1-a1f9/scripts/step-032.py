import re
b='/task/fixtures/round-11/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','search-api','shipping-svc','payments-svc','ledger-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|error|lag|certificate|ttl',l)]
  print(s,len(h),h[:6]);
  if h: print(L[h[0]-1][:200])