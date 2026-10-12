import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|FATAL|WARN',l) and not re.search('slow query|gc|heartbeat',l)]
  print(s,len(h),[x[0] for x in h][:3],[x[0] for x in h][-1:] if h else '')
  for i,l in h[:2]: print(' ',i,l[:160])