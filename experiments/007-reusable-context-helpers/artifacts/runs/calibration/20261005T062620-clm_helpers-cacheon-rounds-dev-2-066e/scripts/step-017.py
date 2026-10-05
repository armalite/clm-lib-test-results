import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
n.append({'id':'n6','role':'note','body':'R6: board.md:3 OPEN RUNBOOK_UPDATE. changes.md:3 CHG-144 log sampling (noise). cert_expired continues auth-svc 4-79, shipping-svc 1-64. No new incidents. Next: advance to round 7.'})
c['entries']=n
json.dump(c,open('/task/workspace/context.json','w'))