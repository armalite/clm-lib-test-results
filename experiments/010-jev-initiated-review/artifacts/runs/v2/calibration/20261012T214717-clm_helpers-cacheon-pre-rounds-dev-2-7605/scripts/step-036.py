import json
ctx=json.load(open('/task/workspace/context.json'))
for e in ctx['entries']:
  if e['id']=='n1':
    e['body']+="\nR7: board Thread B cause revised to CERT_EXPIRED (round-07/board.md:3). Thread D opened UPSTREAM_RATE_LIMIT search-api ongoing (round-07/board.md:4); logs search-api 429 upstream=tax-provider round-07/logs/search-api.log:4,5,20,64 (WARN slow query ms=429 is noise). CERT continues auth/shipping r7. Next: advance to round 8."
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')