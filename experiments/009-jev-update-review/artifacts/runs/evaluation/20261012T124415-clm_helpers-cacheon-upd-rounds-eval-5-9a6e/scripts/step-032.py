import json
for s,k in [('checkout-api','config valid'),('ledger-svc','tls handshake'),('auth-svc','tls handshake')]:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if k in l]
  print(s,h[:5])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R11: board.md:3 Thread B +ledger-svc; :4 Thread B mitigated; :5 Thread C still restarting; :6 CLOSED CUSTOMER_COMMS; CHG-179 PROPOSED ignore. Next: advance R12.'
json.dump(c,open('/task/workspace/context.json','w'))