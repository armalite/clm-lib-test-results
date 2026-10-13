import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
b=n1['body']
i=b.find(' Next: advance round 9.')
if i>0:b=b[:i]
b+=" Round9: round-09/board.md:3 Thread B mitigated; :4 Thread C still ongoing; :5 CLOSED RUNBOOK_UPDATE; changes.md:3 CHG-164 APPLIED retry (irrelevant). r9 429 checkout-api.log:10,66; ledger-svc.log:29,66; pricing-svc ttl errs 10,12,16,26,29,30,33,34,38,65,69. Open: CAPACITY_REVIEW,POSTMORTEM_DRAFT,CUSTOMER_COMMS,ALERT_TUNING. Next: advance round 10."
n1['body']=b
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))
print(len(b))