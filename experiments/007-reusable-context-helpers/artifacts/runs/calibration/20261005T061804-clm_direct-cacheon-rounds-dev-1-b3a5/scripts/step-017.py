import json
c=json.load(open('/task/workspace/context.json'))
n6='R6: board.md:3 CLOSED ALERT_TUNING; :4 OPEN CUSTOMER_COMMS. changes.md:3 CHG-147 retry budget (irrelevant). checkout-api.log:19,30,56,73,76,77 429 fx-rates; payments-svc.log:3,10,11,16,18,33,40,42,43,44,76 429 fx-rates. No pool WARNs, no notify-worker errors.'
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]+[{'id':'n6','role':'note','body':n6}]
json.dump(c,open('/task/workspace/context.json','w'))