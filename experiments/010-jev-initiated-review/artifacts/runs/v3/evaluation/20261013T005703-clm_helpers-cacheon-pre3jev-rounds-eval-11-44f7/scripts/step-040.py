import json
ctx=json.load(open('/task/workspace/context.json'))
n1=[e for e in ctx['entries'] if e['id']=='n1'][0]
b=n1['body'].replace(' Next: advance to R9.','')
b+='\nR9: board Thread D closed false alarm, not incident (round-09/board.md:3). No changes.md. inventory-svc dns SERVFAIL kms.internal continues (round-09/logs/inventory-svc.log:7,13,22,44,66,75,80); NEW shipping-svc also dns lookup failed kms.internal (round-09/logs/shipping-svc.log:17,38,57,58,66,78) -> Thread B DNS affects inventory-svc+shipping-svc. Incidents so far: A UPSTREAM_RATE_LIMIT pricing+search resolved; B DNS_RESOLUTION ongoing. Next: advance to R10.'
n1['body']=b
ctx['entries']=[n1]
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')