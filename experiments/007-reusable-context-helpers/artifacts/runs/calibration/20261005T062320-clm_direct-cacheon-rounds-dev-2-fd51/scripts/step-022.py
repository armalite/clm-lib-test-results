import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']+="\nR7: Thread B cause revised CERT_EXPIRED (round-07/board.md:3). Thread D UPSTREAM_RATE_LIMIT search-api ongoing (round-07/board.md:4); 429 tax-provider round-07/logs/search-api.log:4,5,20. CERT auth round-07/logs/auth-svc.log:1,16,24; shipping round-07/logs/shipping-svc.log:10,11,23. Next: advance to R8."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')