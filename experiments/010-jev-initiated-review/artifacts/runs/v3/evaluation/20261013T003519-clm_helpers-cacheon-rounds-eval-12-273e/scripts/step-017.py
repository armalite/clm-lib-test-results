import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
e.append({'id':'n6','role':'note','body':'R6: board.md:3 Thread A mitigated; :4 OPEN ALERT_TUNING. changes.md:3 CHG-150 APPLIED mitigation search-api. No cert errors in inventory/search. 429 tax-provider now also checkout-api.log:21-74 and ledger-svc.log:17-76. Next: advance R7.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')