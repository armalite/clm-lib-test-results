import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
n.append({'id':'n4','role':'note','body':'R4: board empty. auth-svc cert_expired sso.example.net lines 6-77; shipping-svc ALSO cert_expired sso lines 3-66 (round-04/logs/shipping-svc.log) -> CERT incident services auth-svc+shipping-svc. DNS rates.internal continues checkout-api 1-71, inventory 32-75. Next: advance to round 5.'})
c['entries']=n
json.dump(c,open('/task/workspace/context.json','w'))