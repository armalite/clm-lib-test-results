import json
c=json.load(open('context.json'))
e={x['id']:x for x in c['entries']}
n4='R4: board Thread B opened CACHE_STAMPEDE payments-svc ongoing (round-04/board.md:3) - but logs show 429 fx-rates (UPSTREAM_RATE_LIMIT) in payments-svc round-04/logs/payments-svc.log:1-59 and checkout-api round-04/logs/checkout-api.log:9-62; no cache miss lines seen. changes CHG-133 APPLIED TLS ticket rotation (round-04/changes.md:3, maybe noise). DB pool exhausted continues auth-svc round-04/logs/auth-svc.log:7-26, search-api round-04/logs/search-api.log:4-20.'
c['entries']=[e['n1'],e['n2'],e['n3'],{'id':'n4','role':'note','body':n4}]
json.dump(c,open('context.json','w'))
print('ok')