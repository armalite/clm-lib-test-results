import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: board no updates. changes CHG-137 dashboards (noise). DNS kms.internal SERVFAIL continues round-05/logs/inventory-svc.log:20,27,32,36 (7 hits). 429 sms-gateway continues pricing-svc.log:1,7,12,21; search-api.log:6,14,15,22. checkout/shipping clean. Next: advance to R6.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')