import json
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
e.append({'id':'n6','role':'note','body':'R6: ALERT_TUNING CLOSED (round-06/board.md:3); CUSTOMER_COMMS OPEN (round-06/board.md:4). CHG-147 retry budget irrelevant. 429 fx-rates still: round-06/logs/checkout-api.log:19, payments-svc.log:3. No db pool errs. Open FUs: RUNBOOK_UPDATE, VENDOR_TICKET, CAPACITY_REVIEW, CUSTOMER_COMMS. Next: advance R7.'})
json.dump({'format':'clm-context/v1','entries':e},open(p,'w'))
print('ok')