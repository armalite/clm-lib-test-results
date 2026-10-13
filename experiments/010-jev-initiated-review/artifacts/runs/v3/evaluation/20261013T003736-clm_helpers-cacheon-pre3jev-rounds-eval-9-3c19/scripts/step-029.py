import json
c=json.load(open('/task/workspace/context.json'))
E={e['id']:e for e in c['entries']}
E['n4']['body']+=' [R7: Thread B revised to DISK_PRESSURE, see n7]'
E['n5']['body']+=' [R7: Thread D closed FALSE ALARM - exclude; VENDOR_TICKET still open unless closed]'
n7={'id':'n7','role':'note','body':'Round7: round-07/board.md:3 Thread B cause DISK_PRESSURE (shipping-svc+notify-worker), still ongoing. board.md:4 Thread D false alarm. board.md:5 CLOSED POSTMORTEM_DRAFT. changes.md:3 CHG-149 PROPOSED (ignore). Disk evidence round-07/logs/notify-worker.log:2,19,37,56; shipping-svc.log:18,22,65. Open followups: DATA_BACKFILL, VENDOR_TICKET, RUNBOOK_UPDATE. Next: advance to round 8.'}
c['entries']=[E[k] for k in ['n1','n2','n3','n4','n5','n6']]+[n7]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')