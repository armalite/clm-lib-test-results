import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board Thread B auth-svc DB_POOL_EXHAUSTED ongoing (round-03/board.md:3) BUT logs show CERT_EXPIRED peer=sso.example.net round-03/logs/auth-svc.log:6,9,15,21,25,26,33,48,64,72 (board likely wrong). DNS continues checkout round-03/logs/checkout-api.log:33,74; inventory round-03/logs/inventory-svc.log:3,50. CHG-126 PROPOSED (ignore). Next: advance to R4.'})
json.dump(c,open('/task/workspace/context.json','w'))