import json,glob
b='/task/fixtures/round-01/logs/'
for p in glob.glob(b+'*'):
  for i,l in enumerate(open(p),1):
    if 'ERROR' in l: print(p[-20:],i,l.strip()[:140])
note='R1: board empty. changes.md:3 CHG-110 APPLIED TLS ticket rotation hourly; :4 CHG-113 APPLIED build 7.35.8 checkout-api sets db.pool_max=-4 (suspect BAD_CONFIG_ROLLOUT); :5 CHG-114 auth-svc no config. Logs: slow-query WARNs everywhere (noise). search-api disk usage /var/data 91-97% (round-01/logs/search-api.log:4,12,38,48) -> possible DISK_PRESSURE.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))