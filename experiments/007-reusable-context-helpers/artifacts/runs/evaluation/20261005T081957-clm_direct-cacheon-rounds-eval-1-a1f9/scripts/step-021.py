import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5','n6')]
e.append({'id':'n7','role':'note','body':'R7: board.md:3 follow-up OPEN POSTMORTEM_DRAFT; board.md:4 OPEN DATA_BACKFILL. changes CHG-154 retry budget (noise). CERT_EXPIRED errors continue search-api.log:8,10,11,16 shipping-svc.log:3,16,21,35. No errors auth/ledger/payments. Next: advance to R8.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))