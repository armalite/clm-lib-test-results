import json
c=json.load(open('context.json'))
e={x['id']:x for x in c['entries']}
n3='R3: board Thread A opened DB_POOL_EXHAUSTED auth-svc + search-api ongoing (round-03/board.md:3). changes CHG-125 APPLIED dashboards (noise). Logs pool exhausted auth-svc round-03/logs/auth-svc.log:7-19; search-api round-03/logs/search-api.log:1-14. notify-worker no errors r3.'
c['entries']=[e['n1'],e['n2'],{'id':'n3','role':'note','body':n3}]
json.dump(c,open('context.json','w'))
print('ok')