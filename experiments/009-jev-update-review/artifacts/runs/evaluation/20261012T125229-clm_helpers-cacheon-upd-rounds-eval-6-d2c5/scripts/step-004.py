import json
b='/task/fixtures/round-02/logs/'
import os
for f in sorted(os.listdir(b)):
  n=0
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l:
      n+=1
      if n<=4: print(f,i,l.rstrip()[:140])
  print(f,'count',n)
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. slow query WARNs = noise. ledger-svc 429 upstream=fx-rates round-01/logs/ledger-svc.log:11,17,19,32,42,62.\nR2: board.md:3 Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing; board.md:4 follow-up OPEN CAPACITY_REVIEW. changes.md:4 CHG-120 APPLIED pricing-svc batch_size=0 (BAD_CONFIG candidate); :5 CHG-121 payments no config.'}]}
json.dump(c,open('/task/workspace/context.json','w'))