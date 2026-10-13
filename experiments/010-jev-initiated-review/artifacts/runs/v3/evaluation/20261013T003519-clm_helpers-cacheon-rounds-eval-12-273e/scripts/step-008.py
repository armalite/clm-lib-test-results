import json
n1='R1: board empty. changes.md:3 CHG-110 APPLIED retry budget=1; :4 CHG-113 APPLIED pricing-svc build 3.22.4 sets cache.ttl_s=-1 (suspect BAD_CONFIG_ROLLOUT); :5 CHG-114 ledger-svc 3.22.4 no config. Logs: only routine slow-query WARNs, noise. Scan: print md fully + ERROR/WARN lines excluding slow query.'
n2='R2: board.md:3 follow-up OPEN CAPACITY_REVIEW. changes CHG-115 benign. search-api.log:11-57 ERROR tls sso.example.net certificate_expired.'
n3='R3: board.md:3 Thread A CERT_EXPIRED search-api+inventory-svc ongoing; :4 OPEN RUNBOOK_UPDATE; :5 OPEN POSTMORTEM_DRAFT. changes CHG-126 benign. inventory-svc.log:1-75 & search-api.log:9-78 cert_expired errors.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2},{'id':'n3','role':'note','body':n3}]}
json.dump(c,open('/task/workspace/context.json','w'))