import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md:3 CHG-110 APPLIED TLS ticket rotation hourly; :4 CHG-113 APPLIED checkout-api 7.35.8 sets db.pool_max=-4 (invalid -> BAD_CONFIG_ROLLOUT candidate); :5 CHG-114 auth-svc no cfg. Logs: services shipping-svc, checkout-api, auth-svc, ledger-svc, search-api (+maybe more). Slow-query WARNs everywhere = noise. search-api disk usage high /var/data 91-97% (round-01/logs/search-api.log:4,12,38,48) -> DISK_PRESSURE candidate. Filter out slow query lines in future scans.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import os
b='/task/fixtures/round-01/logs/'
for f in os.listdir(b):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'disk usage' not in l:print(f,i,l.rstrip()[:150])
