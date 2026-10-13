import json
e=[]
def a(i,b):e.append({'id':i,'role':'note','body':b})
a('n1','Round1: board empty. changes: CHG-111 PROPOSED (not applied) round-01/changes.md:3; CHG-113 APPLIED round-01/changes.md:4 build 4.33.8 checkout-api sets feature.batch_size=0 (BAD_CONFIG_ROLLOUT candidate, no errors yet); CHG-114 APPLIED line5 inventory-svc. Baseline WARN slow query 200-450ms is noise.')
a('n2','Round2: board round-02/board.md:3 Follow-up OPEN VENDOR_TICKET; :4 OPEN POSTMORTEM_DRAFT. CHG-116 APPLIED log sampling (irrelevant). pricing-svc 429 upstream=sms-gateway round-02/logs/pricing-svc.log lines 4-73.')
a('n3','Round3: board round-03/board.md:3 Thread A UPSTREAM_RATE_LIMIT pricing-svc + search-api, ongoing. 429 sms-gateway in round-03/logs/pricing-svc.log:4-64 and search-api.log:8-79.')
a('n4','Round4: board round-04/board.md:3 Thread B inventory-svc suspected CERT_EXPIRED ongoing, BUT logs show DNS SERVFAIL host=kms.internal round-04/logs/inventory-svc.log:16-70 (real cause likely DNS_RESOLUTION). :4 Follow-up OPEN CAPACITY_REVIEW. CHG-131 APPLIED TLS ticket rotation (irrelevant).')
a('n5','Round5: board empty; CHG-137 dashboards (irrelevant). inventory DNS SERVFAIL kms.internal round-05/logs/inventory-svc.log:20-67; 429s pricing-svc.log:1-73, search-api.log:6-77. checkout/shipping clean. Next: advance to round 6.')
json.dump({'format':'clm-context/v1','entries':e},open('/task/workspace/context.json','w'))