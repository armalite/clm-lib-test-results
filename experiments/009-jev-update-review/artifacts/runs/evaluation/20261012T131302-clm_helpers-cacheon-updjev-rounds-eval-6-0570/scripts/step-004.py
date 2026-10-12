import json,os
b='/task/fixtures/round-02/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l or '429' in l) and 'slow query' not in l:print(f,i,l.rstrip()[:130])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: no board. Slow query WARNs = noise. ledger-svc 429 upstream=fx-rates round-01/logs/ledger-svc.log:11,17,19,32,42,62.\nR2: board Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing (round-02/board.md:3); follow-up OPEN CAPACITY_REVIEW (board.md:4). changes: CHG-120 APPLIED pricing-svc 4.35.8 feature.batch_size=0 (round-02/changes.md:4) -> watch BAD_CONFIG_ROLLOUT; CHG-121 payments no config (changes.md:5); CHG-116 log sampling (changes.md:3).'}]}
json.dump(c,open('/task/workspace/context.json','w'))