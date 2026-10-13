import json
n1='R1: changes.md:3 CHG-110 APPLIED retry budget GETs=1; :4 CHG-113 APPLIED build 3.22.4 pricing-svc sets cache.ttl_s=-1 (BAD_CONFIG_ROLLOUT candidate, no errors yet); :5 CHG-114 APPLIED 3.22.4 ledger-svc no config.'
n2='R2: board.md:3 Follow-up OPEN CAPACITY_REVIEW. changes.md:3 CHG-115 retry budget. search-api.log 11,15,19 certificate_expired peer=sso.example.net.'
n3='R3: board.md:3 Thread A CERT_EXPIRED search-api + inventory-svc ongoing; :4 OPEN RUNBOOK_UPDATE; :5 OPEN POSTMORTEM_DRAFT. changes.md:3 CHG-126 TLS ticket rotation hourly. inventory-svc.log 1-75 & search-api.log 9-78 cert_expired errors. Open: CAPACITY_REVIEW,RUNBOOK_UPDATE,POSTMORTEM_DRAFT. Next: advance to round 4.'
c={'format':'clm-context/v1','entries':[{'id':k,'role':'note','body':v} for k,v in [('n1',n1),('n2',n2),('n3',n3)]]}
json.dump(c,open('/task/workspace/context.json','w'))