import json,re
L=open('/task/fixtures/round-07/logs/search-api.log').read().splitlines()
d=[i for i,l in enumerate(L,1) if 'disk' in l.lower()]
print('disk',d[:10])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=" | R7: board.md:3 A resolved; :4 Thread C search-api request failures ongoing (cause unknown); :5 D closed false alarm; :6 OPEN VENDOR_TICKET. search-api.log:17,20,23,28,30,39,50,52,58 ERROR config validation failed http.max_inflight=-1 (=CHG-113 BAD_CONFIG, round-01/changes.md:3). checkout heap WARN still, no 429. R7 done -> advance next."
json.dump(c,open('/task/workspace/context.json','w'))