import json
b=open('/task/workspace/context.json').read()
d=json.loads(b)
n=[e for e in d['entries'] if e['id']=='n1'][0]['body']
n=n.replace(' Next: advance to R4.','')
n+='\nR4: board empty (no changes). CERT_EXPIRED sso.example.net now also shipping-svc round-04/logs/shipping-svc.log:3,20,66; auth round-04/logs/auth-svc.log:6,77. DNS continues checkout round-04/logs/checkout-api.log:1,71; inventory round-04/logs/inventory-svc.log:32,75. No search errs. Next: advance to R5.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))