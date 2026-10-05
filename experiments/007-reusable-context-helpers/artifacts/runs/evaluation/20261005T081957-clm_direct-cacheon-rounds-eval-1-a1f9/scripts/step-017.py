import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read())
for s in ['auth-svc','ledger-svc','payments-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l[:130]) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn',l) and 'slow query' not in l]
  print(s,len(h))
  for x in h[:5]: print(x)