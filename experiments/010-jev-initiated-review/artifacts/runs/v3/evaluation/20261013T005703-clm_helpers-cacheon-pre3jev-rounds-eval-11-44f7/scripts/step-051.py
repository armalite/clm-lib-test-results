import json
ctx=json.load(open('/task/workspace/context.json'))
n=[e for e in ctx['entries'] if e['id']=='n1'][0]
b=n['body'].replace('\nR10:','\nR10:')
b=b.replace(' Next: advance to R11.','')
b+='\nR11: board Thread B mitigated (round-11/board.md:3); Thread C pods still restarting, ongoing (board.md:4). checkout-api config validation failed batch_size=0 (round-11/logs/checkout-api.log:2,7,30,36,42,47,63,64). DNS SERVFAIL continues inventory-svc.log:68,70; shipping-svc.log:35,41. Next: advance to R12, then final.'
n['body']=b
ctx['entries']=[n]
json.dump(ctx,open('/task/workspace/context.json','w'))
print(len(b))