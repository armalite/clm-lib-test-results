import json,re
n='R1: board empty. r1/changes.md:3 CHG-113 APPLIED pricing-svc 3.22.4 cache.ttl_s=-1 (suspicious); CHG-110/CHG-115(r2 changes.md:3) retry budget=1 noise. R2: board.md:3 Follow-up OPEN CAPACITY_REVIEW. search-api r2 ERROR tls handshake failed peer=sso.example.net certificate_expired lines 11,15,19,24,27... (CERT_EXPIRED). Other svcs r2 clean. Filter noise: slow query|request ok|heartbeat|gc |health ok.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-02/logs/search-api.log'),1):
    if i>27 and not re.search(r'slow query|request ok|heartbeat|gc |health ok',l,re.I):print(i,l.rstrip()[:130])