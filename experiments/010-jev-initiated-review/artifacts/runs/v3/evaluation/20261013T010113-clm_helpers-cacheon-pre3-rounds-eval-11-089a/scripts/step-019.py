import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'] in('n1','n2')]
keep.append({'id':'n3','role':'note','body':'Round3: board Thread A opened UPSTREAM_RATE_LIMIT pricing-svc + search-api, ongoing (round-03/board.md:3). 429 upstream=sms-gateway in round-03/logs/pricing-svc.log:4,7,8,9,25,40,58,63,64 and search-api.log:8,14,23,31,35-37,46,56,60,72,73,79. Slow query WARNs everywhere are noise. shipping-svc output truncated (only slow queries seen); no changes.md checked yet for r3 -> check r3 changes.md + shipping errors, then advance.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
import os
p='/task/fixtures/round-03/changes.md'
print(open(p).read() if os.path.exists(p) else 'no changes')
for i,l in enumerate(open('/task/fixtures/round-03/logs/shipping-svc.log'),1):
    if 'ERROR' in l: print(i,l.strip()[:100])