import json
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' r9 ledger-svc.log:13,20,23,24,27,34,43 ERROR config validation failed db.pool_max=0 => Thread C = BAD_CONFIG_ROLLOUT via CHG-113 (round-01/changes.md:3). Round 9 done; next: advance.'
json.dump(d,open('/task/workspace/context.json','w'))
print('ok')