import json
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: CHG-113 APPLIED round-01/changes.md:3 notify-worker build 7.58.1 sets db.pool_max=0 (suspect BAD_CONFIG_ROLLOUT; check notify-worker logs). CHG-114 inventory no config (line 4). Board r1 empty. pricing-svc CERT_EXPIRED peer=bank-api round-01/logs/pricing-svc.log:8,10,13,22... (ongoing). Slow query WARNs everywhere = noise. TODO: grep notify-worker non-WARN errors r1.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import re
for i,l in enumerate(open('/task/fixtures/round-01/logs/notify-worker.log'),1):
  if 'slow query' not in l and 'INFO' not in l:print(i,l.strip()[:140])