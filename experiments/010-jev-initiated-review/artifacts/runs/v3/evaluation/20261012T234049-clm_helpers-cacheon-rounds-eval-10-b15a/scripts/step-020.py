import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5','n6')]
e.append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B services +inventory-svc. 429 fx-rates inventory-svc.log:5-66, search-api.log:14-70. auth/checkout/ship clean. Next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))