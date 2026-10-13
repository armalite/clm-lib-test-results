import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','notify-worker','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if not re.search(r'request ok|gc|health|heartbeat|slow query',l)]
  print(s,len(h));[print(x) for x in h[:4]];print(h[-1] if h else '')