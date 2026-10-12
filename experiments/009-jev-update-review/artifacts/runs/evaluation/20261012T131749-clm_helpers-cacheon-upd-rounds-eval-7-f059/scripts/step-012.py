import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R4 logs: checkout-api disk usage high /var/data used_pct 93-98 at round-04/logs/checkout-api.log:7,17,19,28 (10 hits) -> DISK_PRESSURE, board says CACHE_STAMPEDE (likely wrong). 429 tax-provider continues search-api.log:1,14,32,41; shipping-svc.log:7,18,27,38. ledger/payments clean. R4 done; next advance.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')