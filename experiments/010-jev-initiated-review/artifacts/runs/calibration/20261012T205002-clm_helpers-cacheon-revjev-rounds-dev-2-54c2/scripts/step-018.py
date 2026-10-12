import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
keep.append({'id':'n6','role':'note','body':'R6: board.md:3 OPEN RUNBOOK_UPDATE. changes.md:3 CHG-144 log sampling (noise). Logs now JSON format. CERT errs round-06/logs/auth-svc.log:4-79, shipping-svc.log:1-64. No errors checkout/inventory/search. Next: advance.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')