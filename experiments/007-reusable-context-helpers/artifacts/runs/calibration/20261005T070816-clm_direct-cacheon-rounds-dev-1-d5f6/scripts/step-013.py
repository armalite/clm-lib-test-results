import json
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3')]
e.append({'id':'n4','role':'note','body':'R4: Thread B opened CACHE_STAMPEDE payments-svc ongoing (round-04/board.md:3) but logs show 429 fx-rates in payments-svc.log:1 and checkout-api.log:9 -> likely UPSTREAM_RATE_LIMIT (watch). DB pool still exhausted auth-svc.log:7, search-api.log:4. CHG-133 APPLIED TLS ticket rotation hourly (round-04/changes.md:3) - watch for cert issues.'})
json.dump({'format':'clm-context/v1','entries':e},open(p,'w'))
print('ok')