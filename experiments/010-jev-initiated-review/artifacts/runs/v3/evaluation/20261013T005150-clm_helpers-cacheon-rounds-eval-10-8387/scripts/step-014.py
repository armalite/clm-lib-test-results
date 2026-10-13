import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  bad=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|WARN|error|warn|fail|429',l)]
  print(s,len(bad),bad[0][0] if bad else '',bad[-1][0] if bad else '')
  for i,l in bad[:2]: print(' ',i,l[:160])