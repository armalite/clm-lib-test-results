import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board Thread A opened DB_POOL_EXHAUSTED auth-svc + search-api, ongoing (round-03/board.md:3). changes: CHG-125 dashboards only. pool WARNs round-03/logs/auth-svc.log:7-63, round-03/logs/search-api.log:1-77. notify-worker still no errors (CHG-120 watch).'})
json.dump(c,open('/task/workspace/context.json','w'))