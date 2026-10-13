import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3')]
e.append({'id':'n4','role':'note','body':'R4: board empty. DNS errs continue auth-svc.log:3-57, checkout-api.log:2-64; 429 fx-rates search-api.log:4-90. inventory/shipping clean. Next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))