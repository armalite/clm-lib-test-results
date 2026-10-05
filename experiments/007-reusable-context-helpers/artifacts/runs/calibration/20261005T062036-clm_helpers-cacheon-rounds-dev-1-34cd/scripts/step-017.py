import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+=" R6: board closes ALERT_TUNING, opens CUSTOMER_COMMS (round-06/board.md:3,4). CHG-147 retry budget irrelevant. 429 fx-rates payments-svc.log:3,10,11; checkout-api.log:19. No pool errors R6 (only slow query WARNs everywhere = noise). Open now: RUNBOOK_UPDATE, VENDOR_TICKET, CAPACITY_REVIEW, CUSTOMER_COMMS."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))