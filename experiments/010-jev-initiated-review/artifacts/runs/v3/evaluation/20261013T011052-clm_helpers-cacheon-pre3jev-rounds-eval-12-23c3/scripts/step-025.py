import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
for e in c['entries']:
  if e['id']=='n3':e['body']+=' [R6: Thread A now mitigated, see n6]'
c['entries'].append({'id':'n6','role':'note','body':'R6: board.md:3 Thread A (CERT_EXPIRED) status mitigated; :4 OPEN ALERT_TUNING. changes.md:3 CHG-150 APPLIED mitigation thread A search-api. inventory/search/pricing 0 errs. ledger-svc.log 429 tax-provider 17,24,28 (8 errs); checkout-api.log 429 tax-provider 21,30,49 (6 errs) -> UPSTREAM_RATE_LIMIT ledger+checkout likely (board still says QUEUE_BACKLOG thread B). Open: CAPACITY_REVIEW,RUNBOOK_UPDATE,POSTMORTEM_DRAFT,CUSTOMER_COMMS,ALERT_TUNING. Next: advance to round 7.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')