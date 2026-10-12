import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R6 logs: ledger heap WARN round-06/logs/ledger-svc.log:2-52; payments disk round-06/logs/payments-svc.log:3-83. Next: advance to R7.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')