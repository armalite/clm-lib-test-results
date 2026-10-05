import json
c=json.load(open('/task/workspace/context.json'))
n3='R3: board.md:3 Thread A DB_POOL_EXHAUSTED auth-svc + search-api ongoing. changes.md:3 CHG-125 dashboards (irrelevant). auth-svc.log:7,12,13,15 pool WARN; search-api.log:1,14,30 pool WARN. No notify-worker errors yet.'
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]+[{'id':'n3','role':'note','body':n3}]
json.dump(c,open('/task/workspace/context.json','w'))