import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|disk|pool|FATAL',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md: CHG-110 APPLIED TLS ticket rotation hourly (round-01/changes.md:3); CHG-113 APPLIED build 7.35.8 checkout-api sets db.pool_max=-4 (round-01/changes.md:4) -> likely BAD_CONFIG_ROLLOUT later; CHG-114 auth-svc no config (:5). R1 logs: search-api disk /var/data 92-95% (round-01/logs/search-api.log:4,12).'},{'id':'n2','role':'note','body':'R2: Thread A DISK_PRESSURE search-api + shipping-svc, ongoing (round-02/board.md:3). Follow-up OPEN CUSTOMER_COMMS (round-02/board.md:4). CHG-117 dashboards irrelevant.'}]}
json.dump(c,open('/task/workspace/context.json','w'))