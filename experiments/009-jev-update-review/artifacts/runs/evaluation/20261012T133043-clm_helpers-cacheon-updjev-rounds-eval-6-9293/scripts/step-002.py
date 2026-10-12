import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty, no changes.md. Slow-query WARNs everywhere = noise. ledger-svc 429 upstream=fx-rates at round-01/logs/ledger-svc.log:11,17,19,32,42,62 (UPSTREAM_RATE_LIMIT candidate). pricing-svc log truncated after line 42; check rest. Filter out "slow query" in greps.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-01/logs/'
import os
for f in os.listdir(b):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and '429' not in l:print(f,i,l[:150])