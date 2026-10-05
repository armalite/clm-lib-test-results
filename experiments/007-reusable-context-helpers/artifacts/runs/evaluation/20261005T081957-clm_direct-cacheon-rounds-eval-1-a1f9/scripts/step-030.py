import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in ('n1','n2','n4','n5','n6','n7','n8','n9')]
e.append({'id':'n10','role':'note','body':'R10: board.md:3 CLOSED CUSTOMER_COMMS. CHG-173 PROPOSED noise. auth-svc.log config errors 9,17,18,21 (13). CERT errors search-api.log:20,37 shipping-svc.log:58,61. Open: RUNBOOK_UPDATE, DATA_BACKFILL, ALERT_TUNING. Next: advance R11.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))