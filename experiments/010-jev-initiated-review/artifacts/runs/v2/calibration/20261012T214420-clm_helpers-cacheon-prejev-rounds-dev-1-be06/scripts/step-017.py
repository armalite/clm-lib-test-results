import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: Thread B opened payments-svc suspected CACHE_STAMPEDE (round-04/board.md:3) BUT logs show 429 upstream=fx-rates in payments-svc (round-04/logs/payments-svc.log:1-20,45-59) and checkout-api (round-04/logs/checkout-api.log:9-19,50-62) => likely UPSTREAM_RATE_LIMIT. CHG-133 APPLIED TLS ticket rotation (noise?). Raw in spill/s13.obs.txt. Next: advance to R5.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')