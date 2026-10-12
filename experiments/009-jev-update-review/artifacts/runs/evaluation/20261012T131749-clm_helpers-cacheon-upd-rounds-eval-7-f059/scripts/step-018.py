import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R6 logs: checkout-api disk round-06/logs/checkout-api.log:1,11,31,34 (10); 429 stopped in search/shipping (0). ledger line25 heartbeat only. R6 done; next advance.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')