import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR6: round-06/board.md:3 OPEN RUNBOOK_UPDATE. changes.md:3 CHG-144 noise. CERT continues round-06/logs/auth-svc.log:4,10,14; shipping-svc.log:1,18,21. No DNS, search-api clean."
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))