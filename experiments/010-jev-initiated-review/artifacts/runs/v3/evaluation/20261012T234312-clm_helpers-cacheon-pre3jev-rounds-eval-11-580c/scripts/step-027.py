import json
p='/task/workspace/context.json'
c=json.load(open(p))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n5','n6')]
for e in keep:
  if e['id']=='n5':e['body']='R5: no board updates; DNS SERVFAIL and 429s continue.'
keep.insert(3,{'id':'n4','role':'note','body':'R4: round-04/board.md:3 Thread B inventory-svc suspected CERT_EXPIRED (superseded R7). DNS SERVFAIL host=kms.internal round-04/logs/inventory-svc.log:16-34. :4 OPEN CAPACITY_REVIEW. CHG-131 TLS rotation irrelevant.'})
keep.append({'id':'n7','role':'note','body':'R7: round-07/board.md:3 Thread B cause revised DNS_RESOLUTION (inventory-svc, ongoing); SERVFAIL kms.internal round-07/logs/inventory-svc.log:1-21. board.md:4 Thread D MEMORY_LEAK pricing-svc ongoing; heap high round-07/logs/pricing-svc.log:8-20. CHG-153 PROPOSED irrelevant. Open: POSTMORTEM_DRAFT, CAPACITY_REVIEW. Next: advance to R8.'})
c['entries']=keep
json.dump(c,open(p,'w'))