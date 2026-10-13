import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[f'{i+1}:{l[:150]}' for i,l in enumerate(L) if re.search('ERROR|FATAL|429|SERVFAIL',l)]
  print(s,len(h));print('\n'.join(h[:4]))