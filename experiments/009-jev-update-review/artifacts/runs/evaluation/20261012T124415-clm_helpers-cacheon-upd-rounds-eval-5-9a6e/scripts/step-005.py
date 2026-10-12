import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|disk|/var/data|pool|429|cert|DNS',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: round-01/changes.md:3 CHG-110 APPLIED TLS ticket rotation; :4 CHG-113 APPLIED checkout-api db.pool_max=-4 (suspect BAD_CONFIG_ROLLOUT); search-api /var/data 91-97% (round-01/logs/search-api.log:4,12,38,48). R2: round-02/board.md:3 Thread A DISK_PRESSURE search-api+shipping-svc ongoing; :4 follow-up OPEN CUSTOMER_COMMS. CHG-117 dashboards (irrelevant).'}]}
json.dump(c,open('/task/workspace/context.json','w'))