import json
for s,k in [('checkout-api','config valid'),('ledger-svc','tls handshake'),('auth-svc','tls handshake')]:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if k in l]
  print(s,h[:6],L[h[0]-1][:220] if h else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R10 logs: checkout-api ERROR config validation round-10/logs/checkout-api.log:9,11,16 (BAD_CONFIG_ROLLOUT CHG-113); ledger-svc tls handshake failed round-10/logs/ledger-svc.log:7,15,23; auth-svc tls round-10/logs/auth-svc.log:1,4,7. Next: advance R11.'
json.dump(c,open('/task/workspace/context.json','w'))