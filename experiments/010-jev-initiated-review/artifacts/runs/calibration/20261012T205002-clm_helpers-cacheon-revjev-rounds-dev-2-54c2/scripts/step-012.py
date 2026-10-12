import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
keep.append({'id':'n4','role':'note','body':'R4: board empty. CERT_EXPIRED sso.example.net now auth-svc (round-04/logs/auth-svc.log:6-77) AND shipping-svc (shipping-svc.log:3-66). DNS continues checkout-api.log:1-71, inventory-svc.log:32-75. search-api no errors. Next: advance.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')