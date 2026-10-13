import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']=n['body'].replace(' Next: advance to round 6.','')+' R6: Follow-up OPEN RUNBOOK_UPDATE (round-06/board.md:3). CHG-144 log sampling (noise). Cert continues round-06/logs/auth-svc.log:4,10; shipping-svc.log:1,18. R7: board Thread B cause revised CERT_EXPIRED (round-07/board.md:3). Thread D UPSTREAM_RATE_LIMIT search-api ongoing (round-07/board.md:4); logs search-api 429 upstream=tax-provider round-07/logs/search-api.log:4,5,20. Cert continues round-07/logs/auth-svc.log:1,16; shipping-svc.log:10,11. Next: advance to round 8.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))