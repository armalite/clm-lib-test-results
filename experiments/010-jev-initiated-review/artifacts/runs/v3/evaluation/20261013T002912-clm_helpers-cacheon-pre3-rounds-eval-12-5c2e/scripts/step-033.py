import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5','n6','n7')]
e.append({'id':'n8','role':'note','body':'R8: board Thread A CERT_EXPIRED resolved (round-08/board.md:3); Thread B cause revised UPSTREAM_RATE_LIMIT (round-08/board.md:4); Thread C pricing-svc failures ongoing cause unknown (round-08/board.md:5). Logs: pricing-svc config validation failed cache.ttl_s=-1 build 3.22.4 (round-08/logs/pricing-svc.log:5,17,28,38) -> BAD_CONFIG_ROLLOUT from CHG-113; checkout-api 429 (round-08/logs/checkout-api.log:26,27,37,51); ledger-svc 429 (round-08/logs/ledger-svc.log:9,12,21,30). Next: advance R9.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')