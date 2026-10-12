import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
b=n['body'].replace(' Next: advance to R10.','')
b+="\nR10: round-10/board.md:3 Thread D closed FALSE ALARM (drop UPSTREAM_RATE_LIMIT). board.md:4 CLOSED DATA_BACKFILL. changes.md:3 CHG-175 noise. search-api config validation failed http.max_inflight round-10/logs/search-api.log:1,4,7,8,20 (no 429). CERT still auth-svc.log:10,17; shipping-svc.log:3,60. Open: ALERT_TUNING, RUNBOOK_UPDATE. Next: advance to R11."
n['body']=b
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print(len(b))