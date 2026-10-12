import json,os
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: no board/changes. Slow-query WARN=noise. ledger-svc 429 upstream=fx-rates round-01/logs/ledger-svc.log:11,17,19,32,42,62.\nR2: board.md:3 Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing; board.md:4 follow-up OPEN CAPACITY_REVIEW. changes.md:4 CHG-120 APPLIED pricing-svc batch_size=0 (BAD_CONFIG_ROLLOUT candidate); CHG-121 payments no config.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-02/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l:print(f,i,l.strip()[:130])