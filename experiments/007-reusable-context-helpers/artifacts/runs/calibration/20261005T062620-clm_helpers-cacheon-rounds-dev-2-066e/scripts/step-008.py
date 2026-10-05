import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id'] in('n1','n2')]
n.append({'id':'n3','role':'note','body':'R3: board.md:3 Thread B auth-svc suspected DB_POOL_EXHAUSTED ongoing, BUT logs show auth-svc tls certificate_expired peer=sso.example.net (round-03/logs/auth-svc.log 6,9,15,21,25,26,33,48,64,72) -> likely CERT_EXPIRED. changes.md:3 CHG-126 PROPOSED (ignore). DNS rates.internal continues checkout-api 33-74, inventory 3-50. Next: advance to round 4.'})
c['entries']=n
json.dump(c,open('/task/workspace/context.json','w'))