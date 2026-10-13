import re
b='/task/fixtures/round-12/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['shipping-svc','inventory-svc','checkout-api']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if not re.search('slow query|request ok|gc|health|heartbeat',l,re.I):print(s,i,l.rstrip()[:150])