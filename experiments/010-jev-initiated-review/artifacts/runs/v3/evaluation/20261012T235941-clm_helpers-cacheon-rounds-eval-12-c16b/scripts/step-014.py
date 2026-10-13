import json
c=json.load(open('/task/workspace/context.json'))
E=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
E.append({'id':'n5','role':'note','body':'R5: board.md:3 OPEN CUSTOMER_COMMS. Cert errors inventory-svc.log:10-73, search-api.log:6-70. ledger 429 tax-provider ledger-svc.log:7-61. checkout/pricing quiet. Next: advance to R6.'})
json.dump({'format':'clm-context/v1','entries':E},open('/task/workspace/context.json','w'))