import json
ctx=json.load(open('/task/workspace/context.json'))
n1=[e for e in ctx['entries'] if e['id']=='n1'][0]
b=n1['body'].split('\nR10:')[0]
b+='\nR10: board Thread B services += shipping-svc, unchanged otherwise (round-10/board.md:3); Thread C opened checkout-api request failures cause unknown ongoing (round-10/board.md:4). CHG-174 PROPOSED only. checkout-api ERROR config validation failed feature.batch_size=0 (round-10/logs/checkout-api.log:1,4,5,7) -> Thread C = BAD_CONFIG_ROLLOUT from CHG-113 (round-01/changes.md:4). DNS SERVFAIL kms.internal continues inventory-svc.log:2,9,11,20; shipping-svc.log:1,7,8,12. Next: advance to R11.'
n1['body']=b
ctx['entries']=[n1]
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')