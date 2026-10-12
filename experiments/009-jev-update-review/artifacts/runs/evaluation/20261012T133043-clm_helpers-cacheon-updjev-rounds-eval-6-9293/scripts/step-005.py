import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: no board/changes. Slow-query WARN=noise. ledger-svc 429 upstream=fx-rates round-01/logs/ledger-svc.log:11,17,19,32,42,62.\nR2: board.md:3 Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing; board.md:4 follow-up OPEN CAPACITY_REVIEW. changes.md:4 CHG-120 APPLIED pricing-svc batch_size=0 (BAD_CONFIG_ROLLOUT candidate); CHG-121 payments no config. R2 logs: inventory 429 fx-rates round-02/logs/inventory-svc.log:18-38,46-63; ledger round-02/logs/ledger-svc.log:6-23,42-56. No pricing errors seen in R2 logs.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import os
print(os.listdir('/task/fixtures'))