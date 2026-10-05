import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
e.append({'id':'n6','role':'note','body':'R6: round-06/board.md:3 RUNBOOK_UPDATE OPEN. changes.md:3 CHG-144 APPLIED log sampling (noise). Logs: auth-svc.log:4-79, shipping-svc.log:1-64 cert_expired continue; checkout/inventory/search clean. R6 done; next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))