import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'] in('n1','n2')]
keep.append({'id':'n3','role':'note','body':'Round3: board Thread A opened UPSTREAM_RATE_LIMIT pricing-svc + search-api, ongoing (round-03/board.md:3). 429 upstream=sms-gateway in round-03/logs/pricing-svc.log:4,7,8,9,25,40,58,63,64 and search-api.log:8,14,23,31,35-37,46,56,60,72,73,79. Slow query WARNs are noise. No r3 changes.md.'})
keep.append({'id':'n4','role':'note','body':'Round4: board Thread B opened inventory-svc suspected CERT_EXPIRED ongoing (round-04/board.md:3); follow-up OPEN CAPACITY_REVIEW (board.md:4). CHG-131 APPLIED TLS session ticket rotation hourly (round-04/changes.md:3). BUT logs show inventory-svc ERROR dns lookup failed host=kms.internal SERVFAIL at round-04/logs/inventory-svc.log:16,20,34,39,44,64,70 -> actual DNS_RESOLUTION likely. 429 sms-gateway continues pricing-svc.log:11,15,27,53,57,58 and search-api.log:10,11,14,18,34,35,44,47. Round 4 done; next: advance.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')