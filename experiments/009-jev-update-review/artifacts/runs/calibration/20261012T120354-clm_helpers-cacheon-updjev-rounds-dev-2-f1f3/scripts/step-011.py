import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board empty. CERT_EXPIRED sso.example.net now auth-svc (round-04/logs/auth-svc.log:6,8,16,39) AND shipping-svc (round-04/logs/shipping-svc.log:3,20,27,34). DNS continues checkout-api round-04/logs/checkout-api.log:1,8,11,13; inventory-svc :32,36,38,43. search-api still no errors. Next: advance to R5.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')