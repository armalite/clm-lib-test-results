import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R7 logs: ledger heap round-07/logs/ledger-svc.log:7-60; payments disk round-07/logs/payments-svc.log:3-62. Next: advance to R8.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')