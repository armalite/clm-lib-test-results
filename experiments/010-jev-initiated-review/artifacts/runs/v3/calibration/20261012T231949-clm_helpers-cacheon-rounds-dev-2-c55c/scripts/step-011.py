import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board empty. CERT_EXPIRED sso.example.net now auth-svc round-04/logs/auth-svc.log:6,8,16,39,77 AND shipping-svc round-04/logs/shipping-svc.log:3,20,27,66. DNS continues checkout round-04/logs/checkout-api.log:1,71; inventory round-04/logs/inventory-svc.log:32,75. search-api no errors yet. No changes.md. Next: advance to R5.'})
json.dump(c,open('/task/workspace/context.json','w'))