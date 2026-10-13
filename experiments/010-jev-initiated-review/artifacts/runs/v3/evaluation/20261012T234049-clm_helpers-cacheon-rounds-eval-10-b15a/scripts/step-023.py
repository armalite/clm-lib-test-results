import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'].startswith('n')]
e.append({'id':'n8','role':'note','body':'R8: board.md:3 Thread A resolved; :4 Thread B mitigated. CHG-157 PROPOSED only. 429 residual inventory-svc.log:27-31, search-api.log:42-59. Next: advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))