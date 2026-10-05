import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in ('n1','n2','n4','n5','n6','n7','n8')]
for x in e:
  if x['id'] in ('n5','n6','n7'):x['body']=x['body'][:200]
e.append({'id':'n9','role':'note','body':'R9: board.md:3 Thread B mitigated. board.md:4 Thread C pods restarting. board.md:5 CLOSED POSTMORTEM_DRAFT. board.md:6 OPEN CUSTOMER_COMMS. changes CHG-168 noise. auth-svc.log config errors lines 10,12,22 (11 total). CERT errors search-api.log:12,36 shipping-svc.log:53,59 (only 2 each). Open: RUNBOOK_UPDATE, DATA_BACKFILL, ALERT_TUNING, CUSTOMER_COMMS. Next: advance R10.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))