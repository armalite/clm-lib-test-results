import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board Thread B opened payments-svc CACHE_STAMPEDE ongoing (round-04/board.md:3) BUT logs show 429 upstream=fx-rates in payments-svc (round-04/logs/payments-svc.log:1-25, lines 1,3,7,25,31,45..79) and checkout-api (round-04/logs/checkout-api.log:9-62) -> likely UPSTREAM_RATE_LIMIT. changes CHG-133 APPLIED TLS ticket rotation hourly (round-04/changes.md:3, watch CERT). Pool WARNs continue auth-svc.log:7-81, search-api.log:4-83. notify-worker clean.'})
json.dump(c,open('/task/workspace/context.json','w'))