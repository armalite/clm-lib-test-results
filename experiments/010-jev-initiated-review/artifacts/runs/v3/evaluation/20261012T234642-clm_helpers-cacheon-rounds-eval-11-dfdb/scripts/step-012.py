import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board Thread B inventory-svc suspected CERT_EXPIRED ongoing (round-04/board.md:3) BUT logs show dns lookup failed host=kms.internal SERVFAIL round-04/logs/inventory-svc.log:16,20,34,39,44,64,70 -> real cause likely DNS_RESOLUTION. Follow-up OPEN CAPACITY_REVIEW (board.md:4). changes CHG-131 TLS ticket rotation (noise). 429 continues pricing-svc.log:11,15,27,53,57,58; search-api.log:10,11,14,18,34. Next: advance to R5.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')