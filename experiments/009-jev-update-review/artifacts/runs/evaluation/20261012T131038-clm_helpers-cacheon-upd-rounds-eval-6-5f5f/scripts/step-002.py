import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty, no changes.md. Slow query WARNs everywhere (noise). ledger-svc 429 upstream=fx-rates at round-01/logs/ledger-svc.log:11,17,19,32,42,62 -> candidate UPSTREAM_RATE_LIMIT (ledger-svc). Rest of inventory log not seen (check ERROR lines only next time).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
L=open('/task/fixtures/round-01/logs/inventory-svc.log').read().splitlines()
for i,l in enumerate(L):
  if 'ERROR' in l: print(i+1,l[:150])