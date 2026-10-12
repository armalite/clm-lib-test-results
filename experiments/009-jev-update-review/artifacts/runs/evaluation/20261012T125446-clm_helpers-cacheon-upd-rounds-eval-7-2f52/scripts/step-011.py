import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
c['entries'][-1]['body']+=' Logs R4: checkout-api.log disk usage high /var/data used_pct 93-98 at lines 7,17,19,28 (DISK_PRESSURE candidate, board says CACHE_STAMPEDE - check). 429 tax-provider continues search-api.log 1,14,32,41; shipping-svc.log 7,18,27,38. R4 scanned; next: advance.'
json.dump(c,open('/task/workspace/context.json','w'))