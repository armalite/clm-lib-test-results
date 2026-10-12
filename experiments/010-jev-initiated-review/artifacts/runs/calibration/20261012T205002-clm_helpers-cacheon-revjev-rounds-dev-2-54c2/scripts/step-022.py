import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
keep.append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B cause revised CERT_EXPIRED. board.md:4 Thread D UPSTREAM_RATE_LIMIT search-api ongoing; 429 lines round-07/logs/search-api.log:4-66 (4,5,20,22,25,47,64,66). CERT errs round-07/logs/auth-svc.log:1-64, shipping-svc.log:10-66. No errs checkout/inventory. Next: advance.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))