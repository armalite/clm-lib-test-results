import json
p='/task/workspace/context.json'
c=json.load(open(p))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
keep.append({'id':'n5','role':'note','body':'R5: board no updates; CHG-137 irrelevant. DNS SERVFAIL kms.internal continues round-05/logs/inventory-svc.log:20-36; 429 sms-gateway continue round-05/logs/pricing-svc.log:1-21, round-05/logs/search-api.log:6-22. checkout/shipping clean. Next: advance to R6.'})
c['entries']=keep
json.dump(c,open(p,'w'))