import json
c=json.load(open('/task/workspace/context.json'))
E={e['id']:e for e in c['entries']}
E['n6']['body']+=' [R8: Thread A RESOLVED round-08/board.md:3]'
E['n7']['body']=E['n7']['body'].replace('Next: advance to round 8.','[R8: Thread B MITIGATED, VENDOR_TICKET CLOSED]')
n8={'id':'n8','role':'note','body':'Round8: board.md:3 Thread A resolved; :4 Thread B mitigated; :5 Thread C search-api failures ongoing cause unknown (likely BAD_CONFIG_ROLLOUT via CHG-120 round-02/changes.md:4); :6 CLOSED VENDOR_TICKET. changes.md:3 CHG-159 retry budget. search-api config validation failed key http.max_inflight round-08/logs/search-api.log:9,19,22,59. Disk WARN continues shipping-svc.log:14,28 notify-worker.log:17,58. Open followups: DATA_BACKFILL, RUNBOOK_UPDATE. Next: advance to round 9.'}
c['entries']=[E[k] for k in ['n1','n2','n3','n4','n5','n6','n7']]+[n8]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')