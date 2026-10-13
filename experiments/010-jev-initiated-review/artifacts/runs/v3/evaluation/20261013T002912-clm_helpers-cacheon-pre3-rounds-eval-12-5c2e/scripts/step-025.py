import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
e.append({'id':'n6','role':'note','body':'R6: board Thread A (CERT_EXPIRED) mitigated (round-06/board.md:3); Follow-up OPEN ALERT_TUNING (:4). CHG-150 APPLIED mitigation thread A search-api (round-06/changes.md:3). Logs: no cert errors; ledger-svc 429 tax-provider n=8 (round-06/logs/ledger-svc.log:17,24,28,34); checkout-api 429 tax-provider n=6 (round-06/logs/checkout-api.log:21,30,49,50) -> UPSTREAM_RATE_LIMIT spreads to checkout-api. Next: advance R7.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')