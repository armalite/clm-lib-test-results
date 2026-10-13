import json
ctx=json.load(open('/task/workspace/context.json'))
E=[e for e in ctx['entries'] if e['id'].startswith('n')]
for e in E:
  if e['id']=='n10': e['body']='Round10: board Thread B adds shipping-svc (round-10/board.md:3); Thread C opened checkout-api failures cause unknown ongoing (board.md:4). Verified checkout-api ERROR config validation failed key=feature.batch_size value=0 build=4.33.8 at round-10/logs/checkout-api.log:1,4,5,7,11,21,24,32,44,61 -> BAD_CONFIG_ROLLOUT from CHG-113 (round-01/changes.md:4). CHG-174 PROPOSED ignore. dns errors inventory-svc.log:2,9,11,20,22,30,37,40,42,44 shipping-svc.log:1,7,8. Round 10 done; next: advance.'
ctx['entries']=E
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')