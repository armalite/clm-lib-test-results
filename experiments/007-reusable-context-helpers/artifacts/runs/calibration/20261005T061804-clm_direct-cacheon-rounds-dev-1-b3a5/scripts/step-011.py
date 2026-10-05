import json
c=json.load(open('/task/workspace/context.json'))
n4='R4: board.md:3 Thread B CACHE_STAMPEDE payments-svc ongoing (logs show 429 fx-rates instead, no cache errors -> real cause likely UPSTREAM_RATE_LIMIT). changes.md:3 CHG-133 APPLIED TLS ticket rotation. payments-svc.log:1,3,7,25,31,45 429 fx-rates; checkout-api.log:9,19,50,53,59,62 429 fx-rates. auth-svc.log:7,9,19,81 pool WARN; search-api.log:4,11,83 pool WARN.'
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]+[{'id':'n4','role':'note','body':n4}]
json.dump(c,open('/task/workspace/context.json','w'))