import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: Thread A opened DB_POOL_EXHAUSTED auth-svc + search-api, ongoing (round-03/board.md:3). Logs: round-03/logs/auth-svc.log:7-19, round-03/logs/search-api.log:1-14. CHG-125 dashboards irrelevant. Next: advance to round 4 then scan 04.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')