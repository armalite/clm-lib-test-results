import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: ledger-svc 429 upstream=fx-rates round-01/logs/ledger-svc.log:11,17,19,32,42,62. Slow query WARNs = noise.'},{'id':'n2','role':'note','body':'R2: board round-02/board.md:3 Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing; :4 follow-up OPEN CAPACITY_REVIEW. changes round-02/changes.md:4 CHG-120 APPLIED pricing-svc feature.batch_size=0 (possible BAD_CONFIG_ROLLOUT); :5 CHG-121 payments no config.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f)):
    if 'ERROR' in l or ' 429' in l or 'batch' in l: print(f.split('/')[-1],i+1,l.strip()[:120])