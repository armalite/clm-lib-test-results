import json
c=json.load(open('/task/workspace/context.json'))
E=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n6','n7','n8','n9')]
E.append({'id':'n10','role':'note','body':'R10: round-10/board.md:3 Thread C pods still restarting; board.md:4 CLOSED ALERT_TUNING. shipping config validation failed retry.backoff_ms=0 build 6.58.8 round-10/logs/shipping-svc.log:3-74 (13). Sparse 429 search-api.log:13,31 inventory-svc.log:36,59. Next: advance.'})
c['entries']=E
json.dump(c,open('/task/workspace/context.json','w'))