import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md:3 CHG-109 APPLIED TLS ticket rotation hourly; :4 CHG-113 APPLIED notify-worker build 8.20.0 sets db.pool_max=-4 (suspect BAD_CONFIG_ROLLOUT); :5 CHG-114 inventory-svc 8.20.0 no config. Logs: only routine slow query WARNs in all 5 services (notify-worker,pricing-svc,auth-svc,payments-svc,inventory-svc).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for p in glob.glob('/task/fixtures/round-01/logs/*'):
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or 'pool' in l) and 'slow query' not in l: print(p[-20:],i,l[:150].rstrip())