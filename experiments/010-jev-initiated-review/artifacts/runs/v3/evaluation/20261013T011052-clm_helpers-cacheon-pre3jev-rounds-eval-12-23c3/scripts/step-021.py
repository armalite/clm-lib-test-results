import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: board.md:3 OPEN CUSTOMER_COMMS. No changes.md. ledger-svc.log 429 tax-provider lines 7,35,39 (6 errs). inventory-svc cert_expired 12 errs (10,16,19..); search-api cert_expired 7 errs (6,35,48). checkout/pricing no errors. Open follow-ups: CAPACITY_REVIEW,RUNBOOK_UPDATE,POSTMORTEM_DRAFT,CUSTOMER_COMMS. Next: advance to round 6.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')