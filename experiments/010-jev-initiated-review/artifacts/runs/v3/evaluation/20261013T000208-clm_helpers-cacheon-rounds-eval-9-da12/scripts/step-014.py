import sys,re;sys.path.insert(0,'/task/workspace')
import cm
b='/task/fixtures/round-05/logs/'
for s,p in [('shipping-svc','tls'),('shipping-svc','disk'),('notify-worker','disk'),('inventory-svc','dns'),('ledger-svc','dns')]:
  L=[i for i,l in enumerate(open(b+s+'.log'),1) if p in l and 'INFO' not in l]
  print(s,p,L[:1],L[-1:],len(L))
import json
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
cm.setnotes(n+' R5: round-05/board.md:3 Thread B +notify-worker; board.md:4 Thread D CERT_EXPIRED shipping-svc ongoing (shipping tls peer=bank-api certificate_expired); board.md:5 OPEN VENDOR_TICKET. search-api still clean.')