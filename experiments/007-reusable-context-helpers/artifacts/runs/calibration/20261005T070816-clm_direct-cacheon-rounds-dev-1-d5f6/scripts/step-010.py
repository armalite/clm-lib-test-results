import json
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e.append({'id':'n3','role':'note','body':'R3: Thread A opened DB_POOL_EXHAUSTED auth-svc + search-api ongoing (round-03/board.md:3). evidence round-03/logs/auth-svc.log:7, round-03/logs/search-api.log:1. CHG-125 dashboards irrelevant. notify-worker CHG-120 no errors seen yet R2/R3.'})
json.dump({'format':'clm-context/v1','entries':e},open(p,'w'))
print('ok')