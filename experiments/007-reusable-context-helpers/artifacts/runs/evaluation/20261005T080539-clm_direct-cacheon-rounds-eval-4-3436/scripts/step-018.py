import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6','role':'note','body':'R6: board empty (no changes). CHG-142 PROPOSED only. 429 tax-provider continues auth-svc.log:8,23,34,88; shipping-svc.log:11,23,27,88. No pool/other WARNs. Next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))