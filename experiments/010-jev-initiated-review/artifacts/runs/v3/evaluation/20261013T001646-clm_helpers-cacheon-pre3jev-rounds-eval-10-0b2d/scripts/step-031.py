import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n=n.replace('\nNext: advance to round 8.','\nR8: board Thread A resolved (round-08/board.md:3); Thread B mitigated (round-08/board.md:4). CHG-157 PROPOSED (noise). auth/checkout clean; inventory 429 (round-08/logs/inventory-svc.log:27,31); search 429 (round-08/logs/search-api.log:42,59). shipping clean.\nNext: advance to round 9.')
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')