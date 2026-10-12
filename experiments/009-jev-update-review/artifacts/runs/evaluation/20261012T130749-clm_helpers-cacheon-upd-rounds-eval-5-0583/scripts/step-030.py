import json
c=json.load(open('/task/workspace/context.json'))
s=c['entries'][0]['body']+' R10 checkout-api logs: config validation failed key=db.pool_max value=-4 (round-10/logs/checkout-api.log:9,11) => Thread C likely BAD_CONFIG_ROLLOUT via CHG-113. Next: advance to R11.'
c['entries']=[{'id':'sum1','role':'summary','body':s}]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-10/board.md').read())