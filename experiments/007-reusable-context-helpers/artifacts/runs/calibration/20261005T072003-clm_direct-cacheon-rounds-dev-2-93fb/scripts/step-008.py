import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e.append({'id':'n3','role':'note','body':'R3: round-03/board.md:3 Thread B auth-svc suspected DB_POOL_EXHAUSTED ongoing, BUT logs show auth-svc.log:6-72 tls certificate_expired peer=sso.example.net (real cause likely CERT_EXPIRED). changes.md:3 CHG-126 PROPOSED (ignore). checkout-api.log:33-74, inventory-svc.log:3-50 SERVFAIL continue. search/shipping clean. R3 done; next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))