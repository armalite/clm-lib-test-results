import json
e=[]
def a(i,b):e.append({'id':i,'role':'note','body':b})
a('n1','R1: CHG-111 PROPOSED round-01/changes.md:3; CHG-113 APPLIED round-01/changes.md:4 checkout-api feature.batch_size=0 (BAD_CONFIG candidate, no errors yet); CHG-114 APPLIED :5 inventory-svc. slow query WARN = noise.')
a('n2','R2: board round-02/board.md:3 OPEN VENDOR_TICKET; :4 OPEN POSTMORTEM_DRAFT. pricing 429 sms-gateway.')
a('n3','R3: round-03/board.md:3 Thread A UPSTREAM_RATE_LIMIT pricing-svc+search-api ongoing; logs round-03/logs/pricing-svc.log:4-64, search-api.log:8-79.')
a('n4','R4: round-04/board.md:3 Thread B inventory-svc suspected CERT_EXPIRED, logs show DNS SERVFAIL kms.internal round-04/logs/inventory-svc.log:16-70 -> DNS_RESOLUTION. :4 OPEN CAPACITY_REVIEW.')
a('n6','R6: round-06/board.md:3 Thread A mitigated; :4 CLOSED VENDOR_TICKET. round-06/changes.md:4 CHG-150 APPLIED mitigation pricing. 429s gone R6. inventory DNS SERVFAIL continues round-06/logs/inventory-svc.log:3-81. others clean. Next: advance to R7.')
json.dump({'format':'clm-context/v1','entries':e},open('/task/workspace/context.json','w'))