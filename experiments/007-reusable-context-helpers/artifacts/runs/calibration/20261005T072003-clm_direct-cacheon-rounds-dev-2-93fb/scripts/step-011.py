import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3')]
e.append({'id':'n4','role':'note','body':'R4: board empty (no changes). auth-svc.log:6-77 and shipping-svc.log:3-66 tls certificate_expired sso.example.net (CERT_EXPIRED now auth-svc+shipping-svc). checkout-api.log:1-71, inventory-svc.log:32-75 SERVFAIL continue. search clean. R4 done; next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))