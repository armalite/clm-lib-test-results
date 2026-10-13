import json
c=json.load(open('/task/workspace/context.json'))
E=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
E.append({'id':'n6','role':'note','body':'R6: board.md:3 Thread A mitigated; :4 OPEN ALERT_TUNING. changes.md:3 CHG-150 APPLIED mitigation search-api. No cert errors in logs. 429 tax-provider now also checkout-api.log:21-74 (6 lines) + ledger-svc.log:17-76. Next: advance to R7.'})
json.dump({'format':'clm-context/v1','entries':E},open('/task/workspace/context.json','w'))