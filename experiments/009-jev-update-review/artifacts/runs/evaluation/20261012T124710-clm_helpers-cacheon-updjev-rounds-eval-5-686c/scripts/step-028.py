import json
for s,ls in [('checkout-api',[9]),('ledger-svc',[7])]:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').readlines()
  for i in ls:print(s,i,L[i-1][:200])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']+'\nR10 logs: checkout config validation failed (round-10/logs/checkout-api.log:9,11,16,18,44,58) -> Thread C likely BAD_CONFIG_ROLLOUT via CHG-113; ledger-svc tls handshake failed (round-10/logs/ledger-svc.log:7,15,23,24,30,40) -> CERT_EXPIRED may spread to ledger; auth tls continues (round-10/logs/auth-svc.log:1,4,7,9).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))