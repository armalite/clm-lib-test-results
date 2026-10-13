import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
b=n['body'].replace('Next: advance to R10.','R10: board.md:3 Thread D FALSE ALARM (drop UPSTREAM_RATE_LIMIT); :4 CLOSED DATA_BACKFILL; changes.md:3 CHG-175 log sampling (irrelevant). search-api config validation failed round-10/logs/search-api.log:1,4; cert errors round-10/logs/auth-svc.log:10,17, shipping-svc.log:3,60. Open followups now: ALERT_TUNING, RUNBOOK_UPDATE. Next: advance to R11.')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))
print('ok')