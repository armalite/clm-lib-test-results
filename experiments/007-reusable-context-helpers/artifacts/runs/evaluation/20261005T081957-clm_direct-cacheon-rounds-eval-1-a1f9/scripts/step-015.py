import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
e.append({'id':'n5','role':'note','body':'R5: board.md:3 Thread A mitigated. changes.md:3 CHG-143 APPLIED mitigation thread A payments-svc. No lag WARNs anymore in payments/ledger. CERT_EXPIRED errors peer=sso.example.net now also search-api.log:14,35,50,51,79,81 and shipping-svc.log:1,2,18,27,56,59 -> Thread B services shipping-svc+search-api. Next: advance to R6.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))