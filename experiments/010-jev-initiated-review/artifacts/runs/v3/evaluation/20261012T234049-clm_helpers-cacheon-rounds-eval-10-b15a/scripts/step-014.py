import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
e.append({'id':'n5','role':'note','body':'R5: board empty; CHG-140 log sampling only. DNS errs auth-svc.log:1-60, checkout-api.log:2-66; 429 fx-rates search-api.log:5-64. inv/ship clean. Next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))