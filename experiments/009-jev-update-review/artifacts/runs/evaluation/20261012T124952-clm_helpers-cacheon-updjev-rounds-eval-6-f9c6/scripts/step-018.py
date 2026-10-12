import json
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R6 logs: ledger-svc heap high rss_mb ledger-svc.log:2-52 (6 hits); payments-svc disk used_pct=96 payments-svc.log:3-83 (10 hits). Disk on payments not on board yet (untracked incident).'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
print('ok')