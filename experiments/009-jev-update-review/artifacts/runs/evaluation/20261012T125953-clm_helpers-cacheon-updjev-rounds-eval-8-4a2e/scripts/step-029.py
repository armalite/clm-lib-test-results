import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+=' R10 logs: notify-worker ERROR config validation failed key db.* (round-10/logs/notify-worker.log:2,6,12,15,19,21,22,26,28,37,50) -> Thread C likely BAD_CONFIG_ROLLOUT via CHG-113 (round-01/changes.md:4). Next: advance to R11.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')