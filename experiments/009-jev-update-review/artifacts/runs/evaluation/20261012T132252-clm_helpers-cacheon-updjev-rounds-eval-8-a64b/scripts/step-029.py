import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith('s28')]
for e in c['entries']:
  if e['id']=='n10': e['body']+=' R10 logs: notify-worker ERROR config validation failed db.pool_max=-4 (round-10/logs/notify-worker.log:2,6,12) -> C = BAD_CONFIG_ROLLOUT from CHG-113 (round-01/changes.md:4). Next: advance to R11.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')