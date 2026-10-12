import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board Thread B payments-svc CACHE_STAMPEDE ongoing (round-04/board.md:3) BUT logs show 429 upstream=fx-rates errors payments-svc (round-04/logs/payments-svc.log:1,3,7,25,31,45,48,51; 12x) and checkout-api (round-04/logs/checkout-api.log:9,19,50,53,59,62) -> real cause likely UPSTREAM_RATE_LIMIT. CHG-133 TLS ticket rotation irrelevant. Thread A continues: auth pool WARNs round-04/logs/auth-svc.log:7,9,19,26; search-api round-04/logs/search-api.log:4,11,13,14. Still no notify errors. Next: advance to R5.'})
json.dump(c,open('/task/workspace/context.json','w'))