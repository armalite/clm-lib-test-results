import json,os
b='/task/fixtures/round-01/logs/'
for f in os.listdir(b):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and not (f=='ledger-svc.log'):print(f,i,l.rstrip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty, no changes.md. All services: benign slow query WARNs (noise). ledger-svc 429 upstream=fx-rates at round-01/logs/ledger-svc.log:11,17,19,32,42,62 -> UPSTREAM_RATE_LIMIT candidate (ongoing).'}]}
json.dump(c,open('/task/workspace/context.json','w'))