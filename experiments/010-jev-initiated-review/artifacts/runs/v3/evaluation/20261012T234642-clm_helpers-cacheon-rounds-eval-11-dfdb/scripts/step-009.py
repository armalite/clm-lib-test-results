import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board Thread A opened UPSTREAM_RATE_LIMIT pricing-svc + search-api ongoing (round-03/board.md:3). 429 sms-gateway: round-03/logs/pricing-svc.log:4,7,8,9; round-03/logs/search-api.log:8,14,23,31. No changes.md. Next: advance to R4.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')