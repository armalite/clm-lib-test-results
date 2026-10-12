import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: Thread B opened payments-svc CACHE_STAMPEDE ongoing (round-04/board.md:3) BUT logs show 429 fx-rates in payments-svc (round-04/logs/payments-svc.log:1-59) and checkout-api (round-04/logs/checkout-api.log:9-62) -> likely UPSTREAM_RATE_LIMIT. CHG-133 APPLIED TLS ticket rotation (round-04/changes.md:3) maybe irrelevant. DB pool continues auth-svc round-04/logs/auth-svc.log:7-26, search-api round-04/logs/search-api.log:4-20. Next: advance, scan 05.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')