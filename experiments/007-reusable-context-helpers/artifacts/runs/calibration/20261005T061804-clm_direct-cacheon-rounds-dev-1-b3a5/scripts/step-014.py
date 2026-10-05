import json
c=json.load(open('/task/workspace/context.json'))
n5='R5: board.md:3 Thread A mitigated; :4 Thread B adds checkout-api; :5 OPEN CAPACITY_REVIEW. changes.md:3 CHG-138 TLS rotation; :4 CHG-143 APPLIED thread A mitigation auth-svc. No pool WARNs in R5. checkout-api.log:21,23,30,38,42,59,65 429 fx-rates; payments-svc.log:13,19,47,50,55,73 429 fx-rates. notify-worker no errors yet.'
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]+[{'id':'n5','role':'note','body':n5}]
json.dump(c,open('/task/workspace/context.json','w'))