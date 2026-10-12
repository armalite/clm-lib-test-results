import json,glob
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
  for i,l in enumerate(open(p),1):
    if 'ERROR' in l or 'pool' in l.lower(): print(p.split('/')[-1],i,l.strip()[:130])
note='R1: changes.md:3 CHG-110 APPLIED TLS ticket rotation; :4 CHG-113 APPLIED checkout-api db.pool_max=-4 (suspect BAD_CONFIG_ROLLOUT, unconfirmed); :5 CHG-114 auth-svc no config. slow-query WARNs = noise. search-api disk 91-97% (round-01/logs/search-api.log:4,12,38,48).\nR2: board.md:3 Thread A DISK_PRESSURE search-api + shipping-svc ongoing; board.md:4 follow-up OPEN CUSTOMER_COMMS. changes.md:3 CHG-117 dashboards (irrelevant).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))