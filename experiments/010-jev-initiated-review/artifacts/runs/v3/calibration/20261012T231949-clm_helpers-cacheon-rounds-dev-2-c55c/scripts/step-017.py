import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board adds Follow-up OPEN RUNBOOK_UPDATE (round-06/board.md:3). CHG-144 APPLIED log sampling (noise). CERT_EXPIRED continues auth round-06/logs/auth-svc.log:4,10,14,19; shipping round-06/logs/shipping-svc.log:1,18,21,36. No DNS, search-api clean. Next: advance to R7.'})
json.dump(c,open('/task/workspace/context.json','w'))