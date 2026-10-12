import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n10': x['body']+=' Logs R10: ledger-svc.log config validation failed lines 12,13,15,18; checkout-api disk 20,29; payments-svc disk 2,26. R10 scanned; next: advance.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')