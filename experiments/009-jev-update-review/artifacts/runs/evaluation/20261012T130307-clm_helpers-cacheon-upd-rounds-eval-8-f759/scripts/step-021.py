import json
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace('Open: does CHG-113 notify-worker bad config show in logs?','R10 logs: notify-worker.log:2-28 config validation failed db.pool_max=-4 -> Thread C = BAD_CONFIG_ROLLOUT (cite round-01/changes.md:4). Next: advance to R11.')
json.dump({'format':'clm-context/v1','entries':[n]},open('/task/workspace/context.json','w'))
print('ok')