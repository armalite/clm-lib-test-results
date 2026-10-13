import json
c=json.load(open('/task/workspace/context.json'))
b=c['entries'][0]['body']+"\nR4: board.md:3 Thread B inventory-svc suspected CERT_EXPIRED ongoing; but inventory-svc.log:16-70 ERROR dns lookup failed host=kms.internal SERVFAIL (actually DNS_RESOLUTION?). board.md:4 FU OPEN CAPACITY_REVIEW. changes CHG-131 TLS ticket rotation (irrelevant). pricing.log:11-58, search.log:10-79 still 429 sms-gateway. checkout/shipping clean."
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]}
json.dump(c,open('/task/workspace/context.json','w'))