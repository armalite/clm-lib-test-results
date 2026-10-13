import re
print(open('/task/fixtures/round-07/board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-07/logs/{s}.log').read().splitlines()
  c={}
  for i,l in enumerate(L,1):
    if re.search('ERROR|WARN|error|warn',l):
      k=re.sub(r'[0-9]','',l)[-60:]
      c.setdefault(k,[]).append(i)
  for k,v in c.items(): print(s,len(v),v[0],v[-1],k)