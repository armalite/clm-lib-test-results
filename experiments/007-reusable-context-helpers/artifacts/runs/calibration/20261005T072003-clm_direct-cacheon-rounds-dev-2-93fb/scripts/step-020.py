import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'].startswith('n')]
e.append({'id':'n7','role':'note','body':'R7: round-07/board.md:3 Thread B cause revised CERT_EXPIRED; :4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing (search-api.log:4-66 429 tax-provider; note CHG-120 search-api may relate). auth-svc.log:1-64, shipping-svc.log:10-66 cert_expired continue; checkout/inventory clean. R7 done; next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))