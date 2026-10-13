import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
e.append({'id':'n6','role':'note','body':'R6: board.md:3 Thread A mitigated; :4 Thread B cause UPSTREAM_RATE_LIMIT; :5 OPEN ALERT_TUNING. changes.md:3 CHG-150 APPLIED mitigation auth-svc. auth/checkout clean now. 429 fx-rates now also inventory-svc.log:3-69 + search-api.log:6-69. Next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))