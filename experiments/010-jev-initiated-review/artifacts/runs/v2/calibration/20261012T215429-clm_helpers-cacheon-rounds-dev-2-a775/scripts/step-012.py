import json
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace(' Round 3 reviewed; next: advance.','')
n+=' R4: board empty (no changes). No changes.md. CERT_EXPIRED sso.example.net now also shipping-svc round-04/logs/shipping-svc.log:3,66; auth-svc.log:6,77. DNS still failing checkout-api.log:1,71 inventory-svc.log:32,75. search-api no errors. Round 4 reviewed; next: advance.'
c['entries']=[{'id':'notes','role':'note','body':n}]
json.dump(c,open('/task/workspace/context.json','w'))