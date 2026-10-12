import json
ctx=json.load(open('/task/workspace/context.json'))
n=[e for e in ctx['entries'] if e['id']=='n1'][0]
n['body']+="\nR4: board round-04/board.md empty of changes. CERT_EXPIRED now also shipping-svc peer=sso.example.net round-04/logs/shipping-svc.log:3,20; auth-svc.log:6,8. DNS continues round-04/logs/checkout-api.log:1,8; inventory-svc.log:32,36. search-api only heartbeat. Next: advance to round 5."
ctx['entries']=[n]
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')