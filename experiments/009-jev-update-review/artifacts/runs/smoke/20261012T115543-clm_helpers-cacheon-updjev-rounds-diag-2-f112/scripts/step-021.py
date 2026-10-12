import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R6 logs: inventory disk round-06/logs/inventory-svc.log:13,18,24,42; ledger disk round-06/logs/ledger-svc.log:7,16,21,39; others quiet.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')