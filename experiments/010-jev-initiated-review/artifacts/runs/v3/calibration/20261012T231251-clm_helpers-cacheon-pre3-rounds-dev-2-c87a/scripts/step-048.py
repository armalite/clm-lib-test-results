import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']=n['body'].replace(' Next: advance to round 10.','')+' R10: Thread D closed false alarm (round-10/board.md:3) -> drop UPSTREAM_RATE_LIMIT. CLOSED DATA_BACKFILL (:4). CHG-175 noise. Cert logs round-10/logs/auth-svc.log:10,17; shipping-svc.log:3,60. search config fail round-10/logs/search-api.log:1,4. Open followups: ALERT_TUNING, RUNBOOK_UPDATE. Next: advance to round 11.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')