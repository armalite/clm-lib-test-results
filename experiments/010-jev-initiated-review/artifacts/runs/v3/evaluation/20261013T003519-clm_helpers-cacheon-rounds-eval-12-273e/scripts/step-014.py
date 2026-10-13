import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
e.append({'id':'n5','role':'note','body':'R5: board.md:3 OPEN CUSTOMER_COMMS. No changes.md. inventory-svc.log:10-73 & search-api.log:6-70 cert_expired continue; ledger-svc.log:7-61 429 tax-provider continue. checkout/pricing clean. Next: advance to R6.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')