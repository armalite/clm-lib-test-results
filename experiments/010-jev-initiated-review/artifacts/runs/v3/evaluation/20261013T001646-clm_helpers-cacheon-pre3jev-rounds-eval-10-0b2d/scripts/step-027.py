import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n=n.replace('\nNext: advance to round 7.','\nR7: board Thread B services now include inventory-svc, cause/status unchanged (round-07/board.md:3). no changes.md. inventory 429 fx-rates (round-07/logs/inventory-svc.log:5,11,31,47,63); search 429 (round-07/logs/search-api.log:14,24,27,49). auth/checkout/shipping clean.\nNext: advance to round 8.')
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')