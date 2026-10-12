import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R4 logs: inventory/ledger no 429s (A mitigated); payments disk WARN 94% round-04/logs/payments-svc.log:4-73. Next: advance to R5.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')