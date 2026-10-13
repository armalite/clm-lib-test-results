import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'] in('n1','n2','n3','n4')]
keep.append({'id':'n5','role':'note','body':'Round5: board no updates; CHG-137 APPLIED dashboards (benign). inventory-svc dns lookup failed host=kms.internal SERVFAIL round-05/logs/inventory-svc.log:20,27,32,36,64,65,67. 429 sms-gateway pricing-svc.log:1,7,12,21,23,31,32,44,53,67,72,73; search-api.log:6,14,15,22,29,46,48,59,66,72,75-77. Round 5 done; next: advance.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
print('ok')