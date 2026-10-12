import json,os
n1={'id':'n1','role':'note','body':'R1: changes.md:3 CHG-110 TLS ticket hourly; :4 CHG-113 checkout-api build 7.35.8 sets db.pool_max=-4 (BAD_CONFIG suspect); :5 CHG-114 auth-svc no cfg. Logs: slow-query WARNs noise. search-api disk used_pct 91-97 (round-01/logs/search-api.log:4,12,38,48).'}
n2={'id':'n2','role':'note','body':'R2: board.md:3 Thread A DISK_PRESSURE search-api+shipping-svc ongoing; board.md:4 follow-up OPEN CUSTOMER_COMMS; changes.md:3 CHG-117 dashboards (noise).'}
json.dump({'format':'clm-context/v1','entries':[n1,n2]},open('/task/workspace/context.json','w'))
b='/task/fixtures/round-02/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:print(f,i,l.rstrip()[:140])