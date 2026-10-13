import json
p='/task/workspace/context.json'
c=json.load(open(p))
E=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6','n7','n8')]
for e in E:
  if e['id']=='n7': e['body']='R7: round-07/board.md:3 Thread B cause revised DNS_RESOLUTION (inventory-svc, ongoing); SERVFAIL kms.internal round-07/logs/inventory-svc.log:1-21. board.md:4 Thread D MEMORY_LEAK pricing-svc (CLOSED as false alarm R9). CHG-153 PROPOSED irrelevant.'
E.append({'id':'n9','role':'note','body':'R9: round-09/board.md:3 Thread D closed false alarm (not incident). DNS SERVFAIL kms.internal inventory-svc round-09/logs/inventory-svc.log:7-80 AND now shipping-svc round-09/logs/shipping-svc.log:17-78 (add shipping-svc to Thread B services). Open: POSTMORTEM_DRAFT, CAPACITY_REVIEW, DATA_BACKFILL. Next: advance to R10.'})
c['entries']=E
json.dump(c,open(p,'w'))
print('ok')