import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n=n.replace('\nNext: advance to round 6.','\nR6: board Thread A mitigated after CHG-150 (round-06/board.md:3; round-06/changes.md:3); Thread B revised to UPSTREAM_RATE_LIMIT (board.md:4); follow-up OPEN ALERT_TUNING (board.md:5). auth/checkout no errors r6. inventory-svc now ALSO 429 fx-rates (round-06/logs/inventory-svc.log:3,4,10,25) -> add to Thread B services; search 429 (round-06/logs/search-api.log:6,9,12,27). shipping clean.\nNext: advance to round 7.')
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')