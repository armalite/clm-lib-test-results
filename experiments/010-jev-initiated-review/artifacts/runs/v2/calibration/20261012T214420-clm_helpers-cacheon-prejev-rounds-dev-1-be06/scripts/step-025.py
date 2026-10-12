import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board: ALERT_TUNING CLOSED (round-06/board.md:3), CUSTOMER_COMMS OPEN (round-06/board.md:4). CHG-147 APPLIED retry budget=1 (noise?). 429 fx-rates continue: checkout-api round-06/logs/checkout-api.log:19-30,56-77; payments-svc round-06/logs/payments-svc.log:3-18,33-44,76. auth/search/notify clean. Open follow-ups now: RUNBOOK_UPDATE, VENDOR_TICKET, CAPACITY_REVIEW, CUSTOMER_COMMS. Next: advance R7.'})
json.dump(c,open(p,'w'))
print('ok')