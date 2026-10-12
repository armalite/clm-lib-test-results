import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: ALERT_TUNING CLOSED, CUSTOMER_COMMS OPEN (round-06/board.md:3-4). Open follow-ups now: RUNBOOK_UPDATE, VENDOR_TICKET, CAPACITY_REVIEW, CUSTOMER_COMMS. CHG-147 APPLIED retry budget GETs=1 (round-06/changes.md:3). 429 fx-rates continue round-06/logs/payments-svc.log:3-44, round-06/logs/checkout-api.log:19-77. auth/search/notify quiet. Next: advance, scan 07.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')