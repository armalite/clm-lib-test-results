import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B cause revised to UPSTREAM_RATE_LIMIT (auth-svc+shipping-svc). 429 tax-provider auth-svc.log:3,11,17,23,24,34; shipping-svc.log:15,16,20,29,33,34. No pool WARNs. Next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))