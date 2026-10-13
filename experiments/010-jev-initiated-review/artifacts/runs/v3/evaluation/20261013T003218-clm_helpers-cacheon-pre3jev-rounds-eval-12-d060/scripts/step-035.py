import json
ctx=json.load(open('/task/workspace/context.json'))
n=[e for e in ctx['entries'] if e['id']=='n1'][0]
b=n['body']
b=b.replace(' Next: advance to r8.','')
b+=" R8: board.md:3 Thread A RESOLVED; board.md:4 Thread B cause revised UPSTREAM_RATE_LIMIT (ledger-svc+checkout-api, ongoing); board.md:5 Thread C opened pricing-svc ongoing cause unknown. No changes.md. Logs: pricing-svc config validation failed cache.ttl_s=-1 build 3.22.4 round-08/logs/pricing-svc.log:5,17,28,38 (=BAD_CONFIG_ROLLOUT from CHG-113 round-01/changes.md:4). checkout-api 429 round-08/logs/checkout-api.log:26,27,37,51; ledger-svc 429 round-08/logs/ledger-svc.log:9,12,21,30. inventory/search clean. Next: advance to r9."
n['body']=b
ctx['entries']=[n]
json.dump(ctx,open('/task/workspace/context.json','w'))