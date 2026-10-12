import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board Thread A DB_POOL_EXHAUSTED auth-svc, impact search-api, ongoing (round-03/board.md:3). CHG-125 dashboards irrelevant. auth pool WARNs round-03/logs/auth-svc.log:7,12,13; search-api pool WARN round-03/logs/search-api.log:1,14. No notify errors yet. Next: advance to R4.'})
json.dump(c,open('/task/workspace/context.json','w'))